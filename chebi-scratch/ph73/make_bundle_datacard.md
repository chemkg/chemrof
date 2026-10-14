# pH 7.3 major-microspecies benchmark, version {version}

A benchmark for predicting the major protonation state of ChEBI compounds at
pH 7.3. It pairs each ChEBI entity with Rhea's pH 7.3 mapping and adds
predictions from open, RDKit-only rules (`chemrof.converter.protonation`).
Built at chemrof commit `{commit}`. Background and method:
`chebi-scratch/ph73/README.md` and `chebi-scratch/ph73/cleanroom/README.md` in
chemkg/chemrof.

Versions are published under the concept DOI
https://doi.org/10.5281/zenodo.23324328 (all versions); version 2026-10-11 is
https://doi.org/10.5281/zenodo.23324329.

## What changed in 2026-10-14

- Predictions now come from three rule sets.
  - The **default** is the new clean-room set. It is derived only from
    measured pKa values (CC BY 4.0 data) and textbook group pKas, never from
    Rhea, whose changed rows are computed by ChemAxon.
  - The Rhea-fitted, hill-climbed set (the 2026-10-11 "final" rules) and the
    first rules are kept for comparison.
- Column names changed to match (`pred_default_*`, `pred_rhea_fitted_*`,
  `pred_original_*`).
- `disagreements` is based on the default rules.

## Files

| file | rows | contents |
|---|---|---|
| `benchmark.parquet` | {benchmark:,} | one row per Rhea mapping row with usable structures, plus predictions |
| `disagreements.parquet` | {disagreements:,} | rows where the default rules and Rhea pick different ChEBI IDs |
| `chebi_structures.parquet` | {chebi_structures:,} | ChEBI SMILES used, with broken SMILES rebuilt from molfiles |
| `chebi_unparseable_smiles.parquet` | {chebi_unparseable_smiles:,} | ChEBI SMILES that RDKit cannot parse, with molfile-derived SMILES (see chemkg/chemrof#101) |
| `rhea_chebi_pH7_3_mapping.tsv.gz` | | the exact Rhea file used |
| `SHA256SUMS` | | checksums |

## Sources and versions

- **Rhea** `chebi_pH7_3_mapping.tsv`: downloaded 2026-09-29 (Last-Modified
  2026-09-02).
- **ChEBI** `flat_files/structures.tsv.gz` and `compounds.tsv.gz`: downloaded
  2026-09-29. Used for `benchmark`, `disagreements` and `chebi_structures`.
- `chebi_unparseable_smiles` comes from the later 2026-10-06 ChEBI release.

## benchmark.parquet

Rows are Rhea mapping rows. Rows were dropped where either structure was
missing or had R-groups (`*`).

| column | meaning |
|---|---|
| `chebi_id`, `chebi_name` | the source ChEBI entity |
| `rhea_ph7_3_id`, `rhea_ph7_3_name` | Rhea's pH 7.3 form of it |
| `rhea_origin` | `computation` (reportedly ChemAxon) or `curation` |
| `split` | `train` / `dev` / `sealed`, assigned by target ID (see README) |
| `changed` | true if Rhea maps to a different entity ({changed:,} rows) |
| `smiles`, `rhea_ph7_3_smiles` | RDKit canonical SMILES |
| `pred_default_smiles` | prediction from the default (clean-room) rules |
| `pred_default_id` | that structure looked up in ChEBI; falls back to `chebi_id` if absent, as Rhea's file does |
| `default_matches_rhea_structure` | exact canonical-SMILES match with Rhea's form |
| `default_matches_rhea_id` | `pred_default_id` equals `rhea_ph7_3_id` |
| `*_rhea_fitted_*` | the same, for the Rhea-fitted, hill-climbed rules |
| `*_original_*` | the same, for the rules as first committed (355d3cf) |

On changed rows, ID agreement with Rhea is:

- {default_id:.1%} for the default (clean-room) rules;
- {rhea_fitted_id:.1%} for the Rhea-fitted rules;
- {original_id:.1%} for the original rules.

Lower agreement with Rhea is expected for the clean-room rules: against
measured pKa they match the Rhea-fitted rules and are slightly ahead of
ChemAxon on the molecules Rhea covers (see the clean-room README).

All splits are included; the sealed split has already been scored, so this
bundle is no longer a blind test set.

## Not included

- Scores against measured pKa come from the IUPAC Digitized pKa Dataset, which
  is CC BY-NC 4.0. That data and anything derived from it per molecule are left
  out. `iupac_eval.py` in the repo regenerates them.
- The CC BY 4.0 measured-pKa data used to derive the clean-room rules is not
  repackaged here: cite and download it from
  https://doi.org/10.5281/zenodo.7884512.

## Licence

- ChEBI and Rhea are CC BY 4.0, so this bundle is redistributed under CC BY 4.0.
- Please cite ChEBI (https://www.ebi.ac.uk/chebi/) and Rhea
  (https://www.rhea-db.org/) when using it.
- The code that produced it (chemkg/chemrof) is CC0.
