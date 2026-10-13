"""Single-atom entities: classes and atom slots."""

import pytest
from rdkit import Chem

from chemrof.converter.atoms import atom_class, atom_fields, is_single_atom
from chemrof.converter.classify import classify_entity
from chemrof.converter.convert import ChemConverter


@pytest.fixture
def convert():
    return ChemConverter().convert


@pytest.mark.parametrize(
    "smiles, expected",
    [
        ("[Fe]", "UnchargedAtom"),
        ("[Fe+3]", "AtomCation"),
        ("[Cl-]", "AtomAnion"),
        ("[2H]", "Isotope"),
        ("[13C]", "Isotope"),
        ("[13C+]", "FullySpecifiedAtom"),
        ("[37Cl-]", "FullySpecifiedAtom"),
    ],
)
def test_classification(smiles, expected):
    mol = Chem.MolFromSmiles(smiles)
    assert atom_class(mol) == expected
    assert classify_entity(mol) == expected


@pytest.mark.parametrize(
    "smiles, expected",
    [
        ("[Fe]", {"atomic_number": 26, "symbol": "Fe"}),
        ("[Fe+3]", {"atomic_number": 26, "symbol": "Fe", "elemental_charge": 3, "has_element": "Fe"}),
        ("[Cl-]", {"atomic_number": 17, "symbol": "Cl", "elemental_charge": -1, "has_element": "Cl"}),
        ("[13C]", {"atomic_number": 6, "symbol": "C", "neutron_number": 7, "has_element": "C"}),
        # has_element is not a FullySpecifiedAtom slot
        ("[13C+]", {"atomic_number": 6, "symbol": "C", "elemental_charge": 1, "neutron_number": 7}),
        ("[2H]", {"atomic_number": 1, "symbol": "H", "neutron_number": 1, "has_element": "H"}),
    ],
)
def test_atom_fields(smiles, expected):
    assert atom_fields(Chem.MolFromSmiles(smiles)) == expected


def test_is_single_atom():
    assert is_single_atom(Chem.MolFromSmiles("[Ca+2]"))
    assert not is_single_atom(Chem.MolFromSmiles("[OH-]"))
    assert not is_single_atom(Chem.MolFromSmiles("[Na+].[Cl-]"))


def test_converter_populates_atom_slots(convert):
    obj = convert("[Fe+3]")
    assert (obj["atomic_number"], obj["symbol"], obj["elemental_charge"]) == (26, "Fe", 3)
    assert obj["has_element"] == "Fe"


def test_isotope_name_keeps_mass_number(convert):
    assert convert("[13C]")["name"] == "13C"
    assert convert("[56Fe+3]")["name"] == "56Fe+3"
    assert convert("[C]")["name"] == "C"


@pytest.mark.parametrize("smiles", ["[C]", "[Fe]", "[13C]", "[Fe+3]"])
def test_atoms_get_no_organic_or_radical_flag(convert, smiles):
    """RDKit's open-valence count is meaningless for a bare atom."""
    obj = convert(smiles)
    assert "is_organic" not in obj
    assert "is_radical" not in obj


def test_molecules_keep_flags(convert):
    assert convert("CCO")["is_organic"] is True
    assert convert("[CH3]")["is_radical"] is True


def test_salt_components_have_atom_slots():
    from chemrof.converter.autochain import autochain

    mol = Chem.MolFromSmiles("[Na+].[Cl-]")
    chain = autochain(ChemConverter().convert("[Na+].[Cl-]"), {"ChemicalSalt"}, mol)
    by_symbol = {e["symbol"]: e for e in chain if "symbol" in e}
    assert by_symbol["Na"]["atomic_number"] == 11
    assert by_symbol["Cl"]["elemental_charge"] == -1
