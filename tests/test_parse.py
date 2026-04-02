"""Tests for input format detection and parsing."""

import pytest

from chemrof.converter.parse import ParsedInput, parse_input


class TestParseSmiles:
    def test_simple_smiles(self):
        """Plain SMILES string is detected and parsed."""
        result = parse_input("CCO")
        assert result.input_format == "smiles"
        assert result.original == "CCO"
        assert result.mol is not None
        assert result.inchi_stereo_type == ""
        assert result.is_racemic is False

    def test_ion_smiles(self):
        result = parse_input("[Ca+2]")
        assert result.input_format == "smiles"
        assert result.mol is not None

    def test_stereo_smiles(self):
        """SMILES with stereo is parsed with mol retaining chirality."""
        result = parse_input("C[C@@H](N)C(=O)O")
        assert result.input_format == "smiles"
        assert result.mol is not None

    def test_invalid_smiles(self):
        with pytest.raises(ValueError, match="parse"):
            parse_input("not_a_molecule_XYZ")


class TestParseInchi:
    def test_standard_inchi(self):
        """Standard InChI is detected and parsed."""
        inchi = "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3"
        result = parse_input(inchi)
        assert result.input_format == "inchi"
        assert result.original == inchi
        assert result.mol is not None
        assert result.inchi_stereo_type == ""
        assert result.is_racemic is False

    def test_inchi_with_absolute_stereo(self):
        """InChI with /s1 (absolute) is detected."""
        inchi = "InChI=1S/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/m1/s1"
        result = parse_input(inchi)
        assert result.inchi_stereo_type == "s1"
        assert result.is_racemic is False

    def test_racemic_inchi(self):
        """Non-standard InChI with /s3 (racemic) is detected."""
        inchi = "InChI=1/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/s3"
        result = parse_input(inchi)
        assert result.input_format == "inchi"
        assert result.inchi_stereo_type == "s3"
        assert result.is_racemic is True

    def test_invalid_inchi(self):
        with pytest.raises(ValueError, match="parse"):
            parse_input("InChI=1S/")
