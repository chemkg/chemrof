# CLI Reference

The `chemrof` command-line tool provides utilities for working with
chemical structure data in the chemrof framework.

## Installation

```bash
uv sync
```

This installs the `chemrof` command from the project's entry point.

## Commands

### `chemrof convert`

Convert one or more chemical input strings (SMILES or InChI, auto-detected)
into chemrof-compliant records.

```
chemrof convert [OPTIONS] INPUTS...
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `INPUTS` | One or more SMILES or InChI strings (required). Quote ions: `"[Ca+2]"` |

**Options:**

| Option | Default | Description |
|--------|---------|-------------|
| `--format`, `-f` | `yaml` | Output format: `yaml`, `json`, or `owl` |
| `--enrichers`, `-e` | _(none)_ | Comma-separated list of enricher sources |
| `--classes`, `-c` | _(none)_ | Target chemrof classes (implies `--autochain`) |
| `--autochain` | `false` | Generate interlinked dependent entities |
| `--chemont-source` | _(none)_ | Local ChemOnt labels source for `--enrichers chemont`: DuckDB, Parquet, or TSV/ZST |
| `--chemont-dictionary` | _(auto)_ | ChemOnt dictionary TSV/Parquet when it is not bundled with the source |

### Input format detection

The converter auto-detects the input format:

- Starts with `InChI=` → parsed as InChI
- Otherwise → parsed as SMILES

Non-standard InChI with `/s3` (racemic) automatically triggers `--autochain`
with `--classes RacemicMixture`.

### Output formats

**YAML** (default) — one document per entity, or multi-document YAML for
autochain output:

```bash
chemrof convert CCO
```

```yaml
id: INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N
name: C2H6O
type: chemrof:SmallMolecule
smiles_string: CCO
inchi_string: InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3
empirical_formula: C2H6O
molecular_mass: 46.0419
is_organic: true
```

**JSON** — same structure, JSON-encoded:

```bash
chemrof convert CCO --format json
```

**OWL** — OWL Functional Syntax ontology via linkml-data2owl. Types with
`owl.template` annotations (MonoatomicIon, Enantiomer, RacemicMixture)
produce `EquivalentClasses` axioms. Others produce annotation assertions:

```bash
chemrof convert "[Ca+2]" --format owl
```

```
EquivalentClasses(INCHIKEY:... ObjectIntersectionOf(
  chemrof:MonoatomicIon
  ObjectSomeValuesFrom(chemrof:has_element chemrof:Ca)
  DataHasValue(chemrof:elemental_charge "2"^^xsd:integer)
))
```

### Autochain

The `--classes` option generates interlinked entity graphs. Requesting
`RacemicMixture` generates the chirality-agnostic form, both enantiomers,
and the racemic mixture entity — all with relationship slots populated.

```bash
# Generate full racemate graph from stereo-neutral alanine
chemrof convert "CC(N)C(=O)O" --classes RacemicMixture --format json

# Enantiomers only (no mixture entity)
chemrof convert "CC(N)C(=O)O" --classes Enantiomer

# From a specific enantiomer — generates agnostic + mirror + mixture
chemrof convert "C[C@@H](N)C(=O)O" --classes RacemicMixture

# Racemic InChI auto-triggers autochain
chemrof convert "InChI=1/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/s3"
```

**Chemical salts:** Salt SMILES (multi-fragment, opposite charges) are
auto-detected and decomposed into cation + anion + salt entities:

```bash
# NaCl → Na+ entity, Cl- entity, NaCl salt entity
chemrof convert "[Na+].[Cl-]" --format json

# Sodium acetate
chemrof convert "[Na+].CC([O-])=O" --format json

# Explicit --classes flag
chemrof convert "[Ca+2].[Cl-].[Cl-]" --classes ChemicalSalt --format json
```

**Tautomers:** Enumerate tautomeric forms and cross-link via `tautomer_of`:

```bash
# 2-hydroxypyridine / 2-pyridinone tautomers
chemrof convert "Oc1ccccn1" --classes Tautomer --format json
```

v1 limitation: autochain only supports single-stereocenter molecules.

### Enrichers

Enrichers pull additional data from external databases after RDKit
computes the structural properties. Pass a comma-separated list:

```bash
chemrof convert CCO --enrichers pubchem
chemrof convert CCO --enrichers pubchem,chebi
```

| Source | Status | What it adds |
|--------|--------|-------------|
| `pubchem` | Working | Preferred IUPAC name and PubChem CID (via InChIKey lookup) |
| `chemont` | Working | Ordered ChemOnt/ClassyFire tree classes in `classified_by` (via local lookup store) |
| `chebi` | Stub | Will resolve CHEBI identifiers via OLS |
| `wikidata` | Stub | Will resolve Wikidata QIDs via SPARQL |

#### ChemOnt setup and usage

ChemOnt enrichment uses the large ClassyFire/ChemOnt Zenodo release. For
repeated CLI lookups, prepare an indexed DuckDB store once:

```bash
# Download the required Zenodo files into a temporary directory and build DuckDB
chemrof prepare-chemont-from-zenodo chemont.duckdb

