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

    def test_classified_by_outputs_subclass_axioms(self, converter):
        obj = converter.convert("CCO")
        obj["classified_by"] = ["CHEMONTID:0000000", "CHEMONTID:0000286"]
        owl = dicts_to_owl([obj])
        assert "SubClassOf" in owl
        assert "CHEMONTID:0000000" in owl
        assert "CHEMONTID:0000286" in owl
        assert "AnnotationAssertion(chemrof:classified_by" not in owl


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


class TestFattyAcylGroupingEquivalentClasses:
    """Fatty acyl-CoA facet grouping classes emit computable OWL definitions.

    Each facet class carries an ``owl.template`` annotation that turns the
    grouping's defining constraint values into a necessary-and-sufficient
    ``EquivalentClasses`` axiom (genus CHEBI:37554 = fatty acyl-CoA, plus a
    datatype/value restriction on a member-level property).
    """

    @staticmethod
    def _axiom_for(owl: str, class_id: str) -> str:
        for line in owl.splitlines():
            if "EquivalentClasses" in line and class_id in line:
                return line
        raise AssertionError(f"no EquivalentClasses axiom for {class_id}")

    def test_chain_length_range(self):
        owl = dicts_to_owl([
            {"id": "CHEBI:33184", "type": "chemrof:FattyAcylChainLengthGroupingClass",
             "min_carbon_number": 13, "max_carbon_number": 22},
        ])
        ax = self._axiom_for(owl, "CHEBI:33184")
        assert "CHEBI:37554" in ax
        assert "carbon_number" in ax
        assert 'minInclusive> "13"' in ax
        assert 'maxInclusive> "22"' in ax

    def test_chain_length_min_only_has_no_max(self):
        owl = dicts_to_owl([
            {"id": "CHEBI:61910", "type": "chemrof:FattyAcylChainLengthGroupingClass",
             "min_carbon_number": 23},
        ])
        ax = self._axiom_for(owl, "CHEBI:61910")
        assert 'minInclusive> "23"' in ax
        assert "maxInclusive" not in ax

    def test_saturation_exact_zero(self):
        owl = dicts_to_owl([
            {"id": "CHEBI:231546", "type": "chemrof:FattyAcylSaturationGroupingClass",
             "min_carbon_carbon_double_bond_number": 0,
             "max_carbon_carbon_double_bond_number": 0},
        ])
        ax = self._axiom_for(owl, "CHEBI:231546")
        assert "carbon_carbon_double_bond_number" in ax
        assert 'minInclusive> "0"' in ax
        assert 'maxInclusive> "0"' in ax

    def test_branching_boolean(self):
        owl = dicts_to_owl([
            {"id": "chemrof:LinearFattyAcylCoA", "type": "chemrof:FattyAcylBranchingGroupingClass",
             "is_branched": False},
        ])
        ax = self._axiom_for(owl, "chemrof:LinearFattyAcylCoA")
        assert "is_branched" in ax
        assert '"false"' in ax

    def test_carbon_parity_value(self):
        owl = dicts_to_owl([
            {"id": "chemrof:OddNumberedFattyAcylCoA", "type": "chemrof:FattyAcylCarbonParityGroupingClass",
             "carbon_number_parity": "odd"},
        ])
        ax = self._axiom_for(owl, "chemrof:OddNumberedFattyAcylCoA")
        assert "carbon_number_parity" in ax
        assert '"odd"' in ax


class TestCliOwlFormat:
    def test_cli_owl_output(self):
        from typer.testing import CliRunner
        from chemrof.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, ["convert", "CCO", "--format", "owl"])
        assert result.exit_code == 0
        assert "AnnotationAssertion" in result.output
