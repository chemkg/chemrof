"""--siblings: the other members of an input's family."""

import json
import logging

import pytest
from rdkit import Chem
from typer.testing import CliRunner

from chemrof.cli.main import app
from chemrof.converter.convert import ChemConverter
from chemrof.converter.parse import parse_input
from chemrof.converter.siblings import siblings

runner = CliRunner()


def family(smiles: str, **kwargs) -> list[dict]:
    parsed = parse_input(smiles)
    return siblings(ChemConverter().convert_parsed(parsed), parsed.mol, **kwargs)


def types(entities: list[dict]) -> list[str]:
    return sorted(e["type"].split(":")[1] for e in entities)


class TestElementSiblings:
    def test_family_of_iron(self):
        fam = family("[Fe]")
        assert all(e["atomic_number"] == 26 for e in fam)
        assert fam[0]["type"] == "chemrof:UnchargedAtom"
        by_name = {e["name"]: e for e in fam}
        # natural isotopes, including those ChEBI lacks
        assert {"54Fe", "56Fe", "57Fe", "58Fe"} <= set(by_name)
        # ChEBI-known ions
        assert by_name["Fe+2"]["type"] == "chemrof:AtomCation"
        assert by_name["Fe+3"]["elemental_charge"] == 3
        # and charged isotopes
        assert by_name["57Fe+3"]["type"] == "chemrof:FullySpecifiedAtom"

    def test_any_member_yields_the_whole_family(self):
        ids = lambda smi: {e["id"] for e in family(smi)}
        assert ids("[Fe]") == ids("[Fe+3]") == ids("[57Fe]")

    def test_no_duplicates(self):
        fam = family("[C]")
        assert len({e["id"] for e in fam}) == len(fam)

    def test_input_without_chebi_class_is_still_included(self):
        ion = ChemConverter().convert("[Fe+7]")["id"]
        assert ion in {e["id"] for e in family("[Fe+7]")}

    def test_anions_and_labelled_hydrogen(self):
        names = {e["name"] for e in family("[H]")}
        assert {"H-", "H+", "2H", "3H"} <= names

    def test_element_without_natural_isotopes(self):
        fam = family("[Tc]")  # technetium has none; falls back to ChEBI/neutral atom
        assert fam[0]["name"] == "Tc"


