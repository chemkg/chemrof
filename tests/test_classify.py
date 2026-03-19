"""Tests for SMILES-to-chemrof type classification."""

import pytest
from rdkit import Chem

from chemrof.converter.classify import classify_entity


@pytest.mark.parametrize(
    "smiles, expected_type",
    [
        # Neutral small molecules
        ("CCO", "SmallMolecule"),           # ethanol
        ("c1ccccc1", "SmallMolecule"),      # benzene
        ("CC(=O)O", "SmallMolecule"),       # acetic acid
        # Monoatomic cations
        ("[Cu+2]", "AtomCation"),           # copper(2+)
        ("[Ca+2]", "AtomCation"),           # calcium(2+)
        ("[Fe+3]", "AtomCation"),           # iron(3+)
        # Monoatomic anions
        ("[Cl-]", "AtomAnion"),             # chloride
        ("[O-2]", "AtomAnion"),             # oxide
        # Neutral atoms
        ("[He]", "UnchargedAtom"),          # helium
        ("[Ar]", "UnchargedAtom"),          # argon
        # Molecular cations
        ("[NH4+]", "MolecularCation"),      # ammonium
        # Molecular anions
        ("CC([O-])=O", "MolecularAnion"),   # acetate
        ("[OH-]", "MolecularAnion"),        # hydroxide (2 atoms)
    ],
)
def test_classify_entity(smiles: str, expected_type: str):
    mol = Chem.MolFromSmiles(smiles)
    assert mol is not None, f"RDKit failed to parse: {smiles}"
    result = classify_entity(mol)
    assert result == expected_type, f"For {smiles}: expected {expected_type}, got {result}"


def test_classify_invalid_mol():
    """classify_entity raises ValueError on None mol."""
    with pytest.raises(ValueError, match="cannot classify"):
        classify_entity(None)
