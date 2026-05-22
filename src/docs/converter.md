# Chemical Converter

The `chemrof` CLI converts SMILES or InChI strings into chemrof-compliant data
records. Given an input like `CCO` (ethanol), `[Ca+2]` (calcium ion), or
`InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3`, it parses the structure with RDKit,
determines the correct chemrof type, and fills in structural properties
automatically.

## Quick start

```bash
# Install (from the repo root)
uv sync

# Convert a SMILES to YAML
chemrof convert "CCO"

# Multiple molecules, JSON output
chemrof convert "CCO" "c1ccccc1" "[Ca+2]" --format json

# OWL output (OWL Functional Syntax)
chemrof convert "CCO" "[Ca+2]" --format owl

# Pull names from PubChem
chemrof convert "CCO" --enrichers pubchem

# Add ChemOnt/ClassyFire classifications from a local DuckDB store
chemrof convert "CCO" --enrichers chemont --chemont-source chemont.duckdb
```

## What it produces

For each SMILES, the converter outputs a dict with these slots:

| Slot | Source | Example |
|------|--------|---------|
| `id` | InChIKey (computed) | `INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N` |
| `name` | Molecular formula (or enricher) | `C2H6O` |
| `type` | Auto-classified | `chemrof:SmallMolecule` |
| `smiles_string` | Canonical SMILES | `CCO` |
| `inchi_string` | Computed InChI | `InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3` |
| `inchi_chemical_sublayer` | Parsed from InChI | `C2H6O` |
| `empirical_formula` | RDKit | `C2H6O` |
| `molecular_mass` | Exact mass (Da) | `46.0419` |
| `is_organic` | Contains carbon | `true` |
| `elemental_charge` | For ions only | `2` |
| `has_element` | For monoatomic ions | `Ca` |
| `classified_by` | ChemOnt enricher | `CHEMONTID:0000286` |

## Auto-classification

The converter inspects the parsed molecule and picks the right chemrof class:

| Structure | chemrof type |
|-----------|-------------|
| Single atom, positive charge (e.g. `[Ca+2]`) | `AtomCation` |
| Single atom, negative charge (e.g. `[Cl-]`) | `AtomAnion` |
| Single atom, neutral (e.g. `[He]`) | `UnchargedAtom` |
| Multi-atom, net positive (e.g. `[NH4+]`) | `MolecularCation` |
| Multi-atom, net negative (e.g. `CC([O-])=O`) | `MolecularAnion` |
| Multi-atom, neutral (e.g. `CCO`) | `SmallMolecule` |

## Enrichers

By default, the converter fills in only what RDKit can compute from the
structure. To pull additional data from external databases, use `--enrichers`:

```bash
chemrof convert "CCO" --enrichers pubchem
```

This adds a PubChem lookup by InChIKey, filling in the preferred IUPAC name
and a PubChem CID cross-reference.

### Available enrichers

| Name | Status | What it does |
|------|--------|-------------|
| `pubchem` | Working | Looks up the compound in PubChem by InChIKey. Fills `name` (IUPAC preferred) and `pubchem_cid`. |
| `chemont` | Working | Looks up the compound in a local ChemOnt/ClassyFire store by InChIKey. Fills `classified_by` with the ordered ChemOnt path. |
| `chebi` | Stub | Will resolve CHEBI identifiers via the OLS API. |
| `wikidata` | Stub | Will resolve Wikidata QIDs via SPARQL. |

Multiple enrichers run in sequence:

```bash
chemrof convert "CCO" --enrichers pubchem,chemont --chemont-source chemont.duckdb
```

### ChemOnt classification examples

Prepare a local DuckDB lookup store directly from the Zenodo release:

```bash
chemrof prepare-chemont-from-zenodo chemont.duckdb
```

Use a temporary download directory by default, or keep the downloaded files:

```bash
chemrof prepare-chemont-from-zenodo chemont.duckdb \
  --download-dir /tmp/chemrof-chemont-downloads \
  --overwrite
```

Classify a molecule with ChemOnt:

```bash
chemrof convert CCO --enrichers chemont --chemont-source chemont.duckdb
```

The result includes a list of ChemOnt classes:

```yaml
classified_by:
- CHEMONTID:0000000
- CHEMONTID:0004603
- CHEMONTID:0000323
- CHEMONTID:0000129
- CHEMONTID:0000286
```

Set the source as an environment variable to avoid repeating the option:

```bash
export CHEMROF_CHEMONT_SOURCE="$PWD/chemont.duckdb"
chemrof convert CCO --enrichers chemont
```

ChemOnt classifications also work in OWL output. Each `classified_by` value is
emitted as a `SubClassOf` axiom:

```bash
chemrof convert CCO --enrichers chemont --chemont-source chemont.duckdb --format owl
```

```text
SubClassOf(<http://identifiers.org/inchikey/LFQSCWFLJHTTHZ-UHFFFAOYSA-N> CHEMONTID:0000286)
```

For scan-heavy workflows, prepare Parquet instead of DuckDB:

```bash
chemrof prepare-chemont-from-zenodo chemont-parquet --format parquet
chemrof convert CCO --enrichers chemont --chemont-source chemont-parquet
```

To use files that were downloaded separately:

```bash
chemrof prepare-chemont \
  /tmp/chemrof-chemont-downloads/classyfire_dedup_inchikey_smiles.enriched.tsv.zst \
  /tmp/chemrof-chemont-downloads/chemont_dictionary.tsv \
  chemont.duckdb
```

### Writing a custom enricher

Enrichers follow a simple protocol. Any class with a `name` attribute and an
`enrich(obj, context)` method works:

```python
from chemrof.converter.enrichers.base import EnrichmentContext

class MyEnricher:
    name = "my-source"

    def enrich(self, obj: dict, context: EnrichmentContext) -> dict:
        # context.inchikey, context.smiles, context.inchi, context.mol
        # are available for lookups
        obj["my_custom_field"] = look_up_something(context.inchikey)
        return obj
```

The `EnrichmentContext` carries the RDKit mol object and computed identifiers
(InChIKey, canonical SMILES, InChI) so enrichers can use whichever key their
data source accepts.

To use a custom enricher programmatically:

```python
from chemrof.converter.convert import ChemConverter

converter = ChemConverter(enrichers=[MyEnricher()])
result = converter.convert("CCO")
```

## OWL output

The `--format owl` option emits an OWL ontology in Functional Syntax.
Each entity becomes an OWL Class with a `SubClassOf` axiom linking it to
its chemrof type, plus annotation assertions for each structural property:

```
Declaration(Class(chemrof:INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N))
SubClassOf(chemrof:INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N chemrof:SmallMolecule)
AnnotationAssertion(rdfs:label chemrof:INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N "C2H6O")
AnnotationAssertion(chemrof:smiles_string chemrof:INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N "CCO")
```

The Python API equivalent:

```python
from chemrof.converter.convert import ChemConverter
from chemrof.converter.owl_output import dicts_to_owl

converter = ChemConverter()
objs = [converter.convert(s) for s in ["CCO", "[Ca+2]"]]
print(dicts_to_owl(objs))
```

## Python API

The converter is also usable as a library:

```python
from chemrof.converter.convert import ChemConverter

converter = ChemConverter()
result = converter.convert("CCO")
# result is a plain dict with chemrof slots
print(result["type"])           # chemrof:SmallMolecule
print(result["empirical_formula"])  # C2H6O
```
