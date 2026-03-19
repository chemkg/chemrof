"""Enricher protocol and context for the SMILES-to-chemrof pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol, runtime_checkable


@dataclass
class EnrichmentContext:
    """Carries metadata from the RDKit parse for enricher lookups.

    Attributes:
        mol: The RDKit Mol object (or None in tests).
        inchikey: Computed InChIKey for database lookups.
        smiles: The original or canonical SMILES string.
        inchi: Computed InChI string.
    """

    mol: Any  # rdkit.Chem.Mol — Any to avoid import at module level
    inchikey: str
    smiles: str
    inchi: str


@runtime_checkable
class Enricher(Protocol):
    """Protocol for enricher plugins.

    Each enricher takes a chemrof dict and an EnrichmentContext,
    adds or modifies slots, and returns the dict.
    """

    name: str

    def enrich(self, obj: dict, context: EnrichmentContext) -> dict: ...


# --- Registry ---


def _build_registry() -> dict[str, type]:
    """Lazily import enricher classes to avoid circular imports."""
    from chemrof.converter.enrichers.pubchem import PubChemEnricher
    from chemrof.converter.enrichers.chebi import ChebiEnricher
    from chemrof.converter.enrichers.wikidata import WikidataEnricher

    return {
        "pubchem": PubChemEnricher,
        "chebi": ChebiEnricher,
        "wikidata": WikidataEnricher,
    }


def list_enrichers() -> list[str]:
    """Return names of all registered enrichers."""
    return list(_build_registry().keys())


def get_enricher(name: str) -> Enricher:
    """Instantiate an enricher by name.

    >>> e = get_enricher("pubchem")
    >>> e.name
    'pubchem'
    """
    registry = _build_registry()
    if name not in registry:
        raise KeyError(f"Unknown enricher: {name!r}. Available: {list(registry)}")
    return registry[name]()
