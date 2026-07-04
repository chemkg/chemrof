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


class TestGenericGroupingEquivalentClasses:
    """Generic grouping meta-patterns emit computable OWL definitions from data.

    The schema holds only the reusable meta-patterns (GroupingBySmarts,
    GroupingByGenusAndRangeRestriction, GroupingByGenusAndPropertyValue); each
    carries an ``owl.template`` that turns a data instance's genus/on_property/
    value parameters into a genus-differentia axiom. Concrete groupings (long-
    chain fatty acyl-CoA, etc.) are data, not schema subclasses.
    """

    @staticmethod
    def _axiom_for(owl: str, class_id: str, kind: str = "EquivalentClasses") -> str:
        for line in owl.splitlines():
            if kind in line and class_id in line:
                return line
        raise AssertionError(f"no {kind} axiom for {class_id}")

    def test_range_restriction_both_bounds(self):
        owl = dicts_to_owl([
            {"id": "CHEBI:33184", "type": "chemrof:GroupingByGenusAndRangeRestriction",
             "genus": "CHEBI:37554", "on_property": "chemrof:carbon_number",
             "min_value": 13, "max_value": 22},
        ])
        ax = self._axiom_for(owl, "CHEBI:33184")
        assert "CHEBI:37554" in ax
        assert "carbon_number" in ax
        assert 'minInclusive> "13"' in ax
        assert 'maxInclusive> "22"' in ax

    def test_range_restriction_min_only_has_no_max(self):
        owl = dicts_to_owl([
            {"id": "CHEBI:61910", "type": "chemrof:GroupingByGenusAndRangeRestriction",
             "genus": "CHEBI:37554", "on_property": "chemrof:carbon_number",
             "min_value": 23},
        ])
        ax = self._axiom_for(owl, "CHEBI:61910")
        assert 'minInclusive> "23"' in ax
        assert "maxInclusive" not in ax

    def test_range_restriction_exact_zero(self):
        owl = dicts_to_owl([
            {"id": "CHEBI:231546", "type": "chemrof:GroupingByGenusAndRangeRestriction",
             "genus": "CHEBI:37554",
             "on_property": "chemrof:carbon_carbon_double_bond_number",
             "min_value": 0, "max_value": 0},
        ])
        ax = self._axiom_for(owl, "CHEBI:231546")
        assert "carbon_carbon_double_bond_number" in ax
        assert 'minInclusive> "0"' in ax
        assert 'maxInclusive> "0"' in ax

    def test_property_value_boolean(self):
        owl = dicts_to_owl([
            {"id": "chemrof:LinearFattyAcylCoA", "type": "chemrof:GroupingByGenusAndPropertyValue",
             "genus": "CHEBI:37554", "on_property": "chemrof:is_branched",
             "value": "false", "value_datatype": "xsd:boolean"},
        ])
        ax = self._axiom_for(owl, "chemrof:LinearFattyAcylCoA")
        assert "is_branched" in ax
        assert '"false"' in ax
        assert "boolean" in ax

    def test_property_value_default_string_datatype(self):
        owl = dicts_to_owl([
            {"id": "chemrof:OddNumberedFattyAcylCoA", "type": "chemrof:GroupingByGenusAndPropertyValue",
             "genus": "CHEBI:37554", "on_property": "chemrof:carbon_number_parity",
             "value": "odd"},
        ])
        ax = self._axiom_for(owl, "chemrof:OddNumberedFattyAcylCoA")
        assert "carbon_number_parity" in ax
        assert '"odd"' in ax
        assert "string" in ax

    def test_smarts_grouping_is_subclass_of_genus(self):
        owl = dicts_to_owl([
            {"id": "CHEBI:37554", "type": "chemrof:GroupingBySmarts",
             "genus": "CHEBI:17984", "smarts_string": "[#6]C(=O)S"},
        ])
        ax = self._axiom_for(owl, "CHEBI:37554", kind="SubClassOf")
        assert "CHEBI:17984" in ax
        # SMARTS is carried as an annotation, not a DL axiom
        assert "smarts_string" in owl


class TestCliOwlFormat:
    def test_cli_owl_output(self):
        from typer.testing import CliRunner
        from chemrof.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, ["convert", "CCO", "--format", "owl"])
        assert result.exit_code == 0
        assert "AnnotationAssertion" in result.output
