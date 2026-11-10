"""NISPO enricher -- generates IUPAC names locally from structure.

Uses the ``nispo`` package (https://github.com/oxpig/nispo), a pure-Python,
RDKit-based SMILES-to-IUPAC generator whose names are checked to round-trip
through OPSIN. In O'Boyle's 2026 comparison it had the widest coverage of the
open-source generators, but its names are the longest and least often match
literature names, so it is best used last in a chain as a fallback.

Fills: IUPAC_name and name as described in
:mod:`chemrof.converter.enrichers.local_iupac`.

Install the optional dependency with ``pip install 'chemrof[nispo]'``.
"""

from __future__ import annotations

from chemrof.converter.enrichers.local_iupac import LocalIUPACNamerEnricher


class NispoEnricher(LocalIUPACNamerEnricher):
    """Enrich a chemrof dict with an IUPAC name derived by NISPO."""

    name = "nispo"
    package = "nispo"

    def _call_namer(self, smiles: str) -> str | None:
        from nispo import smiles_to_iupac

        # NISPO returns "" for structures outside its rule coverage.
        return smiles_to_iupac(smiles) or None
