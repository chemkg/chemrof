"""PubChem enricher -- looks up compounds by InChIKey via PUG REST.

Fills: name (IUPAC preferred), pubchem_cid (cross-reference).
"""

from __future__ import annotations

import logging
from typing import Any

import httpx

from chemrof.converter.enrichers.base import EnrichmentContext

logger = logging.getLogger(__name__)

_PUG_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{inchikey}/JSON"


class PubChemEnricher:
    """Enrich a chemrof dict with PubChem data via InChIKey lookup."""

    name = "pubchem"

    def __init__(self, timeout: float = 10.0):
        self.timeout = timeout

    def enrich(self, obj: dict, context: EnrichmentContext) -> dict:
        if not context.inchikey:
            return obj
        url = _PUG_URL.format(inchikey=context.inchikey)
        with httpx.Client(timeout=self.timeout) as client:
            resp = client.get(url)
            if resp.status_code == 404:
                logger.debug("PubChem: no compound for %s", context.inchikey)
                return obj
            resp.raise_for_status()
            data = resp.json()
        return self._apply_pubchem_data(obj, data)

    def _apply_pubchem_data(self, obj: dict, data: dict) -> dict:
        """Extract fields from PubChem JSON response and apply to *obj*."""
        compounds = data.get("PC_Compounds", [])
        if not compounds:
            return obj

        compound = compounds[0]

        # CID
        cid = compound.get("id", {}).get("id", {}).get("cid")
        if cid:
            obj["pubchem_cid"] = cid

        # IUPAC preferred name
        for prop in compound.get("props", []):
            urn = prop.get("urn", {})
            if urn.get("label") == "IUPAC Name" and urn.get("name") == "Preferred":
                name = prop.get("value", {}).get("sval")
                if name:
                    obj["name"] = name
                break

        return obj
