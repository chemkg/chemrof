"""Integration tests: SMILES -> chemrof dict matches existing example format."""

import pytest
import yaml

from chemrof.converter.convert import ChemConverter as SmilesConverter


@pytest.fixture
def converter():
    return SmilesConverter()


@pytest.mark.parametrize(
    "smiles, expected_keys",
    [
        ("CCO", ["id", "name", "type", "smiles_string", "inchi_string",
                  "inchi_chemical_sublayer", "empirical_formula", "molecular_mass", "is_organic"]),
        ("[Ca+2]", ["id", "name", "type", "smiles_string", "inchi_string",
                    "inchi_chemical_sublayer", "elemental_charge", "has_element"]),
        ("CC([O-])=O", ["id", "name", "type", "smiles_string", "inchi_string",
                        "elemental_charge"]),
    ],
)
def test_output_has_expected_keys(converter, smiles, expected_keys):
    result = converter.convert(smiles)
    for key in expected_keys:
        assert key in result, f"Missing key {key!r} for {smiles}"


def test_yaml_round_trip(converter):
    """Output can be serialized to YAML and parsed back."""
    result = converter.convert("CCO")
    text = yaml.dump(result, default_flow_style=False)
    parsed = yaml.safe_load(text)
    assert parsed["type"] == "chemrof:SmallMolecule"
    assert parsed["empirical_formula"] == "C2H6O"


def test_acetic_acid_matches_example_style(converter):
    """Acetic acid output has the same slots as the hand-written example."""
    result = converter.convert("CC(=O)O")
    # These slots appear in SmallMolecule-acetic-acid-with-pka.yaml
    assert result["type"] == "chemrof:SmallMolecule"
    assert "smiles_string" in result
    assert "empirical_formula" in result
    assert "molecular_mass" in result
    assert result["empirical_formula"] == "C2H4O2"
