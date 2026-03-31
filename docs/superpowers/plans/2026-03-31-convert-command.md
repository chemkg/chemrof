# `chemrof convert` Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace `from-smiles` with a general `convert` command that auto-detects input format (SMILES/InChI), classifies stereochemistry, and generates interlinked entity graphs (enantiomers, racemic mixtures) via `--autochain`/`--classes`.

**Architecture:** Input parsing → classification → entity population → optional autochain expansion → output (YAML/JSON/OWL). Each stage is a separate module. OWL output switches from direct pyhornedowl to linkml-data2owl for schema-driven axiom generation.

**Tech Stack:** Python 3.10+, RDKit (Chem, EnumerateStereoisomers), typer, linkml-owl (OWLDumper), pytest

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `src/chemrof/converter/parse.py` | CREATE | Input detection (SMILES vs InChI), `ParsedInput` dataclass |
| `src/chemrof/converter/classify.py` | MODIFY | Add stereochemistry detection to `classify_entity()` |
| `src/chemrof/converter/smiles.py` | RENAME → `convert.py` | Accept `ParsedInput`, populate chemrof dicts |
| `src/chemrof/converter/autochain.py` | CREATE | Generate interlinked entity graphs |
| `src/chemrof/converter/owl_output.py` | REWRITE | Use linkml-data2owl OWLDumper |
| `src/chemrof/cli/main.py` | MODIFY | `convert` command + `from-smiles` alias + new options |
| `tests/test_parse.py` | CREATE | Unit tests for input parsing |
| `tests/test_smiles_converter.py` | RENAME → `tests/test_converter.py` | Update imports, add stereo tests |
| `tests/test_autochain.py` | CREATE | Unit tests for autochain |
| `tests/test_owl_output.py` | MODIFY | Update for new OWL output path |
| `src/docs/cli.md` | MODIFY | Update CLI docs for `convert` command |

---

### Task 1: Create `parse.py` — input detection module

**Files:**
- Create: `src/chemrof/converter/parse.py`
- Create: `tests/test_parse.py`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_parse.py`:

```python
"""Tests for input format detection and parsing."""

import pytest

from chemrof.converter.parse import ParsedInput, parse_input


class TestParseSmiles:
    def test_simple_smiles(self):
        """Plain SMILES string is detected and parsed."""
        result = parse_input("CCO")
        assert result.input_format == "smiles"
        assert result.original == "CCO"
        assert result.mol is not None
        assert result.inchi_stereo_type == ""
        assert result.is_racemic is False

    def test_ion_smiles(self):
        result = parse_input("[Ca+2]")
        assert result.input_format == "smiles"
        assert result.mol is not None

    def test_stereo_smiles(self):
        """SMILES with stereo is parsed with mol retaining chirality."""
        result = parse_input("C[C@@H](N)C(=O)O")
        assert result.input_format == "smiles"
        assert result.mol is not None

    def test_invalid_smiles(self):
        with pytest.raises(ValueError, match="parse"):
            parse_input("not_a_molecule_XYZ")


