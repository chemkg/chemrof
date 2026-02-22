"""Wikidata enricher stub -- will resolve Wikidata QIDs via SPARQL."""

from __future__ import annotations

import logging

from chemrof.converter.enrichers.base import EnrichmentContext

logger = logging.getLogger(__name__)


class WikidataEnricher:
    """Stub enricher for Wikidata lookups. Not yet implemented."""

    name = "wikidata"

    def enrich(self, obj: dict, context: EnrichmentContext) -> dict:
        # TODO: SPARQL query by InChIKey, fill wikidata_qid
        logger.debug("WikidataEnricher: not yet implemented")
        return obj
