"""Apply reaction enrichers across a chemrof document.

Accepts the three shapes chemrof data arrives in -- a Collection with an
``entities`` list, a bare list of entities, or a single entity -- finds the
reactions in it, and runs each enricher over them in order. Entities that are not
reactions are left alone, but they are still indexed and handed to the enrichers
as participant records so that structure-based fallbacks can use them.
"""

from __future__ import annotations

from typing import Any, Sequence

from chemrof.converter.enrichers.base import (
    ReactionEnricher,
    ReactionEnrichmentContext,
)

#: Entity types treated as reactions. Compared against the suffix of the ``type``
#: value so that both ``chemrof:Reaction`` and a bare ``Reaction`` match.
REACTION_TYPES = frozenset({"Reaction", "IsomeraseReaction"})


def iter_entities(document: Any) -> list[dict]:
    """Return the entity dicts in a chemrof document, in document order.

    >>> iter_entities({"entities": [{"id": "a"}]})
    [{'id': 'a'}]
    >>> iter_entities([{"id": "a"}, {"id": "b"}])
    [{'id': 'a'}, {'id': 'b'}]
    >>> iter_entities({"id": "a"})
    [{'id': 'a'}]
    """
    if isinstance(document, dict):
        if "entities" in document:
            return [e for e in document["entities"] if isinstance(e, dict)]
        return [document]
    if isinstance(document, list):
        return [e for e in document if isinstance(e, dict)]
    return []


def is_reaction(entity: dict) -> bool:
    """Whether an entity dict looks like a chemrof reaction.

    Falls back on the presence of participant slots, so that data without an
    explicit ``type`` is still handled.

    >>> is_reaction({"type": "chemrof:Reaction"})
    True
    >>> is_reaction({"left_participants": []})
    True
    >>> is_reaction({"type": "chemrof:SmallMolecule"})
    False
    """
    declared = entity.get("type")
    if isinstance(declared, str):
        return declared.rsplit(":", 1)[-1] in REACTION_TYPES
    return "left_participants" in entity or "right_participants" in entity


def enrich_document(
    document: Any,
    enrichers: Sequence[ReactionEnricher],
    context: ReactionEnrichmentContext | None = None,
) -> Any:
    """Run ``enrichers`` over every reaction in ``document``, in place.

    The document is returned for convenience. ``context.participants`` is
    populated from the document's non-reaction entities unless the caller has
    already supplied it.
    """
    entities = iter_entities(document)
    reactions = [e for e in entities if is_reaction(e)]
    if not reactions or not enrichers:
        return document

    context = context or ReactionEnrichmentContext()
    if not context.participants:
        context.participants = {
            entity["id"]: entity
            for entity in entities
            if entity.get("id") and not is_reaction(entity)
        }

    for reaction in reactions:
        for enricher in enrichers:
            enricher.enrich(reaction, context)
    return document


def count_estimates(document: Any) -> int:
    """Count the thermodynamic estimates present across a document.

    Useful for reporting what an enrichment run actually produced.

    >>> count_estimates({"entities": [
    ...     {"type": "chemrof:Reaction",
    ...      "has_thermodynamic_estimate": [{"value": 1.0}, {"value": 2.0}]},
    ... ]})
    2
    """
    return sum(
        len(entity.get("has_thermodynamic_estimate") or [])
        for entity in iter_entities(document)
    )
