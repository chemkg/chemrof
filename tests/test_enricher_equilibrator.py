"""Tests for the eQuilibrator reaction enricher.

``equilibrator-api`` is an optional dependency that pulls in a multi-gigabyte
compound cache, so these tests install a stub ``equilibrator_api`` package into
``sys.modules``. The stub mirrors the parts of the real API the enricher touches
-- ``Q_``, ``ComponentContribution``'s lookup methods and condition properties,
and ``phased_reaction.PhasedReaction`` -- so the import paths and call shapes
under test are the real ones.
"""

from __future__ import annotations

import sys
import types
from dataclasses import dataclass, field

import pytest

from chemrof.converter.enrich_reactions import (
    count_estimates,
    enrich_document,
    is_reaction,
    iter_entities,
)
from chemrof.converter.enrichers.base import (
    ReactionEnricher,
    ReactionEnrichmentContext,
    get_reaction_enricher,
    list_reaction_enrichers,
)
from chemrof.converter.enrichers.equilibrator import (
    EquilibratorEnricher,
    EquilibratorUnavailableError,
    _arrow,
    _external_identifier,
)

ATP = "INCHIKEY:ZKHQWZAMYRWXGA-KQYNXXCUSA-J"
WATER = "INCHIKEY:XLYOFNOQVPJJNP-UHFFFAOYSA-N"
ADP = "INCHIKEY:XTWYTFMLZFPYCI-KQYNXXCUSA-K"
PHOSPHATE = "INCHIKEY:NBIIXXVUZAFLBC-UHFFFAOYSA-L"


# --- stub equilibrator_api ---


class StubQuantity:
    """Stands in for a pint Quantity."""

    def __init__(self, magnitude: float, units: str = ""):
        self.magnitude = magnitude
        self.units = units

    def m_as(self, units: str | None) -> float:
        return self.magnitude

    def check(self, dimension: str) -> bool:
        return True


class StubMeasurement:
    """Stands in for a pint Measurement, which carries a value and an error."""

    def __init__(self, value: float, error: float, units: str = "kJ/mol"):
        self.value = StubQuantity(value, units)
        self.error = StubQuantity(error, units)


@dataclass
class StubCompound:
    """Stands in for an equilibrator_cache Compound."""

    inchi_key: str
    transformable: bool = True

    def can_be_transformed(self) -> bool:
        return self.transformable

    def __hash__(self) -> int:
        return hash(self.inchi_key)


class StubReaction:
    """Stands in for PhasedReaction, recording how it was constructed."""

    #: Flipped by tests that need an unbalanced reaction.
    balanced = True

    def __init__(self, sparse, arrow="<=>", rid=None, sparse_with_phases=None):
        self.sparse = sparse
        self.arrow = arrow
        self.rid = rid

    def is_balanced(self, ignore_atoms=("H",)) -> bool:
        return type(self).balanced


class StubPreprocess:
    """Stands in for the predictor's preprocessor, which holds rmse_inf."""

    def __init__(self, rmse_inf: float = 1e5):
        self.RMSE_inf = rmse_inf


class StubPredictor:
    def __init__(self, rmse_inf: float = 1e5):
        self.preprocess = StubPreprocess(rmse_inf)


@dataclass
class StubComponentContribution:
    """Stands in for ComponentContribution, with scripted lookups."""

    compounds: dict[str, list[StubCompound]] = field(default_factory=dict)
    standard: float = -45.6
    standard_error: float = 1.2
    physiological: float = -62.1
    reversibility: float | None = 3.4
    p_h: object = None
    p_mg: object = None
    ionic_strength: object = None
    temperature: object = None
    inchi_key_queries: list[str] = field(default_factory=list)
    accession_queries: list[str] = field(default_factory=list)
    predictor: object = field(default_factory=StubPredictor)

    def search_compound_by_inchi_key(self, inchi_key: str) -> list[StubCompound]:
        self.inchi_key_queries.append(inchi_key)
        return self.compounds.get(inchi_key, [])

    def get_compound(self, compound_id: str):
        self.accession_queries.append(compound_id)
        hits = self.compounds.get(compound_id, [])
        return hits[0] if hits else None

    def get_compound_by_inchi(self, inchi: str):
        hits = self.compounds.get(inchi, [])
        return hits[0] if hits else None

    def standard_dg_prime(self, reaction) -> StubMeasurement:
        return StubMeasurement(self.standard, self.standard_error)

    def physiological_dg_prime(self, reaction) -> StubMeasurement:
        return StubMeasurement(self.physiological, self.standard_error)

    def ln_reversibility_index(self, reaction) -> StubMeasurement:
        if self.reversibility is None:
            raise ValueError("unbounded")
        return StubMeasurement(self.reversibility, 0.5, units="")


