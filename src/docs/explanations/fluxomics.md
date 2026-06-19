# Fluxomics: Use Cases and ChEMROF Extensions

This document surveys **fluxomics** — the quantitative study of metabolic
reaction rates (fluxes) in a biological system — and analyzes how the ChEMROF
schema can be *used as-is* and where it could be *extended* to serve as a
chemical-entity backbone for fluxomics data and models.

It is written as a scoping/explanation document. Nothing here changes the
schema; it is intended to inform a future design discussion (and any
follow-up issues/PRs).

## 1. What is fluxomics?

Fluxomics is the "-omics" layer concerned with *flux* — the rate at which
metabolites are interconverted through a metabolic network, conventionally
expressed in units such as mmol·gDW⁻¹·h⁻¹ (millimoles per gram dry weight per
hour) for cellular systems. Unlike concentrations (metabolomics) or expression
levels (transcriptomics/proteomics), a flux is not a pool size but a
*throughput* through a reaction. Fluxes are not measured directly; they are
*inferred* by combining:

- a **reaction network** (stoichiometry + reversibility/directionality),
- **constraints** (thermodynamic, capacity, uptake/secretion bounds), and
- **experimental data** (extracellular rates and/or stable-isotope labeling
  patterns).

The two dominant methodological families are **constraint-based modeling**
(Flux Balance Analysis and relatives) and **isotope-based Metabolic Flux
Analysis** (¹³C-MFA and its non-stationary variant). They impose quite
different data requirements, and ChEMROF is differentially ready for each.

## 2. Core use cases and their data requirements

### 2.1 Constraint-based modeling / Flux Balance Analysis (FBA)

FBA operates on a **genome-scale metabolic model** (GEM/GSMM). The network is
encoded as a **stoichiometric matrix `S`** (rows = metabolites, columns =
reactions, entries = stoichiometric coefficients). Assuming metabolic
steady state (`S·v = 0`), linear programming finds a flux vector `v` that
optimizes an **objective function** (commonly biomass production) subject to
**flux bounds** (`lb ≤ v ≤ ub`).

Data requirements:

- Metabolites with **compartment** assignment (e.g. cytosol `c`,
  mitochondrion `m`, extracellular `e`) and database cross-references.
- Reactions with **signed, possibly non-integer** stoichiometric coefficients,
  **reversibility/bounds**, gene–protein–reaction (GPR) associations, and a
  classification (internal / transport / exchange / biomass pseudo-reaction).
- An **objective** (which reaction(s) to maximize/minimize, and weights).

The de-facto standard is **SBML Level 3 with the Flux Balance Constraints
(`fbc`) package** (objective functions, flux bounds, charge/formula for
balancing). Models are richly cross-referenced via **MIRIAM** identifiers and
annotated with **Systems Biology Ontology (SBO)** terms (e.g. distinguishing
biomass pseudo-reactions, transport reactions, exchange reactions). Reference
resources include **BiGG Models**, **MetaNetX**, **KEGG**, **MetaCyc/BioCyc**,
and **Rhea**. The **FROG** report (Flux variability, Reaction deletion,
Objective, Gene deletion) is an emerging reproducibility standard for curated
GEMs.

### 2.2 Stable-isotope ¹³C Metabolic Flux Analysis (¹³C-MFA)

¹³C-MFA is considered the "gold standard" for *intracellular* flux
quantification under metabolic (quasi-)steady state. Cells are fed a
¹³C-labeled substrate (e.g. [1-¹³C] or [U-¹³C] glucose); the label propagates
through the network, and the resulting **labeling patterns** of downstream
metabolites (measured by MS or NMR) are fit to a model to estimate fluxes.

The distinguishing data requirement beyond FBA is the **atom mapping** (a.k.a.
**atom transition network**): for each reaction, a one-to-one correspondence
between each substrate atom and the product atom it becomes. Carbon atom
mappings are what let a model predict how label flows. Key concepts:

- **Atom mapping / atom transition** — substrate-atom → product-atom
  correspondence per reaction (e.g. encoded as mapped reaction SMILES/SMIRKS,
  RXN files, or RInChI). Curated mappings are available from **MetaCyc** and
  the open **MetAMDB** (~43,000 reactions).