class TestParseInchi:
    def test_standard_inchi(self):
        """Standard InChI is detected and parsed."""
        inchi = "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3"
        result = parse_input(inchi)
        assert result.input_format == "inchi"
        assert result.original == inchi
        assert result.mol is not None
        assert result.inchi_stereo_type == ""
        assert result.is_racemic is False

    def test_inchi_with_absolute_stereo(self):
        """InChI with /s1 (absolute) is detected."""
        inchi = "InChI=1S/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/m1/s1"
        result = parse_input(inchi)
        assert result.inchi_stereo_type == "s1"
        assert result.is_racemic is False

    def test_racemic_inchi(self):
        """Non-standard InChI with /s3 (racemic) is detected."""
        inchi = "InChI=1/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/s3"
        result = parse_input(inchi)
        assert result.input_format == "inchi"
        assert result.inchi_stereo_type == "s3"
        assert result.is_racemic is True

    def test_invalid_inchi(self):
        with pytest.raises(ValueError, match="parse"):
            parse_input("InChI=1S/ZZZZZZ/invalid")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_parse.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'chemrof.converter.parse'`

- [ ] **Step 3: Implement `parse.py`**

Create `src/chemrof/converter/parse.py`:

```python
"""Detect input format (SMILES vs InChI) and parse to RDKit Mol.

>>> parse_input("CCO").input_format
'smiles'
>>> parse_input("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3").input_format
'inchi'
>>> parse_input("InChI=1/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/s3").is_racemic
True
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rdkit.Chem import Mol


@dataclass
class ParsedInput:
    """Result of parsing a chemical input string.

    Attributes:
        mol: RDKit Mol object.
        input_format: Detected format — ``"smiles"`` or ``"inchi"``.
        original: The raw input string.
        inchi_stereo_type: The ``/s`` layer value (e.g. ``"s1"``, ``"s3"``), or ``""`` if absent.
        is_racemic: True when ``inchi_stereo_type`` is ``"s3"``.
    """

    mol: Mol
    input_format: str
    original: str
    inchi_stereo_type: str = ""
    is_racemic: bool = False


def _extract_inchi_stereo_type(inchi: str) -> str:
    """Extract the /s layer from an InChI string.

    >>> _extract_inchi_stereo_type("InChI=1S/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/m1/s1")
    's1'
    >>> _extract_inchi_stereo_type("InChI=1/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/s3")
    's3'
    >>> _extract_inchi_stereo_type("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3")
    ''
    """
    match = re.search(r"/(s\d+)", inchi)
    return match.group(1) if match else ""


def parse_input(raw: str) -> ParsedInput:
    """Parse a SMILES or InChI string into a ``ParsedInput``.

    Raises:
        ValueError: If the string cannot be parsed by RDKit.
    """
    if raw.startswith("InChI="):
        return _parse_inchi(raw)
    return _parse_smiles(raw)


def _parse_smiles(smiles: str) -> ParsedInput:
    from rdkit import Chem

    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"RDKit could not parse SMILES: {smiles!r}")
    return ParsedInput(mol=mol, input_format="smiles", original=smiles)


def _parse_inchi(inchi: str) -> ParsedInput:
    from rdkit.Chem import inchi as rdkit_inchi

    stereo_type = _extract_inchi_stereo_type(inchi)
    mol = rdkit_inchi.MolFromInchi(inchi)
    if mol is None:
        raise ValueError(f"RDKit could not parse InChI: {inchi!r}")
    return ParsedInput(
        mol=mol,
        input_format="inchi",
        original=inchi,
        inchi_stereo_type=stereo_type,
        is_racemic=(stereo_type == "s3"),
    )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_parse.py -v`
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/chemrof/converter/parse.py tests/test_parse.py
git commit -m "feat: add parse.py for input format detection (SMILES/InChI)"
```

---

### Task 2: Extend `classify.py` with stereochemistry detection

**Files:**
- Modify: `src/chemrof/converter/classify.py`
- Create: `tests/test_classify.py`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_classify.py`:

```python
"""Tests for entity classification including stereochemistry."""

import pytest
from rdkit import Chem

from chemrof.converter.classify import classify_entity


class TestChargeClassification:
    """Existing charge-based classification (regression)."""

    def test_neutral_molecule(self):
        assert classify_entity(Chem.MolFromSmiles("CCO")) == "SmallMolecule"

    def test_atom_cation(self):
        assert classify_entity(Chem.MolFromSmiles("[Ca+2]")) == "AtomCation"

    def test_atom_anion(self):
        assert classify_entity(Chem.MolFromSmiles("[Cl-]")) == "AtomAnion"

    def test_molecular_cation(self):
        assert classify_entity(Chem.MolFromSmiles("[NH4+]")) == "MolecularCation"

    def test_molecular_anion(self):
        assert classify_entity(Chem.MolFromSmiles("CC([O-])=O")) == "MolecularAnion"


class TestStereoClassification:
    """New stereochemistry-aware classification."""

    def test_assigned_stereo_is_enantiomer(self):
        """SMILES with all stereocenters assigned → Enantiomer."""
        mol = Chem.MolFromSmiles("C[C@@H](N)C(=O)O")  # L-alanine
        assert classify_entity(mol) == "Enantiomer"

    def test_unassigned_stereo_stays_small_molecule(self):
        """SMILES with unassigned stereocenters → SmallMolecule (agnostic)."""
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")  # alanine, no stereo
        assert classify_entity(mol) == "SmallMolecule"

    def test_no_stereocenters(self):
        """Achiral molecule stays SmallMolecule."""
        mol = Chem.MolFromSmiles("CCO")
        assert classify_entity(mol) == "SmallMolecule"

    def test_charged_enantiomer_stays_charged(self):
        """Charged molecule with stereo keeps charge-based type (ions are more specific)."""
        mol = Chem.MolFromSmiles("C[C@@H]([NH3+])C(=O)[O-]")  # zwitterion, net 0
        assert classify_entity(mol) == "Enantiomer"

    def test_none_mol_raises(self):
        with pytest.raises(ValueError):
            classify_entity(None)
```

- [ ] **Step 2: Run tests to verify the new stereo tests fail**

Run: `uv run pytest tests/test_classify.py -v`
Expected: `TestStereoClassification::test_assigned_stereo_is_enantiomer` FAILS (returns "SmallMolecule")

- [ ] **Step 3: Update `classify.py`**

Replace the full contents of `src/chemrof/converter/classify.py`:

```python
"""Classify an RDKit Mol into the appropriate chemrof entity type.

>>> from rdkit import Chem
>>> classify_entity(Chem.MolFromSmiles("CCO"))
'SmallMolecule'
>>> classify_entity(Chem.MolFromSmiles("[Ca+2]"))
'AtomCation'
>>> classify_entity(Chem.MolFromSmiles("C[C@@H](N)C(=O)O"))
'Enantiomer'
>>> classify_entity(Chem.MolFromSmiles("CC(N)C(=O)O"))
'SmallMolecule'
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from rdkit.Chem import AddHs, FindMolChiralCenters

if TYPE_CHECKING:
    from rdkit.Chem import Mol


def classify_entity(mol: Mol | None) -> str:
    """Determine the chemrof class name for an RDKit mol.

    Classification priority:
    1. Single-atom ions (AtomCation, AtomAnion, UnchargedAtom)
    2. Multi-atom: stereochemistry check (Enantiomer if all centers assigned)
    3. Multi-atom charge (MolecularCation, MolecularAnion)
    4. Default: SmallMolecule
    """
    if mol is None:
        raise ValueError("cannot classify a None mol")

    mol_h = AddHs(mol)
    num_atoms = mol_h.GetNumAtoms()
    charge = sum(atom.GetFormalCharge() for atom in mol_h.GetAtoms())

    # Single-atom entities
    if num_atoms == 1:
        if charge > 0:
            return "AtomCation"
        if charge < 0:
            return "AtomAnion"
        return "UnchargedAtom"

    # Multi-atom: check stereochemistry
    chiral_centers = FindMolChiralCenters(mol, includeUnassigned=True)
    if chiral_centers:
        all_assigned = all(c[1] != "?" for c in chiral_centers)
        if all_assigned:
            return "Enantiomer"

    # Multi-atom: charge-based
    if charge > 0:
        return "MolecularCation"
    if charge < 0:
        return "MolecularAnion"
    return "SmallMolecule"
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_classify.py -v`
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/chemrof/converter/classify.py tests/test_classify.py
git commit -m "feat: classify Enantiomer when all stereocenters assigned"
```

