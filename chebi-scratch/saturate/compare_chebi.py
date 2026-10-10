"""Compare a `chemrof saturate` graph with ChEBI.

Usage:
    python compare_chebi.py GRAPH.json CHEBI_DIR

GRAPH.json is `chemrof saturate ... -f json` output, seeded with ChEBI ids in
the third column. CHEBI_DIR holds ChEBI's flat files (structures.tsv.gz,
compounds.tsv.gz, relation.tsv.gz) from
https://ftp.ebi.ac.uk/pub/databases/chebi/flat_files/.

Reports:
  * how many generated entities are ChEBI entries (matched by InChIKey;
    zwitterions are matched by InChIKey plus net charge 0 and charge separation
    in the ChEBI SMILES, as InChIKey alone cannot tell them apart);
  * recall of ChEBI's conjugate acid/base, enantiomer and tautomer links
    between entities that are both in the graph.
"""

import csv
import gzip
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from rdkit import Chem, RDLogger

RDLogger.DisableLog("rdApp.*")
csv.field_size_limit(sys.maxsize)

CONJUGATE, ENANTIOMER, TAUTOMER = "6 7", "8", "11"


def read(path):
    with gzip.open(path, "rt") as f:
        yield from csv.DictReader(f, delimiter="\t")


def main(graph_path, chebi_dir):
    chebi_dir = Path(chebi_dir)
    graph = json.loads(Path(graph_path).read_text())
    if isinstance(graph, dict):
        graph = [graph]

    accession = {r["id"]: r["chebi_accession"] for r in read(chebi_dir / "compounds.tsv.gz")}
    by_key = defaultdict(list)  # InChIKey -> [(CHEBI id, is zwitterion)]
    for r in read(chebi_dir / "structures.tsv.gz"):
        key, acc = r["standard_inchi_key"], accession.get(r["compound_id"])
        if not key or not acc:
            continue
        mol = Chem.MolFromSmiles(r["smiles"]) if r["smiles"] else None
        zw = bool(
            mol
            and Chem.GetFormalCharge(mol) == 0
            and any(a.GetFormalCharge() > 0 for a in mol.GetAtoms())
            and any(a.GetFormalCharge() < 0 for a in mol.GetAtoms())
        )
        by_key[key].append((acc, zw))

    # entity id -> CHEBI id
    to_chebi, kinds = {}, Counter()
    for e in graph:
        eid = e["id"]
        if eid.startswith("CHEBI:"):
            to_chebi[eid] = eid
            kinds["seed"] += 1
            continue
        if eid.startswith("chemrof:rac-"):
            kinds["racemate (not compared)"] += 1
            continue
        zw = eid.startswith("chemrof:zwitterion-")
        key = eid.removeprefix("chemrof:zwitterion-").removeprefix("INCHIKEY:")
        hits = [acc for acc, is_zw in by_key.get(key, []) if is_zw == zw]
        if hits:
            to_chebi[eid] = hits[0]
            kinds["generated, in ChEBI"] += 1
        else:
            kinds["generated, not in ChEBI"] += 1
    print(f"{len(graph)} entities")
    for k, n in kinds.most_common():
        print(f"  {k}: {n}")

    in_graph = set(to_chebi.values())
    links = set()
    for e in graph:
        src = to_chebi.get(e["id"])
        for slot in ("has_major_microspecies_at_pH7_3", "conjugate_acid_of", "conjugate_base_of", "tautomer_of"):
            vals = e.get(slot, [])
            for v in vals if isinstance(vals, list) else [vals]:
                if src and v in to_chebi:
                    links.add(("conj" if slot != "tautomer_of" else "taut", frozenset((src, to_chebi[v]))))
        if e.get("type") == "chemrof:RacemicMixture":
            left, right = to_chebi.get(e.get("has_left_enantiomer")), to_chebi.get(e.get("has_right_enantiomer"))
            if left and right:
                links.add(("enan", frozenset((left, right))))

    found, total = Counter(), Counter()
    seen = set()
    for r in read(chebi_dir / "relation.tsv.gz"):
        kind = {"6": "conj", "7": "conj", "8": "enan", "11": "taut"}.get(r["relation_type_id"])
        a, b = accession.get(r["init_id"]), accession.get(r["final_id"])
        if not kind or a not in in_graph or b not in in_graph:
            continue
        pair = (kind, frozenset((a, b)))
        if pair in seen:
            continue
        seen.add(pair)
        total[kind] += 1
        # ChEBI may link a zwitterion as "tautomer" where we link it as a microspecies
        if pair in links or (kind == "taut" and ("conj", pair[1]) in links) or (
            kind == "conj" and ("taut", pair[1]) in links
        ):
            found[kind] += 1
    print("ChEBI links between entities both in the graph, recovered:")
    for kind, label in (("conj", "conjugate acid/base"), ("enan", "enantiomer"), ("taut", "tautomer")):
        if total[kind]:
            print(f"  {label}: {found[kind]}/{total[kind]} ({100 * found[kind] / total[kind]:.1f}%)")


if __name__ == "__main__":
    main(*sys.argv[1:3])