@pytest.fixture
def stub_equilibrator(monkeypatch):
    """Install a stub equilibrator_api package for the duration of a test."""
    api = types.ModuleType("equilibrator_api")
    api.Q_ = StubQuantity
    api.ComponentContribution = StubComponentContribution

    phased = types.ModuleType("equilibrator_api.phased_reaction")
    phased.PhasedReaction = StubReaction
    api.phased_reaction = phased

    monkeypatch.setitem(sys.modules, "equilibrator_api", api)
    monkeypatch.setitem(sys.modules, "equilibrator_api.phased_reaction", phased)
    return api


@pytest.fixture
def atpase_reaction() -> dict:
    """ATP + H2O = ADP + phosphate, written without balancing protons."""
    return {
        "id": "RHEA:13065",
        "type": "chemrof:Reaction",
        "name": "ATP phosphohydrolase reaction",
        "direction": "l->r",
        "left_participants": [
            {"participant": ATP, "stoichiometry": 1.0},
            {"participant": WATER, "stoichiometry": 1.0},
        ],
        "right_participants": [
            {"participant": ADP, "stoichiometry": 1.0},
            {"participant": PHOSPHATE, "stoichiometry": 1.0},
        ],
    }


def _all_resolvable() -> dict[str, list[StubCompound]]:
    """Map the 25-character InChIKey prefixes the enricher will search for."""
    keys = [ATP, WATER, ADP, PHOSPHATE]
    return {
        curie.removeprefix("INCHIKEY:")[:25]: [
            StubCompound(curie.removeprefix("INCHIKEY:"))
        ]
        for curie in keys
    }


# --- registry and protocol ---


def test_equilibrator_is_registered():
    assert "equilibrator" in list_reaction_enrichers()


def test_get_reaction_enricher_by_name():
    enricher = get_reaction_enricher("equilibrator")
    assert enricher.name == "equilibrator"
    assert isinstance(enricher, ReactionEnricher)


def test_get_unknown_reaction_enricher():
    with pytest.raises(KeyError, match="nonexistent"):
        get_reaction_enricher("nonexistent")


def test_reaction_enricher_kwargs_are_forwarded():
    enricher = get_reaction_enricher("equilibrator", include_physiological=False)
    assert enricher.include_physiological is False


def test_context_defaults_match_equilibrator():
    """Defaults mirror ComponentContribution's physiological defaults."""
    context = ReactionEnrichmentContext()
    assert context.p_h == 7.5
    assert context.ionic_strength == 0.25
    assert context.p_mg == 3.0
    assert context.temperature == 298.15


# --- identifier mapping ---


def test_chebi_identifiers_pass_through_unchanged():
    """eQuilibrator's get_compound special-cases ChEBI itself."""
    assert _external_identifier("CHEBI:30616") == "CHEBI:30616"


def test_divergent_prefixes_are_rewritten():
    assert _external_identifier("KEGG.COMPOUND:C00002") == "kegg:C00002"
    assert _external_identifier("MetaCyc:ATP") == "metacyc.compound:ATP"


def test_unknown_prefixes_pass_through():
    assert _external_identifier("bigg.metabolite:atp") == "bigg.metabolite:atp"
    assert _external_identifier("C00002") == "C00002"


