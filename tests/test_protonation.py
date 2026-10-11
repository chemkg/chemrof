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
        # rules added by hill-climbing against measured pKa (see chebi-scratch/ph73)
        ("4-nitropyridine not protonated", "O=[N+]([O-])c1ccncc1", "O=[N+]([O-])c1ccncc1"),
        ("sulfinic acid", "O=S(O)c1ccccc1", "O=S([O-])c1ccccc1"),
        ("thiophenol", "Sc1ccccc1", "[S-]c1ccccc1"),
        ("1-methyl-2-iminopyrimidine", "CN1C=CC=NC1=N", "Cn1cccnc1=[NH2+]"),
        ("N1-substituted adenine left neutral", "Cn1cnc2c(c1=N)ncn2C", "Cn1cnc2c(c1=N)ncn2C"),
        ("tropolone", "O=c1cccccc1O", "O=c1cccccc1[O-]"),
        ("1,1-dinitropropane", "CCC([N+](=O)[O-])[N+](=O)[O-]", "CC[C-]([N+](=O)[O-])[N+](=O)[O-]"),
        ("cyclohexane-1,3-dione", "O=C1CCCC(=O)C1", "O=C1C=C([O-])CCC1"),
        ("acetylacetone stays neutral", "CC(=O)CC(C)=O", "CC(=O)CC(C)=O"),
        ("bis(2-chloroethyl)methylamine", "CN(CCCl)CCCl", "CN(CCCl)CCCl"),
        ("6-azauracil", "O=c1cn[nH]c(=O)[nH]1", "O=c1cn[nH]c(=O)[n-]1"),
        ("uracil stays neutral", "O=c1cc[nH]c(=O)[nH]1", "O=c1cc[nH]c(=O)[nH]1"),
        ("deuterated acid does not crash", "[2H]OC(=O)C(F)(F)F", "[2H]OC(=O)C(F)(F)F"),
    ],
)
def test_predict(name, smiles, expected):
    assert predict_major_microspecies(smiles) == can(expected), name


def test_invalid_smiles():
    assert predict_major_microspecies("not a smiles") is None


def test_rule_smarts_parse():
    for name, smarts, _ in protonation.ACIDS:
        # the acid loop reads match[1] as the centre atom
        assert protonation._pat(smarts).GetNumAtoms() >= 2, name
    for smarts in (protonation.PHOSPHORIC_KEEP + protonation.WEAK_AMINES + protonation.AMIDINES
                   + [protonation.TROPOLONE, protonation.CYCLIC_DIKETONE, protonation.IMINO_ACID]):
        protonation._pat(smarts)


def test_doctests():
    assert doctest.testmod(protonation).failed == 0