---

### Task 3: Rename `smiles.py` → `convert.py` and accept `ParsedInput`

**Files:**
- Rename: `src/chemrof/converter/smiles.py` → `src/chemrof/converter/convert.py`
- Modify: `src/chemrof/converter/__init__.py`
- Rename: `tests/test_smiles_converter.py` → `tests/test_converter.py`
- Modify: `src/chemrof/cli/main.py` (update import)
- Modify: `tests/test_owl_output.py` (update import)

- [ ] **Step 1: Rename files with git mv**

```bash
git mv src/chemrof/converter/smiles.py src/chemrof/converter/convert.py
git mv tests/test_smiles_converter.py tests/test_converter.py
```

- [ ] **Step 2: Update `convert.py` to accept `ParsedInput` while keeping the SMILES string interface**

Replace the full contents of `src/chemrof/converter/convert.py`:

```python
"""Convert chemical inputs to chemrof-compliant dicts.

>>> converter = ChemConverter()
>>> result = converter.convert("CCO")
>>> result["type"]
'chemrof:SmallMolecule'
>>> result["empirical_formula"]
'C2H6O'
>>> result = converter.convert("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3")
>>> result["type"]
'chemrof:SmallMolecule'
"""

from __future__ import annotations

from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors, inchi, FindMolChiralCenters

from chemrof.converter.classify import classify_entity
from chemrof.converter.enrichers.base import Enricher, EnrichmentContext
from chemrof.converter.inchi import parse_inchi_sublayers
from chemrof.converter.parse import ParsedInput, parse_input


# chemrof type URI prefix
_TYPE_PREFIX = "chemrof:"

# Types where elemental_charge applies
_ION_TYPES = {"AtomCation", "AtomAnion", "MolecularCation", "MolecularAnion"}
_MONOATOMIC_TYPES = {"AtomCation", "AtomAnion", "UnchargedAtom"}


class ChemConverter:
    """Converts chemical input strings to chemrof-compliant dicts.

    Accepts SMILES or InChI strings (auto-detected).

    >>> ChemConverter().convert("[Ca+2]")["type"]
    'chemrof:AtomCation'
    """

    def __init__(self, enrichers: list[Enricher] | None = None):
        self.enrichers: list[Enricher] = enrichers or []

    def convert(self, raw: str) -> dict:
        """Parse an input string and return a chemrof dict.

        Args:
            raw: A SMILES or InChI string.

        Returns:
            A dict with chemrof slots populated.

        Raises:
            ValueError: If RDKit cannot parse the input.
        """
        parsed = parse_input(raw)
        return self.convert_parsed(parsed)

    def convert_parsed(self, parsed: ParsedInput) -> dict:
        """Convert a pre-parsed input to a chemrof dict."""
        entity_type = classify_entity(parsed.mol)
        obj = self._populate(parsed, entity_type)

        # Run enricher pipeline
        inchikey = obj.get("id", "").replace("INCHIKEY:", "")
        context = EnrichmentContext(
            mol=parsed.mol,
            inchikey=inchikey,
            smiles=obj.get("smiles_string", ""),
            inchi=obj.get("inchi_string", ""),
        )
        for enricher in self.enrichers:
            obj = enricher.enrich(obj, context)

        return obj

    def _populate(self, parsed: ParsedInput, entity_type: str) -> dict:
        """Fill chemrof slots from the parsed input."""
        mol = parsed.mol

        # Canonical SMILES
        canonical = Chem.MolToSmiles(mol)

        # InChI and InChIKey
        inchi_str = inchi.MolToInchi(mol) or ""
        inchikey = inchi.InchiToInchiKey(inchi_str) if inchi_str else ""

        # Molecular formula
        formula = rdMolDescriptors.CalcMolFormula(mol)

        # Molecular mass (exact)
        mass = Descriptors.ExactMolWt(mol)

        # Net formal charge
        charge = sum(atom.GetFormalCharge() for atom in mol.GetAtoms())

        # Radical check
        has_radical = any(atom.GetNumRadicalElectrons() > 0 for atom in mol.GetAtoms())

        # Is organic (contains carbon)
        has_carbon = any(atom.GetAtomicNum() == 6 for atom in mol.GetAtoms())

        obj: dict = {
            "id": f"INCHIKEY:{inchikey}" if inchikey else f"smiles:{canonical}",
            "name": formula,
            "type": f"{_TYPE_PREFIX}{entity_type}",
            "smiles_string": canonical,
            "inchi_string": inchi_str,
            "empirical_formula": formula,
            "molecular_mass": round(mass, 4),
        }

        # InChI sublayers
        sublayers = parse_inchi_sublayers(inchi_str)
        obj.update(sublayers)

        # Charge-related slots
        if entity_type in _ION_TYPES:
            obj["elemental_charge"] = charge

        # Monoatomic: has_element
        if entity_type in _MONOATOMIC_TYPES:
            obj["has_element"] = mol.GetAtomWithIdx(0).GetSymbol()

        # Boolean flags
        if has_carbon:
            obj["is_organic"] = True
        if has_radical:
            obj["is_radical"] = True

        # Enantiomer-specific slots
        if entity_type == "Enantiomer":
            obj["isomeric_smiles_string"] = Chem.MolToSmiles(mol, isomericSmiles=True)
            chiral_centers = FindMolChiralCenters(mol)
            if len(chiral_centers) == 1:
                obj["absolute_configuration"] = f"({chiral_centers[0][1]})"

        return obj


# Backwards-compatible alias
SmilesConverter = ChemConverter
```

