# SMILES Converter

The `chemrof` CLI converts SMILES strings into chemrof-compliant data records.
Given a SMILES like `CCO` (ethanol) or `[Ca+2]` (calcium ion), it parses the
structure with RDKit, determines the correct chemrof type, and fills in
structural properties automatically.

## Quick start

```bash
# Install (from the repo root)
uv sync

# Convert a SMILES to YAML
chemrof from-smiles "CCO"

# Multiple molecules, JSON output
chemrof from-smiles "CCO" "c1ccccc1" "[Ca+2]" --format json

# Pull names from PubChem
chemrof from-smiles "CCO" --enrichers pubchem
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
chemrof from-smiles "CCO" --enrichers pubchem
```

This adds a PubChem lookup by InChIKey, filling in the preferred IUPAC name
and a PubChem CID cross-reference.

### Available enrichers

| Name | Status | What it does |
|------|--------|-------------|
| `pubchem` | Working | Looks up the compound in PubChem by InChIKey. Fills `name` (IUPAC preferred) and `pubchem_cid`. |
| `chebi` | Stub | Will resolve CHEBI identifiers via the OLS API. |
| `wikidata` | Stub | Will resolve Wikidata QIDs via SPARQL. |

Multiple enrichers run in sequence:

```bash
chemrof from-smiles "CCO" --enrichers pubchem,chebi
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
from chemrof.converter.smiles import SmilesConverter

converter = SmilesConverter(enrichers=[MyEnricher()])
result = converter.convert("CCO")
```

## Python API

The converter is also usable as a library:

```python
from chemrof.converter.smiles import SmilesConverter

converter = SmilesConverter()
result = converter.convert("CCO")
# result is a plain dict with chemrof slots
print(result["type"])           # chemrof:SmallMolecule
print(result["empirical_formula"])  # C2H6O
```
