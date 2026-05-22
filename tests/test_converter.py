"""Tests for the SMILES-to-chemrof converter."""

import pytest

from chemrof.converter.convert import ChemConverter as SmilesConverter


@pytest.fixture
def converter():
    return SmilesConverter()


class TestBasicConversion:
    def test_ethanol(self, converter):
        """Ethanol produces a SmallMolecule with structural slots filled."""
        result = converter.convert("CCO")
        assert result["type"] == "chemrof:SmallMolecule"
        assert result["smiles_string"] == "CCO"
        assert result["inchi_string"].startswith("InChI=")
        assert result["inchi_chemical_sublayer"] == "C2H6O"
        assert result["empirical_formula"] == "C2H6O"
        assert result["is_organic"] is True
        assert isinstance(result["molecular_mass"], float)
        assert result["molecular_mass"] == pytest.approx(46.042, abs=0.01)
        # ID is InChIKey
        assert result["id"].startswith("INCHIKEY:")

    def test_benzene(self, converter):
        """Benzene SMILES gets canonicalized."""
        result = converter.convert("c1ccccc1")
        assert result["type"] == "chemrof:SmallMolecule"
        assert result["empirical_formula"] == "C6H6"

    def test_calcium_ion(self, converter):
        """Monoatomic cation is classified as AtomCation."""
        result = converter.convert("[Ca+2]")
        assert result["type"] == "chemrof:AtomCation"
        assert result["elemental_charge"] == 2
        assert result["has_element"] == "Ca"
        assert result["inchi_chemical_sublayer"] == "Ca"

    def test_chloride(self, converter):
        """Monoatomic anion is classified as AtomAnion."""
        result = converter.convert("[Cl-]")
        assert result["type"] == "chemrof:AtomAnion"
        assert result["elemental_charge"] == -1
        assert result["has_element"] == "Cl"

    def test_acetate(self, converter):
        """Molecular anion classified correctly."""
        result = converter.convert("CC([O-])=O")
        assert result["type"] == "chemrof:MolecularAnion"
        assert result["elemental_charge"] == -1

    def test_ammonium(self, converter):
        """Molecular cation classified correctly."""
        result = converter.convert("[NH4+]")
        assert result["type"] == "chemrof:MolecularCation"
        assert result["elemental_charge"] == 1


class TestInvalidInput:
    def test_invalid_smiles(self, converter):
        """Invalid SMILES raises ValueError."""
        with pytest.raises(ValueError, match="parse"):
            converter.convert("not_a_smiles_XYZ123")


class TestEnricherPipeline:
    def test_enricher_called(self, converter):
        """Enrichers in the pipeline get called in order."""
        call_log = []

        class LoggingEnricher:
            name = "logger"

            def enrich(self, obj, context):
                call_log.append(self.name)
                obj["_enriched_by"] = self.name
                return obj

        converter.enrichers = [LoggingEnricher()]
        result = converter.convert("CCO")
        assert call_log == ["logger"]
        assert result["_enriched_by"] == "logger"

    def test_multiple_enrichers_run_in_order(self, converter):
        """Multiple enrichers run sequentially."""
        order = []

        class E1:
            name = "first"
            def enrich(self, obj, ctx):
                order.append("first")
                return obj

        class E2:
            name = "second"
            def enrich(self, obj, ctx):
                order.append("second")
                return obj

        converter.enrichers = [E1(), E2()]
        converter.convert("CCO")
        assert order == ["first", "second"]


class TestInchiInput:
    def test_ethanol_inchi(self):
        """InChI input produces same result as SMILES."""
        converter = SmilesConverter()
        result = converter.convert("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3")
        assert result["type"] == "chemrof:SmallMolecule"
        assert result["empirical_formula"] == "C2H6O"

    def test_enantiomer_classification(self):
        """SMILES with assigned stereo classified as Enantiomer."""
        converter = SmilesConverter()
        result = converter.convert("C[C@@H](N)C(=O)O")
        assert result["type"] == "chemrof:Enantiomer"
        assert result["absolute_configuration"] == "(R)"
        assert "isomeric_smiles_string" in result


class TestBackwardsCompat:
    def test_smiles_converter_alias(self):
        """SmilesConverter still works as an alias."""
        from chemrof.converter.convert import SmilesConverter
        converter = SmilesConverter()
        result = converter.convert("CCO")
        assert result["type"] == "chemrof:SmallMolecule"
