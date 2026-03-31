"""Tests for OWL output from SMILES converter."""

import pytest

from chemrof.converter.smiles import SmilesConverter
from chemrof.converter.owl_output import dicts_to_owl


@pytest.fixture
def converter():
    return SmilesConverter()


class TestDictsToOwl:
    def test_small_molecule(self, converter):
        obj = converter.convert("CCO")
        owl = dicts_to_owl([obj])
        assert "SubClassOf" in owl
        assert "SmallMolecule" in owl
        assert "LFQSCWFLJHTTHZ" in owl
        assert "CCO" in owl

    def test_atom_cation(self, converter):
        obj = converter.convert("[Ca+2]")
        owl = dicts_to_owl([obj])
        assert "AtomCation" in owl
        assert "has_element" in owl or "Ca" in owl

    def test_atom_anion(self, converter):
        obj = converter.convert("[Cl-]")
        owl = dicts_to_owl([obj])
        assert "AtomAnion" in owl

    def test_multiple_molecules(self, converter):
        objs = [converter.convert(s) for s in ["CCO", "[Ca+2]"]]
        owl = dicts_to_owl(objs)
        assert "SmallMolecule" in owl
        assert "AtomCation" in owl

    def test_ofn_format(self, converter):
        obj = converter.convert("CCO")
        owl = dicts_to_owl([obj], output_type="ofn")
        assert "Ontology(" in owl
        assert "Declaration(Class(" in owl

    def test_rdfxml_format(self, converter):
        obj = converter.convert("CCO")
        owl = dicts_to_owl([obj], output_type="owl")
        assert "rdf:RDF" in owl or "owl:Class" in owl or "xml" in owl.lower()

    def test_annotation_assertions(self, converter):
        obj = converter.convert("CCO")
        owl = dicts_to_owl([obj])
        assert "AnnotationAssertion" in owl
        assert "smiles_string" in owl
        assert "inchi_string" in owl
        assert "empirical_formula" in owl
        assert "molecular_mass" in owl

    def test_label(self, converter):
        obj = converter.convert("CCO")
        owl = dicts_to_owl([obj])
        assert "rdfs:label" in owl or "label" in owl


class TestCliOwlFormat:
    def test_cli_owl_output(self):
        from typer.testing import CliRunner
        from chemrof.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, ["from-smiles", "CCO", "--format", "owl"])
        assert result.exit_code == 0
        assert "SubClassOf" in result.output
        assert "SmallMolecule" in result.output
