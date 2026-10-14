"""Tests for the clean-room pH 7.3 rules (derived without Rhea / ChemAxon output)."""

import doctest

import pytest
from rdkit import Chem

from chemrof.converter import protonation, protonation_cleanroom
from chemrof.converter.protonation_cleanroom import (
    CLEANROOM_RULES,
    DROPPED,
    PROVENANCE,
    predict_major_microspecies,
)


def can(smiles: str) -> str:
    return Chem.MolToSmiles(Chem.MolFromSmiles(smiles))


@pytest.mark.parametrize(
    "name,smiles,expected",
    [
        ("citric acid", "OC(=O)CC(O)(CC(O)=O)C(O)=O", "[O-]C(=O)CC(O)(CC([O-])=O)C([O-])=O"),
        ("L-lysine", "NCCCC[C@H](N)C(O)=O", "[NH3+]CCCC[C@H]([NH3+])C([O-])=O"),
        ("phosphate monoester", "CC(O)COP(O)(O)=O", "CC(O)COP([O-])([O-])=O"),
        ("methylphosphonic acid", "CP(O)(O)=O", "CP(O)([O-])=O"),
        ("thiophenol", "Sc1ccccc1", "[S-]c1ccccc1"),
        # differences from the Rhea-fitted rules
        ("7-hydroxyflavone stays neutral (pKa ~7.4)", "O=c1cc(-c2ccccc2)oc2cc(O)ccc12",
         "O=c1cc(-c2ccccc2)oc2cc(O)ccc12"),
        ("1,9-dimethyladenine protonated (pKaH ~8.3)", "Cn1cnc2c(c1=N)ncn2C", "Cn1cnc2c(ncn2C)c1=[NH2+]"),
        ("imino acid: C=N not protonated","OC(=O)C1=NCCC1", "[O-]C(=O)C1=NCCC1"),
    ],
)
def test_predict(name, smiles, expected):
    assert predict_major_microspecies(smiles) == can(expected), name


def test_every_acid_rule_has_provenance():
    for name, _, _ in CLEANROOM_RULES.acids:
        assert name in PROVENANCE, name


def test_dropped_rules_are_absent():
    names = {name for name, _, _ in CLEANROOM_RULES.acids}
    assert not names & set(DROPPED)
    assert CLEANROOM_RULES.imino_acid is None


def test_default_rules_unchanged():
    # the clean-room set must not alter the default predictor
    assert protonation.predict_major_microspecies("O=c1cc(-c2ccccc2)oc2cc(O)ccc12") == can(
        "O=c1cc(-c2ccccc2)oc2cc([O-])ccc12"
    )


def test_doctests():
    assert doctest.testmod(protonation_cleanroom).failed == 0
