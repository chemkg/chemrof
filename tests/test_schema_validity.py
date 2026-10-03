"""Converter output must validate against the chemrof LinkML schema.

Unit tests that only check ``result["type"]`` miss slots the schema does not
allow on a class, or values that fail its patterns; this checks both.
"""

from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

from chemrof.converter.autochain import autochain
from chemrof.converter.convert import ChemConverter
from chemrof.converter.parse import parse_input
from chemrof.converter.siblings import siblings

SCHEMA = Path(__file__).resolve().parent.parent / "src/chemrof/schema/chemrof.yaml"


@pytest.fixture(scope="module")
def validator():
    return Validator(str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)])


def problems(validator, obj: dict) -> list[str]:
    target = obj["type"].split(":")[-1]
    return [r.message for r in validator.validate(obj, target).results]


SMILES = [
    # atoms
    "[C]", "[Fe]", "[He]",              # neutral
    "[Fe+3]", "[Ca+2]",                 # cations
    "[Cl-]", "[O-2]",                   # anions
    "[2H]", "[13C]", "[56Fe]",          # isotopes
    "[13C+]", "[56Fe+3]",               # charged isotopes
    # molecules
    "CCO", "c1ccccc1", "[OH-]", "CC([O-])=O", "[NH4+]",
    "C[C@@H](N)C(=O)O", "CC(N)C(=O)O",
]


@pytest.mark.parametrize("smiles", SMILES)
def test_converter_output_is_valid(validator, smiles):
    assert problems(validator, ChemConverter().convert(smiles)) == []


# These graphs are not yet schema-valid for reasons unrelated to atoms or InChI
# layers: ChemicalSalt has no has_cationic_component / has_anionic_component /
# elemental_charge slots, and SmallMolecule has no tautomer_of slot. strict=True
# makes them fail loudly once the schema catches up, so the marker gets removed.
@pytest.mark.parametrize(
    "smiles, classes",
    [
        ("CC(N)C(=O)O", {"RacemicMixture"}),
        pytest.param(
            "[Na+].[Cl-]", {"ChemicalSalt"},
            marks=pytest.mark.xfail(strict=True, reason="schema: ChemicalSalt lacks component slots"),
        ),
        pytest.param(
            "Oc1ccccn1", {"Tautomer"},
            marks=pytest.mark.xfail(strict=True, reason="schema: SmallMolecule lacks tautomer_of"),
        ),
    ],
)
def test_autochain_output_is_valid(validator, smiles, classes):
    parsed = parse_input(smiles)
    entity = ChemConverter().convert_parsed(parsed)
    for obj in autochain(entity, classes, parsed.mol):
        assert problems(validator, obj) == [], obj["id"]


@pytest.mark.parametrize("smiles", ["[Fe]", "[Fe+3]", "CC(O)C(C)O", "C[C@H](N)C(=O)O", "CC=CC"])
def test_siblings_output_is_valid(validator, smiles):
    parsed = parse_input(smiles)
    entity = ChemConverter().convert_parsed(parsed)
    family = siblings(entity, parsed.mol)
    assert len(family) > 1
    for obj in family:
        assert problems(validator, obj) == [], obj["id"]
