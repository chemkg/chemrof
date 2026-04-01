"""Tests for autochain entity graph generation."""

import pytest
from rdkit import Chem

from chemrof.converter.autochain import autochain
from chemrof.converter.convert import ChemConverter


@pytest.fixture
def converter():
    return ChemConverter()


class TestAutochainFromAgnostic:
    """Input is a stereo-neutral SMILES -> generate full racemate graph."""

    def test_alanine_racemic_mixture(self, converter):
        """Stereo-neutral alanine + RacemicMixture -> 4 entities."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        types = [r["type"] for r in results]
        assert "chemrof:SmallMolecule" in types  # agnostic
        assert types.count("chemrof:Enantiomer") == 2
        assert "chemrof:RacemicMixture" in types
        assert len(results) == 4

    def test_enantiomers_have_enantiomer_form_of(self, converter):
        """Generated enantiomers link back to agnostic form."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        agnostic = [r for r in results if r["type"] == "chemrof:SmallMolecule"][0]
        enantiomers = [r for r in results if r["type"] == "chemrof:Enantiomer"]
        for e in enantiomers:
            assert e["enantiomer_form_of"] == agnostic["id"]

    def test_racemic_mixture_links(self, converter):
        """RacemicMixture entity links enantiomers and agnostic form."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        mixture = [r for r in results if r["type"] == "chemrof:RacemicMixture"][0]
        enantiomer_ids = {r["id"] for r in results if r["type"] == "chemrof:Enantiomer"}
        agnostic_id = [r for r in results if r["type"] == "chemrof:SmallMolecule"][0]["id"]

        assert mixture["has_left_enantiomer"] in enantiomer_ids
        assert mixture["has_right_enantiomer"] in enantiomer_ids
        assert mixture["has_left_enantiomer"] != mixture["has_right_enantiomer"]
        assert mixture["chirality_agnostic_form"] == agnostic_id

    def test_racemic_mixture_has_no_inchi(self, converter):
        """RacemicMixture is a mixture -- no InChI, SMILES, or mass."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        mixture = [r for r in results if r["type"] == "chemrof:RacemicMixture"][0]
        assert "inchi_string" not in mixture
        assert "smiles_string" not in mixture
        assert "molecular_mass" not in mixture

    def test_enantiomers_have_stereo_inchi(self, converter):
        """Generated enantiomers have InChI with /t and /s layers."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        enantiomers = [r for r in results if r["type"] == "chemrof:Enantiomer"]
        configs = {e["absolute_configuration"] for e in enantiomers}
        assert configs == {"(R)", "(S)"}
        for e in enantiomers:
            assert "/t" in e["inchi_string"]
            assert "inchi_tetrahedral_stereochemical_sublayer" in e
            assert "inchi_stereochemical_type_sublayer" in e


class TestAutochainFromEnantiomer:
    """Input is a specific enantiomer -> generate agnostic + mirror + mixture."""

    def test_from_specific_enantiomer(self, converter):
        """L-alanine + RacemicMixture -> 4 entities (agnostic + R + S + mixture)."""
        entity = converter.convert("C[C@@H](N)C(=O)O")
        mol = Chem.MolFromSmiles("C[C@@H](N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        types = [r["type"] for r in results]
        assert "chemrof:SmallMolecule" in types
        assert types.count("chemrof:Enantiomer") == 2
        assert "chemrof:RacemicMixture" in types


class TestAutochainEnantiomerOnly:
    """--classes Enantiomer without RacemicMixture."""

    def test_enantiomer_only(self, converter):
        """Stereo-neutral + Enantiomer -> 3 entities (agnostic + R + S, no mixture)."""
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"Enantiomer"}, mol)

        types = [r["type"] for r in results]
        assert "chemrof:SmallMolecule" in types
        assert types.count("chemrof:Enantiomer") == 2
        assert "chemrof:RacemicMixture" not in types


class TestAutochainSalt:
    """Salt autochain decomposes into cation + anion + salt entity."""

    def test_nacl_produces_three_entities(self, converter):
        """NaCl -> Na+ entity, Cl- entity, salt entity."""
        entity = converter.convert("[Na+].[Cl-]")
        mol = Chem.MolFromSmiles("[Na+].[Cl-]")
        results = autochain(entity, {"ChemicalSalt"}, mol)

        assert len(results) == 3
        types = [r["type"] for r in results]
        assert "chemrof:AtomCation" in types
        assert "chemrof:AtomAnion" in types
        assert "chemrof:ChemicalSalt" in types

    def test_salt_links_components(self, converter):
        """Salt entity has has_cationic_component and has_anionic_component."""
        entity = converter.convert("[Na+].[Cl-]")
        mol = Chem.MolFromSmiles("[Na+].[Cl-]")
        results = autochain(entity, {"ChemicalSalt"}, mol)

        salt = [r for r in results if r["type"] == "chemrof:ChemicalSalt"][0]
        cation = [r for r in results if r["type"] == "chemrof:AtomCation"][0]
        anion = [r for r in results if r["type"] == "chemrof:AtomAnion"][0]

        assert salt["has_cationic_component"] == cation["id"]
        assert salt["has_anionic_component"] == anion["id"]
        assert salt["elemental_charge"] == 0

    def test_sodium_acetate(self, converter):
        """Molecular anion salt: Na+ + acetate."""
        entity = converter.convert("[Na+].CC([O-])=O")
        mol = Chem.MolFromSmiles("[Na+].CC([O-])=O")
        results = autochain(entity, {"ChemicalSalt"}, mol)

        types = [r["type"] for r in results]
        assert "chemrof:AtomCation" in types
        assert "chemrof:MolecularAnion" in types
        assert "chemrof:ChemicalSalt" in types

    def test_components_have_structural_data(self, converter):
        """Component entities have their own InChI/SMILES."""
        entity = converter.convert("[Na+].[Cl-]")
        mol = Chem.MolFromSmiles("[Na+].[Cl-]")
        results = autochain(entity, {"ChemicalSalt"}, mol)

        for comp in results[:-1]:  # all except salt
            assert "inchi_string" in comp
            assert "smiles_string" in comp

    def test_salt_has_structural_data(self, converter):
        """Salt entity itself has InChI/SMILES for the full compound."""
        entity = converter.convert("[Na+].[Cl-]")
        mol = Chem.MolFromSmiles("[Na+].[Cl-]")
        results = autochain(entity, {"ChemicalSalt"}, mol)

        salt = [r for r in results if r["type"] == "chemrof:ChemicalSalt"][0]
        assert "inchi_string" in salt
        assert "smiles_string" in salt


class TestAutochainMultipleStereocenters:
    """Multi-stereocenter molecules are not supported in v1."""

    def test_multi_stereo_warns(self, converter):
        """Molecule with >1 stereocenter returns just the input entity."""
        # Tartaric acid: 2 stereocenters
        entity = converter.convert("OC(C(O)C(=O)O)C(=O)O")
        mol = Chem.MolFromSmiles("OC(C(O)C(=O)O)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)

        # Should return just the original entity (no expansion)
        assert len(results) == 1
        assert results[0]["id"] == entity["id"]
