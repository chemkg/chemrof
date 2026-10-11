"""Lookup of ChEBI atomic species: neutral atoms, monoatomic ions and isotopes.

The data lives in ``data/atomic_species.tsv`` and is generated from a ChEBI
release by ``scripts/build_atomic_species.py``. A species is identified by
``(atomic_number, charge, mass_number)``; ``mass_number`` is ``None`` when the
class does not specify an isotope.

>>> lookup(26).name
'iron atom'
>>> lookup(26, charge=3).chebi_id
'CHEBI:29034'
>>> lookup(6, mass_number=13).name
'carbon-13 atom'
>>> lookup(26, charge=7) is None
True
>>> sorted({s.charge for s in species_of_element("Fe") if s.mass_number is None})
[0, 2, 3]
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from functools import lru_cache
from importlib import resources

from rdkit import Chem


@dataclass(frozen=True)
class Species:
    chebi_id: str
    name: str
    atomic_number: int
    symbol: str
    charge: int
    mass_number: int | None

    @property
    def neutron_number(self) -> int | None:
        return None if self.mass_number is None else self.mass_number - self.atomic_number

    @property
    def smiles(self) -> str:
        """SMILES for this species, e.g. ``[56Fe+3]``."""
        mass = "" if self.mass_number is None else str(self.mass_number)
        sign = "+" if self.charge > 0 else "-"
        charge = "" if not self.charge else sign + ("" if abs(self.charge) == 1 else str(abs(self.charge)))
        return f"[{mass}{self.symbol}{charge}]"


@lru_cache(maxsize=1)
def _load() -> dict[tuple[int, int, int | None], Species]:
    path = resources.files("chemrof.converter") / "data" / "atomic_species.tsv"
    with path.open(encoding="utf-8") as f:
        lines = (line for line in f if not line.startswith("#"))
        rows = list(csv.DictReader(lines, delimiter="\t"))
    table = {}
    for r in rows:
        sp = Species(
            chebi_id=r["chebi_id"],
            name=r["name"],
            atomic_number=int(r["atomic_number"]),
            symbol=r["symbol"],
            charge=int(r["charge"]),
            mass_number=int(r["mass_number"]) if r["mass_number"] else None,
        )
        table[(sp.atomic_number, sp.charge, sp.mass_number)] = sp
    return table


def lookup(atomic_number: int, charge: int = 0, mass_number: int | None = None) -> Species | None:
    """The ChEBI species for an exact (Z, charge, mass number), or None."""
    return _load().get((atomic_number, charge, mass_number))


def element_number(element: int | str) -> int:
    """Atomic number for a number or element symbol/name.

    >>> element_number("Fe"), element_number(26)
    (26, 26)
    """
    if isinstance(element, int):
        return element
    return Chem.GetPeriodicTable().GetAtomicNumber(element)


def species_of_element(element: int | str) -> list[Species]:
    """All ChEBI species of an element, neutral atom first, then by mass number and charge."""
    z = element_number(element)
    found = [sp for sp in _load().values() if sp.atomic_number == z]
    return sorted(found, key=lambda sp: (sp.mass_number or 0, sp.charge != 0, sp.charge))