- **Isotopomer** — a specific labeling configuration of a molecule (which
  *positions* carry the heavy isotope); for *n* carbons there are 2ⁿ
  isotopomers.
- **Isotopologue / mass isotopomer** — molecules that differ only in *number*
  of heavy atoms (M+0, M+1, M+2, …), without regard to position; what a mass
  spectrometer typically resolves.
- **Mass Isotopomer Distribution (MID)** / **Mass Distribution Vector (MDV)** —
  the fractional abundances of M+0, M+1, … normalized to sum 1; the primary
  measurement input.
- **Elementary Metabolite Unit (EMU)** framework — a decomposition that
  reduces the isotopomer balance equations (1000s) to a much smaller EMU set
  (100s), the computational backbone of modern simulators (INCA, 13CFLUX2,
  OpenFLUX, mfapy, etc.).

The dominant exchange format is **FluxML** — an XML language semantically
similar to SBML but extended with atom mappings, parameter constraints
(net/exchange fluxes), and measurement configurations.

### 2.3 Isotopically non-stationary MFA (INST-MFA)

For systems where isotopic steady state is impractical (e.g. autotrophs,
photosynthesis), **INST-MFA** fits the *time course* of label incorporation.
This adds a **temporal dimension** (time-series MIDs) and requires metabolite
**pool sizes** (concentrations) as additional parameters, coupling fluxomics to
metabolomics.

### 2.4 Kinetic / mechanistic modeling

Beyond steady-state flux estimation, kinetic models express each reaction rate
`v` as an explicit function of metabolite concentrations and **kinetic
parameters** (e.g. `kcat`, `Km`, `Vmax`, rate constants). These are the bridge
from fluxomics to dynamic simulation and parameter-estimation tools.

### 2.5 A typology of fluxomics experiments

"Fluxomics" is not one experiment but a family, and the experiment *type*
dictates which data (and therefore which schema constructs) are needed. It is
useful to type an experiment along four orthogonal axes:

**Axis A — inference paradigm**

| Type | Tracer? | Steady state | Primary inputs |
| --- | --- | --- | --- |
| Constraint-based (FBA, and pFBA/FVA/MOMA/dFBA variants) | no | metabolic | stoichiometry, bounds, objective |
| Stoichiometric MFA / metabolite balancing | no | metabolic | stoichiometry + measured uptake/secretion rates |
| Stationary ¹³C-MFA (SS-MFA) | yes | metabolic **and** isotopic | atom mappings + MIDs at steady state |
| Isotopically non-stationary MFA (INST-MFA) | yes | metabolic only | time-series MIDs + pool sizes |
| Dynamic MFA (DMFA) | optional | none | time-series rates/labeling |
| ¹³C flux-ratio analysis (METAFoR) | yes | isotopic | local labeling patterns → flux *ratios* |

**Axis B — labeling design**

- **Single-tracer** vs **parallel labeling experiments (PLE)** — two or more
  tracer cultures fit jointly to one model. Using complementary parallel
  tracers is the **COMPLETE-MFA** approach, now regarded as the gold standard
  for flux precision/observability.
- **Tracer positional design**: positional (e.g. `[1-¹³C]`, `[1,2-¹³C]`,
  `[1,6-¹³C]` glucose) vs uniform (`[U-¹³C₆]`).

**Axis C — tracer isotope** — ¹³C dominates, but ²H, ¹⁵N, ¹⁷O/¹⁸O are used,
and combined designs exist (e.g. one-shot ¹³C/¹⁵N for simultaneous carbon and
nitrogen flux).

**Axis D — measurement platform** — GC-MS, LC-MS/MS, tandem MS (MS/MS), and
NMR (¹H/¹³C/¹⁵N HSQC). The platform determines whether **positional
isotopomers** (NMR, MS/MS) or only **mass isotopologues / MIDs** (single-stage
MS) are observed — a distinction ChEMROF can already express via
`isotopomer_of` vs `isotopologue_of`.

