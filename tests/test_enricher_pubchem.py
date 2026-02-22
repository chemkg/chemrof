"""Tests for PubChem enricher — uses mocked HTTP."""

import pytest

from chemrof.converter.enrichers.base import EnrichmentContext
from chemrof.converter.enrichers.pubchem import PubChemEnricher


@pytest.fixture
def enricher():
    return PubChemEnricher()


def test_pubchem_enricher_name(enricher):
    assert enricher.name == "pubchem"


def test_parse_pubchem_response(enricher):
    """Test the response-parsing logic without HTTP."""
    raw = {
        "PC_Compounds": [
            {
                "id": {"id": {"cid": 702}},
                "props": [
                    {
                        "urn": {"label": "IUPAC Name", "name": "Preferred"},
                        "value": {"sval": "ethanol"},
                    },
                ],
            }
        ]
    }
    obj = {"id": "INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "name": "C2H6O"}
    result = enricher._apply_pubchem_data(obj, raw)
    assert result["name"] == "ethanol"
    assert result["pubchem_cid"] == 702


def test_no_results_leaves_obj_unchanged(enricher):
    """When PubChem returns no compounds, the object is unchanged."""
    obj = {"id": "INCHIKEY:XXXXXXXXXXX", "name": "C2H6O"}
    result = enricher._apply_pubchem_data(obj, {"PC_Compounds": []})
    assert result["name"] == "C2H6O"
    assert "pubchem_cid" not in result
