"""Tests that stub enrichers exist and follow the protocol."""

from chemrof.converter.enrichers.base import EnrichmentContext, Enricher
from chemrof.converter.enrichers.chebi import ChebiEnricher
from chemrof.converter.enrichers.wikidata import WikidataEnricher


def test_chebi_enricher_is_enricher():
    e = ChebiEnricher()
    assert isinstance(e, Enricher)
    assert e.name == "chebi"


def test_wikidata_enricher_is_enricher():
    e = WikidataEnricher()
    assert isinstance(e, Enricher)
    assert e.name == "wikidata"


def test_stubs_pass_through():
    """Stubs return the object unchanged."""
    ctx = EnrichmentContext(mol=None, inchikey="X", smiles="C", inchi="InChI=1S/CH4/h1H4")
    obj = {"id": "test", "name": "methane"}

    assert ChebiEnricher().enrich(obj, ctx) == obj
    assert WikidataEnricher().enrich(obj, ctx) == obj
