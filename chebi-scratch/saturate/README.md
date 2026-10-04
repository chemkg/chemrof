# Saturating ChEBI 3-star structures

A first full run of `chemrof saturate` over ChEBI, and a comparison of the
result with ChEBI itself.

## Recipe

```bash
mkdir -p chebi && cd chebi
for f in structures compounds relation; do
  curl -O https://ftp.ebi.ac.uk/pub/databases/chebi/flat_files/$f.tsv.gz
done
cd ..
python chebi-scratch/saturate/chebi_seeds.py chebi seeds_3star.tsv          # 45,970 seeds
chemrof saturate seeds_3star.tsv -w 4 -f json -o chebi3_saturated.json     # ~20 min on 4 cores
python chebi-scratch/saturate/compare_chebi.py chebi3_saturated.json chebi
```

`-f owl` writes OWL instead (`--workers` also parallelises the OWL export):
the run above with `-f owl` takes ~36 min and writes a 949 MB OWL
Functional Syntax file (5.9M lines). Parsing all of it in one go with
pyhornedowl needs more than 14 GB of RAM; each chunk is parsed by linkml-owl
during export, and a 200k-axiom slice of the merged file parses cleanly.

## Results (ChEBI flat files of October 2026)

Seeds: 45,970 3-star compounds with a structure (42,780 from SMILES, 3,190
from InChI where RDKit cannot kekulise ChEBI's SMILES; 6,986 skipped, mostly
R-group structures). Default generators (`stereo,salt,protonation`),
`--max-siblings 64`.

| | |
|---|---|
| entities | 454,007 |
| seeds (447 ChEBI entries share a structure with another; the first one's id and name are kept) | 45,523 |
| generated, already in ChEBI (by InChIKey) | 2,542 |
| generated, not in ChEBI | 279,353 |
| racemates (not compared) | 126,589 |

By type: 253,516 `Enantiomer`, 126,589 `RacemicMixture`, 35,885
`SmallMolecule`, 16,740 `Stereoisomer`, 13,033 `MolecularAnion`, 6,221
`MolecularCation`, 1,332 `ChemicalSalt`, and atoms.

Links: 106,285 `has_major_microspecies_at_pH7_3`, 72,834 conjugate
acid/base pairs, 21,898 `tautomer_of` (zwitterions), 252,660
`enantiomer_form_of`.

Recall of ChEBI's own links, between pairs of entities both in the graph:

| ChEBI relation | recovered |
|---|---|
| is conjugate acid/base of | 6,048 / 7,482 (80.8%) |
| is enantiomer of | 1,148 / 1,235 (93.0%) |
| is tautomer of | 492 / 674 (73.0%) |

## Observations

- Stereo enumeration dominates: enantiomers and racemates are 84% of the
  graph. Every stereo family of up to 64 members is enumerated in full, with
  a racemate per mirror pair; ChEBI has few of these. A lower
  `--max-siblings` (bigger families then get only parent + mirror + racemate)
  or dropping the `stereo` generator gives a much smaller graph.
- Conjugate acid/base misses are mostly ChEBI's intermediate charge states
  (citrate(1-), citrate(2-)): only the pH 7.3 major microspecies is
  generated. Tautomer misses are mostly keto/enol and lactam/lactim pairs,
  which need the (off by default) `tautomer` generator.
- Multi-fragment non-salts (drug hydrochlorides written `X.Cl`) are not
  decomposed; the generators skip them.
- One 100-seed chunk took ~20 minutes of the run; some molecule in ChEBI
  3-star rows 14,101-14,200 is very slow to saturate (not yet identified).
