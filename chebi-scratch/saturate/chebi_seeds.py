"""Write a `chemrof saturate` seed file from ChEBI's flat files.

Usage:
    python chebi_seeds.py CHEBI_DIR OUT.tsv [STARS]

One line per ChEBI compound with STARS stars (default 3) and a structure:
the SMILES, or the standard InChI when RDKit cannot read the SMILES (ChEBI
has aromatic SMILES that do not kekulise). Generic structures with R groups
(``*``) are skipped.
"""

import csv
import gzip
import sys
from pathlib import Path

from rdkit import Chem, RDLogger

RDLogger.DisableLog("rdApp.*")
csv.field_size_limit(sys.maxsize)


def read(path):
    with gzip.open(path, "rt") as f:
        yield from csv.DictReader(f, delimiter="\t")


def main(chebi_dir, out, stars="3"):
    chebi_dir = Path(chebi_dir)
    compounds = {r["id"]: r for r in read(chebi_dir / "compounds.tsv.gz") if r["stars"] == stars}
    seen, counts = set(), {"smiles": 0, "inchi": 0, "skipped": 0}
    with open(out, "w") as o:
        o.write(f"# ChEBI {stars}-star compounds: structure, name, id\n")
        for r in read(chebi_dir / "structures.tsv.gz"):
            c = compounds.get(r["compound_id"])
            if not c or c["chebi_accession"] in seen:
                continue
            smiles, structure = r["smiles"], None
            if smiles and "*" not in smiles and Chem.MolFromSmiles(smiles) is not None:
                structure = smiles
                counts["smiles"] += 1
            elif "*" not in smiles and r["standard_inchi"] and Chem.MolFromInchi(r["standard_inchi"]):
                structure = r["standard_inchi"]
                counts["inchi"] += 1
            if structure is None:
                counts["skipped"] += 1
                continue
            seen.add(c["chebi_accession"])
            o.write(f"{structure}\t{c['name']}\t{c['chebi_accession']}\n")
    print(counts, file=sys.stderr)


if __name__ == "__main__":
    main(*sys.argv[1:4])
