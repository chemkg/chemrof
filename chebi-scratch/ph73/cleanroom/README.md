# Clean-room pH 7.3 rules

## Why

Rhea's `chebi_pH7_3_mapping.tsv` has 122,732 rows:

- 121,834 are labelled `computation` (reportedly ChemAxon). These include
  **all** 8,900 rows that map an entry to a different protonation form.
- 898 are labelled `curation`, and all of them map an entry to itself.

The first rule set in `chemrof.converter.protonation` was written by checking
rules against those computed rows, so in effect it was fitted to ChemAxon
output. No ChemAxon software or code was used, but if reusing ChemAxon output
is a problem, those rules inherit it.

`chemrof.converter.protonation_cleanroom` rebuilds the rules without Rhea or
ChemAxon output. It uses the same engine with its own rule tables.

## Sources

Rules may only come from:

1. **Measured pKa** from the raw ChEMBL25 and DataWarrior extracts in
   Baltruschat & Czodrowski, *Machine learning meets pKa*
   ([doi:10.5281/zenodo.7884512](https://doi.org/10.5281/zenodo.7884512),
   datasets CC BY 4.0). That gives 11,738 molecules, 5,603 of which have a
   single ionizable group.
   - The authors' cleaned and combined files are **not** used. Their pipeline
     dropped values that disagreed with ChemAxon Marvin and labelled the
     ionizing atom with Marvin.
   - To know which atom a measured pKa belongs to without Marvin,
     `audit_exp.py` uses only molecules with a single ionizable group.
2. **Textbook group pKa values**, cited per rule.

Rhea is used only as an outside comparison, never to choose a rule. Each rule's
evidence is in `PROVENANCE` in the module; rules that only Rhea supported are
in `DROPPED`.

## Differences from the current rules

| Rule | Evidence without Rhea | Clean-room |
|---|---|---|
| flavone / isoflavone 7-OH ionized | measured median 7.35 (n=3), 1 of 3 ionized | dropped |
| flavone 5-OH ionized when 7-O substituted | no data; H-bonded to C4=O, pKa ~11 | dropped |
| imino acid C=N protonated | no data or textbook source | dropped |
| ring imines: non-fused rings only | 1-methyladenosine pKaH ~8.3–8.8 | restriction removed |

Every other rule is kept. Each has measured support (for example amines:
n=1,781, 81% protonated; carboxylic acids: n=1,005, 98% ionized) or a cited
textbook value.

## Results

`evaluate.py` scores agreement with measured pKa. The test set is the IUPAC
molecules usable by `iupac_eval.py` that are **not** in the CC BY training
data, matched by InChIKey: 2,152 of 3,380.

| Measured-pKa match (95% CI) | all test (2,152) | charged (1,175) | in ChEBI + Rhea (217) |
|---|---|---|---|
| **clean-room rules** | **0.895** [0.882, 0.908] | **0.854** | **0.959** |
| current rules | 0.894 | 0.849 | 0.959 |
| first rules (Rhea-fitted) | 0.827 | 0.731 | 0.954 |
| ChemAxon (via Rhea) | – | – | 0.945 |

- Against measured pKa, the clean-room rules are as good as the current rules
  (+5 fixed, −1 broken).
- On molecules Rhea covers, they score 95.9% vs ChemAxon's 94.5%: 3 molecules
  only the clean-room rules get right, 0 only ChemAxon gets right. The
  difference is borderline (+0.014 [0.000, 0.032]).

Agreement with Rhea (`evalr.py`, all splits, aggregate only) drops as
expected:

- changed rows: 90.2% vs 91.6% for the current rules (14 fixed, 129 broken);
- 119 rows that Rhea leaves unchanged now break as well.

Nearly all of the loss comes from the dropped Rhea-only conventions:

- flavone phenolates: 119, plus flavone sources that are already anions;
- imino acids: 18;
- fused ring imines: 5.

## Caveats

- **Contamination.** The current rules' hill-climbing rounds used IUPAC train
  and dev failures, and this IUPAC test set includes those molecules. The
  clean-room rules keep those rules (each is also supported by the CC BY data
  or a textbook value), so the test is not fully blind for them.
- **Licence check.** ChEMBL data is CC BY-SA upstream. The redistributed
  extract is labelled CC BY 4.0, but the ChEMBL terms may still apply.
- **Weak evidence.** Several rules rest on a textbook value or very few
  measurements (aminal N, aza-imides, thiophosphates); `PROVENANCE` says which.

## Reproducing

From `chebi-scratch/ph73`:

```sh
uv run python cleanroom/exp_data.py         # clones the CC BY data into data/mlpka, writes data/exp_pka.tsv
(cd cleanroom && uv run python audit_exp.py '[OX2H1:1]c')   # measured pKa for a group
(cd cleanroom && PYTHONPATH=../../../src uv run python audit_rules.py chemrof.converter.protonation_cleanroom)
PYTHONPATH=../../src uv run python cleanroom/evaluate.py
PYTHONPATH=../../src uv run python evalr.py p_cleanroom --split all --unseal --compare p_chemrof
```
