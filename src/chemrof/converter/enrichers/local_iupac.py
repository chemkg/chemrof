"""Shared base for enrichers that generate IUPAC names locally from structure.

Several open-source SMILES-to-IUPAC generators appeared in 2026 (openclatura,
NISPO, Orthonym). They differ in coverage and name quality -- see Noel
O'Boyle's comparison at
https://baoilleach.blogspot.com/2026/10/assessing-open-source-iupac-name.html
-- so chemrof wraps each as its own enricher and lets them be chained.

Fills: IUPAC_name (only when not already set, so the first enricher in the
chain that produces a name wins) and name (only when the object still carries
a placeholder such as the empirical formula). Chaining e.g.
``pubchem,orthonym,openclatura,nispo`` therefore prefers a database name, then
falls back through the local generators in order.
"""

from __future__ import annotations

import logging

from chemrof.converter.enrichers.base import EnrichmentContext

logger = logging.getLogger(__name__)


class LocalIUPACNamerEnricher:
    """Base class: enrich a chemrof dict with an IUPAC name from its SMILES.

    Subclasses set ``name`` and ``package`` and implement :meth:`_call_namer`.
    """

    name: str = ""
    #: Importable module name of the optional dependency, used for messages.
    package: str = ""
    _warned_missing = False

    def enrich(self, obj: dict, context: EnrichmentContext) -> dict:
        if obj.get("IUPAC_name"):
            return obj
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
            return self._call_namer(smiles) or None
        except ImportError:
            if not self._warned_missing:
                logger.warning(
                    "%s is not installed; skipping. "
                    "Install it with `pip install 'chemrof[%s]'`.",
                    self.package,
                    self.name,
                )
                self._warned_missing = True
            return None
        except Exception as exc:  # namers may raise on structures they can't name
            logger.debug("%s could not name %s: %s", self.name, smiles, exc)
            return None

    def _call_namer(self, smiles: str) -> str | None:
        """Call the underlying library; may raise ImportError if it is absent."""
        raise NotImplementedError

    def _apply_name(self, obj: dict, iupac_name: str) -> dict:
        """Apply a derived IUPAC name to *obj* without clobbering better names.

        >>> e = LocalIUPACNamerEnricher()
        >>> e._apply_name({"name": "C2H6O", "empirical_formula": "C2H6O"}, "ethanol")
        {'name': 'ethanol', 'empirical_formula': 'C2H6O', 'IUPAC_name': 'ethanol'}
        >>> e._apply_name({"IUPAC_name": "ethanol"}, "ethyl alcohol")["IUPAC_name"]
        'ethanol'
        """
        obj.setdefault("IUPAC_name", iupac_name)
        current = obj.get("name")
        if not current or current == obj.get("empirical_formula"):
            obj["name"] = obj["IUPAC_name"]
        return obj
