# tests/test_enricher_registry.py
"""Tests for the enricher registry."""

import pytest

from chemrof.converter.enrichers.base import get_enricher, list_enrichers


def test_list_enrichers():
    names = list_enrichers()
    assert "pubchem" in names
    assert "chebi" in names
    assert "wikidata" in names


def test_get_enricher_by_name():
    e = get_enricher("pubchem")
    assert e.name == "pubchem"


def test_get_unknown_enricher():
    with pytest.raises(KeyError, match="nonexistent"):
        get_enricher("nonexistent")
