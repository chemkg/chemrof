#!/usr/bin/env python
"""Build the bundled ChEBI atomic-species table from a ChEBI OBO release.

Writes ``src/chemrof/converter/data/atomic_species.tsv``: every ChEBI class that
denotes a single atom, keyed by (atomic number, charge, mass number):

* neutral atoms          -- ``iron atom``                (charge 0, no mass number)
* monoatomic ions        -- ``iron(3+)``, ``chloride``   (charge != 0)
* isotope-labelled forms -- ``carbon-13 atom``, ``helion`` (mass number set)

Selection rule
--------------
ChEBI does not store atomic numbers, but each of these classes carries the
standard InChI of a bare atom (``InChI=1S/Fe``, ``InChI=1S/Fe/q+3``,
``InChI=1S/ClH/h1H/p-1``, ``InChI=1S/C/i1+1``). The InChI is read back through
RDKit; a class qualifies if the result is one atom (hydrogen atoms included,
bound hydrogens excluded). The mass number is InChI's reference isotope plus the
``/i`` delta -- RDKit reports 0 for a zero delta, so it is computed here and
cross-checked against the ``X-NN`` in the ChEBI label.

Several ChEBI classes share one key; the periodic-table class is the one that is
not under ``monoatomic ...`` or ``elemental ...`` (e.g. ``iron(0)``, ``iron(.)``,
``monoatomic iron``); if several remain, the one named ``X atom`` wins. Anything
still ambiguous is reported, never guessed.

Usage::

    curl -L -o chebi.obo http://purl.obolibrary.org/obo/chebi.obo
    python scripts/build_atomic_species.py chebi.obo
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

from rdkit import Chem, RDLogger
from rdkit.Chem import inchi as rdkit_inchi

RDLogger.DisableLog("rdApp.*")

DEFAULT_OUT = Path(__file__).resolve().parent.parent / "src/chemrof/converter/data/atomic_species.tsv"
HEADER = ["chebi_id", "name", "atomic_number", "symbol", "charge", "mass_number"]

# InChI=1S/Fe, /Fe/q+3, /ClH/h1H/p-1, /H/q-1/i1+1 ... plus the bare proton, InChI=1S/p+1
_ATOMIC_INCHI = re.compile(r"^InChI=1S/(?:([A-Z][a-z]?)(?:H\d*)?(?:/|$)|p\+1$)")
_INCHI_PROP = re.compile(
    r'^property_value: (?:chemrof:inchi_string|http://purl\.obolibrary\.org/obo/chebi/inchi) "(InChI=1S/[^"]*)"'
)
_ISO_DELTA = re.compile(r"/i1([+-]\d+)(?:/|$)")
_NAME_MASS = re.compile(r"^[A-Za-z]+-(\d+)(?:[ (]|$)")
_PERIODIC_TABLE = Chem.GetPeriodicTable()


def read_terms(path: Path):
    """Return ({id: name}, [terms with an atomic InChI], header) from an OBO file."""
    names: dict[str, str] = {}
    terms: list[dict] = []
    header: dict[str, str] = {}
    cur: dict = {}

    def flush():
        if cur.get("id") and "name" in cur:
            names[cur["id"]] = cur["name"]
            if cur.get("inchi") and not cur.get("obsolete"):
                terms.append(cur)

    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line == "[Term]":
                flush()
                cur = {}
            elif not cur and line.startswith(("data-version: ", "date: ")):
                key, _, value = line.partition(": ")
                header[key] = value
            elif line.startswith("id: "):
                cur["id"] = line[4:]
            elif line.startswith("name: "):
                cur["name"] = line[6:]
            elif line.startswith("is_obsolete: true"):
                cur["obsolete"] = True
            elif line.startswith("is_a: CHEBI:"):
                cur.setdefault("parents", []).append(line[6:].split(" !")[0])
            elif line.startswith("property_value:"):
                m = _INCHI_PROP.match(line)
                if m and _ATOMIC_INCHI.match(m.group(1)):
                    cur["inchi"] = m.group(1)
    flush()
    return names, terms, header


_default_mass_cache: dict[int, int] = {}


def default_mass(z: int) -> int:
    """The isotope InChI treats as the reference (``/i1+0``) for element z."""
    if z not in _default_mass_cache:
        symbol = _PERIODIC_TABLE.GetElementSymbol(z)
        guess = _PERIODIC_TABLE.GetMostCommonIsotope(z)
        for mass in sorted(range(max(1, guess - 6), guess + 7), key=lambda m: abs(m - guess)):
            inchi = rdkit_inchi.MolToInchi(Chem.MolFromSmiles(f"[{mass}{symbol}]")) or ""
            if "/i1+0" in inchi:
                _default_mass_cache[z] = mass
                break
        else:
            raise RuntimeError(f"cannot find InChI reference isotope for {symbol}")
    return _default_mass_cache[z]


def species_key(term: dict):
    """(atomic_number, charge, mass_number or None) for a term, or None if not a lone atom."""
    mol = rdkit_inchi.MolFromInchi(term["inchi"])
    if mol is None or mol.GetNumAtoms() != 1:
        return None
    atom = mol.GetAtomWithIdx(0)
    if atom.GetTotalNumHs() > 0:  # HCl, NH3, ... are molecules, not atoms
        return None
    z = atom.GetAtomicNum()
    mass = atom.GetIsotope() or None
    delta = _ISO_DELTA.search(term["inchi"])
    if delta and mass is None:
        mass = default_mass(z) + int(delta.group(1))
    label = _NAME_MASS.match(term["name"])
    if label and mass is not None and int(label.group(1)) != mass:
        print(f"warning: {term['id']} {term['name']!r}: label says {label.group(1)}, InChI says {mass}", file=sys.stderr)
    return z, atom.GetFormalCharge(), mass


def is_generic(term: dict, names: dict[str, str]) -> bool:
    """True for the 'monoatomic X' / 'elemental X' / 'X(0)'-style siblings."""
    parents = [names.get(p, "") for p in term.get("parents", [])]
    return term["name"].startswith(("elemental ", "monoatomic ")) or any(
        p.startswith(("monoatomic ", "elemental ")) for p in parents
    )


def build(names: dict[str, str], terms: list[dict]):
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for term in terms:
        key = species_key(term)
        if key is not None:
            groups[key].append(term)

    rows, ambiguous = [], []
    for key, candidates in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][2] or 0, kv[0][1])):
        chosen = [t for t in candidates if not is_generic(t, names)] or candidates
        if len(chosen) > 1:
            chosen = [t for t in chosen if t["name"].endswith(" atom")] or chosen
        if len(chosen) > 1:
            ambiguous.append((key, chosen))
            continue
        z, charge, mass = key
        rows.append(
            [chosen[0]["id"], chosen[0]["name"], z, _PERIODIC_TABLE.GetElementSymbol(z), charge, mass or ""]
        )
    return rows, ambiguous


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("obo", type=Path, help="ChEBI OBO file (chebi.obo)")
    ap.add_argument("-o", "--output", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args(argv)

    names, terms, header = read_terms(args.obo)
    rows, ambiguous = build(names, terms)
    for key, chosen in ambiguous:
        print(f"ambiguous {key}: " + ", ".join(f"{t['id']} {t['name']!r}" for t in chosen), file=sys.stderr)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as out:
        out.write(
            "# Generated by scripts/build_atomic_species.py from ChEBI "
            f"data-version {header.get('data-version', '?')} ({header.get('date', '?')}). Do not edit.\n"
        )
        out.write("\t".join(HEADER) + "\n")
        for row in rows:
            out.write("\t".join(str(c) for c in row) + "\n")
    print(f"wrote {len(rows)} species to {args.output} ({len(ambiguous)} ambiguous keys skipped)")
    return 1 if ambiguous else 0


if __name__ == "__main__":
    sys.exit(main())
