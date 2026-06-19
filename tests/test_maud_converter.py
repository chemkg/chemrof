"""Tests for the Maud kinetic-model -> chemrof converter."""

from __future__ import annotations

import json

import yaml
from typer.testing import CliRunner

from chemrof.cli.main import app
from chemrof.converter.maud import MaudConverter, convert_maud_file

runner = CliRunner()

# A minimal Maud kinetic model exercising metabolites, a reaction with signed
# float stoichiometry, a reversible mechanism, allostery and competitive
# inhibition.
SAMPLE_MODEL = {
    "metabolite": [
        {"id": "met-L", "name": "methionine", "inchi_key": "FFEARJCKVFRZRR-BYPYZUCNSA-N"},
        {"id": "atp", "name": "ATP", "inchi_key": "ZKHQWZAMYRWXGA-KQYNXXCUSA-J"},
        {"id": "amet", "name": "S-adenosylmethionine", "inchi_key": "MEFKEPWMEQBLKI-AIRLBKTGSA-O"},
        {"id": "pi", "name": "phosphate"},  # no inchi_key -> maud.metabolite id
    ],
    "metabolite_in_compartment": [
        {"metabolite_id": m, "compartment_id": "c"}
        for m in ["met-L", "atp", "amet", "pi"]
    ],
    "reaction": [
        {
            "id": "METAT",
            "name": "Methionine adenosyltransferase",
            "mechanism": "irreversible_michaelis_menten",
            "stoichiometry": {"met-L_c": -1.0, "atp_c": -1.0, "amet_c": 1.0, "pi_c": 1.0},
        },
        {
            "id": "AHC",
            "name": "SAH hydrolase",
            "mechanism": "reversible_michaelis_menten",
            "stoichiometry": {"amet_c": -1.0, "met-L_c": 1.0},
        },
    ],
    "enzyme_reaction": [
        {"enzyme_id": "MAT1", "reaction_id": "METAT"},
        {"enzyme_id": "MAT3", "reaction_id": "METAT"},
    ],
    "allostery": [
        {"enzyme_id": "MAT3", "metabolite_id": "amet", "compartment_id": "c",
         "modification_type": "activation"},
    ],
    "competitive_inhibition": [
        {"enzyme_id": "MAT1", "reaction_id": "METAT", "metabolite_id": "amet",
         "compartment_id": "c"},
    ],
}


def _reactions(collection):
    return {
        e["id"]: e for e in collection["entities"] if e["type"] == "chemrof:Reaction"
    }


def _metabolites(collection):
    return [e for e in collection["entities"] if e["type"] == "chemrof:SmallMolecule"]


class TestConvertModel:
    def setup_method(self):
        self.coll = MaudConverter().convert_model(SAMPLE_MODEL)

    def test_metabolites_keyed_by_inchikey(self):
        mets = {m["id"]: m for m in _metabolites(self.coll)}
        assert "INCHIKEY:FFEARJCKVFRZRR-BYPYZUCNSA-N" in mets
        assert mets["INCHIKEY:FFEARJCKVFRZRR-BYPYZUCNSA-N"]["inchi_key_string"] == \
            "FFEARJCKVFRZRR-BYPYZUCNSA-N"

    def test_metabolite_without_inchikey_uses_fallback_id(self):
        ids = {m["id"] for m in _metabolites(self.coll)}
        assert "maud.metabolite:pi" in ids

    def test_reaction_participants_split_by_sign(self):
        rxn = _reactions(self.coll)["maud.reaction:METAT"]
        left = {p["participant"] for p in rxn["left_participants"]}
        right = {p["participant"] for p in rxn["right_participants"]}
        assert "INCHIKEY:FFEARJCKVFRZRR-BYPYZUCNSA-N" in left  # met-L consumed
        assert "INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O" in right  # amet produced
        assert all(isinstance(p["stoichiometry"], float) for p in rxn["left_participants"])

    def test_mechanism_and_direction(self):
        rxns = _reactions(self.coll)
        assert rxns["maud.reaction:METAT"]["reaction_mechanism"] == "irreversible_michaelis_menten"
        assert rxns["maud.reaction:METAT"]["direction"] == "l->r"
        assert rxns["maud.reaction:AHC"]["direction"] == "bidirectional"

    def test_allosteric_regulation_attached_to_right_reaction(self):
        rxn = _reactions(self.coll)["maud.reaction:METAT"]
        regs = rxn["has_allosteric_regulation"]
        assert any(
            r["regulated_enzyme"] == "MAT3"
            and r["modification_type"] == "activation"
            and r["effector"] == "INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O"
            for r in regs
        )

    def test_competitive_inhibition_attached(self):
        rxn = _reactions(self.coll)["maud.reaction:METAT"]
        ci = rxn["has_competitive_inhibition"]
        assert ci[0]["regulated_enzyme"] == "MAT1"
        assert ci[0]["effector"] == "INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O"


class TestConvertFile:
    def test_reads_toml_file(self, tmp_path):
        import toml

        path = tmp_path / "model.toml"
        path.write_text(toml.dumps(SAMPLE_MODEL))
        coll = convert_maud_file(path)
        assert len(_metabolites(coll)) == 4
        assert len(_reactions(coll)) == 2

    def test_resolves_config_indirection(self, tmp_path):
        import toml

        (tmp_path / "kin.toml").write_text(toml.dumps(SAMPLE_MODEL))
        config = tmp_path / "config.toml"
        config.write_text(toml.dumps({"name": "x", "kinetic_model_file": "kin.toml"}))
        coll = convert_maud_file(config)
        assert len(_reactions(coll)) == 2


class TestCli:
    def test_convert_maud_yaml(self, tmp_path):
        import toml

        path = tmp_path / "model.toml"
        path.write_text(toml.dumps(SAMPLE_MODEL))
        result = runner.invoke(app, ["convert-maud", str(path)])
        assert result.exit_code == 0
        data = yaml.safe_load(result.output)
        assert "entities" in data

    def test_convert_maud_json(self, tmp_path):
        import toml

        path = tmp_path / "model.toml"
        path.write_text(toml.dumps(SAMPLE_MODEL))
        result = runner.invoke(app, ["convert-maud", str(path), "--format", "json"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert any(e["type"] == "chemrof:Reaction" for e in data["entities"])