These axes combine: a typical study is e.g. *stationary ¹³C-MFA, parallel
`[1,2-¹³C]` + `[U-¹³C₆]` glucose, GC-MS, central-carbon model*. A fluxomics
schema should therefore treat "experiment type" as a small set of controlled
vocabularies (one per axis) rather than a single flat enum, and let a
**`FluxomicsExperiment`** carry one or more **`Tracer`** specifications plus its
measurement platform and timepoints (sketched in §7.4).

## 3. Standards landscape (for alignment)

| Concern | Standard / resource |
| --- | --- |
| Constraint-based model exchange | SBML L3 + `fbc` package |
| Isotope-labeling model exchange | FluxML; OpenFLUX/INCA/13CFLUX2 formats |
| Kinetic / Bayesian model exchange | SBML (kinetics); Maud (TOML) |
| Semantic typing of model parts | Systems Biology Ontology (SBO) |
| Reaction identity & balancing | Rhea, RInChI, reaction SMILES/SMIRKS |
| Atom mappings | MetaCyc, MetAMDB (RXN/SMILES with atom maps) |
| Metabolite/reaction identifiers | BiGG, MetaNetX, KEGG, ChEBI, HMDB |
| Reproducibility report | FROG |

ChEMROF already lists `RHEA`, `KEGG.REACTION`, `MetaCyc`, `EC`,
`MetaNetX.reaction`, `SEED`, `RetroRules`, `RXNO`, `bigg.metabolite`,
`MetaNetX.chemical` etc. among its `id_prefixes`, so it is well-positioned to
*cross-reference* these resources.

### 3.1 Do we have FluxML mappings? (a crosswalk)

Short answer: **no — there are currently no FluxML (or SBML/`fbc`/SBO)
mappings in the schema, and FluxML is not the kind of artifact you map to
directly.** Two clarifications:

1. **FluxML is an exchange *format* (an XML schema), not a controlled
   vocabulary with stable term IRIs.** So there is nothing to put in a
   LinkML `exact_mappings`/SSSOM table for FluxML the way there is for, say,
   `RXNO:` or `CHEBI:`. What you *can* map are (a) the **entity identifiers**
   that FluxML documents reference (Rhea/KEGG/BiGG/MetaNetX metabolite and
   reaction IDs) and (b) the **structural elements** of a FluxML document onto
   ChEMROF classes/slots (an element-level crosswalk).

2. **At the identifier level we are already aligned**: ChEMROF's `id_prefixes`
   for metabolites (`CHEBI`, `bigg.metabolite`, `KEGG`, `MetaNetX.chemical`,
   `HMDB`, …) and reactions (`RHEA`, `KEGG.REACTION`, `MetaCyc`, `EC`,
   `MetaNetX.reaction`, `bigg.metabolite`/`MetaNetX.reaction`) cover the
   namespaces FluxML/SBML models use, so ChEMROF can serve as the
   chemical-identity hub for the metabolites and reactions a FluxML model names.

What is **missing** is the structural crosswalk. A proposed element-level
mapping (to be implemented in a companion schema that imports ChEMROF):

| FluxML element / concept | ChEMROF equivalent | Status |
| --- | --- | --- |
| `<metabolitepool>` (id, atoms) | `ChemicalEntity` (+ `has_atom_occurrences`) | identifiers ✅, atom count via occurrences ✅ |
| `<reaction>` | `Reaction` | ✅ |
| `<reduct>` / `<rproduct>` (educt/product, with carbon labels) | `ReactionParticipant` (`left`/`right_participants`) | partial — see atom mapping |
| atom-transition string (e.g. `A#abc + B#de -> C#abcde`) | `AtomTransition` over `AtomOccurrence` (proposed §7.2) | ❌ not yet |
| net / exchange (forward/back) flux, `<constraint>`/`<flux>` | `MetabolicFlux` + bounds (proposed §7.4) | ❌ not yet |
| isotopomer / cumomer / EMU labeling state | `isotopomer_of` / `isotopologue_of`; `MassIsotopomerDistribution` (proposed §7.3) | relations ✅, distribution object ❌ |
| `<measurement>` (MS/MS/NMR config + data) | `FluxomicsExperiment` measurement (proposed §7.4) | ❌ not yet |
| `<configuration>` / tracer input (`<input>` labeling) | `Tracer` (proposed §7.4) | ❌ not yet |

