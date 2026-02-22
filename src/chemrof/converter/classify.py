"""Classify an RDKit Mol into the appropriate chemrof entity type."""

from __future__ import annotations

from typing import TYPE_CHECKING

from rdkit.Chem import AddHs

if TYPE_CHECKING:
    from rdkit.Chem import Mol


def classify_entity(mol: Mol | None) -> str:
    """Determine the chemrof class name for an RDKit mol.

    >>> from rdkit import Chem
    >>> classify_entity(Chem.MolFromSmiles("CCO"))
    'SmallMolecule'
    >>> classify_entity(Chem.MolFromSmiles("[Ca+2]"))
    'AtomCation'
    >>> classify_entity(Chem.MolFromSmiles("[Cl-]"))
    'AtomAnion'
    """
    if mol is None:
        raise ValueError("cannot classify a None mol")

    # Add explicit hydrogens so that e.g. [NH4+] counts as 5 atoms, not 1
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

    # Multi-atom entities
    if charge > 0:
        return "MolecularCation"
    if charge < 0:
        return "MolecularAnion"
    return "SmallMolecule"
