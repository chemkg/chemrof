"""Reaction enricher that adds thermodynamic estimates from eQuilibrator.

eQuilibrator estimates standard transformed Gibbs free energies with the
component contribution method, which blends measured reactant contributions with
group contributions so that estimates stay consistent around thermodynamic
cycles. See https://equilibrator.readthedocs.io/.

``equilibrator-api`` is an optional dependency, installable as the ``thermo``
extra. It is imported lazily because constructing a ``ComponentContribution``
downloads and loads a multi-gigabyte compound cache, which should never happen
as a side effect of importing chemrof.

Two things about the underlying model shape this module:

Protonation is not an input. eQuilibrator aggregates each compound's
microspecies (its protonation and magnesium-bound forms) into a single
pseudoisomer group at the requested pH and pMg, so a reaction must be written
*without* balancing protons, and a participant identifier that names a specific
protonation state resolves to the same compound as any other. That is why
InChIKey lookups here deliberately drop the final (protonation) block of the
key.

Not every compound can be transformed. A compound with no structure, or one
ChemAxon could not analyse, has no microspecies ladder and therefore no
meaningful pH dependence. Those participants are recorded in
``unresolved_participants`` on the estimate so downstream consumers can discount
it.

Two guards keep meaningless numbers out of the data. eQuilibrator will happily
return a free energy for an unbalanced reaction, which is not a physical
quantity, so an unbalanced reaction gets ``is_balanced`` and nothing else. And
for a reaction covered by neither reactant nor group contribution, eQuilibrator
signals failure not by raising but by returning an uncertainty of ``rmse_inf``
(1e5 kJ/mol by default); those estimates are dropped rather than recorded.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

from chemrof.converter.enrichers.base import ReactionEnrichmentContext

#: The chemrof id prefix used for structure-derived identifiers.
INCHIKEY_PREFIX = "INCHIKEY:"

#: Length of the InChIKey skeleton (connectivity) block.
_SKELETON_LEN = 14

#: Length of skeleton plus stereo block, i.e. everything bar the protonation
#: block. Matching on this prefix keeps stereochemistry but ignores protonation,
#: which is what eQuilibrator's pseudoisomer grouping already does.
_SKELETON_AND_STEREO_LEN = 25

#: chemrof prefixes whose lowercased form is not the eQuilibrator registry
#: namespace. Anything absent from this map is passed through to
#: ``get_compound``, which lowercases the namespace itself and special-cases
#: ChEBI, so ``CHEBI:30616`` and ``bigg.metabolite:atp`` both work unaided.
_PREFIX_OVERRIDES = {
    "KEGG.COMPOUND": "kegg",
    "METACYC": "metacyc.compound",
    "METACYC.COMPOUND": "metacyc.compound",
    "BIGG.METABOLITE": "bigg.metabolite",
    "SEED.COMPOUND": "seed",
    "METANETX.CHEMICAL": "metanetx.chemical",
}

#: Quantity types written into ``has_thermodynamic_estimate``.
STANDARD_DG_PRIME = "standard_transformed_gibbs_free_energy_change"
PHYSIOLOGICAL_DG_PRIME = "physiological_transformed_gibbs_free_energy_change"
LN_REVERSIBILITY_INDEX = "ln_reversibility_index"

#: chemrof ``direction`` values mapped onto eQuilibrator reaction arrows.
_DIRECTION_TO_ARROW = {
    "l->r": "=>",
    "r->l": "<=",
    "bidirectional": "<=>",
    "neutral": "<=>",
}

#: eQuilibrator's default ``rmse_inf``, the uncertainty it reports for a reaction
#: covered by neither reactant nor group contribution. Used as a fallback when the
#: configured value cannot be read off the predictor.
DEFAULT_RMSE_INF = 1e5

#: Fraction of ``rmse_inf`` at or above which an estimate is treated as a failure
#: rather than a number. Real uncertainties are at most tens of kJ/mol, so
#: anything near the sentinel is unambiguous.
RMSE_INF_FRACTION = 0.5

ENERGY_UNIT = "kJ/mol"
ESTIMATION_METHOD = "component_contribution"


class EquilibratorUnavailableError(RuntimeError):
    """Raised when ``equilibrator-api`` is not installed."""


@dataclass
class ResolvedParticipant:
    """A chemrof participant paired with the eQuilibrator compound it resolved to.

    Attributes:
        chemrof_id: The participant id as it appears in the chemrof reaction.
        coefficient: Signed stoichiometric coefficient, negative on the left.
        compound: The resolved eQuilibrator ``Compound``, or None.
        ambiguous: True when the lookup matched more than one compound and the
            first was taken.
    """

    chemrof_id: str
    coefficient: float
    compound: Any = None
    ambiguous: bool = False

    @property
    def resolved(self) -> bool:
        """Whether an eQuilibrator compound was found at all."""
        return self.compound is not None

    @property
    def transformable(self) -> bool:
        """Whether the compound has a microspecies ladder to transform."""
        return self.resolved and bool(self.compound.can_be_transformed())


class EquilibratorEnricher:
    """Add thermodynamic estimates to a chemrof reaction using eQuilibrator.

    The enricher resolves every participant to an eQuilibrator compound, builds a
    reaction from the resulting stoichiometry, and writes one
    ``has_thermodynamic_estimate`` entry per quantity it could compute. It also
    fills ``is_balanced`` from eQuilibrator's atom balance check.

    Args:
        component_contribution: An existing ``ComponentContribution``. Supply one
            to reuse a loaded cache across many reactions, or to inject a double
            in tests. When omitted, one is constructed on first use.
        include_physiological: Also estimate the 1 mM (physiological) quantity.
        include_reversibility_index: Also estimate the reversibility index.
        require_balanced: Emit no estimates for a reaction that does not balance.
            A free energy for an unbalanced reaction is not a physical quantity,
            so this defaults to True. ``is_balanced`` is still filled in.
    """

    name = "equilibrator"

    def __init__(
        self,
        component_contribution: Any = None,
        *,
        include_physiological: bool = True,
        include_reversibility_index: bool = False,
        require_balanced: bool = True,
    ):
        self._cc = component_contribution
        self.include_physiological = include_physiological
        self.include_reversibility_index = include_reversibility_index
        self.require_balanced = require_balanced

    # -- public API ------------------------------------------------------

    def enrich(self, obj: dict, context: ReactionEnrichmentContext) -> dict:
        """Add thermodynamic estimates to ``obj``, returning it.

        Returns ``obj`` untouched when the reaction has no participants, or when
        no participant could be resolved to an eQuilibrator compound.
        """
        participants = list(self._iter_participants(obj, context))
        if not participants:
            return obj

        if not any(p.resolved for p in participants):
            return obj

        cc = self._component_contribution()
        self._apply_conditions(cc, context)

        reaction = self._build_reaction(obj, participants)
        if reaction is None:
            return obj

        balanced = _safe_call(reaction.is_balanced)
        if balanced is not None:
            obj["is_balanced"] = bool(balanced)
            if self.require_balanced and not balanced:
                return obj

        estimates = self._estimates(cc, reaction, participants, context)
        if estimates:
            obj.setdefault("has_thermodynamic_estimate", []).extend(estimates)
        return obj

    # -- participant resolution -----------------------------------------

    def _iter_participants(
        self, obj: dict, context: ReactionEnrichmentContext
    ) -> Iterable[ResolvedParticipant]:
        """Resolve left and right participants, signing coefficients by side."""
        for slot, sign in (("left_participants", -1.0), ("right_participants", 1.0)):
            for entry in obj.get(slot) or []:
                chemrof_id = entry.get("participant")
                if not chemrof_id:
                    continue
                coefficient = sign * float(entry.get("stoichiometry", 1.0))
                compound, ambiguous = self._resolve(chemrof_id, context)
                yield ResolvedParticipant(
                    chemrof_id=chemrof_id,
                    coefficient=coefficient,
                    compound=compound,
                    ambiguous=ambiguous,
                )

    def _resolve(
        self, chemrof_id: str, context: ReactionEnrichmentContext
    ) -> tuple[Any, bool]:
        """Find the eQuilibrator compound for a chemrof participant id.

        Returns a ``(compound, ambiguous)`` pair; ``compound`` is None when
        nothing matched.
        """
        cc = self._component_contribution()

        override = context.identifier_overrides.get(chemrof_id)
        if override:
            return _safe_call(cc.get_compound, override), False

        if chemrof_id.startswith(INCHIKEY_PREFIX):
            compound, ambiguous = self._resolve_by_inchi_key(
                cc, chemrof_id[len(INCHIKEY_PREFIX) :]
            )
            if compound is not None:
                return compound, ambiguous
        else:
            compound = _safe_call(cc.get_compound, _external_identifier(chemrof_id))
            if compound is not None:
                return compound, False

        # Last resort: an exact InChI from the participant's own chemrof record.
        inchi = (context.participants.get(chemrof_id) or {}).get("inchi_string")
        if inchi:
            return _safe_call(cc.get_compound_by_inchi, inchi), False

        return None, False

    def _resolve_by_inchi_key(self, cc: Any, inchi_key: str) -> tuple[Any, bool]:
        """Look a compound up by InChIKey, ignoring the protonation block.

        eQuilibrator stores one compound per pseudoisomer group, so the final
        block of a chemrof InChIKey -- which encodes protonation state -- must not
        take part in the match. Tries skeleton plus stereo first, then falls back
        to the skeleton alone.
        """
        for length in (_SKELETON_AND_STEREO_LEN, _SKELETON_LEN):
            prefix = inchi_key[:length]
            if not prefix:
                continue
            hits = _safe_call(cc.search_compound_by_inchi_key, prefix) or []
            if hits:
                return hits[0], len(hits) > 1
        return None, False

    # -- estimation -----------------------------------------------------

    def _build_reaction(self, obj: dict, participants: list[ResolvedParticipant]) -> Any:
        """Build an eQuilibrator reaction, or None if nothing resolved.

        Participants that appear on both sides and cancel out are dropped, which
        is what eQuilibrator's own formula parser does.
        """
        from equilibrator_api.phased_reaction import PhasedReaction

        sparse: dict[Any, float] = {}
        for participant in participants:
            if not participant.resolved:
                continue
            compound = participant.compound
            sparse[compound] = sparse.get(compound, 0.0) + participant.coefficient

        sparse = {compound: coeff for compound, coeff in sparse.items() if coeff != 0.0}
        if not sparse:
            return None
        return PhasedReaction(
            sparse,
            arrow=_arrow(obj.get("direction")),
            rid=obj.get("id"),
        )

    def _estimates(
        self,
        cc: Any,
        reaction: Any,
        participants: list[ResolvedParticipant],
        context: ReactionEnrichmentContext,
    ) -> list[dict]:
        """Compute every requested quantity that eQuilibrator will give us."""
        unresolved = sorted(
            {p.chemrof_id for p in participants if not p.transformable}
        )

        wanted: list[tuple[str, Any, str | None]] = [
            (STANDARD_DG_PRIME, cc.standard_dg_prime, ENERGY_UNIT),
        ]
        if self.include_physiological:
            wanted.append(
                (PHYSIOLOGICAL_DG_PRIME, cc.physiological_dg_prime, ENERGY_UNIT)
            )
        if self.include_reversibility_index:
            wanted.append(
                (LN_REVERSIBILITY_INDEX, cc.ln_reversibility_index, None)
            )

        sentinel = _rmse_inf(cc) * RMSE_INF_FRACTION

        estimates = []
        for quantity_type, method, unit in wanted:
            measurement = _safe_call(method, reaction)
            if measurement is None:
                continue
            estimate = _measurement_to_estimate(measurement, quantity_type, unit)
            if estimate is None:
                continue
            if estimate.get("standard_error", 0.0) >= sentinel:
                # eQuilibrator reports "cannot estimate" as a huge uncertainty
                # rather than by raising.
                continue
            estimate.update(_conditions(context))
            estimate["estimation_method"] = ESTIMATION_METHOD
            estimate["source"] = self._source()
            if unresolved:
                estimate["unresolved_participants"] = unresolved
            estimates.append(estimate)
        return estimates

    # -- plumbing -------------------------------------------------------

    def _component_contribution(self) -> Any:
        """Return the ComponentContribution, constructing one on first use."""
        if self._cc is None:
            try:
                from equilibrator_api import ComponentContribution
            except ImportError as exc:  # pragma: no cover - depends on env
                raise EquilibratorUnavailableError(
                    "The equilibrator reaction enricher needs equilibrator-api. "
                    "Install it with: pip install 'chemrof[thermo]'. Note that "
                    "the first use downloads a large compound cache."
                ) from exc
            self._cc = ComponentContribution()
        return self._cc

    def _apply_conditions(self, cc: Any, context: ReactionEnrichmentContext) -> None:
        """Push the requested conditions onto the ComponentContribution."""
        from equilibrator_api import Q_

        cc.p_h = Q_(context.p_h)
        cc.p_mg = Q_(context.p_mg)
        cc.ionic_strength = Q_(context.ionic_strength, "M")
        cc.temperature = Q_(context.temperature, "K")

    def _source(self) -> str:
        """Describe the estimate's provenance, with a version where available."""
        try:
            from importlib.metadata import version

            return f"eQuilibrator (equilibrator-api {version('equilibrator-api')})"
        except Exception:  # pragma: no cover - metadata is best-effort
            return "eQuilibrator"