So: identifier-level mappings exist today; the **structural FluxML↔ChEMROF
crosswalk, and especially atom transitions and labeling-data objects, are the
concrete pieces to add.** Building a small FluxML↔ChEMROF round-trip converter
(validating on one published model) would be the most direct way to prove the
crosswalk and surface remaining gaps.

## 4. What ChEMROF already provides

ChEMROF is primarily a **chemical-entity** ontology/schema, but it already
contains the chemistry that fluxomics models hang their data on:

- **`Reaction`** (`RXNO:0000000`) with `left_participants` /
  `right_participants` (each a `ReactionParticipant`), `direction`,
  `is_balanced`, `is_transport`, `is_fully_characterized`, `reaction_center`,
  and reaction-level cross-refs to RHEA/KEGG/MetaCyc/EC/MetaNetX/SEED/BiGG.
- **`ReactionParticipant`** linking a `Reaction` to a `ChemicalEntity` with a
  `stoichiometry` slot.
- **Kinetic slots already on `Reaction`/elsewhere**: `reaction_rate` (`v`,
  units mol·m⁻³·s⁻¹), `reaction_rate_coefficient`, plus `kcat` (turnover
  number) and `michaelis_constant` (`Km`).
- **Reaction-structure representations**: `has_reaction_smiles_representation`,
  `has_reaction_smarts_representation`, `has_rinchi_representation`,
  `has_smirks_representation`, `has_reaction_representation` — directly relevant
  to encoding atom-mapped reactions.
- **Isotope machinery**: `Isotope`/`Nuclide` classes, and the relations
  `isotopologue_of` and `isotopomer_of` (alongside related nuclear-family
  relations such as `isobar_of`, `isotone_of`, `isotope_of`), plus an
  `isomeric_smiles_string` whose description already cites `[13C]`. This is the
  conceptual vocabulary that ¹³C-MFA needs.