def test_direction_maps_to_arrow():
    assert _arrow("l->r") == "=>"
    assert _arrow("r->l") == "<="
    assert _arrow("bidirectional") == "<=>"
    assert _arrow(None) == "<=>"


# --- enrichment ---


def test_adds_standard_and_physiological_estimates(
    stub_equilibrator, atpase_reaction
):
    cc = StubComponentContribution(compounds=_all_resolvable())
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    estimates = atpase_reaction["has_thermodynamic_estimate"]
    assert [e["quantity_type"] for e in estimates] == [
        "standard_transformed_gibbs_free_energy_change",
        "physiological_transformed_gibbs_free_energy_change",
    ]
    assert estimates[0]["value"] == -45.6
    assert estimates[0]["standard_error"] == 1.2
    assert estimates[0]["unit"] == "kJ/mol"
    assert estimates[1]["value"] == -62.1


def test_estimates_record_their_conditions(stub_equilibrator, atpase_reaction):
    cc = StubComponentContribution(compounds=_all_resolvable())
    context = ReactionEnrichmentContext(
        p_h=7.0, ionic_strength=0.1, p_mg=14.0, temperature=310.15
    )
    EquilibratorEnricher(cc).enrich(atpase_reaction, context)

    estimate = atpase_reaction["has_thermodynamic_estimate"][0]
    assert estimate["p_h"] == 7.0
    assert estimate["ionic_strength"] == 0.1
    assert estimate["p_mg"] == 14.0
    assert estimate["temperature"] == 310.15
    assert estimate["estimation_method"] == "component_contribution"
    assert estimate["source"].startswith("eQuilibrator")


def test_conditions_are_pushed_onto_component_contribution(
    stub_equilibrator, atpase_reaction
):
    cc = StubComponentContribution(compounds=_all_resolvable())
    context = ReactionEnrichmentContext(p_h=6.5, p_mg=14.0, ionic_strength=0.15)
    EquilibratorEnricher(cc).enrich(atpase_reaction, context)

    assert cc.p_h.magnitude == 6.5
    assert cc.p_mg.magnitude == 14.0
    assert cc.ionic_strength.magnitude == 0.15
    assert cc.temperature.magnitude == 298.15


def test_inchikey_lookup_ignores_protonation_block(
    stub_equilibrator, atpase_reaction
):
    """The protonation block must not take part in the match.

    eQuilibrator holds one compound per pseudoisomer group, so ATP(4-)'s '-J'
    suffix would never match its stored key.
    """
    cc = StubComponentContribution(compounds=_all_resolvable())
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    assert "ZKHQWZAMYRWXGA-KQYNXXCUSA" in cc.inchi_key_queries
    assert not any(q.endswith("-J") for q in cc.inchi_key_queries)


def test_falls_back_to_skeleton_only_match(stub_equilibrator, atpase_reaction):
    """A stereo-block mismatch falls back to the 14-character skeleton."""
    compounds = {
        curie.removeprefix("INCHIKEY:")[:14]: [
            StubCompound(curie.removeprefix("INCHIKEY:"))
        ]
        for curie in (ATP, WATER, ADP, PHOSPHATE)
    }
    cc = StubComponentContribution(compounds=compounds)
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    assert "ZKHQWZAMYRWXGA" in cc.inchi_key_queries
    assert atpase_reaction["has_thermodynamic_estimate"]


def test_signs_coefficients_by_side(stub_equilibrator, atpase_reaction):
    """Substrates are negative and products positive, as eQuilibrator expects."""
    captured = {}

    class RecordingReaction(StubReaction):
        def __init__(self, sparse, arrow="<=>", rid=None, sparse_with_phases=None):
            super().__init__(sparse, arrow, rid, sparse_with_phases)
            captured["sparse"] = sparse
            captured["arrow"] = arrow
            captured["rid"] = rid

    stub_equilibrator.phased_reaction.PhasedReaction = RecordingReaction
    cc = StubComponentContribution(compounds=_all_resolvable())
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    by_key = {c.inchi_key: coeff for c, coeff in captured["sparse"].items()}
    assert by_key["ZKHQWZAMYRWXGA-KQYNXXCUSA-J"] == -1.0
    assert by_key["XTWYTFMLZFPYCI-KQYNXXCUSA-K"] == 1.0
    assert captured["arrow"] == "=>"
    assert captured["rid"] == "RHEA:13065"