# --- helpers ---


def _external_identifier(chemrof_id: str) -> str:
    """Map a chemrof CURIE onto the accession eQuilibrator expects.

    ``get_compound`` lowercases the namespace and special-cases ChEBI itself, so
    only genuinely divergent prefixes need rewriting here.

    >>> _external_identifier("CHEBI:30616")
    'CHEBI:30616'
    >>> _external_identifier("KEGG.COMPOUND:C00002")
    'kegg:C00002'
    >>> _external_identifier("bigg.metabolite:atp")
    'bigg.metabolite:atp'
    """
    prefix, _, accession = chemrof_id.partition(":")
    if not accession:
        return chemrof_id
    namespace = _PREFIX_OVERRIDES.get(prefix.upper())
    return f"{namespace}:{accession}" if namespace else chemrof_id


def _arrow(direction: str | None) -> str:
    """Map a chemrof ``direction`` value onto an eQuilibrator reaction arrow.

    >>> _arrow("l->r")
    '=>'
    >>> _arrow("bidirectional")
    '<=>'
    >>> _arrow(None)
    '<=>'
    """
    return _DIRECTION_TO_ARROW.get(direction or "", "<=>")


def _rmse_inf(cc: Any) -> float:
    """The configured ``rmse_inf`` in kJ/mol, falling back on the default.

    Read off the predictor so that a caller who passed a non-default
    ``rmse_inf`` to ``ComponentContribution`` still gets a matching threshold.
    """
    value = getattr(getattr(cc, "predictor", None), "preprocess", None)
    value = getattr(value, "RMSE_inf", None)
    try:
        return float(value)
    except (TypeError, ValueError):
        return DEFAULT_RMSE_INF


