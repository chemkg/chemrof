"""Orthonym enricher -- generates Preferred IUPAC Names locally from structure.

Uses the ``orthonym`` package (https://github.com/Steinbeck-Lab/Orthonym),
which builds names from the IUPAC 2013 recommendations and, at its default
tier, returns a name only when it is a verified Preferred IUPAC Name (PIN)
that OPSIN reads back to the same structure. In O'Boyle's 2026 comparison its
names were the shortest and most often matched literature names, but its
coverage was the narrowest, so it suits the front of a naming chain.

Orthonym drives OPSIN through a JVM, so a Java runtime is required; the first
call downloads the OPSIN jars to ``~/.cache/orthonym`` and starts the JVM.

Fills: IUPAC_name and name as described in
:mod:`chemrof.converter.enrichers.local_iupac`.

Install the optional dependency with ``pip install 'chemrof[orthonym]'``.
"""

from __future__ import annotations

from chemrof.converter.enrichers.local_iupac import LocalIUPACNamerEnricher


class OrthonymEnricher(LocalIUPACNamerEnricher):
    """Enrich a chemrof dict with a Preferred IUPAC Name derived by Orthonym."""

    name = "orthonym"
    package = "orthonym"

    def _call_namer(self, smiles: str) -> str | None:
        from orthonym import name_compound

        # Default "pin" style: returns "" when no verified PIN can be built.
        return name_compound(smiles) or None
