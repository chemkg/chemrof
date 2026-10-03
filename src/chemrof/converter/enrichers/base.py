"""Enricher protocols and contexts for the chemrof conversion pipeline.

Two families of enricher live here. Compound enrichers take a single chemical
entity plus an :class:`EnrichmentContext` built from an RDKit parse. Reaction
enrichers take a chemrof reaction plus a :class:`ReactionEnrichmentContext`,
which carries the aqueous conditions the enrichment applies at and whatever is
known about the reaction's participants.
"""

from __future__ import annotations

from dataclasses import dataclass, field
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
    from chemrof.converter.enrichers.chemont import ChemOntEnricher
    from chemrof.converter.enrichers.pubchem import PubChemEnricher
    from chemrof.converter.enrichers.chebi import ChebiEnricher
    from chemrof.converter.enrichers.wikidata import WikidataEnricher

    return {
        "chemont": ChemOntEnricher,
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


# --- Reaction-level enrichment ---

#: Conditions assumed when none are given. These match the defaults that
#: eQuilibrator's ComponentContribution applies, which are its *physiological*
#: defaults rather than the module-level ``default_pH``/``default_pMg``
#: constants, and are close to typical intracellular conditions.
DEFAULT_P_H = 7.5
DEFAULT_IONIC_STRENGTH = 0.25
DEFAULT_P_MG = 3.0
DEFAULT_TEMPERATURE = 298.15


@dataclass
class ReactionEnrichmentContext:
    """Conditions and participant lookups for reaction-level enrichers.

    Transformed ("primed") thermodynamic quantities are only defined relative to
    a set of aqueous conditions, so the conditions travel with the request rather
    than being hard-coded by each enricher.

    Attributes:
        p_h: The pH to compute at.
        ionic_strength: Ionic strength in mol/L.
        p_mg: Negative log of free Mg2+ activity. Raise towards 14 to model a
            magnesium-free solution.
        temperature: Temperature in kelvin.
        participants: Optional map of chemrof entity id to the chemrof dict for
            that entity. Lets an enricher fall back on ``inchi_string`` when an
            identifier cannot be resolved in an external registry.
        identifier_overrides: Optional map of chemrof entity id to the external
            identifier to look it up by, for participants whose chemrof id is not
            resolvable on its own.
    """

    p_h: float = DEFAULT_P_H
    ionic_strength: float = DEFAULT_IONIC_STRENGTH
    p_mg: float = DEFAULT_P_MG
    temperature: float = DEFAULT_TEMPERATURE
    participants: dict[str, dict] = field(default_factory=dict)
    identifier_overrides: dict[str, str] = field(default_factory=dict)


@runtime_checkable
class ReactionEnricher(Protocol):
    """Protocol for reaction enricher plugins.

    Each reaction enricher takes a chemrof reaction dict and a
    :class:`ReactionEnrichmentContext`, adds or modifies slots, and returns the
    dict.
    """

    name: str

    def enrich(self, obj: dict, context: ReactionEnrichmentContext) -> dict: ...


def _build_reaction_registry() -> dict[str, type]:
    """Lazily import reaction enricher classes to avoid circular imports."""
    from chemrof.converter.enrichers.equilibrator import EquilibratorEnricher

    return {
        "equilibrator": EquilibratorEnricher,
    }


def list_reaction_enrichers() -> list[str]:
    """Return names of all registered reaction enrichers.

    >>> list_reaction_enrichers()
    ['equilibrator']
    """
    return list(_build_reaction_registry().keys())


def get_reaction_enricher(name: str, **kwargs: Any) -> ReactionEnricher:
    """Instantiate a reaction enricher by name.

    >>> e = get_reaction_enricher("equilibrator")
    >>> e.name
    'equilibrator'
    """
    registry = _build_reaction_registry()
    if name not in registry:
        raise KeyError(
            f"Unknown reaction enricher: {name!r}. Available: {list(registry)}"
        )
    return registry[name](**kwargs)
