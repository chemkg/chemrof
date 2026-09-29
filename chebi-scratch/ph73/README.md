# Open rules for the pH 7.3 major microspecies

An open, rule-based replacement for the ChemAxon-computed rows of Rhea's
[`chebi_pH7_3_mapping.tsv`](https://ftp.expasy.org/databases/rhea/tsv/chebi_pH7_3_mapping.tsv).
The predictor is `chemrof.converter.protonation.predict_major_microspecies`
([source](../../src/chemrof/converter/protonation.py)). It uses only RDKit:
SMARTS rules plus a few heuristics for groups that interact.

There was no separate rule-learning loop (LEIA-style). An agent wrote the rules
directly, checking each one against the Rhea file with `audit.py`, and scored
every version on a training split. The test split was held back until the end.

## Benchmark

- Rhea mapping downloaded 2026-09-29 (Last-Modified 2026-09-02): 122,732 rows.
- ChEBI structures from the `flat_files` release.
- 107,437 rows have parseable structures for both IDs and no R-groups. Of these,
  7,706 map to a *different* ChEBI entity ("changed").
- The train/test split (80/20) is by target ID, so all protonation forms of a
  compound land on the same side.

There are two scores:

- **ID**: the predicted structure is looked up in ChEBI. If it is not there,
  the entry maps to itself. This is how Rhea's file behaves, since it can only
  point at entities that exist, and it is the score that matters for replacing it.
- **STRUCT**: exact canonical-SMILES match with Rhea's target. This is stricter,
  because Rhea maps many entries to themselves only when the charged form is
  missing from ChEBI.

| predictor (test split) | ID all | ID changed | STRUCT all | STRUCT changed |
|---|---|---|---|---|
| identity (change nothing) | 0.927 | 0.000 | 0.927 | 0.000 |
| Dimorphite-DL 2.0, pH 7.3, precision 0 | 0.985 | 0.807 | 0.670 | 0.807 |
| **chemrof rules** | **0.991** | **0.913** | **0.966** | **0.913** |

The rules score 0.919 on the changed rows in training and 0.913 on the test
split, so there is little overfitting.

Dimorphite-DL protonates amide N, deprotonates simple phenols (pKa ~10) and
deprotonates the histidine imidazole. It keeps a high ID score only because
most of those wrong forms are not in ChEBI.

## Conventions learned from Rhea

Counts come from `audit.py` over training targets whose protonation group has
more than one member in ChEBI.

- Phosphate monoesters go to 2−, diesters to 1−. Phosphonates go to **1−**
  (22 of 42 OH deprotonated, i.e. one per P). Inorganic phosphate is HPO4 2-,
  diphosphate HP2O7 3-, carbonate HCO3-.
- Amidines and guanidines are protonated (107/107) and drawn as C=[NH2+].
- Aminal N (N–C–N) is never protonated (0/107). Morpholine N stays neutral (3/4).
- In 1,2-diamines (piperazine etc.) only one N is protonated. In 1,3-diamines
  both usually are (72/101).
- Phenols are neutral (1151/1381) except: flavone/isoflavone 7-OH (67/67);
  flavone 5-OH when 7-O is substituted (21/25); o/p-nitrophenols;
  2,6-dihalophenols.
- Plain imines are neutral (80/103), but imino acids (C=N–COO−) are protonated.
- Single atoms and metal-containing species are left unchanged. Rhea maps
  these by hand.

## Disagreements

`disagreements.tsv` lists the 877 rows (of 107,437) where the rules and Rhea
pick different ChEBI IDs:

- 574 **rules miss the change**. These are mostly remaining rule gaps:
  poly-amine charge alternation, anthraquinone/polyketide phenols,
  tetracycline-type enols, porphyrin/corrin N, and odd radicals.
- 303 **rules pick another existing ChEBI entity**. This is where to look for
  errors in the Rhea file, but most are still rule gaps rather than Rhea errors.

## Sodium

In the current file, sodium atom (CHEBI:26708) and sodium(1+) (CHEBI:29101)
both map to themselves, and nothing else maps to either. This benchmark found
no sodium error.

## Reproducing

```sh
./fetch.sh                                 # data/ (gitignored)
uv run python prep.py                      # data/chebi_smiles.tsv
uv run python bench.py                     # data/bench.tsv (+ split)
uv run python idx.py                       # data/chebi_can_idx.pkl
PYTHONPATH=../../src uv run python evalr.py p_chemrof test
PYTHONPATH=../../src uv run python evalr.py p_chemrof all && uv run python disagree.py
uv run python audit.py '<SMARTS with :1 on the atom of interest>'
uv run python fails.py data/out_p_chemrof_train.tsv 'False:NEG' 10
```

`p_dimorphite.py` needs `pip install dimorphite_dl`.
