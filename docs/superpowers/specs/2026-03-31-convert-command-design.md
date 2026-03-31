# Design: `chemrof convert` command

**Date:** 2026-03-31
**Branch:** (to be created from `linkml-owl-annotations`)
**Status:** Approved

## Problem

The current `chemrof from-smiles` command only accepts SMILES input, cannot detect
stereochemistry, and produces flat SubClassOf OWL output that lacks EquivalentClasses
axioms. It also cannot generate interlinked entity graphs (e.g., a racemic mixture
with its enantiomers and chirality-agnostic form).

## Goals

1. Rename `from-smiles` to `convert` (keep `from-smiles` as hidden alias)
2. Accept both SMILES and InChI input with auto-detection
3. Detect stereochemistry and classify Enantiomer vs chirality-agnostic forms
4. Add `--autochain` flag + `--classes` hint to generate interlinked entity graphs
5. Wire `--format owl` through linkml-data2owl for proper EquivalentClasses axioms

## CLI Interface

```bash
# Basic conversion (same as today, new command name)
chemrof convert CCO
chemrof convert "[Ca+2]" --format json

# Auto-detect InChI input
chemrof convert "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3"

# Non-standard racemic InChI → auto-triggers autochain
chemrof convert "InChI=1/.../t9-/s3"

# Explicit target classes (hint-based, generates full dependency graph)
chemrof convert "CC(N)C(=O)O" --classes RacemicMixture
chemrof convert "C[C@@H](N)C(=O)O" --classes RacemicMixture,Enantiomer

# Combined with output format
chemrof convert "CC(N)C(=O)O" --classes RacemicMixture --format owl

# Hidden alias preserved for backwards compat
chemrof from-smiles CCO  # still works
```

### Options

| Option | Default | Description |
|--------|---------|-------------|
| `--format`, `-f` | `yaml` | Output format: `yaml`, `json`, or `owl` |
| `--enrichers`, `-e` | _(none)_ | Comma-separated enricher sources |
| `--classes`, `-c` | _(none)_ | Comma-separated target chemrof classes (hint-based) |
| `--autochain` | `false` | Generate interlinked dependent entities |

`--classes` implies `--autochain`. A non-standard InChI with `/s3` also implies
`--autochain` with `--classes RacemicMixture`.

### Output

Without `--autochain`: single entity dict (or list for multiple inputs), same as today.

With `--autochain`: always a list of interlinked entity dicts. For YAML, each entity
is a separate document. For JSON, a JSON array. For OWL, all entities in one ontology.

## Architecture

### Input Detection — `converter/parse.py` (new)

Auto-detect input format and normalize to RDKit Mol + metadata:

```python
@dataclass
class ParsedInput:
    mol: Chem.Mol
    input_format: str          # "smiles" | "inchi"
    original: str              # raw input string
    inchi_stereo_type: str     # "" | "s1" | "s2" | "s3"
    is_racemic: bool           # True if /s3 detected
```

Detection rules:
- Starts with `InChI=` → parse as InChI via `Chem.MolFromInchi()`
- Otherwise → parse as SMILES via `Chem.MolFromSmiles()`

For InChI input, extract the `/s` layer value before parsing (since RDKit's
`MolFromInchi` discards non-standard stereo metadata).

### Classification — extend `converter/classify.py`

Add stereochemistry awareness after existing charge-based classification:

```python
def classify_entity(mol) -> str:
    # ... existing charge-based logic for ions ...
    
    # Stereochemistry detection (multi-atom neutral/charged molecules)
    chiral_centers = FindMolChiralCenters(mol, includeUnassigned=True)
    if chiral_centers:
        all_assigned = all(c[1] != '?' for c in chiral_centers)
        if all_assigned:
            return "Enantiomer"   # specific stereoisomer
        # else: unassigned stereocenters = chirality-agnostic, keep current type
    
    # ... existing fallthrough to SmallMolecule/MolecularCation/etc ...
```

Note: Enantiomer classification only applies when ALL stereocenters are assigned.
Mixed (some assigned, some not) stays as the base type.

### Converter — rename `converter/smiles.py` to `converter/convert.py`

The converter accepts a `ParsedInput` instead of a raw SMILES string. The
`_populate` method gains new slots for stereochemistry:

New slots populated for Enantiomer:
- `enantiomer_form_of`: ID of chirality-agnostic form (populated during autochain)
- `absolute_configuration`: R/S from `FindMolChiralCenters` (single-center only)
- `isomeric_smiles_string`: SMILES with stereo (from `MolToSmiles`)
- `inchi_tetrahedral_stereochemical_sublayer`: from InChI `/t` layer
- `inchi_stereochemical_type_sublayer`: from InChI `/s` layer

