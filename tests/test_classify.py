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
        # Enantiomers (assigned stereocenters)
        ("C[C@@H](N)C(=O)O", "Enantiomer"),   # L-alanine
        ("C[C@H](N)C(=O)O", "Enantiomer"),    # D-alanine
        # Unassigned stereocenters stay SmallMolecule
        ("CC(N)C(=O)O", "SmallMolecule"),     # alanine, no stereo annotation
        # Zwitterion with assigned stereo → Enantiomer (net charge 0, stereo wins)
        ("C[C@@H]([NH3+])C(=O)[O-]", "Enantiomer"),
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
