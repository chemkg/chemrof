from chemrof.converter.enrichers.base import EnrichmentContext, Enricher


def test_enrichment_context_creation():
    """EnrichmentContext stores mol metadata for enricher lookups."""
    ctx = EnrichmentContext(
        mol=None,  # RDKit mol not needed for this test
        inchikey="LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
        smiles="CCO",
        inchi="InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3",
    )
    assert ctx.inchikey == "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"
    assert ctx.smiles == "CCO"


def test_enricher_protocol():
    """An enricher must have a name and an enrich method."""

    class DummyEnricher:
        name = "dummy"

        def enrich(self, obj: dict, context: EnrichmentContext) -> dict:
            obj["name"] = "dummy-enriched"
            return obj

    e: Enricher = DummyEnricher()
    ctx = EnrichmentContext(mol=None, inchikey="X", smiles="C", inchi="InChI=1S/CH4/h1H4")
    result = e.enrich({"id": "test"}, ctx)
    assert result["name"] == "dummy-enriched"