- [ ] **Step 3: Update `__init__.py`**

Read and update `src/chemrof/converter/__init__.py` — if it imports `SmilesConverter`, update the import path to point to `convert.py`. If it's empty, leave it.

- [ ] **Step 4: Update test file imports**

Replace imports in `tests/test_converter.py`:

```python
# Old:
from chemrof.converter.smiles import SmilesConverter
# New:
from chemrof.converter.convert import ChemConverter as SmilesConverter
```

Also add a new test class at the end of `tests/test_converter.py`:

```python
class TestInchiInput:
    def test_ethanol_inchi(self):
        """InChI input produces same result as SMILES."""
        converter = SmilesConverter()
        result = converter.convert("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3")
        assert result["type"] == "chemrof:SmallMolecule"
        assert result["empirical_formula"] == "C2H6O"

    def test_enantiomer_classification(self):
        """SMILES with assigned stereo classified as Enantiomer."""
        converter = SmilesConverter()
        result = converter.convert("C[C@@H](N)C(=O)O")
        assert result["type"] == "chemrof:Enantiomer"
        assert result["absolute_configuration"] == "(R)"
        assert "isomeric_smiles_string" in result


class TestBackwardsCompat:
    def test_smiles_converter_alias(self):
        """SmilesConverter still works as an alias."""
        from chemrof.converter.convert import SmilesConverter
        converter = SmilesConverter()
        result = converter.convert("CCO")
        assert result["type"] == "chemrof:SmallMolecule"
```

- [ ] **Step 5: Update `cli/main.py` import**

In `src/chemrof/cli/main.py`, change:

```python
# Old:
from chemrof.converter.smiles import SmilesConverter
# New:
from chemrof.converter.convert import ChemConverter
```

And replace `SmilesConverter` with `ChemConverter` in the function body.

- [ ] **Step 6: Update `tests/test_owl_output.py` import**

In `tests/test_owl_output.py`, change:

```python
# Old:
from chemrof.converter.smiles import SmilesConverter
# New:
from chemrof.converter.convert import ChemConverter as SmilesConverter
```

- [ ] **Step 7: Run all tests**

Run: `uv run pytest tests/test_converter.py tests/test_owl_output.py tests/test_parse.py tests/test_classify.py -v`
Expected: all PASS

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "refactor: rename smiles.py → convert.py, accept SMILES and InChI input"
```

---

### Task 4: Create `autochain.py` — entity graph generation

**Files:**
- Create: `src/chemrof/converter/autochain.py`
- Create: `tests/test_autochain.py`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_autochain.py`:

```python
"""Tests for autochain entity graph generation."""

import pytest
from rdkit import Chem

from chemrof.converter.autochain import autochain
from chemrof.converter.convert import ChemConverter


@pytest.fixture
def converter():
    return ChemConverter()


class TestAutochainFromAgnostic:
    """Input is a stereo-neutral SMILES → generate full racemate graph."""

    def test_alanine_racemic_mixture(self, converter):
        """Stereo-neutral alanine + RacemicMixture → 4 entities."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        types = [r["type"] for r in results]
        assert "chemrof:SmallMolecule" in types  # agnostic
        assert types.count("chemrof:Enantiomer") == 2
        assert "chemrof:RacemicMixture" in types
        assert len(results) == 4

    def test_enantiomers_have_enantiomer_form_of(self, converter):
        """Generated enantiomers link back to agnostic form."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        agnostic = [r for r in results if r["type"] == "chemrof:SmallMolecule"][0]
        enantiomers = [r for r in results if r["type"] == "chemrof:Enantiomer"]
        for e in enantiomers:
            assert e["enantiomer_form_of"] == agnostic["id"]

    def test_racemic_mixture_links(self, converter):
        """RacemicMixture entity links enantiomers and agnostic form."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        mixture = [r for r in results if r["type"] == "chemrof:RacemicMixture"][0]
        enantiomer_ids = {r["id"] for r in results if r["type"] == "chemrof:Enantiomer"}
        agnostic_id = [r for r in results if r["type"] == "chemrof:SmallMolecule"][0]["id"]

        assert mixture["has_left_enantiomer"] in enantiomer_ids
        assert mixture["has_right_enantiomer"] in enantiomer_ids
        assert mixture["has_left_enantiomer"] != mixture["has_right_enantiomer"]
        assert mixture["chirality_agnostic_form"] == agnostic_id

    def test_racemic_mixture_has_no_inchi(self, converter):
        """RacemicMixture is a mixture — no InChI, SMILES, or mass."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        mixture = [r for r in results if r["type"] == "chemrof:RacemicMixture"][0]
        assert "inchi_string" not in mixture
        assert "smiles_string" not in mixture
        assert "molecular_mass" not in mixture

    def test_enantiomers_have_stereo_inchi(self, converter):
        """Generated enantiomers have InChI with /t and /s layers."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        enantiomers = [r for r in results if r["type"] == "chemrof:Enantiomer"]
        configs = {e["absolute_configuration"] for e in enantiomers}
        assert configs == {"(R)", "(S)"}
        for e in enantiomers:
            assert "/t" in e["inchi_string"]
            assert "inchi_tetrahedral_stereochemical_sublayer" in e
            assert "inchi_stereochemical_type_sublayer" in e


class TestAutochainFromEnantiomer:
    """Input is a specific enantiomer → generate agnostic + mirror + mixture."""

    def test_from_specific_enantiomer(self, converter):
        """L-alanine + RacemicMixture → 4 entities (agnostic + R + S + mixture)."""
        entity = converter.convert("C[C@@H](N)C(=O)O")
        mol = Chem.MolFromSmiles("C[C@@H](N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        types = [r["type"] for r in results]
        assert "chemrof:SmallMolecule" in types
        assert types.count("chemrof:Enantiomer") == 2
        assert "chemrof:RacemicMixture" in types


class TestAutochainEnantiomerOnly:
    """--classes Enantiomer without RacemicMixture."""

    def test_enantiomer_only(self, converter):
        """Stereo-neutral + Enantiomer → 3 entities (agnostic + R + S, no mixture)."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"Enantiomer"}, mol)

        types = [r["type"] for r in results]
        assert "chemrof:SmallMolecule" in types
        assert types.count("chemrof:Enantiomer") == 2
        assert "chemrof:RacemicMixture" not in types


class TestAutochainMultipleStereocenters:
    """Multi-stereocenter molecules are not supported in v1."""

    def test_multi_stereo_warns(self, converter):
        """Molecule with >1 stereocenter returns just the input entity."""
        # Tartaric acid: 2 stereocenters
        entity = converter.convert("OC(C(O)C(=O)O)C(=O)O")
        mol = Chem.MolFromSmiles("OC(C(O)C(=O)O)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        # Should return just the original entity (no expansion)
        assert len(results) == 1
        assert results[0]["id"] == entity["id"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_autochain.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'chemrof.converter.autochain'`