# Keep the downloaded Zenodo files for reuse or inspection
chemrof prepare-chemont-from-zenodo chemont.duckdb \
  --download-dir /tmp/chemrof-chemont-downloads \
  --overwrite
```

Then run the ChemOnt enricher against the local store:

```bash
chemrof convert CCO --enrichers chemont --chemont-source chemont.duckdb
```

The output includes the ordered ChemOnt path in `classified_by`:

```yaml
classified_by:
- CHEMONTID:0000000
- CHEMONTID:0004603
- CHEMONTID:0000323
- CHEMONTID:0000129
- CHEMONTID:0000286
```

For repeated use, set the source once:

```bash
export CHEMROF_CHEMONT_SOURCE="$PWD/chemont.duckdb"
chemrof convert CCO --enrichers chemont
```

OWL output maps each `classified_by` value to a `SubClassOf` axiom:

```bash
chemrof convert CCO \
  --enrichers chemont \
  --chemont-source chemont.duckdb \
  --format owl
```

```text
SubClassOf(<http://identifiers.org/inchikey/LFQSCWFLJHTTHZ-UHFFFAOYSA-N> CHEMONTID:0000286)
```

Parquet output is also available for scan-heavy workflows:

```bash
chemrof prepare-chemont-from-zenodo chemont-parquet --format parquet
chemrof convert CCO --enrichers chemont --chemont-source chemont-parquet
```

If the Zenodo files are already downloaded, build a local store directly:

```bash
chemrof prepare-chemont \
  /tmp/chemrof-chemont-downloads/classyfire_dedup_inchikey_smiles.enriched.tsv.zst \
  /tmp/chemrof-chemont-downloads/chemont_dictionary.tsv \
  chemont.duckdb \
  --overwrite
```

### Auto-classification

The converter inspects the parsed molecule and picks the most specific
chemrof class:

| Structure | chemrof type |
|-----------|-------------|
| Single atom, positive (e.g. `[Ca+2]`) | `AtomCation` |
| Single atom, negative (e.g. `[Cl-]`) | `AtomAnion` |
| Single atom, neutral (e.g. `[He]`) | `UnchargedAtom` |
| Multi-fragment salt (e.g. `[Na+].[Cl-]`) | `ChemicalSalt` |
| Multi-atom, all stereocenters assigned (e.g. `C[C@@H](N)C(=O)O`) | `Enantiomer` |
| Multi-atom, positive (e.g. `[NH4+]`) | `MolecularCation` |
| Multi-atom, negative (e.g. `CC([O-])=O`) | `MolecularAnion` |
| Multi-atom, neutral (e.g. `CCO`) | `SmallMolecule` |

### `chemrof from-smiles` (deprecated)

Hidden alias for `chemrof convert`. Still works for backwards compatibility
but does not support `--classes` or `--autochain`.

## Examples

```bash
# Ethanol as YAML
chemrof convert CCO

# InChI input
chemrof convert "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3"

# Benzene and water as JSON
chemrof convert c1ccccc1 O --format json

# Calcium ion with PubChem enrichment
chemrof convert "[Ca+2]" --enrichers pubchem

# Build a ChemOnt lookup store from Zenodo, then classify ethanol
chemrof prepare-chemont-from-zenodo chemont.duckdb
chemrof convert CCO --enrichers chemont --chemont-source chemont.duckdb

# Emit ChemOnt classifications as OWL SubClassOf axioms
chemrof convert CCO --enrichers chemont --chemont-source chemont.duckdb --format owl

# Enantiomer detection
chemrof convert "C[C@@H](N)C(=O)O" --format json

# Full racemic mixture graph
chemrof convert "CC(N)C(=O)O" --classes RacemicMixture --format json

# Multiple ions as OWL
chemrof convert "[Ca+2]" "[Cl-]" "[NH4+]" --format owl

# Pipe OWL output to a file
chemrof convert CCO --format owl > ethanol.ofn
```
