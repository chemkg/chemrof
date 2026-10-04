"""Tests for the pH 7.3 major microspecies rules.

Expected values follow Rhea's chebi_pH7_3_mapping.tsv.
"""

import doctest

import pytest
from rdkit import Chem

from chemrof.converter import protonation
from chemrof.converter.protonation import predict_major_microspecies


def can(smiles: str) -> str:
    return Chem.MolToSmiles(Chem.MolFromSmiles(smiles))


@pytest.mark.parametrize(
    "name,smiles,expected",
    [
        ("citric acid", "OC(=O)CC(O)(CC(O)=O)C(O)=O", "[O-]C(=O)CC(O)(CC([O-])=O)C([O-])=O"),
        ("L-cysteine", "N[C@@H](CS)C(O)=O", "[NH3+][C@@H](CS)C([O-])=O"),
        ("L-histidine", "N[C@@H](Cc1cnc[nH]1)C(O)=O", "[NH3+][C@@H](Cc1cnc[nH]1)C([O-])=O"),
        ("L-lysine", "NCCCC[C@H](N)C(O)=O", "[NH3+]CCCC[C@H]([NH3+])C([O-])=O"),
        ("L-arginine", "NC(N)=NCCC[C@H](N)C(O)=O", "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O"),
        ("already charged input", "[NH3+]CC([O-])=O", "[NH3+]CC([O-])=O"),
        ("phenol", "Oc1ccccc1", "Oc1ccccc1"),
        ("4-nitrophenol", "Oc1ccc(cc1)[N+]([O-])=O", "[O-]c1ccc(cc1)[N+]([O-])=O"),
        ("apigenin", "O=c1cc(-c2ccc(O)cc2)oc2cc(O)cc(O)c12", "O=c1cc(-c2ccc(O)cc2)oc2cc([O-])cc(O)c12"),
        ("phosphoric acid", "OP(O)(O)=O", "OP([O-])([O-])=O"),
        ("diphosphoric acid", "OP(=O)(O)OP(=O)(O)O", "OP(=O)([O-])OP(=O)([O-])[O-]"),
        ("phosphate monoester", "CC(O)COP(O)(O)=O", "CC(O)COP([O-])([O-])=O"),
        ("phosphate diester", "COP(O)(=O)OC", "COP([O-])(=O)OC"),
        ("methylphosphonic acid", "CP(O)(O)=O", "CP(O)([O-])=O"),
        ("carbonic acid", "OC(O)=O", "OC([O-])=O"),
        ("morpholine N stays neutral", "O=S(=O)(O)CCCN1CCOCC1", "O=S(=O)([O-])CCCN1CCOCC1"),
        ("piperazine: one N", "C1CNCCN1", "C1C[NH2+]CCN1"),
        ("acetamide", "CC(N)=O", "CC(N)=O"),
        ("1-pyrroline-2-carboxylic acid", "OC(=O)C1=NCCC1", "[O-]C(=O)C1=[NH+]CCC1"),
        ("sodium(1+) unchanged", "[Na+]", "[Na+]"),
    ],
)
def test_predict(name, smiles, expected):
    assert predict_major_microspecies(smiles) == can(expected), name


def test_invalid_smiles():
    assert predict_major_microspecies("not a smiles") is None


def test_rule_smarts_parse():
    for _, smarts, _ in protonation.ACIDS:
        protonation._pat(smarts)
    for smarts in protonation.PHOSPHORIC_KEEP + protonation.WEAK_AMINES + protonation.AMIDINES:
        protonation._pat(smarts)


def test_doctests():
    assert doctest.testmod(protonation).failed == 0
