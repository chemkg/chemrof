"""openclatura enricher -- generates IUPAC names locally from structure.

Unlike the PubChem enricher, this needs no network: it derives a systematic
IUPAC name directly from the molecule's SMILES using the ``openclatura``
package (https://github.com/lamalab-org/openclatura), which walks the
molecular graph following IUPAC Blue Book 2013 rules.

Fills: IUPAC_name (always, when a name is derived) and name (only when the
object still carries a placeholder such as the empirical formula, so a better
name from another enricher is never clobbered).

Install the optional dependency with ``pip install openclatura``.
"""

from __future__ import annotations

import logging

from chemrof.converter.enrichers.base import EnrichmentContext

logger = logging.getLogger(__name__)


class OpenclaturaEnricher:
    """Enrich a chemrof dict with an IUPAC name derived from its SMILES."""

    name = "openclatura"
    _warned_missing = False

    def enrich(self, obj: dict, context: EnrichmentContext) -> dict:
        smiles = context.smiles or obj.get("smiles_string", "")
        if not smiles:
            return obj
        iupac = self._name_smiles(smiles)
        if iupac:
            return self._apply_name(obj, iupac)
        return obj

    def _name_smiles(self, smiles: str) -> str | None:
        """Return the IUPAC name for *smiles*, or None if unavailable.

        Isolated so the library call can be swapped out in tests.
        """
        try:
            from openclatura import name as oc_name
        except ImportError:
            if not self._warned_missing:
                logger.warning(
                    "openclatura is not installed; skipping. "
                    "Install it with `pip install 'chemrof[openclatura]'`."
                )
                self._warned_missing = True
            return None
        try:
            result = oc_name(smiles)
        except Exception as exc:  # openclatura raises on structures it can't name
            logger.debug("openclatura could not name %s: %s", smiles, exc)
            return None
        if getattr(result, "ok", False) and getattr(result, "name", None):
            return result.name
        return None

    def _apply_name(self, obj: dict, iupac_name: str) -> dict:
        """Apply a derived IUPAC name to *obj* without clobbering better names."""
        obj["IUPAC_name"] = iupac_name
        current = obj.get("name")
        if not current or current == obj.get("empirical_formula"):
            obj["name"] = iupac_name
        return obj
