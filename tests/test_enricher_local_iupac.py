"""Tests for the local SMILES-to-IUPAC enrichers (openclatura, NISPO, Orthonym).

The naming libraries are optional, so library calls are monkeypatched and
these tests run whether or not they are installed.
"""

import builtins

import pytest

from chemrof.converter.enrichers.base import Enricher, EnrichmentContext, get_enricher

LOCAL_NAMERS = ["openclatura", "nispo", "orthonym"]


def _ctx(smiles: str = "") -> EnrichmentContext:
    return EnrichmentContext(mol=None, inchikey="", smiles=smiles, inchi="")


@pytest.mark.parametrize("name", LOCAL_NAMERS)
def test_follows_enricher_protocol(name):
    enricher = get_enricher(name)
    assert enricher.name == name
    assert isinstance(enricher, Enricher)


@pytest.mark.parametrize("name", LOCAL_NAMERS)
def test_enrich_fills_names(monkeypatch, name):
    enricher = get_enricher(name)
    monkeypatch.setattr(enricher, "_call_namer", lambda smiles: "ethanol")
    obj = {"name": "C2H6O", "empirical_formula": "C2H6O"}
    result = enricher.enrich(obj, _ctx(smiles="CCO"))
    assert result["IUPAC_name"] == "ethanol"
    assert result["name"] == "ethanol"


@pytest.mark.parametrize("name", LOCAL_NAMERS)
def test_enrich_keeps_existing_iupac_name(monkeypatch, name):
    """A name from an earlier enricher (e.g. PubChem) is not overwritten."""
    enricher = get_enricher(name)
    monkeypatch.setattr(enricher, "_call_namer", lambda smiles: "ethyl alcohol")
    obj = {"name": "ethanol", "IUPAC_name": "ethanol"}
    result = enricher.enrich(obj, _ctx(smiles="CCO"))
    assert result["IUPAC_name"] == "ethanol"


@pytest.mark.parametrize("name", LOCAL_NAMERS)
def test_enrich_namer_error_is_noop(monkeypatch, name):
    enricher = get_enricher(name)

    def boom(smiles):
        raise ValueError("cannot name")

    monkeypatch.setattr(enricher, "_call_namer", boom)
    obj = {"name": "C2H6O", "empirical_formula": "C2H6O"}
    result = enricher.enrich(obj, _ctx(smiles="CCO"))
    assert "IUPAC_name" not in result


@pytest.mark.parametrize("name", LOCAL_NAMERS)
def test_missing_package_returns_none(monkeypatch, name):
    enricher = get_enricher(name)
    real_import = builtins.__import__

    def fake_import(mod, *args, **kwargs):
        if mod == enricher.package:
            raise ImportError(f"no {mod}")
        return real_import(mod, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fake_import)
    assert enricher._name_smiles("CCO") is None


def test_chain_first_namer_wins(monkeypatch):
    """Chaining namers falls back only when earlier ones produce nothing."""
    orthonym = get_enricher("orthonym")
    nispo = get_enricher("nispo")
    monkeypatch.setattr(orthonym, "_call_namer", lambda smiles: None)
    monkeypatch.setattr(nispo, "_call_namer", lambda smiles: "4-acetamidophenol")
    obj = {"name": "C8H9NO2", "empirical_formula": "C8H9NO2"}
    ctx = _ctx(smiles="CC(=O)Nc1ccc(O)cc1")
    for enricher in (orthonym, nispo):
        obj = enricher.enrich(obj, ctx)
    assert obj["IUPAC_name"] == "4-acetamidophenol"

    monkeypatch.setattr(orthonym, "_call_namer", lambda smiles: "N-(4-hydroxyphenyl)acetamide")
    obj = {"name": "C8H9NO2", "empirical_formula": "C8H9NO2"}
    for enricher in (orthonym, nispo):
        obj = enricher.enrich(obj, ctx)
    assert obj["IUPAC_name"] == "N-(4-hydroxyphenyl)acetamide"
