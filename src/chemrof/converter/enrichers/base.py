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
