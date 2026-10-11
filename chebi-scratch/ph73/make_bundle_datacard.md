# pH 7.3 major-microspecies benchmark, version {version}

A benchmark for predicting the major protonation state of ChEBI compounds at
pH 7.3. It pairs each ChEBI entity with Rhea's pH 7.3 mapping and adds
predictions from open, RDKit-only rules (`chemrof.converter.protonation`).
Built at chemrof commit `{commit}`. Background and method:
`chebi-scratch/ph73/README.md` in chemkg/chemrof.

## Files

| file | rows | contents |
|---|---|---|
| `benchmark.parquet` | {benchmark:,} | one row per Rhea mapping row with usable structures, plus predictions |
| `disagreements.parquet` | {disagreements:,} | rows where the final rules and Rhea pick different ChEBI IDs |
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
| `rhea_origin` | `computation` (ChemAxon) or `curation` |
| `split` | `train` / `dev` / `sealed`, assigned by target ID (see README) |
| `changed` | true if Rhea maps to a different entity ({changed:,} rows) |
| `smiles`, `rhea_ph7_3_smiles` | RDKit canonical SMILES |
| `pred_final_smiles` | prediction from the final rules |
| `pred_final_id` | that structure looked up in ChEBI; falls back to `chebi_id` if absent, as Rhea's file does |
| `final_matches_rhea_structure` | exact canonical-SMILES match with Rhea's form |
| `final_matches_rhea_id` | `pred_final_id` equals `rhea_ph7_3_id` (primary score) |
| `*_original_*` | the same, for the rules as first committed (355d3cf) |

On changed rows, ID agreement with Rhea is {final_id:.1%} for the final rules
and {original_id:.1%} for the original rules. All splits are included; the
sealed split has already been scored, so this bundle is no longer a blind test
set.

## Not included

Scores against measured pKa come from the IUPAC Digitized pKa Dataset, which is
CC BY-NC 4.0. That data and anything derived from it per molecule are left out.
`iupac_eval.py` in the repo regenerates them.

## Licence

- ChEBI and Rhea are CC BY 4.0, so this bundle is redistributed under CC BY 4.0.
- Please cite ChEBI (https://www.ebi.ac.uk/chebi/) and Rhea
  (https://www.rhea-db.org/) when using it.
- The code that produced it (chemkg/chemrof) is CC0.
