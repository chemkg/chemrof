"""Tests for InChI string decomposition into chemrof sublayer slots."""

import pytest

from chemrof.converter.inchi import parse_inchi_sublayers


def test_parse_ethanol():
    """Ethanol InChI decomposes into formula and connections."""
    result = parse_inchi_sublayers("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3")
    assert result["inchi_chemical_sublayer"] == "C2H6O"
    assert result["inchi_atom_connections_sublayer"] == "1-2-3"
    assert result["inchi_hydrogen_connections_sublayer"] == "3H,2H2,1H3"


def test_parse_calcium_ion():
    """Monoatomic ion InChI has formula and charge."""
    result = parse_inchi_sublayers("InChI=1S/Ca/q+2")
    assert result["inchi_chemical_sublayer"] == "Ca"
    assert result["inchi_charge_sublayer"] == "+2"
    assert "inchi_atom_connections_sublayer" not in result


def test_parse_acetate():
    """Acetate has formula, connections, hydrogen, and charge layers."""
    result = parse_inchi_sublayers("InChI=1S/C2H4O2/c1-2(3)4/h1H3,(H,3,4)/p-1")
    assert result["inchi_chemical_sublayer"] == "C2H4O2"
    assert result["inchi_proton_sublayer"] == "-1"


def test_parse_invalid():
    """Non-InChI strings return empty dict."""
    assert parse_inchi_sublayers("not-an-inchi") == {}
    assert parse_inchi_sublayers("") == {}