- [ ] **Step 3: Implement `autochain.py`**

Create `src/chemrof/converter/autochain.py`:

```python
"""Generate interlinked entity graphs from a single chemical input.

Given a chemrof entity dict and a set of target classes, autochain
generates dependent entities (enantiomers, racemic mixtures) with
proper relationship slots populated.

>>> from chemrof.converter.convert import ChemConverter
>>> from rdkit import Chem
>>> entity = ChemConverter().convert("CC(N)C(=O)O")
>>> mol = Chem.MolFromSmiles("CC(N)C(=O)O")
>>> results = autochain(entity, {"RacemicMixture"}, mol)
>>> len(results)
4
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from rdkit import Chem
from rdkit.Chem import (
    AllChem,
    Descriptors,
    EnumerateStereoisomers,
    FindMolChiralCenters,
    inchi,
    rdMolDescriptors,
)

from chemrof.converter.inchi import parse_inchi_sublayers

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)

_TYPE_PREFIX = "chemrof:"


def autochain(entity: dict, target_classes: set[str], mol: Chem.Mol) -> list[dict]:
    """Generate dependent entities for target classes.

    Returns a list of chemrof dicts including the original entity
    and all generated dependents, with relationship slots populated.

    Args:
        entity: The chemrof dict from the converter.
        target_classes: Set of chemrof class names (e.g. ``{"RacemicMixture"}``).
        mol: The RDKit Mol for the input.

    Returns:
        List of interlinked chemrof dicts.
    """
    wants_racemate = "RacemicMixture" in target_classes
    wants_enantiomers = "Enantiomer" in target_classes or wants_racemate

    if not wants_enantiomers:
        return [entity]

    # Check stereocenter count — v1 only supports single stereocenter
    chiral_centers = FindMolChiralCenters(mol, includeUnassigned=True)
    if len(chiral_centers) == 0:
        logger.warning("No stereocenters found — cannot generate enantiomers")
        return [entity]
    if len(chiral_centers) > 1:
        logger.warning(
            "Multiple stereocenters (%d) — autochain v1 only supports single stereocenter",
            len(chiral_centers),
        )
        return [entity]

    return _build_stereo_graph(entity, mol, wants_racemate)


def _strip_stereo(mol: Chem.Mol) -> Chem.Mol:
    """Return a copy of mol with all stereochemistry removed."""
    mol_copy = Chem.RWMol(mol)
    Chem.RemoveStereochemistry(mol_copy)
    return mol_copy.GetMol()


def _mol_to_entity(mol: Chem.Mol, entity_type: str) -> dict:
    """Build a basic chemrof dict from an RDKit mol."""
    canonical = Chem.MolToSmiles(mol)
    inchi_str = inchi.MolToInchi(mol) or ""
    inchikey = inchi.InchiToInchiKey(inchi_str) if inchi_str else ""
    formula = rdMolDescriptors.CalcMolFormula(mol)
    mass = Descriptors.ExactMolWt(mol)
    has_carbon = any(atom.GetAtomicNum() == 6 for atom in mol.GetAtoms())

    obj: dict = {
        "id": f"INCHIKEY:{inchikey}" if inchikey else f"smiles:{canonical}",
        "name": formula,
        "type": f"{_TYPE_PREFIX}{entity_type}",
        "smiles_string": canonical,
        "inchi_string": inchi_str,
        "empirical_formula": formula,
        "molecular_mass": round(mass, 4),
    }

    sublayers = parse_inchi_sublayers(inchi_str)
    obj.update(sublayers)

    if has_carbon:
        obj["is_organic"] = True

    return obj


def _build_stereo_graph(entity: dict, mol: Chem.Mol, include_mixture: bool) -> list[dict]:
    """Build the full stereoisomer entity graph for a single-stereocenter molecule."""
    # Step 1: Get the agnostic form
    agnostic_mol = _strip_stereo(mol)
    agnostic = _mol_to_entity(agnostic_mol, "SmallMolecule")

    # Step 2: Enumerate enantiomers from the agnostic mol
    opts = EnumerateStereoisomers.StereoEnumerationOptions(unique=True)
    isomers = list(EnumerateStereoisomers.EnumerateStereoisomers(agnostic_mol, options=opts))

    enantiomers = []
    for iso_mol in isomers:
        enantiomer = _mol_to_entity(iso_mol, "Enantiomer")
        enantiomer["enantiomer_form_of"] = agnostic["id"]
        enantiomer["isomeric_smiles_string"] = Chem.MolToSmiles(iso_mol, isomericSmiles=True)

        centers = FindMolChiralCenters(iso_mol)
        if len(centers) == 1:
            enantiomer["absolute_configuration"] = f"({centers[0][1]})"

        enantiomers.append(enantiomer)

    results = [agnostic] + enantiomers

    # Step 3: Build RacemicMixture if requested
    if include_mixture and len(enantiomers) == 2:
        agnostic_inchikey = agnostic["id"].replace("INCHIKEY:", "")
        mixture: dict = {
            "id": f"chemrof:rac-{agnostic_inchikey}",
            "name": f"rac-{agnostic['name']}",
            "type": f"{_TYPE_PREFIX}RacemicMixture",
            "has_left_enantiomer": enantiomers[0]["id"],
            "has_right_enantiomer": enantiomers[1]["id"],
            "chirality_agnostic_form": agnostic["id"],
        }
        results.append(mixture)

    return results
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_autochain.py -v`
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/chemrof/converter/autochain.py tests/test_autochain.py
git commit -m "feat: add autochain for generating enantiomer/racemate entity graphs"
```

---

### Task 5: Update CLI — `convert` command with `--autochain`/`--classes`

**Files:**
- Modify: `src/chemrof/cli/main.py`
- Create: `tests/test_cli.py`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_cli.py`:

```python
"""Tests for the chemrof CLI."""

import json

import pytest
import yaml
from typer.testing import CliRunner

from chemrof.cli.main import app

runner = CliRunner()


class TestConvertCommand:
    def test_basic_smiles(self):
        result = runner.invoke(app, ["convert", "CCO"])
        assert result.exit_code == 0
        data = yaml.safe_load(result.output)
        assert data["type"] == "chemrof:SmallMolecule"

    def test_json_format(self):
        result = runner.invoke(app, ["convert", "CCO", "--format", "json"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["type"] == "chemrof:SmallMolecule"

    def test_inchi_input(self):
        result = runner.invoke(app, ["convert", "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3"])
        assert result.exit_code == 0
        data = yaml.safe_load(result.output)
        assert data["type"] == "chemrof:SmallMolecule"
        assert data["empirical_formula"] == "C2H6O"

    def test_owl_format(self):
        result = runner.invoke(app, ["convert", "CCO", "--format", "owl"])
        assert result.exit_code == 0
        assert "SubClassOf" in result.output or "AnnotationAssertion" in result.output


class TestFromSmilesAlias:
    def test_alias_works(self):
        result = runner.invoke(app, ["from-smiles", "CCO"])
        assert result.exit_code == 0
        data = yaml.safe_load(result.output)
        assert data["type"] == "chemrof:SmallMolecule"


class TestAutochain:
    def test_classes_implies_autochain(self):
        result = runner.invoke(app, ["convert", "CC(N)C(=O)O", "--classes", "RacemicMixture", "--format", "json"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert isinstance(data, list)
        types = [d["type"] for d in data]
        assert "chemrof:RacemicMixture" in types
        assert types.count("chemrof:Enantiomer") == 2

    def test_autochain_yaml(self):
        result = runner.invoke(app, ["convert", "CC(N)C(=O)O", "--classes", "RacemicMixture"])
        assert result.exit_code == 0
        # YAML multi-doc: load all documents
        docs = list(yaml.safe_load_all(result.output))
        types = [d["type"] for d in docs]
        assert "chemrof:RacemicMixture" in types

    def test_racemic_inchi_auto_triggers(self):
        """Non-standard InChI with /s3 auto-triggers autochain."""
        rac_inchi = "InChI=1/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/s3"
        result = runner.invoke(app, ["convert", rac_inchi, "--format", "json"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert isinstance(data, list)
        types = [d["type"] for d in data]
        assert "chemrof:RacemicMixture" in types
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_cli.py -v`
Expected: FAIL — `convert` command not found or wrong args

- [ ] **Step 3: Rewrite `cli/main.py`**

Replace the full contents of `src/chemrof/cli/main.py`:

```python
"""chemrof CLI -- convert chemical structures to chemrof YAML/JSON/OWL."""

from __future__ import annotations

import json
from enum import Enum
from typing import Optional

import typer
import yaml

from chemrof.converter.convert import ChemConverter
from chemrof.converter.enrichers.base import get_enricher
from chemrof.converter.parse import parse_input

app = typer.Typer(
    name="chemrof",
    help="Chemical Entities, Materials, and Reactions Ontological Framework -- CLI tools.",
    no_args_is_help=True,
    invoke_without_command=True,
)


@app.callback()
def _main_callback() -> None:
    """chemrof CLI entry point."""


class OutputFormat(str, Enum):
    yaml = "yaml"
    json = "json"
    owl = "owl"


_ENRICHER_HELP = """Optionally pull extra data from external databases.

Pass a comma-separated list of source names. Available sources:

  pubchem   -- Look up the compound in PubChem by InChIKey.
               Fills in the preferred IUPAC name and PubChem CID.

  chebi     -- (stub) Will resolve CHEBI identifiers via OLS.

  wikidata  -- (stub) Will resolve Wikidata QIDs via SPARQL.

Example: --enrichers pubchem"""

_CLASSES_HELP = """Target chemrof classes to generate (hint-based).

Pass a comma-separated list. Supported: RacemicMixture, Enantiomer.
Implies --autochain. Requesting RacemicMixture automatically generates
Enantiomer entities and the chirality-agnostic form.

Example: --classes RacemicMixture"""


def _do_convert(
    inputs: list[str],
    format: OutputFormat,
    enrichers: Optional[str],
    classes: Optional[str],
    autochain: bool,
) -> None:
    """Shared implementation for convert and from-smiles commands."""
    enricher_instances = []
    if enrichers:
        for name in enrichers.split(","):
            enricher_instances.append(get_enricher(name.strip()))

    target_classes: set[str] = set()
    if classes:
        target_classes = {c.strip() for c in classes.split(",")}
        autochain = True

    converter = ChemConverter(enrichers=enricher_instances)

    all_results = []
    for raw in inputs:
        parsed = parse_input(raw)

        # Non-standard racemic InChI auto-triggers autochain
        if parsed.is_racemic:
            target_classes.add("RacemicMixture")
            autochain = True

        result = converter.convert_parsed(parsed)

        if autochain and target_classes:
            from chemrof.converter.autochain import autochain as do_autochain

            chain = do_autochain(result, target_classes, parsed.mol)
            all_results.extend(chain)
        else:
            all_results.append(result)

    if format == OutputFormat.owl:
        from chemrof.converter.owl_output import dicts_to_owl

        typer.echo(dicts_to_owl(all_results))
        return

    output = all_results if len(all_results) > 1 else all_results[0]

    if format == OutputFormat.json:
        typer.echo(json.dumps(output, indent=2))
    else:
        if isinstance(output, list):
            # Multi-document YAML
            typer.echo(yaml.dump_all(output, default_flow_style=False, sort_keys=False).rstrip())
        else:
            typer.echo(yaml.dump(output, default_flow_style=False, sort_keys=False).rstrip())


@app.command()
def convert(
    inputs: list[str] = typer.Argument(
        help="One or more SMILES or InChI strings.",
    ),
    format: OutputFormat = typer.Option(
        OutputFormat.yaml, "--format", "-f", help="Output format.",
    ),
    enrichers: Optional[str] = typer.Option(
        None, "--enrichers", "-e", help=_ENRICHER_HELP,
    ),
    classes: Optional[str] = typer.Option(
        None, "--classes", "-c", help=_CLASSES_HELP,
    ),
    autochain: bool = typer.Option(
        False, "--autochain", help="Generate interlinked dependent entities.",
    ),
):
    """Convert chemical inputs to chemrof data.

    Parses each input string (SMILES or InChI, auto-detected) with RDKit,
    classifies the entity type, and outputs chemrof-compliant records.

    Examples:

        chemrof convert CCO

        chemrof convert "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3" --format json

        chemrof convert "CC(N)C(=O)O" --classes RacemicMixture

        chemrof convert "[Ca+2]" --enrichers pubchem
    """
    _do_convert(inputs, format, enrichers, classes, autochain)


@app.command(hidden=True)
def from_smiles(
    smiles: list[str] = typer.Argument(
        help="One or more SMILES strings.",
    ),
    format: OutputFormat = typer.Option(
        OutputFormat.yaml, "--format", "-f", help="Output format.",
    ),
    enrichers: Optional[str] = typer.Option(
        None, "--enrichers", "-e", help=_ENRICHER_HELP,
    ),
):
    """(Deprecated) Convert SMILES to chemrof data. Use 'convert' instead."""
    _do_convert(smiles, format, enrichers, classes=None, autochain=False)
```

- [ ] **Step 4: Run tests**

Run: `uv run pytest tests/test_cli.py tests/test_converter.py tests/test_owl_output.py -v`
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/chemrof/cli/main.py tests/test_cli.py
git commit -m "feat: add 'convert' command with --autochain/--classes, keep from-smiles alias"
```

---

### Task 6: Rewrite `owl_output.py` to use linkml-data2owl

**Files:**
- Modify: `src/chemrof/converter/owl_output.py`
- Modify: `tests/test_owl_output.py`

- [ ] **Step 1: Write the failing tests**

Add new tests to `tests/test_owl_output.py` for EquivalentClasses axiom output:

```python
class TestEquivalentClassesAxioms:
    def test_atom_cation_equivalent_classes(self):
        """AtomCation produces EquivalentClasses axiom via owl.template."""
        from chemrof.converter.convert import ChemConverter
        from chemrof.converter.owl_output import dicts_to_owl

        obj = ChemConverter().convert("[Ca+2]")
        owl = dicts_to_owl([obj])
        assert "EquivalentClasses" in owl
        assert "MonoatomicIon" in owl
        assert "has_element" in owl
        assert "elemental_charge" in owl

    def test_enantiomer_equivalent_classes(self):
        """Enantiomer produces EquivalentClasses axiom."""
        from chemrof.converter.convert import ChemConverter
        from chemrof.converter.owl_output import dicts_to_owl

        obj = ChemConverter().convert("C[C@@H](N)C(=O)O")
        owl = dicts_to_owl([obj])
        assert "EquivalentClasses" in owl
        assert "Enantiomer" in owl

    def test_autochain_owl(self):
        """Autochain entities all appear in OWL output."""
        from rdkit import Chem
        from chemrof.converter.convert import ChemConverter
        from chemrof.converter.autochain import autochain
        from chemrof.converter.owl_output import dicts_to_owl

        entity = ChemConverter().convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)
        owl = dicts_to_owl(results)
        assert "RacemicMixture" in owl
        assert "Enantiomer" in owl
        assert "SmallMolecule" in owl