New slots populated for RacemicMixture:
- `has_left_enantiomer`: ID of one enantiomer
- `has_right_enantiomer`: ID of other enantiomer
- `chirality_agnostic_form`: ID of agnostic form
- No `inchi_string`, `smiles_string`, or `molecular_mass` (it's a mixture, not a molecule)

### Autochain — `converter/autochain.py` (new)

Takes a single converted entity + target classes, returns a list of interlinked dicts.

```python
def autochain(entity: dict, target_classes: set[str], mol: Chem.Mol) -> list[dict]:
    """Generate dependent entities for target classes.
    
    Returns a list of chemrof dicts including the original entity
    and all generated dependents, with relationship slots populated.
    """
```

#### Autochain logic for RacemicMixture

Input: any form (agnostic SMILES, specific enantiomer, or racemic InChI).

1. **Determine the agnostic mol**: strip stereochemistry from input mol
   (`Chem.RemoveAllHs` + clear stereo flags, or parse without stereo).

2. **Generate enantiomers**: `EnumerateStereoisomers(agnostic_mol)`.
   Limited to single-stereocenter molecules in v1.
   For each isomer, compute InChI with `-SAbs` flag (standard, absolute stereo).

3. **Build entity dicts**:

   a. **Agnostic form** — `SmallMolecule` type, stereo-free InChI, no `/t`/`/s` layers.
   
   b. **R-enantiomer** — `Enantiomer` type, with:
      - `enantiomer_form_of` → agnostic form ID
      - `absolute_configuration` → `"(R)"`
      - Full stereo InChI with `/t.../m1/s1`
   
   c. **S-enantiomer** — `Enantiomer` type, same pattern with `"(S)"` and `/m0/s1`.
   
   d. **RacemicMixture** — with:
      - `has_left_enantiomer` → S-enantiomer ID
      - `has_right_enantiomer` → R-enantiomer ID
      - `chirality_agnostic_form` → agnostic form ID
      - `IUPAC_name` → `"rac-{name}"` if name available
      - ID: synthesized from agnostic form's InChIKey: `chemrof:rac-{inchikey}`
        (the agnostic form always has an InChIKey since it's a valid molecule)
      - No InChI, SMILES, or mass (not a molecule)

4. **Return**: `[agnostic, r_enantiomer, s_enantiomer, racemic_mixture]`

#### Autochain logic for Enantiomer (without RacemicMixture)

If `--classes Enantiomer` on a stereo-neutral input:
1. Generate the agnostic form entity
2. Enumerate enantiomers
3. Return `[agnostic, r_enantiomer, s_enantiomer]` (no mixture entity)

#### Starting from a specific enantiomer

If input already has assigned stereo (e.g., `C[C@@H](N)C(=O)O`):
1. The input IS one enantiomer
2. Strip stereo → generate agnostic form
3. Generate the mirror enantiomer via `EnumerateStereoisomers` on agnostic
4. Build RacemicMixture linking both + agnostic form

### OWL Output — rewrite `converter/owl_output.py`

Replace direct pyhornedowl construction with linkml-data2owl:

```python
def dicts_to_owl(objs: list[dict], output_type: str = "ofn") -> str:
    """Convert chemrof dicts to OWL via linkml-data2owl."""
    sv = SchemaView(schema_path)
    dumper = OWLDumper()
    dumper.schemaview = sv
    
    for obj in objs:
        class_name = obj["type"].replace("chemrof:", "")
        # Load as linkml instance
        instance = load_instance(obj, class_name, sv)
        dumper.transform(instance, sv.schema)
    
    return dumper.ontology.save_to_string(output_type)
```

This means:
- MonoatomicIon entities get EquivalentClasses axioms (from owl.template)
- Enantiomer entities get EquivalentClasses axioms (from owl.template)
- RacemicMixture entities get EquivalentClasses axioms (from owl.template)
- Simple SmallMolecules get SubClassOf + AnnotationAssertions (from slot annotations)

### CLI — `cli/main.py`

```python
@app.command()
def convert(
    inputs: list[str] = typer.Argument(...),
    format: OutputFormat = typer.Option(OutputFormat.yaml, "--format", "-f"),
    enrichers: Optional[str] = typer.Option(None, "--enrichers", "-e"),
    classes: Optional[str] = typer.Option(None, "--classes", "-c"),
    autochain: bool = typer.Option(False, "--autochain"),
):
    ...

# Hidden alias for backwards compatibility
@app.command(hidden=True)
def from_smiles(
    # same signature, delegates to convert
):
    ...
```

## Module Layout

```
src/chemrof/converter/
  parse.py          # NEW: input detection (SMILES vs InChI), ParsedInput
  classify.py       # EXTEND: add stereochemistry detection
  convert.py        # RENAME from smiles.py: accept ParsedInput, populate dicts
  autochain.py      # NEW: generate interlinked entity graphs
  owl_output.py     # REWRITE: use linkml-data2owl
  enrichers/        # UNCHANGED
src/chemrof/cli/
  main.py           # MODIFY: rename command, add --classes/--autochain options
```

## Scope Limits (v1)

- Autochain only for single-stereocenter molecules (classic racemates)
- Input formats: SMILES and InChI only (database ID lookup is future)
- `--classes` only supports `RacemicMixture` and `Enantiomer` as targets
- Multi-stereocenter molecules warn and skip autochain

## Testing Strategy

- **Unit tests for parse.py**: SMILES vs InChI detection, `/s3` extraction
- **Unit tests for classify.py**: Enantiomer detection, mixed-stereo fallthrough
- **Unit tests for autochain.py**: entity graph generation, relationship linking,
  starting from agnostic/enantiomer/racemic InChI
- **Integration test**: full pipeline from SMILES → autochain → OWL output with
  EquivalentClasses axioms
- **CLI tests**: `convert` command, `from-smiles` alias, `--classes`, `--autochain`
- **Doctest**: key functions with inline examples