class TestStereoSiblings:
    def test_single_stereocenter_matches_classes_racemic_mixture(self):
        fam = family("C[C@H](N)C(=O)O")
        assert types(fam) == ["Enantiomer", "Enantiomer", "RacemicMixture", "SmallMolecule"]
        cli = runner.invoke(app, ["convert", "CC(N)C(=O)O", "--classes", "RacemicMixture", "--format", "json"])
        via_classes = {e["id"] for e in json.loads(cli.output)}
        assert {e["id"] for e in fam} == via_classes

    def test_enantiomers_are_linked_to_the_parent(self):
        fam = family("C[C@H](N)C(=O)O")
        parent = next(e for e in fam if e["type"] == "chemrof:SmallMolecule")
        enantiomers = [e for e in fam if e["type"] == "chemrof:Enantiomer"]
        assert {e["enantiomer_form_of"] for e in enantiomers} == {parent["id"]}
        assert {e["absolute_configuration"] for e in enantiomers} == {"(R)", "(S)"}

    def test_two_centers_with_meso_form(self):
        # butane-2,3-diol: (R,R) and (S,S) are mirror images, (R,S) is meso
        fam = family("CC(O)C(C)O")
        assert types(fam) == ["Enantiomer", "Enantiomer", "RacemicMixture", "SmallMolecule", "Stereoisomer"]
        meso = next(e for e in fam if e["type"] == "chemrof:Stereoisomer")
        assert "enantiomer_form_of" not in meso

    def test_each_mirror_pair_gets_one_racemic_mixture(self):
        fam = family("OCC(O)C(O)C=O")  # erythrose/threose: 4 stereoisomers, 2 pairs
        assert types(fam).count("Enantiomer") == 4
        mixtures = [e for e in fam if e["type"] == "chemrof:RacemicMixture"]
        assert len(mixtures) == 2
        assert len({m["id"] for m in mixtures}) == 2
        ids = {e["id"] for e in fam}
        for m in mixtures:
            assert m["has_left_enantiomer"] in ids and m["has_right_enantiomer"] in ids
            assert m["has_left_enantiomer"] != m["has_right_enantiomer"]

    def test_double_bond_isomers_are_not_enantiomers(self):
        fam = family("C/C=C/C")
        assert types(fam) == ["SmallMolecule", "Stereoisomer", "Stereoisomer"]

    def test_all_stereoisomers_have_isomeric_smiles(self):
        for e in family("CC(O)C(C)O"):
            if e["type"] in ("chemrof:Enantiomer", "chemrof:Stereoisomer"):
                assert Chem.MolFromSmiles(e["isomeric_smiles_string"]) is not None

    def test_cap_limits_output_and_warns(self, caplog):
        with caplog.at_level(logging.WARNING):
            fam = family("OCC(O)C(O)C(O)C(O)C=O", max_siblings=4)  # 16 possible
        assert sum(e["type"] != "chemrof:SmallMolecule" and "isomeric_smiles_string" in e for e in fam) == 4
        assert "16 stereoisomers possible" in caplog.text

    def test_racemate_ids_do_not_depend_on_the_cap(self):
        ids = lambda n: {e["id"] for e in family("OCC(O)C(O)C(O)C=O", max_siblings=n) if e["type"].endswith("Racemic")}
        # the mixtures present in a truncated run keep the id they have in the full run
        full = {e["id"] for e in family("OCC(O)C(O)C(O)C=O", max_siblings=64) if "rac-" in e["id"]}
        part = {e["id"] for e in family("OCC(O)C(O)C(O)C=O", max_siblings=8) if "rac-" in e["id"]}
        assert part <= full

    def test_achiral_molecule_has_no_siblings(self, caplog):
        with caplog.at_level(logging.WARNING):
            fam = family("CCO")
        assert [e["type"] for e in fam] == ["chemrof:SmallMolecule"]
        assert "No stereo elements" in caplog.text

    def test_salt_falls_back_with_warning(self, caplog):
        with caplog.at_level(logging.WARNING):
            fam = family("[Na+].[Cl-]")
        assert [e["type"] for e in fam] == ["chemrof:ChemicalSalt"]
        assert "does not apply to salts" in caplog.text


class TestCli:
    def test_siblings_flag(self):
        result = runner.invoke(app, ["convert", "[Fe]", "--siblings", "--format", "json"])
        assert result.exit_code == 0
        assert len(json.loads(result.output)) > 5

    def test_siblings_with_chebi_enrichment(self):
        result = runner.invoke(app, ["convert", "[Fe]", "--siblings", "-e", "chebi", "--format", "json"])
        ids = {e["id"] for e in json.loads(result.output)}
        assert {"CHEBI:18248", "CHEBI:29033", "CHEBI:29034"} <= ids

    def test_siblings_keep_racemate_links_after_enrichment(self):
        result = runner.invoke(app, ["convert", "CC(O)C(C)O", "--siblings", "-e", "chebi", "--format", "json"])
        data = json.loads(result.output)
        ids = {e["id"] for e in data}
        mixture = next(e for e in data if e["type"] == "chemrof:RacemicMixture")
        assert {mixture["has_left_enantiomer"], mixture["has_right_enantiomer"]} <= ids

    def test_max_siblings_option(self):
        result = runner.invoke(
            app, ["convert", "OCC(O)C(O)C(O)C=O", "--siblings", "--max-siblings", "4", "--format", "json"]
        )
        assert result.exit_code == 0
        assert sum("isomeric_smiles_string" in e for e in json.loads(result.output)) == 4

    @pytest.mark.parametrize("extra", [["--classes", "Enantiomer"], ["--autochain"]])
    def test_conflicts_with_autochain_options(self, extra):
        result = runner.invoke(app, ["convert", "CC(N)C(=O)O", "--siblings", *extra])
        assert result.exit_code != 0
        assert "cannot be combined" in result.output

    def test_owl_output(self):
        result = runner.invoke(app, ["convert", "C[C@H](N)C(=O)O", "--siblings", "--format", "owl"])
        assert result.exit_code == 0
        assert "RacemicMixture" in result.output
