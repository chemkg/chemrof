"""The bundled ChEBI atomic-species table and its builder script."""

import importlib.util
from pathlib import Path

import pytest

from chemrof.converter.species import Species, element_number, lookup, species_of_element

ROOT = Path(__file__).resolve().parent.parent


def test_all_118_elements_have_a_neutral_atom():
    missing = [z for z in range(1, 119) if lookup(z) is None]
    assert missing == []


def test_neutral_atoms_are_distinct_chebi_ids():
    ids = [lookup(z).chebi_id for z in range(1, 119)]
    assert len(set(ids)) == 118


@pytest.mark.parametrize(
    "z, charge, mass, chebi_id",
    [
        (6, 0, None, "CHEBI:27594"),    # carbon atom
        (26, 0, None, "CHEBI:18248"),   # iron atom
        (26, 3, None, "CHEBI:29034"),   # iron(3+)
        (17, -1, None, "CHEBI:17996"),  # chloride
        (6, 0, 13, "CHEBI:36928"),      # carbon-13 atom
        (1, 1, None, "CHEBI:15378"),    # hydron (bare proton)
        (48, 0, None, "CHEBI:22977"),   # cadmium atom, not 'elemental cadmium'
    ],
)
def test_known_species(z, charge, mass, chebi_id):
    assert lookup(z, charge, mass).chebi_id == chebi_id


def test_unknown_species_is_none():
    assert lookup(26, charge=9) is None


def test_neutral_atoms_are_named_like_atoms():
    for z in range(1, 119):
        sp = lookup(z)
        assert not sp.name.startswith(("elemental ", "monoatomic ")), sp


def test_species_smiles_and_neutrons():
    sp = Species("CHEBI:1", "x", 26, "Fe", 3, 56)
    assert sp.smiles == "[56Fe+3]"
    assert sp.neutron_number == 30
    assert lookup(26).smiles == "[Fe]"
    assert lookup(17, -1).smiles == "[Cl-]"


def test_species_of_element_orders_neutral_atom_first():
    family = species_of_element("Fe")
    assert family[0].charge == 0 and family[0].mass_number is None
    assert {s.charge for s in family if s.mass_number is None} == {0, 2, 3}
    assert species_of_element(26) == family


def test_element_number():
    assert element_number("Og") == 118
    assert element_number(8) == 8


@pytest.fixture(scope="module")
def builder():
    spec = importlib.util.spec_from_file_location("build_atomic_species", ROOT / "scripts/build_atomic_species.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "inchi, expected",
    [
        ("InChI=1S/Fe", (26, 0, None)),
        ("InChI=1S/Fe/q+3", (26, 3, None)),
        ("InChI=1S/ClH/h1H/p-1", (17, -1, None)),
        ("InChI=1S/p+1", (1, 1, None)),
        ("InChI=1S/C/i1+1", (6, 0, 13)),
        ("InChI=1S/He/i1-1", (2, 0, 3)),
        # RDKit reports isotope 0 for a zero delta; the builder resolves it
        ("InChI=1S/Na/q+1/i1+0", (11, 1, 23)),
    ],
)
def test_builder_species_key(builder, inchi, expected):
    assert builder.species_key({"id": "CHEBI:0", "name": "x", "inchi": inchi}) == expected


def test_builder_rejects_molecules(builder):
    assert builder.species_key({"id": "CHEBI:0", "name": "x", "inchi": "InChI=1S/ClH/h1H"}) is None
    assert builder.species_key({"id": "CHEBI:0", "name": "x", "inchi": "InChI=1S/H2/h1H"}) is None


def test_builder_reference_isotopes(builder):
    assert [builder.default_mass(z) for z in (1, 6, 11, 26)] == [1, 12, 23, 56]
