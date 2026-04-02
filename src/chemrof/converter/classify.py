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
>>> classify_entity(Chem.MolFromSmiles("[Na+].[Cl-]"))
'ChemicalSalt'
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from rdkit.Chem import AddHs, FindMolChiralCenters, rdmolops

if TYPE_CHECKING:
    from rdkit.Chem import Mol


def _is_salt(mol: Mol) -> bool:
    """Return True if *mol* is a disconnected salt (cation + anion fragments, net charge 0).

    >>> from rdkit import Chem
    >>> _is_salt(Chem.MolFromSmiles("[Na+].[Cl-]"))
    True
    >>> _is_salt(Chem.MolFromSmiles("[Na+].CC([O-])=O"))
    True
    >>> _is_salt(Chem.MolFromSmiles("CCO"))
    False
    >>> _is_salt(Chem.MolFromSmiles("[Ca+2]"))
    False
    """
    frags = rdmolops.GetMolFrags(mol, asMols=True)
    if len(frags) < 2:
        return False
    has_pos = False
    has_neg = False
    total_charge = 0
    for frag in frags:
        frag_charge = sum(a.GetFormalCharge() for a in frag.GetAtoms())
        total_charge += frag_charge
        if frag_charge > 0:
            has_pos = True
        if frag_charge < 0:
            has_neg = True
    return has_pos and has_neg and total_charge == 0


def classify_entity(mol: Mol | None) -> str:
    """Determine the chemrof class name for an RDKit mol.

    Classification priority:
    1. Single-atom ions (AtomCation, AtomAnion, UnchargedAtom)
    2. Multi-fragment salt (ChemicalSalt)
    3. Multi-atom: stereochemistry check (Enantiomer if all centers assigned)
    4. Multi-atom charge (MolecularCation, MolecularAnion)
    5. Default: SmallMolecule
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

    # Multi-fragment salt check (before other multi-atom checks)
    if _is_salt(mol):
        return "ChemicalSalt"

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