- **Per-atom individuation**: `AtomOccurrence` ("one of two occurrences of
  oxygen in nitrate") with `occurrence_of → Atom`, `valence`, `oxidation_number`,
  etc., reached via `has_atom_occurrences`. This is the natural anchor for
  **atom mapping**, because atom transitions are relations between individuated
  substrate and product atom occurrences.
- **Concentration** (`Concentration` class + `concentration` slot +
  `ConcentrationUnitEnum`) — supports the pool-size / metabolomics coupling
  needed by INST-MFA.
- **`ReactionGroupingClass`** and **`ReactionTypeEnum`** for classifying
  reactions (currently organic-synthesis flavored: oxidation, hydrolysis,
  isomerization, …).

In short: ChEMROF already models reactions, participants, stoichiometry,
isotopes/isotopologues/isotopomers, per-atom occurrences, reaction-structure
linear notations, concentrations, and basic enzyme kinetics. That is a
surprisingly large fraction of the *chemistry* underlying fluxomics.

## 5. Gaps relative to fluxomics use cases

The gaps are mostly about **quantitative network modeling** rather than
chemistry per se — i.e. the parts that SBML-`fbc`/FluxML add on top of a
chemical reaction network:

1. **Stoichiometry is integer-only and unsigned.** `ReactionParticipant.stoichiometry`
   has `range: integer`. GEMs routinely use **fractional** coefficients
   (biomass reactions, lumped reactions, cofactor ratios). Left/right is
   captured by participant lists, but a single signed `float` coefficient is
   the modeling convention.

2. **No flux quantity.** `reaction_rate` exists as an intrinsic kinetic rate,
   but there is no notion of an *estimated/observed network flux* with its
   units (mmol·gDW⁻¹·h⁻¹), confidence interval, and the *experiment/condition*
   it pertains to. Flux is condition-specific data, not an intrinsic property
   of a reaction.

3. **No flux bounds / objective / FBA scaffolding.** No `lower_bound`,
   `upper_bound`, `reversible` flag, or objective-function representation.

4. **No compartment / cellular-location model.** Metabolites and reactions in
   GEMs are compartmentalized; transport reactions move species between
   compartments. ChEMROF has `is_transport: boolean` but no compartment entity
   or per-participant compartment.

5. **No first-class atom-mapping / atom-transition construct.** `AtomOccurrence`
   exists, but there is no relation asserting "substrate atom occurrence *X*
   becomes product atom occurrence *Y* in reaction *R*." Atom-mapped reaction
   SMILES could carry this implicitly, but a structured construct is what MFA
   tooling consumes.

6. **No measurement/distribution model for labeling.** No `MassIsotopomerDistribution`
   (MID/MDV vector), no per-position labeling state, no EMU construct, and no
   way to attach measured labeling data to a metabolite in an experiment.

7. **No experiment / dataset context, and no notion of experiment type.**
   Fluxes and MIDs are only meaningful relative to an organism, strain, growth
   condition, tracer, timepoint, measurement platform, and the *kind* of
   experiment (FBA vs stationary ¹³C-MFA vs INST-MFA vs parallel/COMPLETE-MFA;
   see the typology in §2.5). ChEMROF has no such context or experiment-type
   construct (appropriately — it is a chemistry schema), so a fluxomics
   extension must decide what lives here vs. in a companion schema (§7.4).

8. **GPR associations** (gene/enzyme → reaction) are out of scope for a
   chemistry schema and would belong in a companion model that *references*
   ChEMROF reactions.

The worked example in Appendix A (a Bayesian *kinetic* model) surfaces three
further gaps that matter for the kinetic/dynamic experiment type:

9. **No reaction rate-law / mechanism typing.** Kinetic models tag each
   reaction with a rate law (e.g. reversible vs irreversible Michaelis–Menten,
   mass-action, a "drain"/boundary flux). ChEMROF has the *parameters* (`kcat`,
   `michaelis_constant`) but no controlled vocabulary for the *mechanism* they
   parameterize, and no inhibition constant (`Ki`).

10. **No enzyme-regulation relationships.** Allosteric activation/inhibition and
    competitive inhibition (metabolite → enzyme effects) are central to kinetic
    models. ChEMROF has `ChemicalRole`/`has_chemical_role` but nothing for
    metabolite-on-enzyme regulatory interactions (these may belong in a
    companion enzyme/kinetics schema).

11. **No reaction thermodynamics.** Standard Gibbs free energy of formation
    (ΔGf°, the `dgf` priors in the example), temperature, transported charge,
    and membrane potential drive reversibility/direction. ChEMROF has assorted
    `thermophysical_property` slots but no ΔGf°/ΔGr° for reactions or a
    thermodynamics-based directionality model.

## 6. Two strategic options

**Option A — ChEMROF as the chemistry substrate, fluxomics in a companion
schema (recommended).** Keep ChEMROF focused on chemical entities and
reactions, and build a thin fluxomics LinkML module that *imports* ChEMROF and
adds the modeling/experiment layer (fluxes, bounds, objectives, compartments,
MIDs, experiments). This mirrors how SBML-`fbc` and FluxML sit *on top of* a
reaction network, and keeps ChEMROF from absorbing systems-biology scope. The
companion would reuse ChEMROF `Reaction`, `ReactionParticipant`,
`ChemicalEntity`, `Concentration`, `Isotope`, and `AtomOccurrence`.

**Option B — Extend ChEMROF in place.** Add the minimal *chemistry-adjacent*
pieces that clearly belong here (atom transitions, signed/float stoichiometry,
isotopologue/MID vocabulary) and leave the network-modeling layer to consumers.

A pragmatic split: do the **chemistry-adjacent** items (Sections 7.1–7.3) in
ChEMROF, and the **modeling/experiment** items (7.4–7.5) in a companion schema.

## 7. Concrete extension sketches

These are illustrative LinkML fragments for discussion, not finished schema.

### 7.1 Allow signed, fractional stoichiometry (small, in-place)

```yaml
slots:
  stoichiometry:
    range: float          # was: integer
    description: >-
      Signed stoichiometric coefficient of the participant in the reaction
      (negative for consumed, positive for produced, by convention), allowing
      fractional values as used in genome-scale biomass and lumped reactions.
```

(If integer semantics are still wanted for elementary reactions, keep
`stoichiometry: integer` and add a separate `stoichiometric_coefficient: float`
for network modeling.)

### 7.2 Atom transitions (atom mapping) using existing `AtomOccurrence`

```yaml
classes:
  AtomTransition:
    is_a: ChemicalRelationship
    description: >-
      Asserts that a substrate atom occurrence corresponds to (becomes) a
      product atom occurrence within a specific reaction — the unit of an atom
      mapping / atom transition network used in 13C-MFA.
    attributes:
      reactant_atom:
        range: AtomOccurrence
        required: true
      product_atom:
        range: AtomOccurrence
        required: true
slots:
  has_atom_transitions:
    range: AtomTransition
    multivalued: true
    inlined: true
    domain: Reaction
```

This lets ChEMROF represent the same information as MetAMDB / mapped reaction
SMILES, but in a queryable structured form, while reusing `AtomOccurrence`.

### 7.3 Isotope-labeling vocabulary (chemistry-adjacent)

```yaml
classes:
  MassIsotopomerDistribution:
    description: >-
      The fractional abundances (summing to 1) of the mass isotopologues
      (M+0, M+1, M+2, …) of a chemical entity or molecular fragment; the
      primary measurement in 13C-MFA (a.k.a. mass distribution vector, MDV).
    attributes:
      fragment_of:
        range: ChemicalEntity
      fractions:                 # ordered M+0, M+1, ...
        range: float
        multivalued: true
      tracer:
        description: e.g. "[U-13C6] glucose"
```

`Isotopologue`/isotopomer relations already exist; this adds the
*distribution* object that fluxomics measures. (`EMU` could be added later as a
fragment construct if structured isotope simulation is in scope.)

### 7.4 Network-modeling layer (companion schema, sketch)

```yaml
classes:
  Compartment:
    description: A bounded cellular space (e.g. cytosol, mitochondrion).
  MetabolicFlux:
    description: >-
      An estimated or observed throughput through a reaction under a specific
      condition, with units and uncertainty.
    attributes:
      reaction:        {range: Reaction}
      value:           {range: float}
      unit:            {description: e.g. mmol/gDW/h}
      lower_bound:     {range: float}
      upper_bound:     {range: float}
      confidence_low:  {range: float}
      confidence_high: {range: float}
      condition:       {range: GrowthCondition}
  Objective:
    description: FBA objective (reaction coefficients to maximize/minimize).
  Tracer:
    description: >-
      A labeled substrate used in an isotope-labeling experiment, specifying
      which isotope sits at which atom position(s).
    attributes:
      substrate:        {range: ChemicalEntity}
      isotope:          {range: Isotope}        # e.g. carbon-13
      labeled_positions:                        # e.g. [1, 2] for [1,2-13C]
        range: integer
        multivalued: true
      purity:           {range: float}          # fractional isotopic purity
  FluxomicsExperiment:
    description: >-
      A single fluxomics experiment, typed along the axes in section 2.5.
    attributes:
      inference_paradigm: {range: FluxInferenceParadigmEnum}
      tracers:            {range: Tracer, multivalued: true}  # >1 ⇒ parallel/COMPLETE-MFA
      measurement_platform: {range: FluxMeasurementPlatformEnum}
      isotopic_steady_state: {range: boolean}
      timepoints:         {range: float, multivalued: true}   # for INST/dynamic
      condition:          {range: GrowthCondition}
enums:
  FluxInferenceParadigmEnum:    # Axis A
    permissible_values:
      flux_balance_analysis: {}
      stoichiometric_mfa: {}
      stationary_13C_mfa: {}
      nonstationary_mfa: {}      # INST-MFA
      dynamic_mfa: {}
      flux_ratio_analysis: {}
  FluxMeasurementPlatformEnum:  # Axis D
    permissible_values:
      GC_MS: {}
      LC_MS: {}
      tandem_MS: {}
      NMR: {}
```

A multivalued `tracers` slot naturally captures **parallel labeling /
COMPLETE-MFA** (more than one tracer for the same model), and `isotope` +
`labeled_positions` on `Tracer` covers Axes B and C (positional vs uniform,
¹³C vs ¹⁵N/²H/¹⁸O). This keeps "experiment type" as a few small controlled
vocabularies rather than one flat enum.

### 7.5 SBO/SBML alignment

Tag reaction subtypes (transport, exchange, biomass pseudo-reaction) so models
round-trip with SBML-`fbc`. ChEMROF already has `is_transport`; an enum or SBO
cross-reference for `exchange` / `biomass` / `demand`/`sink` reactions would
complete the picture.

## 8. Recommendation

1. **Adopt Option A** as the overall architecture: a fluxomics LinkML module
   that imports ChEMROF, keeping systems-biology scope out of the chemistry
   schema.
2. **In ChEMROF itself, make the small chemistry-adjacent additions** that are
   independently useful and clearly in-scope:
   - signed/float stoichiometry (or a parallel `stoichiometric_coefficient`),
   - an `AtomTransition` construct reusing `AtomOccurrence`,
   - a `MassIsotopomerDistribution` class to complement the existing
     isotopologue/isotopomer relations.
3. **Validate against real examples**: (a) for the isotope path, encode one
   well-characterized pathway (e.g. glycolysis/TCA) with atom mappings and a
   [U-¹³C]glucose tracer and round-trip a small FBA model from BiGG; (b) for the
   kinetic path, reuse the **methionine-cycle Maud model** dissected in
   Appendix A — its metabolites already carry InChIKeys and BiGG IDs, so it is a
   ready-made test of ChEMROF as the metabolite/reaction identity provider.
4. **Engage standards**: align reaction typing with SBO, and ensure reaction
   and metabolite identifiers map cleanly to BiGG/MetaNetX/Rhea so ChEMROF can
   act as the chemical-identity hub for fluxomics datasets.

## Appendix A. Worked example: the biosustain methionine-cycle (Maud) model

To ground the analysis, this appendix dissects a real public model —
[`biosustain/Methionine_model`](https://github.com/biosustain/Methionine_model)
(`data/methionine`). It is a **Maud** model: Bayesian inference of a *kinetic*
metabolic model with thermodynamic constraints (Stan/HMC under the hood). It is
the **kinetic / dynamic** experiment type from §2.5 — not ¹³C-MFA — which makes
it a useful contrast: it stresses ChEMROF's kinetics and identity features and
needs *none* of the isotope/atom-mapping machinery.

The methionine cycle is modeled in one compartment (`c`) with 10 reactions
(`METAT`, `METH`, `GNMT`, `AHC`, `MS`, `BHMT`, `CBS`, `MTHFR`, `PROT`, plus a
`met-L-source` drain) over 19 metabolites (methionine, ATP, S-adenosyl­methionine,
S-adenosyl­homocysteine, homocysteine, 5-methyl-THF, …).

**What maps cleanly onto ChEMROF today**

- **Metabolites → `ChemicalEntity`.** Every metabolite is given by
  **InChIKey** *and* a **BiGG** source URL, e.g.
  `met-L → FFEARJCKVFRZRR-BYPYZUCNSA-N` (bigg `met__L`). ChEMROF already has
  `inchi_key_string` and the `bigg.metabolite` prefix — this is exactly the
  identity-hub role ChEMROF is built for, and is its clearest immediate value
  to such a project.
- **Reactions → `Reaction` + `ReactionParticipant`.** Each reaction has a
  signed stoichiometry table; e.g. `METAT`: `met-L −1, atp −1, pi +1, ppi +1,
  amet +1`.
- **Kinetic parameters → existing slots.** Priors are specified for `kcat`
  (per enzyme/reaction) and `km` (per metabolite/enzyme/reaction) — directly the
  ChEMROF `kcat` and `michaelis_constant` slots.

**What the example proves ChEMROF is missing** (cross-referencing §5)

| Maud construct (this model) | ChEMROF status |
| --- | --- |
| `stoichiometry = -1.0 / 1.0` (signed **float**) | gap #1 — ChEMROF `stoichiometry` is integer |
| `target_type = "flux"` measurements with error | gap #2 — no measured/estimated flux quantity |
| `compartment` + `metabolite_in_compartment` (`balanced` = internal/boundary) | gap #4 — no compartment model |
| `mechanism = irreversible_michaelis_menten / reversible_michaelis_menten / drain` | gap #9 — no rate-law/mechanism vocabulary |
| `ki` priors; `allostery` (activation/inhibition); `competitive_inhibition` | gaps #9/#10 — no `Ki`, no enzyme-regulation relations |
| `dgf` (ΔGf°), `temperature`, `transported_charge`, `psi` | gap #11 — no reaction thermodynamics |
| `experiment` blocks with `is_train`/`is_test`, `enzyme_knockouts` | gap #7 — no experiment/condition context |
| `enzyme` / `enzyme_reaction` / `subunits` | gap #8 — GPR; out of ChEMROF scope |

**Two things worth emphasizing**

- *No atom mappings, isotopomers, or MIDs appear anywhere in this model.* That
  is not a deficiency — it confirms §2.5's claim that the **experiment type
  selects which extensions matter**. A kinetic model needs mechanism/Ki/ΔGf°
  and measured flux+concentration; the §7.2–7.3 isotope constructs are simply
  irrelevant here.
- *ChEMROF already does the part that is hardest to get right* — unambiguous
  chemical identity (InChIKey, formula, charge, and the cross-refs needed to
  later attach ΔGf° and pKa). The missing pieces are the systems-biology
  modeling layer, which (per Option A) belongs in a companion schema that
  imports ChEMROF and reuses `ChemicalEntity`/`Reaction`/`Concentration`.

A small, high-value proof of concept: write a converter that ingests this
`methionine_cycle.toml` and emits ChEMROF `ChemicalEntity` records (keyed by
InChIKey/BiGG) plus `Reaction`/`ReactionParticipant` records, leaving fluxes,
kinetics, regulation, and thermodynamics to a companion `maud`-aligned module.

## 9. Sources

- Weitzel et al., *The Design of FluxML: A Universal Modeling Language for
  ¹³C Metabolic Flux Analysis*, Front. Microbiol. 2019 —
  <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6543931/>
- Weitzel et al., *13CFLUX2 — high-performance software suite for ¹³C-MFA*,
  Bioinformatics 2013 — <https://academic.oup.com/bioinformatics/article/29/1/143/273014>
- Antoniewicz et al., *Elementary Metabolite Units (EMU): a novel framework for
  modeling isotopic distributions*, Metab. Eng. 2007 —
  <https://www.sciencedirect.com/science/article/abs/pii/S109671760600084X>
- *EMUlator: an EMU-based isotope simulator* —
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC6503117/>
- *MetAMDB: Metabolic Atom Mapping Database* —
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC8878866/>
- *Comparative evaluation of atom mapping algorithms for balanced metabolic
  reactions (Recon 3D)*, J. Cheminform. 2017 —
  <https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0223-1>
- Olivier & Bergmann, *SBML Level 3 Package: Flux Balance Constraints (fbc)* —
  <https://pubmed.ncbi.nlm.nih.gov/26528567/>
- *SBOannotator: automated assignment of Systems Biology Ontology terms*,
  Bioinformatics 2023 — <https://academic.oup.com/bioinformatics/article/39/7/btad437/7224245>
- *Achieving Metabolic Flux Analysis for S. cerevisiae at a Genome-Scale* —
  <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4588810/>
- Crown & Antoniewicz, *Integrated ¹³C-MFA of 14 parallel labeling experiments
  in E. coli* (COMPLETE-MFA), Metab. Eng. 2015 —
  <https://pubmed.ncbi.nlm.nih.gov/25596508/>
- *Optimal tracers for parallel labeling experiments and ¹³C-MFA: a precision
  and synergy scoring system*, Metab. Eng. 2016 —
  <https://pubmed.ncbi.nlm.nih.gov/27267409/>
- *One-shot ¹³C¹⁵N-MFA for simultaneous quantification of carbon and nitrogen
  flux* — <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9996240/>
- *An analytic framework for estimating metabolic flux ratios from ¹³C tracer
  experiments (METAFoR)* — <https://pmc.ncbi.nlm.nih.gov/articles/PMC2430715/>
- *OpenFLUX2: ¹³C-MFA software for single and parallel labeling experiments* —
  <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4263107/>
- *biosustain/Methionine_model* (worked example, Appendix A) —
  <https://github.com/biosustain/Methionine_model>
- *Maud* — Bayesian inference of kinetic models of metabolism (biosustain) —
  <https://github.com/biosustain/Maud>
</content>
</invoke>
