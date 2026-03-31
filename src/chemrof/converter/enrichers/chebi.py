"""ChEBI enricher stub -- will resolve CHEBI IDs via OLS API."""

from __future__ import annotations

import logging

from chemrof.converter.enrichers.base import EnrichmentContext

logger = logging.getLogger(__name__)


class ChebiEnricher:
    """Stub enricher for ChEBI lookups. Not yet implemented."""

    name = "chebi"

    def enrich(self, obj: dict, context: EnrichmentContext) -> dict:
        # TODO: look up InChIKey in OLS/ChEBI, fill obj["id"] with CHEBI:NNNNN
        logger.debug("ChebiEnricher: not yet implemented")
        return obj
