"""Tests for the openclatura enricher.

The name-application logic is exercised without importing the optional
``openclatura`` package, so these tests run even when it is not installed.
"""

import pytest

from chemrof.converter.enrichers.base import EnrichmentContext
from chemrof.converter.enrichers.openclatura import OpenclaturaEnricher


@pytest.fixture
def enricher():
    return OpenclaturaEnricher()


def _ctx(smiles: str = "") -> EnrichmentContext:
    return EnrichmentContext(mol=None, inchikey="", smiles=smiles, inchi="")


def test_openclatura_enricher_name(enricher):
    assert enricher.name == "openclatura"


def test_apply_name_sets_iupac_name(enricher):
    """IUPAC_name is always filled from the derived name."""
    obj = {"id": "INCHIKEY:LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "name": "C2H6O",
           "empirical_formula": "C2H6O"}
    result = enricher._apply_name(obj, "ethanol")
    assert result["IUPAC_name"] == "ethanol"


def test_apply_name_replaces_formula_placeholder(enricher):
    """A name that is still just the empirical formula is upgraded."""
    obj = {"name": "C2H6O", "empirical_formula": "C2H6O"}
    result = enricher._apply_name(obj, "ethanol")
    assert result["name"] == "ethanol"


def test_apply_name_preserves_existing_name(enricher):
    """A real name (e.g. from PubChem) is not clobbered."""
    obj = {"name": "grain alcohol", "empirical_formula": "C2H6O"}
    result = enricher._apply_name(obj, "ethanol")
    assert result["name"] == "grain alcohol"
    assert result["IUPAC_name"] == "ethanol"


def test_apply_name_fills_missing_name(enricher):
    obj = {"empirical_formula": "C2H6O"}
    result = enricher._apply_name(obj, "ethanol")
    assert result["name"] == "ethanol"


def test_enrich_no_smiles_is_noop(enricher):
    """Without a SMILES there is nothing to name."""
    obj = {"name": "C2H6O"}
    result = enricher.enrich(obj, _ctx(smiles=""))
    assert result == {"name": "C2H6O"}


def test_enrich_uses_injected_naming(monkeypatch, enricher):
    """enrich() applies whatever _name_smiles returns."""
    monkeypatch.setattr(enricher, "_name_smiles", lambda smiles: "ethanol")
    obj = {"name": "C2H6O", "empirical_formula": "C2H6O"}
    result = enricher.enrich(obj, _ctx(smiles="CCO"))
    assert result["IUPAC_name"] == "ethanol"
    assert result["name"] == "ethanol"


def test_enrich_naming_failure_leaves_obj_unchanged(monkeypatch, enricher):
    monkeypatch.setattr(enricher, "_name_smiles", lambda smiles: None)
    obj = {"name": "C2H6O", "empirical_formula": "C2H6O"}
    result = enricher.enrich(obj, _ctx(smiles="CCO"))
    assert "IUPAC_name" not in result
    assert result["name"] == "C2H6O"


def test_name_smiles_missing_package_returns_none(monkeypatch, enricher):
    """When openclatura is not importable, _name_smiles degrades gracefully."""
    import builtins

    real_import = builtins.__import__

    def fake_import(name, *args, **kwargs):
        if name == "openclatura":
            raise ImportError("no openclatura")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fake_import)
    assert enricher._name_smiles("CCO") is None