def test_participants_cancelling_out_are_dropped(stub_equilibrator):
    """A compound with equal coefficients on both sides leaves the stoichiometry."""
    captured = {}

    class RecordingReaction(StubReaction):
        def __init__(self, sparse, arrow="<=>", rid=None, sparse_with_phases=None):
            super().__init__(sparse, arrow, rid, sparse_with_phases)
            captured["sparse"] = sparse

    stub_equilibrator.phased_reaction.PhasedReaction = RecordingReaction
    shared = StubCompound("WATERKEY")
    cc = StubComponentContribution(
        compounds={
            "XLYOFNOQVPJJNP-UHFFFAOYSA": [shared],
            "ZKHQWZAMYRWXGA-KQYNXXCUSA": [StubCompound("ATPKEY")],
        }
    )
    reaction = {
        "id": "test:1",
        "type": "chemrof:Reaction",
        "left_participants": [
            {"participant": ATP, "stoichiometry": 1.0},
            {"participant": WATER, "stoichiometry": 1.0},
        ],
        "right_participants": [{"participant": WATER, "stoichiometry": 1.0}],
    }
    EquilibratorEnricher(cc).enrich(reaction, ReactionEnrichmentContext())

    assert shared not in captured["sparse"]


def test_fills_is_balanced(stub_equilibrator, atpase_reaction):
    cc = StubComponentContribution(compounds=_all_resolvable())
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())
    assert atpase_reaction["is_balanced"] is True


def test_untransformable_participants_are_flagged(
    stub_equilibrator, atpase_reaction
):
    """A compound with no microspecies ladder makes the estimate unreliable."""
    compounds = _all_resolvable()
    key = ADP.removeprefix("INCHIKEY:")[:25]
    compounds[key] = [StubCompound("XTWYTFMLZFPYCI", transformable=False)]
    cc = StubComponentContribution(compounds=compounds)
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    estimate = atpase_reaction["has_thermodynamic_estimate"][0]
    assert estimate["unresolved_participants"] == [ADP]


def test_unresolved_participants_are_flagged(stub_equilibrator, atpase_reaction):
    """A participant that resolves to nothing is reported, not silently dropped."""
    compounds = _all_resolvable()
    del compounds[PHOSPHATE.removeprefix("INCHIKEY:")[:25]]
    compounds.pop(PHOSPHATE.removeprefix("INCHIKEY:")[:14], None)
    cc = StubComponentContribution(compounds=compounds)
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    estimate = atpase_reaction["has_thermodynamic_estimate"][0]
    assert PHOSPHATE in estimate["unresolved_participants"]


def test_identifier_overrides_are_used(stub_equilibrator, atpase_reaction):
    cc = StubComponentContribution(
        compounds={"kegg:C00002": [StubCompound("ATPKEY")], **_all_resolvable()}
    )
    context = ReactionEnrichmentContext(
        identifier_overrides={ATP: "kegg:C00002"}
    )
    EquilibratorEnricher(cc).enrich(atpase_reaction, context)

    assert "kegg:C00002" in cc.accession_queries


def test_inchi_string_fallback(stub_equilibrator):
    """An unresolvable id falls back on the participant's own InChI."""
    inchi = "InChI=1S/H2O/h1H2"
    cc = StubComponentContribution(compounds={inchi: [StubCompound("WATERKEY")]})
    reaction = {
        "id": "test:1",
        "type": "chemrof:Reaction",
        "left_participants": [{"participant": "local:water", "stoichiometry": 1.0}],
        "right_participants": [],
    }
    context = ReactionEnrichmentContext(
        participants={"local:water": {"id": "local:water", "inchi_string": inchi}}
    )
    EquilibratorEnricher(cc).enrich(reaction, context)

    assert reaction["has_thermodynamic_estimate"]


