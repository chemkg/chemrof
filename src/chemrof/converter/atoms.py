"""Atom-level slots for single-atom chemrof entities.

A single atom (neutral, ionic and/or isotopically labelled) is described in
chemrof by ``atomic_number``, ``symbol`` and, depending on the class, by
``elemental_charge``, ``has_element`` and ``neutron_number``:

=====================  =====================================================
class                  atom slots
=====================  =====================================================
``UnchargedAtom``      ``atomic_number``, ``symbol``
``AtomCation/Anion``   ``atomic_number``, ``symbol``, ``elemental_charge``,
                       ``has_element``
``Isotope``            ``atomic_number``, ``symbol``, ``neutron_number``,
                       ``has_element`` (neutral, mass number specified)
``FullySpecifiedAtom`` ``atomic_number``, ``symbol``, ``elemental_charge``,
                       ``neutron_number`` (charged *and* mass number specified)
=====================  =====================================================

>>> from rdkit import Chem
>>> atom_fields(Chem.MolFromSmiles("[Fe+3]"))
{'atomic_number': 26, 'symbol': 'Fe', 'elemental_charge': 3, 'has_element': 'Fe'}
>>> atom_fields(Chem.MolFromSmiles("[13C]"))
{'atomic_number': 6, 'symbol': 'C', 'neutron_number': 7, 'has_element': 'C'}
>>> atom_fields(Chem.MolFromSmiles("[Fe]"))
{'atomic_number': 26, 'symbol': 'Fe'}
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from rdkit.Chem import AddHs

if TYPE_CHECKING:
    from rdkit.Chem import Mol


def is_single_atom(mol: Mol) -> bool:
    """True if *mol* is exactly one atom once implicit hydrogens are made explicit.

    >>> from rdkit import Chem
    >>> is_single_atom(Chem.MolFromSmiles("[Ca+2]"))
    True
    >>> is_single_atom(Chem.MolFromSmiles("[OH-]"))
    False
    """
    return AddHs(mol).GetNumAtoms() == 1


def atom_class(mol: Mol) -> str:
    """Return the chemrof class name for a single-atom mol.

    >>> from rdkit import Chem
    >>> [atom_class(Chem.MolFromSmiles(s)) for s in ("[Fe]", "[Fe+3]", "[Cl-]", "[13C]", "[13C+]")]
    ['UnchargedAtom', 'AtomCation', 'AtomAnion', 'Isotope', 'FullySpecifiedAtom']
    """
    atom = mol.GetAtomWithIdx(0)
    charge = atom.GetFormalCharge()
    if atom.GetIsotope():
        # AtomCation/AtomAnion are mass-number neutral, so a labelled ion needs
        # the class that carries both charge and neutron number.
        return "Isotope" if charge == 0 else "FullySpecifiedAtom"
    if charge > 0:
        return "AtomCation"
    if charge < 0:
        return "AtomAnion"
    return "UnchargedAtom"


def atom_fields(mol: Mol) -> dict:
    """Atom slots for a single-atom mol; see the module docstring for the layout."""
    atom = mol.GetAtomWithIdx(0)
    z = atom.GetAtomicNum()
    symbol = atom.GetSymbol()
    charge = atom.GetFormalCharge()
    mass_number = atom.GetIsotope()

    fields: dict = {"atomic_number": z, "symbol": symbol}
    if charge:
        fields["elemental_charge"] = charge
    if mass_number:
        fields["neutron_number"] = mass_number - z
    # has_element exists on MonoatomicIon and Isotope, not on FullySpecifiedAtom
    if bool(charge) != bool(mass_number):
        fields["has_element"] = symbol
    return fields
