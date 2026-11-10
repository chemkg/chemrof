# Rhea: ChEBI major microspecies at pH 7.3

Cached copies of Rhea's `chebi_pH7_3_mapping.tsv`, which maps ChEBI
entities to their major microspecies at pH 7.3.

| File | Rhea release | Release date | Rows | sha256 of uncompressed TSV |
|---|---|---|---|---|
| `chebi_pH7_3_mapping-r143.tsv.gz` | 143 | 2026-11-04 | 122,872 | `99b04938a37ad6432cea67d4ea4df00323779700661ae34429564d6b6fe25170` |

Columns (release 143): `CHEBI`, `CHEBI_PH7_3`, `ORIGIN`
(`computation` or `curation`). IDs are bare numbers, without the `CHEBI:` prefix.

## Why it is cached

Release 143 is the last release that covers all of ChEBI. The
[Rhea news](https://ftp.expasy.org/databases/rhea/rhea_news.html) for
release 143 says that, because the license of the software used to
compute the major microspecies changed, from release 144 onward:

- the mapping is provided only for ChEBI compounds used in Rhea or UniProt;
- the third column (`ORIGIN`) is dropped.

About 16% of the release 143 rows map to a ChEBI ID used in Rhea, so the
live file is expected to lose most of its rows. The cached copy keeps the
full mapping available to the ETL (`database/chebi_pH7_3_mapping.tsv` in
`etl.mk`) and as a reference for `src/chemrof/converter/protonation.py`.

Up to release 143 the file changed very little between releases: from
release 130 to 143 only 12 of about 96,000 shared ChEBI IDs changed their
major microspecies; the rest of the differences are added or removed IDs.

## Recreating or adding a release

The snapshots are built from the release archives in
<https://ftp.expasy.org/databases/rhea/old_releases/>:

```bash
make external/rhea/chebi_pH7_3_mapping-r143.tsv.gz
```

This streams the whole release archive (about 400 MB) and keeps only the
pH 7.3 file. The same rule works for any release number.

## License

Rhea data are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Rhea's
copyright statement is in `LICENSE.txt` next to this file and must be
kept with these copies.
