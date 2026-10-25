"""openclatura enricher -- generates IUPAC names locally from structure.

Unlike the PubChem enricher, this needs no network: it derives a systematic
IUPAC name directly from the molecule's SMILES using the ``openclatura``
package (https://github.com/lamalab-org/openclatura), which walks the
molecular graph following IUPAC Blue Book 2013 rules.

Fills: IUPAC_name (when not already set by an earlier enricher) and name (only
when the object still carries a placeholder such as the empirical formula, so
a better name from another enricher is never clobbered). See
:mod:`chemrof.converter.enrichers.local_iupac`.

Install the optional dependency with ``pip install 'chemrof[openclatura]'``.
"""

from __future__ import annotations

from chemrof.converter.enrichers.local_iupac import LocalIUPACNamerEnricher


class OpenclaturaEnricher(LocalIUPACNamerEnricher):
    """Enrich a chemrof dict with an IUPAC name derived by openclatura."""

    name = "openclatura"
    package = "openclatura"

    def _call_namer(self, smiles: str) -> str | None:
        from openclatura import name as oc_name

        result = oc_name(smiles)
        if getattr(result, "ok", False) and getattr(result, "name", None):
            return result.name
        return None