def test_no_participants_is_a_no_op(stub_equilibrator):
    reaction = {"id": "test:1", "type": "chemrof:Reaction"}
    cc = StubComponentContribution()
    assert EquilibratorEnricher(cc).enrich(reaction, ReactionEnrichmentContext()) == {
        "id": "test:1",
        "type": "chemrof:Reaction",
    }


def test_nothing_resolvable_is_a_no_op(stub_equilibrator, atpase_reaction):
    cc = StubComponentContribution(compounds={})
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())
    assert "has_thermodynamic_estimate" not in atpase_reaction


def test_reversibility_index_is_opt_in(stub_equilibrator, atpase_reaction):
    cc = StubComponentContribution(compounds=_all_resolvable())
    EquilibratorEnricher(cc, include_reversibility_index=True).enrich(
        atpase_reaction, ReactionEnrichmentContext()
    )

    quantities = [e["quantity_type"] for e in atpase_reaction["has_thermodynamic_estimate"]]
    assert "ln_reversibility_index" in quantities
    index = next(
        e
        for e in atpase_reaction["has_thermodynamic_estimate"]
        if e["quantity_type"] == "ln_reversibility_index"
    )
    assert "unit" not in index


def test_a_failing_quantity_does_not_abort_the_rest(
    stub_equilibrator, atpase_reaction
):
    cc = StubComponentContribution(compounds=_all_resolvable(), reversibility=None)
    EquilibratorEnricher(cc, include_reversibility_index=True).enrich(
        atpase_reaction, ReactionEnrichmentContext()
    )

    quantities = [e["quantity_type"] for e in atpase_reaction["has_thermodynamic_estimate"]]
    assert "standard_transformed_gibbs_free_energy_change" in quantities
    assert "ln_reversibility_index" not in quantities


def test_estimates_append_rather_than_replace(stub_equilibrator, atpase_reaction):
    """Re-running at new conditions keeps the earlier estimate."""
    cc = StubComponentContribution(compounds=_all_resolvable())
    enricher = EquilibratorEnricher(cc, include_physiological=False)
    enricher.enrich(atpase_reaction, ReactionEnrichmentContext(p_h=7.0))
    enricher.enrich(atpase_reaction, ReactionEnrichmentContext(p_h=8.0))

    estimates = atpase_reaction["has_thermodynamic_estimate"]
    assert [e["p_h"] for e in estimates] == [7.0, 8.0]


def test_missing_dependency_raises_a_helpful_error(monkeypatch, atpase_reaction):
    """Without equilibrator-api the enricher says how to install it."""
    monkeypatch.setitem(sys.modules, "equilibrator_api", None)
    with pytest.raises(EquilibratorUnavailableError, match="chemrof\\[thermo\\]"):
        EquilibratorEnricher().enrich(atpase_reaction, ReactionEnrichmentContext())


def test_unbalanced_reactions_get_no_estimates(stub_equilibrator, atpase_reaction):
    """A free energy for an unbalanced reaction is not a physical quantity."""
    cc = StubComponentContribution(compounds=_all_resolvable())

    class Unbalanced(StubReaction):
        balanced = False

    stub_equilibrator.phased_reaction.PhasedReaction = Unbalanced
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    assert atpase_reaction["is_balanced"] is False
    assert "has_thermodynamic_estimate" not in atpase_reaction


def test_unbalanced_reactions_can_be_estimated_on_request(
    stub_equilibrator, atpase_reaction
):
    cc = StubComponentContribution(compounds=_all_resolvable())

    class Unbalanced(StubReaction):
        balanced = False

    stub_equilibrator.phased_reaction.PhasedReaction = Unbalanced
    EquilibratorEnricher(cc, require_balanced=False).enrich(
        atpase_reaction, ReactionEnrichmentContext()
    )

    assert atpase_reaction["is_balanced"] is False
    assert atpase_reaction["has_thermodynamic_estimate"]