```

- [ ] **Step 2: Run to verify new tests fail**

Run: `uv run pytest tests/test_owl_output.py::TestEquivalentClassesAxioms -v`
Expected: FAIL — current owl_output.py only produces SubClassOf, not EquivalentClasses

- [ ] **Step 3: Rewrite `owl_output.py`**

Replace the full contents of `src/chemrof/converter/owl_output.py`:

```python
"""Convert chemrof dicts to OWL ontology via linkml-data2owl.

Uses the OWLDumper from linkml-owl with the annotated chemrof schema
to generate proper OWL axioms including EquivalentClasses for types
that have owl.template annotations (MonoatomicIon, Enantiomer,
RacemicMixture).

>>> from chemrof.converter.convert import ChemConverter
>>> obj = ChemConverter().convert("CCO")
>>> owl = dicts_to_owl([obj])
>>> "SmallMolecule" in owl
True
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from linkml_runtime.loaders import json_loader
from linkml_runtime.utils.schemaview import SchemaView
from linkml_owl.dumpers.owl_dumper import OWLDumper

_SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "chemrof.yaml"


@lru_cache(maxsize=1)
def _get_schemaview() -> SchemaView:
    return SchemaView(str(_SCHEMA_PATH))


@lru_cache(maxsize=1)
def _get_python_module():
    """Lazily load the generated Python datamodel."""
    from linkml_owl.util.loader_wrapper import get_python_module
    sv = _get_schemaview()
    return get_python_module(sv)


def _dict_to_instance(obj: dict, sv: SchemaView, python_module):
    """Convert a chemrof dict to a linkml runtime instance."""
    from linkml_owl.util.loader_wrapper import instantiate_object
    class_name = obj.get("type", "chemrof:SmallMolecule").replace("chemrof:", "")
    target_class = getattr(python_module, class_name)
    # Filter to only slots that the target class accepts
    return instantiate_object(obj, target_class, python_module=python_module, schemaview=sv)


def dicts_to_owl(objs: list[dict], output_type: str = "ofn") -> str:
    """Convert chemrof dicts to an OWL ontology string.

    Uses linkml-owl OWLDumper with schema annotations to produce
    EquivalentClasses axioms for annotated types and SubClassOf +
    AnnotationAssertions for others.

    Args:
        objs: List of chemrof dicts (from ChemConverter).
        output_type: ``"ofn"`` (OWL Functional Syntax) or ``"owl"`` (RDF/XML).

    Returns:
        OWL string in the requested format.
    """
    sv = _get_schemaview()
    python_module = _get_python_module()

    dumper = OWLDumper()
    dumper.schemaview = sv

    for obj in objs:
        instance = _dict_to_instance(obj, sv, python_module)
        dumper.to_ontology_document(instance, sv.schema)

    return dumper.ontology.save_to_string(output_type)
```

- [ ] **Step 4: Run all OWL tests**

Run: `uv run pytest tests/test_owl_output.py -v`
Expected: all PASS (both old and new tests)

Note: Some old tests may need adjustment if the new OWL output format differs
(e.g., `Declaration(Class(` may no longer appear). If tests fail, update assertions
to match the new linkml-owl output while preserving the semantic checks (SubClassOf,
AnnotationAssertion, class name presence).

- [ ] **Step 5: Commit**

```bash
git add src/chemrof/converter/owl_output.py tests/test_owl_output.py
git commit -m "feat: rewrite OWL output to use linkml-data2owl for EquivalentClasses axioms"
```

---

### Task 7: Update CLI docs

**Files:**
- Modify: `src/docs/cli.md`

- [ ] **Step 1: Update CLI reference docs**

Replace the contents of `src/docs/cli.md` to document the new `convert` command,
InChI input support, `--autochain`, `--classes`, and the stereochemistry features.
Key changes:

- Rename section from `chemrof from-smiles` to `chemrof convert`
- Add InChI input examples
- Add `--classes` and `--autochain` options to the table
- Add autochain examples showing racemic mixture generation
- Update auto-classification table to include Enantiomer
- Note that `from-smiles` still works as a hidden alias

- [ ] **Step 2: Commit**

```bash
git add src/docs/cli.md
git commit -m "docs: update CLI reference for convert command and autochain"
```

---

### Task 8: Run full test suite and push

**Files:** none (verification only)

- [ ] **Step 1: Run full test suite**

```bash
uv run pytest tests/ -v
```

Expected: all PASS

- [ ] **Step 2: Run doctests**

```bash
uv run pytest --doctest-modules src/chemrof/converter/parse.py src/chemrof/converter/classify.py src/chemrof/converter/convert.py src/chemrof/converter/autochain.py -v
```

Expected: all PASS

- [ ] **Step 3: Run example tests**

```bash
make test-examples
```

Expected: exit code 0

- [ ] **Step 4: Push and create PR**

```bash
git push -u origin linkml-owl-annotations
```

Then create PR with `gh pr create` targeting `main`, summarizing all changes.
