"""Tests for the chemrof CLI."""

import json

import pytest
import yaml
from typer.testing import CliRunner

from chemrof.cli.main import app

runner = CliRunner()


class TestConvertCommand:
    def test_basic_smiles(self):
        result = runner.invoke(app, ["convert", "CCO"])
        assert result.exit_code == 0
        data = yaml.safe_load(result.output)
        assert data["type"] == "chemrof:SmallMolecule"

    def test_json_format(self):
        result = runner.invoke(app, ["convert", "CCO", "--format", "json"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["type"] == "chemrof:SmallMolecule"

    def test_inchi_input(self):
        result = runner.invoke(app, ["convert", "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3"])
        assert result.exit_code == 0
        data = yaml.safe_load(result.output)
        assert data["type"] == "chemrof:SmallMolecule"
        assert data["empirical_formula"] == "C2H6O"

    def test_owl_format(self):
        result = runner.invoke(app, ["convert", "CCO", "--format", "owl"])
        assert result.exit_code == 0
        assert "SubClassOf" in result.output or "AnnotationAssertion" in result.output


class TestFromSmilesAlias:
    def test_alias_works(self):
        result = runner.invoke(app, ["from-smiles", "CCO"])
        assert result.exit_code == 0
        data = yaml.safe_load(result.output)
        assert data["type"] == "chemrof:SmallMolecule"


class TestAutochain:
    def test_classes_implies_autochain(self):
        result = runner.invoke(app, ["convert", "CC(N)C(=O)O", "--classes", "RacemicMixture", "--format", "json"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert isinstance(data, list)
        types = [d["type"] for d in data]
        assert "chemrof:RacemicMixture" in types
        assert types.count("chemrof:Enantiomer") == 2

    def test_autochain_yaml(self):
        result = runner.invoke(app, ["convert", "CC(N)C(=O)O", "--classes", "RacemicMixture"])
        assert result.exit_code == 0
        # YAML multi-doc: load all documents
        docs = list(yaml.safe_load_all(result.output))
        types = [d["type"] for d in docs]
        assert "chemrof:RacemicMixture" in types

    def test_racemic_inchi_auto_triggers(self):
        """Non-standard InChI with /s3 auto-triggers autochain."""
        rac_inchi = "InChI=1/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/s3"
        result = runner.invoke(app, ["convert", rac_inchi, "--format", "json"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert isinstance(data, list)
        types = [d["type"] for d in data]
        assert "chemrof:RacemicMixture" in types
