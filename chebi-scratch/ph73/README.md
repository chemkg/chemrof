# Open rules for the pH 7.3 major microspecies

An open, rule-based replacement for the ChemAxon-computed rows of Rhea's
[`chebi_pH7_3_mapping.tsv`](https://ftp.expasy.org/databases/rhea/tsv/chebi_pH7_3_mapping.tsv).
The predictor is `chemrof.converter.protonation.predict_major_microspecies`
([source](../../src/chemrof/converter/protonation.py)). It uses only RDKit:
SMARTS rules plus a few heuristics for groups that interact.

There was no separate rule-learning loop (LEIA-style). An agent wrote the
rules, using two graders:

1. **Rhea**: does the prediction match Rhea's mapping (i.e. ChemAxon)?
2. **IUPAC**: does the prediction's charge match measured pKa values?

The first rule set was written against Rhea alone. Ten further rounds of
hill-climbing used both graders under a fixed acceptance rule; see
[`hillclimb_log.md`](hillclimb_log.md).

**Since 2026-10-14 the default rules are the clean-room set**, derived only
from measured pKa (CC BY 4.0 data) and textbook values, because Rhea's changed
rows are all ChemAxon output. The Rhea-fitted rules described below are kept as
`RHEA_FITTED_RULES`. See [`cleanroom/README.md`](cleanroom/README.md); the scores
below are for the Rhea-fitted rules.

## Data

The benchmark, predictions, broken-SMILES list and the exact Rhea file used
are published on Zenodo: [doi:10.5281/zenodo.23324329](https://doi.org/10.5281/zenodo.23324329)
(all versions: [doi:10.5281/zenodo.23324328](https://doi.org/10.5281/zenodo.23324328);
CC BY 4.0, built by `make_bundle.py`). Version 2026-10-14 adds the clean-room
predictions as the default.

## Final scores (sealed sets, scored once)

The sealed sets were scored once, at the end (`data/unseal.log`).

| | rules as first committed | **final rules** | ChemAxon (Rhea) |
|---|---|---|---|
| Rhea sealed, changed rows (n=856) | 0.908 | **0.908 [0.885, 0.928]** | (the reference) |
| Rhea sealed, all rows (n=11,486) | 0.990 | **0.991** | (the reference) |
| IUPAC sealed, all molecules (n=1,658) | 0.870 | **0.918 [0.905, 0.931]** | – |
| IUPAC sealed, charged molecules (n=865) | 0.792 | **0.881** | – |
| IUPAC sealed, molecules in ChEBI+Rhea (n=311) | 0.981 | **0.981** | 0.987 |

- **Hill-climbing improved agreement with measured pKa by +4.8 points
  [3.7, 5.9] on unseen molecules** (84 fixed, 5 broken). Agreement with Rhea
  did not change.
- On molecules that Rhea covers, the rules and ChemAxon are statistically tied
  against measured pKa: −0.006 [−0.016, +0.000].
- Dimorphite-DL scores 0.768 on IUPAC sealed and 0.817 on Rhea dev changed
  rows.

## Benchmark 1: agreement with Rhea

- Rhea mapping downloaded 2026-09-29 (Last-Modified 2026-09-02): 122,732 rows.
- ChEBI structures from the `flat_files` release.
- The ChEBI flat-file SMILES drop the H on some aromatic NH atoms (indoles,
  purines, pterins...), so they don't parse. `prep.py` rebuilds those 13,089
  structures from the molfiles.
- 113,385 rows have structures for both IDs and no R-groups. Of these, 8,402
  map to a *different* ChEBI entity ("changed").
- Until 2026-10-11 the molfile fallback was missing and the benchmark had
  107,437 rows. Older numbers in the git history refer to that version.

There are two scores:

- **ID**: the predicted structure is looked up in ChEBI. If it is not there,
  the entry maps to itself. This is how Rhea's file behaves, since it can only
  point at entities that exist, and it is the score that matters for replacing it.
- **STRUCT**: exact canonical-SMILES match with Rhea's target. This is stricter,
  because Rhea maps many entries to themselves only when the charged form is
  missing from ChEBI.

**ID on changed rows is the primary metric.** ID on all rows is near its
ceiling (92.4% for "change nothing"), so it hides differences.

### Splits

Splits are by target ID, so every protonation form of a compound lands on the
same side.

| split | rows | changed | use |
|---|---|---|---|
| train | 90,510 | 6,684 | rules may be written from it; failures may be read |
| dev | 11,389 | 862 | accept/reject decisions only (`--compare`); failures are not read |
| sealed | 11,486 | 856 | final score only; `evalr.py` refuses it without `--unseal` and logs each use |

History, so the numbers can be judged fairly:

- The first rule set used an 80/20 train/test split.
- The 20% test split had its aggregate score checked about five times during
  development, and one decision was influenced by it. Its failures were never
  read, apart from a 40-row sample of disagreements drawn from all splits.
- On 2026-09-30 that 20% was halved into dev and sealed. Sealed was first
  scored on 2026-10-11, after hill-climbing ended.

### Results on dev

95% bootstrap intervals, resampled by target:

| predictor | ID changed | ID all | STRUCT changed | STRUCT all |
|---|---|---|---|---|
| identity (change nothing) | 0.000 | 0.924 | 0.000 | 0.924 |
| Dimorphite-DL 2.1.0, pH 7.3, precision 0 | 0.817 [0.787, 0.846] | 0.985 | 0.817 | 0.810 |
| **chemrof rules (final)** | **0.918 [0.895, 0.939]** | **0.991** | **0.918** | **0.966** |

- Train (ID changed) is 0.917 [0.909, 0.925], so there is no sign of
  overfitting.
- Dev has 862 changed rows, so its interval is about ±2 points.
- Dimorphite-DL with `max_variants=1` is not deterministic: about 9% of IUPAC
  molecules got a different charge between runs. Its scores are only a rough
  baseline.
- Dimorphite-DL protonates amide N, deprotonates simple phenols (pKa ~10) and
  deprotonates the histidine imidazole. It keeps a high ID-all score only
  because most of those wrong forms are not in ChEBI.

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
  were of this kind. A broad, rule-independent group counter flags them.

That leaves 3,380 molecules, split by InChIKey into train (835), dev (887) and
sealed (1,658). Before the split, the full set had been scored once, and 38
molecules where both methods disagreed with it had been read to check the
grader.

Rhea's charges were looked up through ChEBI by InChIKey. That is only possible
for molecules that are in ChEBI and in the Rhea file.

Licence: the IUPAC dataset is CC BY-NC 4.0, which is incompatible with this
repo's CC0. It is downloaded into `data/` (gitignored), and only aggregate
scores are committed here.

## Hill-climbing

Acceptance rule, fixed before any IUPAC failure was read:

- each round makes one change, aimed at one root cause seen in *train*
  failures;
- the change is kept only if it fixes more than it breaks on train (Rhea +
  IUPAC) and on dev (Rhea + IUPAC), with no significant regression on either
  dev set;
- finally, the cumulative change must beat noise on dev before the sealed sets
  are scored.

`round.sh` runs one round: the working-tree rules against the last accepted
copy (`p_baseline`) on all four sets. `p_original` is the rule set as first
committed.

The cumulative change on dev, against the original rules:

- IUPAC dev: +5.2 points [3.5, 6.9], 50 fixed and 4 broken;
- Rhea dev: changed rows +2/−0, unchanged rows +1/−0.

The sealed gain (+4.8) matched the dev gain.

The rounds, in order (details and per-set counts in
[`hillclimb_log.md`](hillclimb_log.md)):

1. Bug: the 4-aminopyridine rule matched nitro N.
2. Sulfinic acids deprotonated.
3. Thiophenols deprotonated.
4. Exocyclic imines on non-fused azine/azole rings protonated.
5. Bug: crash on explicit-H (deuterium) acids.
6. Tropolones deprotonated.
7. gem-Dinitro carbon acids deprotonated.
8. Cyclic 1,3-diketones converted to the enolate.
9. Amines with two β electron-withdrawing groups left neutral.
10. Aza-imide NH deprotonated.

Where Rhea and measured pKa conflict, the rules side with Rhea:

- N1-substituted adenines stay neutral (round 4 was restricted to non-fused
  rings).
- A tropolone beside a carboxylate stays neutral.

Places where Rhea may itself be wrong:

- **Flavin N3–H.** Deprotonated in Rhea (e.g. FAD(3−)), but its pKa is ~10.
- **6-Azauridine-MP.** Neutral in Rhea, but its pKa is ~6.7.
- **Uric acid (CHEBI:17775).** Maps to itself in Rhea, but its pKa is ~5.4.

## Conventions learned from Rhea

Counts come from `audit.py` over training targets whose protonation group has
more than one member in ChEBI.

- Phosphate monoesters go to 2−, diesters to 1−. Phosphonates go to **1−**
  (22 of 42 OH deprotonated, i.e. one per P). Inorganic phosphate is HPO4 2-,
  diphosphate HP2O7 3-, carbonate HCO3-. Sulfinic acids go to the anion (16/16).
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

`disagreements.tsv` lists the 870 train and dev rows (of 101,899) where the
rules and Rhea pick different ChEBI IDs. Sealed rows are excluded.

- 559 **rules miss the change**. These are mostly remaining rule gaps:
  poly-amine charge alternation, anthraquinone/polyketide phenols,
  tetracycline-type enols, porphyrin/corrin N, and odd radicals.
- 311 **rules pick another existing ChEBI entity**. This is where to look for
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
export PYTHONPATH=../../src
uv run python evalr.py p_chemrof --split dev
uv run python iupac_eval.py table p_chemrof --split dev   # clones the IUPAC dataset into data/

# a hill-climbing round: freeze the accepted rules, edit, compare
mkdir -p data/baseline && cp ../../src/chemrof/converter/protonation.py data/baseline/protonation_baseline.py
git show 355d3cf:src/chemrof/converter/protonation.py > data/baseline/protonation_original.py
./round.sh

uv run python evalr.py p_chemrof --split all && uv run python disagree.py
uv run python audit.py '<SMARTS with :1 on the atom of interest>'
uv run python fails.py data/out_p_chemrof_train.tsv 'False:NEG' 10
```

`p_dimorphite.py` needs `dimorphite_dl` (`uv run --with dimorphite_dl ...`).