def _conditions(context: ReactionEnrichmentContext) -> dict:
    """The condition slots that every estimate carries."""
    return {
        "p_h": context.p_h,
        "ionic_strength": context.ionic_strength,
        "p_mg": context.p_mg,
        "temperature": context.temperature,
    }


def _measurement_to_estimate(
    measurement: Any, quantity_type: str, unit: str | None
) -> dict | None:
    """Convert a pint Measurement into a chemrof ThermodynamicEstimate dict.

    Returns None when the value is not finite, which is how eQuilibrator reports
    a quantity it cannot bound -- an infinite reversibility index, for instance.
    """
    value = _magnitude(measurement.value, unit)
    if value is None:
        return None

    estimate: dict[str, Any] = {"quantity_type": quantity_type, "value": value}
    if unit:
        estimate["unit"] = unit

    error = _magnitude(getattr(measurement, "error", None), unit)
    if error is not None:
        estimate["standard_error"] = error
    return estimate


def _magnitude(quantity: Any, unit: str | None) -> float | None:
    """Extract a finite float from a pint Quantity, or None."""
    if quantity is None:
        return None
    try:
        value = float(quantity.m_as(unit) if unit else quantity.m_as(""))
    except Exception:
        return None
    if value != value or value in (float("inf"), float("-inf")):
        return None
    return round(value, 6)


def _safe_call(method: Any, *args: Any) -> Any:
    """Call into eQuilibrator, returning None rather than raising.

    A single unsupported compound should degrade one quantity, not abort the
    whole enrichment run.
    """
    try:
        return method(*args)
    except Exception:
        return None
