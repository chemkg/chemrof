# tests/test_cli.py
"""Tests for the chemrof CLI."""

import json

import yaml
import pytest
from typer.testing import CliRunner

from chemrof.cli.main import app

runner = CliRunner()


def test_from_smiles_yaml_output():
    """Default output is YAML."""
    result = runner.invoke(app, ["from-smiles", "CCO"])
    assert result.exit_code == 0, result.output
    data = yaml.safe_load(result.output)
    assert data["type"] == "chemrof:SmallMolecule"
    assert data["empirical_formula"] == "C2H6O"


def test_from_smiles_json_output():
    """--format json produces valid JSON."""
    result = runner.invoke(app, ["from-smiles", "CCO", "--format", "json"])
    assert result.exit_code == 0, result.output
    data = json.loads(result.output)
    assert data["type"] == "chemrof:SmallMolecule"


def test_from_smiles_multiple():
    """Multiple SMILES produce a YAML list."""
    result = runner.invoke(app, ["from-smiles", "CCO", "c1ccccc1"])
    assert result.exit_code == 0, result.output
    # Output should be a YAML list
    data = yaml.safe_load(result.output)
    assert isinstance(data, list)
    assert len(data) == 2


def test_from_smiles_invalid():
    """Invalid SMILES reports an error."""
    result = runner.invoke(app, ["from-smiles", "NOT_VALID_XYZ"])
    assert result.exit_code != 0 or "Error" in result.output


def test_from_smiles_ion():
    """Ions are classified correctly via CLI."""
    result = runner.invoke(app, ["from-smiles", "[Ca+2]", "--format", "json"])
    assert result.exit_code == 0, result.output
    data = json.loads(result.output)
    assert data["type"] == "chemrof:AtomCation"
