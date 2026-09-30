# Open rules for the pH 7.3 major microspecies

An open, rule-based replacement for the ChemAxon-computed rows of Rhea's
[`chebi_pH7_3_mapping.tsv`](https://ftp.expasy.org/databases/rhea/tsv/chebi_pH7_3_mapping.tsv).
The predictor is `chemrof.converter.protonation.predict_major_microspecies`
([source](../../src/chemrof/converter/protonation.py)). It uses only RDKit:
SMARTS rules plus a few heuristics for groups that interact.

There was no separate rule-learning loop (LEIA-style). An agent wrote the rules
directly, checking each one against the Rhea file with `audit.py`, and scored
every version on a training split.

## Benchmark 1: agreement with Rhea

- Rhea mapping downloaded 2026-09-29 (Last-Modified 2026-09-02): 122,732 rows.
- ChEBI structures from the `flat_files` release.
- 107,437 rows have parseable structures for both IDs and no R-groups. Of these,
  7,706 map to a *different* ChEBI entity ("changed").

There are two scores:

- **ID**: the predicted structure is looked up in ChEBI. If it is not there,
  the entry maps to itself. This is how Rhea's file behaves, since it can only
  point at entities that exist, and it is the score that matters for replacing it.
- **STRUCT**: exact canonical-SMILES match with Rhea's target. This is stricter,
  because Rhea maps many entries to themselves only when the charged form is
  missing from ChEBI.

**ID on changed rows is the primary metric.** ID on all rows is near its
ceiling (92.7% for "change nothing"), so it hides differences.

### Splits

Splits are by target ID, so every protonation form of a compound lands on the
same side.

| split | rows | changed | use |
|---|---|---|---|
| train | 85,780 | 6,131 | rules may be written from it; failures may be read |
| dev | 10,786 | 785 | accept/reject decisions only (`--compare`); failures are not read |
| sealed | 10,871 | 790 | final score only; `evalr.py` refuses it without `--unseal` and logs each use |

History, so the numbers can be judged fairly:

- The first rule set used an 80/20 train/test split.
- The 20% test split had its aggregate score checked about five times during
  development, and one decision was influenced by it. Its failures were never
  read, apart from a 40-row sample of disagreements drawn from all splits.
- On 2026-09-30 that 20% was halved into dev and sealed. Sealed has not been
  scored since.

### Results

Scores on dev with 95% bootstrap intervals, resampled by target:

| predictor | ID changed | ID all | STRUCT changed | STRUCT all |
|---|---|---|---|---|
| identity (change nothing) | 0.000 | 0.927 | 0.000 | 0.927 |
| Dimorphite-DL 2.0, pH 7.3, precision 0 | 0.806 [0.777, 0.835] | 0.985 | 0.806 | 0.664 |
| **chemrof rules** | **0.919 [0.897, 0.940]** | **0.992** | **0.919** | **0.968** |

- Train (ID changed) is 0.919 [0.910, 0.926], the same as dev, so there is no
  sign of overfitting.
- Dev has only 785 changed rows, so its interval is about ±2 points.
- To decide on a rule change, use the paired comparison
  `evalr.py p_new --split dev --compare p_chemrof`. It counts only the rows the
  change fixes or breaks, and prints ACCEPT only when the 95% interval of the
  difference is above zero.

Dimorphite-DL protonates amide N, deprotonates simple phenols (pKa ~10) and
deprotonates the histidine imidazole. It keeps a high ID-all score only because
most of those wrong forms are not in ChEBI.

## Benchmark 2: agreement with measured pKa (IUPAC)

Benchmark 1 grades against ChemAxon's output. So it rewards reproducing
ChemAxon's quirks and would penalise a rule that fixes a real ChemAxon error.
`iupac_eval.py` is an independent grader. It uses the
[IUPAC Digitized pKa Dataset](https://github.com/IUPAC/Dissociation-Constants)
(v2.4, high-confidence subset), keeping only measurements that are:

- at 20–30 °C;
- in water (no cosolvent);
- not assessed "Uncertain";
- plain pKa or pKaH labels.

For each neutral molecule the expected net charge at pH 7.3 is
`#(pKaH > 7.3) − #(pKa < 7.3)`. This checks the charge state, not which atom
carries it.

Two filters make the grader trustworthy:

- **Borderline molecules are dropped.** These have a pK within 0.5 of 7.3, so
  no single form clearly dominates.
- **Complete pKa lists only.** Many entries list fewer pKas than the molecule
  has ionizable groups. Terephthalic acid, for example, lists one pKa, and
  tyramine lists only its phenol. Their expected charge is then wrong. When
  checking the grader, most cases where the rules and ChemAxon *both* "failed"
  were of this kind. A broad, rule-independent group counter flags them, and
  the table below keeps only complete lists.

Rhea's charges were looked up through ChEBI by InChIKey. That is only possible
for molecules that are in ChEBI and in the Rhea file.

| predictor | all (n=3380) | charged (1769) | in ChEBI+Rhea (563) | in Rhea, charged (204) |
|---|---|---|---|---|
| identity | 0.477 | 0.000 | 0.638 | 0.000 |
| Dimorphite-DL | 0.691 [0.675, 0.707] | 0.739 | 0.723 | 0.863 |
| **chemrof rules** | **0.864 [0.851, 0.875]** | **0.781** | **0.970 [0.956, 0.982]** | **0.941** |
| Rhea (ChemAxon) | – | – | 0.979 [0.966, 0.989] | 0.956 |

- On molecules in Rhea, the rules and ChemAxon are statistically tied on
  measured charge. The paired difference is −0.009 [−0.020, +0.002]; only the
  rules are right on 2 molecules, only ChemAxon on 7.
- On the wider IUPAC set, which is mostly not biochemical, the rules drop to
  0.864. They were tuned on ChEBI/Rhea biochemicals, so this is the main place
  to improve. Some misses shared with ChemAxon are real, e.g. the
  cyclohexane-1,3-dione keto form (pKa 5.2), squaric acid and tropolone.
- The IUPAC set has not been used to tune any rule. To start tuning on it,
  split it into dev and sealed halves first.

Licence: the IUPAC dataset is CC BY-NC 4.0, which is incompatible with this
repo's CC0. It is downloaded into `data/` (gitignored), and only aggregate
scores are committed here.

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

`disagreements.tsv` lists the 773 train and dev rows (of 96,566) where the
rules and Rhea pick different ChEBI IDs. Sealed rows are excluded until
unsealing.

- 507 **rules miss the change**. These are mostly remaining rule gaps:
  poly-amine charge alternation, anthraquinone/polyketide phenols,
  tetracycline-type enols, porphyrin/corrin N, and odd radicals.
- 266 **rules pick another existing ChEBI entity**. This is where to look for
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
PYTHONPATH=../../src uv run python evalr.py p_chemrof --split dev
PYTHONPATH=../../src uv run python evalr.py p_new --split dev --compare p_chemrof   # accept/reject
PYTHONPATH=../../src uv run python evalr.py p_chemrof --split all && uv run python disagree.py
uv run --with dimorphite_dl python iupac_eval.py      # clones the IUPAC dataset into data/
uv run python audit.py '<SMARTS with :1 on the atom of interest>'
uv run python fails.py data/out_p_chemrof_train.tsv 'False:NEG' 10
```

`p_dimorphite.py` needs `dimorphite_dl` (`uv run --with dimorphite_dl ...`).