def test_sentinel_uncertainty_is_dropped(stub_equilibrator, atpase_reaction):
    """eQuilibrator reports an unestimable reaction as an rmse_inf uncertainty.

    It does not raise, so a naive enricher would record 1e5 kJ/mol as if it were
    a real error bar.
    """
    cc = StubComponentContribution(
        compounds=_all_resolvable(), standard=2757.4, standard_error=100006.57
    )
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    assert "has_thermodynamic_estimate" not in atpase_reaction


def test_sentinel_threshold_tracks_configured_rmse_inf(
    stub_equilibrator, atpase_reaction
):
    """A caller who lowered rmse_inf gets a correspondingly lower cutoff."""
    cc = StubComponentContribution(
        compounds=_all_resolvable(),
        standard_error=60.0,
        predictor=StubPredictor(rmse_inf=100.0),
    )
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    assert "has_thermodynamic_estimate" not in atpase_reaction


def test_plausible_uncertainties_are_kept(stub_equilibrator, atpase_reaction):
    cc = StubComponentContribution(compounds=_all_resolvable(), standard_error=12.5)
    EquilibratorEnricher(cc).enrich(atpase_reaction, ReactionEnrichmentContext())

    assert atpase_reaction["has_thermodynamic_estimate"][0]["standard_error"] == 12.5


# --- document traversal ---


def test_iter_entities_handles_all_three_shapes():
    assert iter_entities({"entities": [{"id": "a"}]}) == [{"id": "a"}]
    assert iter_entities([{"id": "a"}]) == [{"id": "a"}]
    assert iter_entities({"id": "a"}) == [{"id": "a"}]
    assert iter_entities(None) == []


def test_is_reaction():
    assert is_reaction({"type": "chemrof:Reaction"})
    assert is_reaction({"type": "chemrof:IsomeraseReaction"})
    assert is_reaction({"type": "Reaction"})
    assert is_reaction({"left_participants": []})
    assert not is_reaction({"type": "chemrof:SmallMolecule"})


def test_enrich_document_indexes_participants(stub_equilibrator, atpase_reaction):
    """Non-reaction entities become the participants map automatically."""
    inchi = "InChI=1S/H2O/h1H2"
    document = {
        "entities": [
            {"id": "local:water", "type": "chemrof:SmallMolecule", "inchi_string": inchi},
            {
                "id": "test:1",
                "type": "chemrof:Reaction",
                "left_participants": [
                    {"participant": "local:water", "stoichiometry": 1.0}
                ],
                "right_participants": [],
            },
        ]
    }
    cc = StubComponentContribution(compounds={inchi: [StubCompound("WATERKEY")]})
    enrich_document(document, [EquilibratorEnricher(cc)])

    assert count_estimates(document) == 2
    assert "local:water" not in document["entities"][0].get(
        "has_thermodynamic_estimate", {}
    )


def test_enrich_document_leaves_non_reactions_alone(
    stub_equilibrator, atpase_reaction
):
    molecule = {"id": ATP, "type": "chemrof:SmallMolecule"}
    document = {"entities": [molecule, atpase_reaction]}
    cc = StubComponentContribution(compounds=_all_resolvable())
    enrich_document(document, [EquilibratorEnricher(cc)])

    assert "has_thermodynamic_estimate" not in molecule
    assert "has_thermodynamic_estimate" in atpase_reaction


def test_enrich_document_without_enrichers_is_a_no_op(atpase_reaction):
    document = {"entities": [atpase_reaction]}
    assert enrich_document(document, []) is document
    assert "has_thermodynamic_estimate" not in atpase_reaction


def test_count_estimates():
    assert count_estimates({"entities": []}) == 0
    assert (
        count_estimates(
            {
                "entities": [
                    {
                        "type": "chemrof:Reaction",
                        "has_thermodynamic_estimate": [{"value": 1.0}],
                    }
                ]
            }
        )
        == 1
    )
