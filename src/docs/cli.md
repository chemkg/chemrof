# CLI Reference

The `chemrof` command-line tool provides utilities for working with
chemical structure data in the chemrof framework.

## Installation

```bash
uv sync
```

This installs the `chemrof` command from the project's entry point.

## Commands

### `chemrof from-smiles`

Convert one or more SMILES strings into chemrof-compliant records.

```
chemrof from-smiles [OPTIONS] SMILES...
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `SMILES` | One or more SMILES strings (required). Quote ions: `"[Ca+2]"` |

**Options:**

| Option | Default | Description |
|--------|---------|-------------|
| `--format`, `-f` | `yaml` | Output format: `yaml`, `json`, or `owl` |
| `--enrichers`, `-e` | _(none)_ | Comma-separated list of enricher sources |

### Output formats

**YAML** (default) — one document per SMILES, or a list for multiple inputs:

```bash
chemrof from-smiles CCO
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
chemrof from-smiles CCO --format json
```

**OWL** — OWL Functional Syntax ontology. Each entity becomes an OWL
class with `SubClassOf` to its chemrof type and annotation assertions
for structural properties:

```bash
chemrof from-smiles CCO "[Ca+2]" --format owl
```

```
SubClassOf(chemrof:INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N chemrof:SmallMolecule)
AnnotationAssertion(rdfs:label chemrof:INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N "C2H6O")
AnnotationAssertion(chemrof:smiles_string chemrof:INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N "CCO")
```

### Enrichers

Enrichers pull additional data from external databases after RDKit
computes the structural properties. Pass a comma-separated list:

```bash
chemrof from-smiles CCO --enrichers pubchem
chemrof from-smiles CCO --enrichers pubchem,chebi
```

| Source | Status | What it adds |
|--------|--------|-------------|
| `pubchem` | Working | Preferred IUPAC name and PubChem CID (via InChIKey lookup) |
| `chebi` | Stub | Will resolve CHEBI identifiers via OLS |
| `wikidata` | Stub | Will resolve Wikidata QIDs via SPARQL |

### Auto-classification

The converter inspects the parsed molecule and picks the most specific
chemrof class:

| Structure | chemrof type |
|-----------|-------------|
| Single atom, positive (e.g. `[Ca+2]`) | `AtomCation` |
| Single atom, negative (e.g. `[Cl-]`) | `AtomAnion` |
| Single atom, neutral (e.g. `[He]`) | `UnchargedAtom` |
| Multi-atom, positive (e.g. `[NH4+]`) | `MolecularCation` |
| Multi-atom, negative (e.g. `CC([O-])=O`) | `MolecularAnion` |
| Multi-atom, neutral (e.g. `CCO`) | `SmallMolecule` |

## Examples

```bash
# Ethanol as YAML
chemrof from-smiles CCO

# Benzene and water as JSON
chemrof from-smiles c1ccccc1 O --format json

# Calcium ion with PubChem enrichment
chemrof from-smiles "[Ca+2]" --enrichers pubchem

# Multiple ions as OWL
chemrof from-smiles "[Ca+2]" "[Cl-]" "[NH4+]" --format owl

# Pipe OWL output to a file
chemrof from-smiles CCO --format owl > ethanol.ofn
```
