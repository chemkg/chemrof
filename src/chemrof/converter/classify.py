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
