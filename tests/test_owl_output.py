"""Tests for OWL output via linkml-data2owl."""

import pytest

from chemrof.converter.convert import ChemConverter
from chemrof.converter.owl_output import dicts_to_owl


@pytest.fixture
def converter():
    return ChemConverter()


class TestDictsToOwl:
    def test_small_molecule(self, converter):
        obj = converter.convert("CCO")
        owl = dicts_to_owl([obj])
        assert "LFQSCWFLJHTTHZ" in owl
        assert "CCO" in owl

    def test_atom_cation_equivalent_classes(self, converter):
        """AtomCation produces EquivalentClasses axiom via owl.template."""
        obj = converter.convert("[Ca+2]")
        owl = dicts_to_owl([obj])
        assert "EquivalentClasses" in owl
        assert "MonoatomicIon" in owl
        assert "has_element" in owl
        assert "elemental_charge" in owl

    def test_atom_anion(self, converter):
        obj = converter.convert("[Cl-]")
        owl = dicts_to_owl([obj])
        assert "VEXZGXHMUGYJMC" in owl or "Cl" in owl

    def test_multiple_molecules(self, converter):
        objs = [converter.convert(s) for s in ["CCO", "[Ca+2]"]]
        owl = dicts_to_owl(objs)
        assert "LFQSCWFLJHTTHZ" in owl  # ethanol InChIKey
        assert "MonoatomicIon" in owl  # from Ca2+ template

    def test_ofn_format(self, converter):
        obj = converter.convert("CCO")
        owl = dicts_to_owl([obj], output_type="ofn")
        assert "Ontology(" in owl
        assert "AnnotationAssertion" in owl

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

    def test_label(self, converter):
        obj = converter.convert("CCO")
        owl = dicts_to_owl([obj])
        assert "label" in owl


class TestEquivalentClassesAxioms:
    def test_enantiomer_equivalent_classes(self, converter):
        """Enantiomer produces EquivalentClasses axiom."""
        obj = converter.convert("C[C@@H](N)C(=O)O")
        owl = dicts_to_owl([obj])
        assert "EquivalentClasses" in owl
        assert "Enantiomer" in owl

    def test_autochain_owl(self):
        """Autochain entities all appear in OWL output."""
        from rdkit import Chem
        from chemrof.converter.autochain import autochain

        converter = ChemConverter()
        entity = converter.convert("CC(N)C(=O)O")
        mol = Chem.MolFromSmiles("CC(N)C(=O)O")
        results = autochain(entity, {"RacemicMixture"}, mol)
        owl = dicts_to_owl(results)
        assert "RacemicMixture" in owl
        assert "Enantiomer" in owl


class TestCliOwlFormat:
    def test_cli_owl_output(self):
        from typer.testing import CliRunner
        from chemrof.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, ["convert", "CCO", "--format", "owl"])
        assert result.exit_code == 0
        assert "AnnotationAssertion" in result.output
