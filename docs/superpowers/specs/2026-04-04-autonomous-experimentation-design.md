# Design: extending ChemROF toward autonomous experimentation

**Date:** 2026-04-04
**Updated:** 2026-04-12
**Branch:** `feat/autonomous-experimentation-scout`
**Status:** Scouting proposal

## Context

ChemROF already provides a strong semantic layer for chemical identity: atoms,
molecules, mixtures, roles, and reactions are modeled in LinkML and can be
rendered into JSON Schema, SHACL, OWL, and other artifacts. That is a useful
starting point for autonomous experimentation, but it is only one layer of the
stack.

The literature now gives a fairly consistent answer about what the rest of the
stack looks like. Across recent autonomous experimentation papers, orchestration
frameworks, and adjacent standards, the recurring pattern is a separation
between:

1. stable identification of chemicals and formulations
2. executable procedure definitions
3. concrete experiment executions on hardware
4. measurements, observations, and derived outcomes
5. campaign-level goals, constraints, and closed-loop decisions

That convergence shows up in different forms:

- Pagel, Jirasek, and Cronin (published 2026-04-03) move from literature text,
  to XDL procedure, to simulated execution, to robot execution.
- ORD structures executed reactions around inputs, setup, conditions,
  observations, workups, outcomes, and provenance.
- LabOP separates reusable protocol definitions from execution traces, agents,
  parameter values, and datasets.
- SiLA 2 separates capability exposure and command transport from the domain
  data exchanged through those capabilities.
- HELAO-async, ChemOS 2.0, Atlas/Olympus, the dynamic knowledge graph work, and
  recent closed-loop electrochemistry platforms all add campaign state,
  asynchronous orchestration, and optimization history on top of chemistry and
  measurements.

The seed paper on literature verification via chemputation and LLMs is
especially relevant because it reinforces the same layering in a chemistry-first
setting: the system extracts procedures from papers, translates them into XDL,
simulates execution on a target platform, and finally executes them on a
robotic system. In other words, autonomous experimentation is not just about
reactions; it is about the path from text to executable procedure to measured
run to optimization loop.

## Repo-State Readout

ChemROF is already useful for autonomous experimentation in the following ways:

- `src/chemrof/schema/chemrof.yaml` already defines a strong chemistry and
  formulation layer through classes such as `ChemicalEntity`, `Material`,
  `Concentration`, and `IngredientRole`. That is already enough to ground
  reagents, solvents, additives, and stock formulations in a normalized schema.
- The same schema defines `Reaction` and `ReactionParticipant` as an abstract
  transformation layer, and it already contains an explicit TODO to align that
  area with ORD. That is an important clue that the repo already recognizes the
  need for an executed-reaction interchange target.
- `docs/explanations/clinical-assays.md` already argues for separating analyte
  identity from assay result and downstream interpretation. That is directly
  relevant to autonomous experimentation, where the path from raw observation to
  derived optimization metric must remain explicit.
- `src/chemrof/cli/main.py` already exposes a practical ingest path: the
  `chemrof convert` command can normalize SMILES or InChI into ChemROF records
  and optionally enrich them. That is immediately useful for reconciling
  reagent identities coming from procedure text, robot software, or analytical
  pipelines.
- LinkML generation already gives ChemROF a validation and artifact-generation
  path for future autonomous-experiment records.

What ChemROF does **not** currently model is the experiment/campaign layer:
there are no first-class classes for procedures, steps, executions, samples,
measurements, objectives, constraints, or optimization state.

## What Autonomous Experimentation Needs

The table below summarizes the common representational layers in current
autonomous-experimentation systems and what they imply for ChemROF.

| Need | How mature systems represent it | Implication for ChemROF |
|---|---|---|
| Procedure definition | XDL models hardware-independent, executable procedures with standard steps, parameters, blueprints, iteration, monitoring, and parallel execution | ChemROF should not invent a second XDL, but it does need a normalized `ProcedureDefinition`/`ProcedureStep` layer and explicit links to external XDL payloads |
| Protocol execution history | LabOP represents protocols as RDF and distinguishes protocol definitions from repeated `Execution` histories with agents, parameter values, and feedback measurements | ChemROF needs a hard distinction between a reusable procedure and a concrete run |
| Descriptive reaction record | ORD models reaction inputs, setup, conditions, observations, workups, outcomes, analyses, and provenance | ChemROF should add an executed-reaction layer that aligns naturally to ORD rather than overloading the current conceptual `Reaction` class |
| Device interoperability | SiLA 2 exposes device capabilities as discoverable features with commands and properties; it recommends AnIML for analytical data | ChemROF should reference device capabilities and command provenance, not try to replace SiLA |
| Analytical data capture | AnIML and Allotrope focus on raw analytical datasets, metadata, instrument settings, and result context | ChemROF needs measurement/result objects plus links to raw files; it should not absorb n-dimensional analytical payloads |
| Closed-loop optimization | Atlas/Olympus use an ask-tell interface over parameter spaces, observations, optimization trajectories, and objectives; HELAO and ChemOS orchestrate asynchronous workflows; knowledge-graph approaches add explicit goals, plans, and experiment history | ChemROF needs campaign, objective, constraint, design-space, suggestion, and run-status classes if it wants to participate in autonomous loops |
| Failure handling and quality control | HELAO, dynamic-knowledge-graph systems, and autonomous electrochemistry platforms explicitly track asynchronous runs, abnormal measurements, exclusions, and human/AI oversight | ChemROF must represent failed runs, rejected measurements, anomalies, and whether a result was used for optimization |

## Main Gap: ChemROF Stops at Chemistry, Not Experiments

The current schema is strongest when answering questions like:

- What chemical entities are involved?
- How are they structurally represented?
- What broad reaction transformation is intended?
- What roles do ingredients play in a mixture?

Autonomous experimentation adds a different set of questions:

- What exact procedure was proposed?
- Which hardware or software executed it?
- Which concrete sample, aliquot, or well was acted upon?
- What measurements were recorded, and from which raw dataset?
- Which metrics were derived from those measurements?
- Which goals and constraints drove the next decision?
- Which experiments failed, were excluded, or are still pending?

Those questions currently have no canonical home in ChemROF.

## Literature-Backed Design Principles

The sources above support a fairly specific modeling strategy rather than a
generic "more metadata" recommendation.

### 1. Separate abstract chemistry from executed experiment records

ORD, ChemOS-style orchestration, HELAO-async, and the closed-loop
electrochemistry work all derive value from what was actually executed,
measured, excluded, or retried. ChemROF's current `Reaction` class is best kept
as the chemistry transformation layer; the autonomous extension should add a
distinct executed-record layer rather than overloading `Reaction` itself.

### 2. Keep executable payloads external, but surface semantic handles

XDL and LabOP already provide richer procedure semantics than ChemROF should try
to recreate. ChemROF should model the minimum needed for indexing, linking,
querying, and validation: procedure identity, high-level step structure,
parameter settings, execution status, and provenance. The full XDL or LabOP
payload should remain external and authoritative.

### 3. Model occurrences and lineage, not only classes of chemicals

The autonomous systems in the literature operate on actual samples, aliquots,
wells, vessels, flow segments, and datasets. A chemistry schema without a
sample-occurrence layer cannot capture the difference between "acetone" as a
chemical entity and "this 150 uL aliquot in well B3" as the thing a robot
actually touched.

### 4. Make the path from raw data to optimization metric explicit

AnIML, ORD analyses, the clinical-assays note already in this repo, and the
electrochemistry platform all point to the same requirement: the schema must be
able to distinguish raw analytical artifacts, measurement events, intermediate
results, and the derived metric that was finally used for ranking or Bayesian
optimization.

### 5. Treat orchestration state and exceptions as first-class

HELAO-async, ChemOS 2.0, Atlas/Olympus, and dynamic-knowledge-graph systems all
need explicit run status, objectives, constraints, exclusions, and agent/device
provenance. A self-driving-lab data model that only records successful final
outcomes is not enough to support auditability or closed-loop learning.

## Recommended Modeling Direction

ChemROF should extend toward autonomous experimentation through a **separate
experiment module**, not by turning the core chemistry schema into a lab
operating system.

Recommended shape:

- Keep `chemrof.yaml` centered on chemical semantics.
- Add a new LinkML module, for example
  `src/chemrof/schema/extensions/autonomous_experimentation.yaml`, that imports
  the chemical core.
- Model a thin semantic layer for experiment definitions, executions, results,
  and optimization state.
- Link out to XDL, ORD, SiLA, AnIML, Allotrope, LabOP, or orchestration systems
  for payloads that those standards already own well.

This preserves ChemROF's current value while making it interoperable with
autonomous systems.

One concrete refinement follows from the literature and from the likely growth
of the ecosystem: avoid adding one bespoke slot per external standard. A single
typed `ExternalReference` pattern is more durable than parallel slots such as
`xdl_id`, `ord_reaction_id`, `labop_id`, or `animl_uri`.

## Missing Schema Pieces

### 1. Executed Experiment Layer

ChemROF needs a class that separates a conceptual reaction from a concrete
performed run.

Recommended additions:

- `ReactionExperiment`
- `ExperimentCampaign`
- `ExperimentBatch`
- `ExperimentRunStatusEnum`

Minimum useful slots:

- `realizes_reaction: Reaction`
- `part_of_campaign: ExperimentCampaign`
- `run_status`
- `started_at`
- `ended_at`
- `executed_by_agent`
- `executed_on_instrument`
- `has_input_sample`
- `has_output_sample`
- `has_measurement`
- `has_outcome`
- `has_external_reference`

Why this matters:

- ORD, HELAO, ChemOS, and dynamic knowledge graph systems all distinguish the
  abstract chemistry from the executed run.
- Closed-loop systems learn from executed runs, not from bare reaction classes.

### 2. Procedure Definition and Step Layer

ChemROF needs a normalized model of procedures, even if the authoritative source
is XDL or LabOP.

Recommended additions:

- `ProcedureDefinition`
- `ProcedureExecution`
- `ProcedureSection`
- `ProcedureStep`
- `MaterialHandlingStep`
- `ConditioningStep`
- `MeasurementStep`
- `WorkupStep`
- `PurificationStep`
- `ParameterSetting`

Minimum useful slots:

- `has_step`
- `step_order`
- `uses_parameter_setting`
- `acts_on_sample`
- `uses_reagent`
- `target_container`
- `step_status`
- `has_external_reference`

Do not start by modeling every XDL primitive as a dedicated ChemROF class.
Instead:

- begin with a small number of generic step families
- support step typing via enums or a shallow hierarchy
- preserve links to external XDL/LabOP identifiers through `ExternalReference`
  records

### 3. Sample, Container, and Material-Occurrence Layer

Autonomous platforms act on **occurrences** of chemicals, not only on abstract
species. ChemROF currently models species and mixtures well, but not concrete
samples in vessels, wells, or flow lines.

Recommended additions:

- `ChemicalAmount` or `MaterialPortion`
- `Sample`
- `Aliquot`
- `Container`
- `Well`
- `Plate`
- `Reservoir`
- `Vessel`

Minimum useful slots:

- `represents_entity: ChemicalEntity`
- `located_in`
- `derived_from_sample`
- `has_volume`
- `has_mass`
- `has_concentration`
- `has_composition`
- `container_position`

This is essential for:

- plate-based experimentation
- flow chemistry
- sampling for offline analysis
- tracking source and destination during robotic actions

### 4. Measurement, Observation, and Derived Metric Layer

Autonomous experimentation rarely optimizes directly on raw analytical data. It
usually works through a chain like:

raw dataset -> measurement event -> derived metric -> objective evaluation

Recommended additions:

- `MeasurementEvent`
- `Observation`
- `AnalyticalDataset`
- `MeasurementResult`
- `DerivedMetric`
- `PerformanceIndicator`
- `MeasurementQualityFlagEnum`

Minimum useful slots:

- `measures_sample`
- `measures_analyte`
- `uses_measurement_method`
- `has_raw_dataset`
- `has_result_value`
- `has_unit`
- `has_uncertainty`
- `derived_from_measurement`
- `quality_flag`
- `used_for_optimization`

This layer is where ChemROF can extend the assay precision work already visible
in the repo. For example:

- HPLC chromatogram peak area is not the same thing as yield
- cyclic voltammogram trace is not the same thing as oxidation peak voltage
- absorbance trace is not the same thing as growth rate

The schema should be able to represent both the raw observation and the derived
metric that drives optimization.

### 5. Goal, Constraint, and Optimization Layer

This is the largest missing piece if ChemROF wants to interoperate with
self-driving labs rather than just store finished results.

Recommended additions:

- `GoalSet`
- `Goal`
- `Objective`
- `Constraint`
- `DesignSpace`
- `OptimizationVariable`
- `SuggestedExperiment`
- `DecisionRound`
- `DecisionPolicy`
- `OptimizationHistory`

Minimum useful slots:

- `optimizes_metric: DerivedMetric`
- `objective_direction`
- `target_value`
- `constraint_expression`
- `has_variable`
- `variable_type`
- `allowed_range`
- `allowed_values`
- `suggested_parameters`
- `based_on_historical_data`
- `decision_rationale`

Practical design rule:

- Represent the **state of the optimization loop**, not the internals of every
  optimizer.
- ChemROF should know that an experiment was suggested to improve yield under a
  temperature constraint.
- ChemROF does not need to encode all Gaussian process kernel settings.

### 6. Provenance, Agents, and Exceptions

Autonomous experimentation is operationally fragile. The schema needs explicit
support for partial success, anomalies, exclusions, and mixed human/AI control.

Recommended additions:

- `Agent`
- `HumanAgent`
- `SoftwareAgent`
- `Instrument`
- `DeviceCapability`
- `ExceptionRecord`
- `FailureMode`
- `ExclusionReason`

Minimum useful slots:

- `proposed_by_agent`
- `approved_by_agent`
- `executed_by_agent`
- `reported_by_instrument`
- `has_exception`
- `excluded_from_model_update`
- `failure_reason`

This matters because real systems:

- run asynchronously
- pause or fail on hardware faults
- mark outliers or invalid analyses
- continue campaigns even when one instrument drops out

## A Minimal ChemROF-AE Kernel

If ChemROF wants a practical first milestone, the smallest useful kernel is:

```text
ExperimentCampaign
  -> GoalSet
  -> Objective*
  -> Constraint*
  -> SuggestedExperiment*
  -> ReactionExperiment*

ReactionExperiment
  -> realizes_reaction: Reaction
  -> uses_procedure: ProcedureDefinition
  -> execution: ProcedureExecution
  -> input_sample: Sample*
  -> output_sample: Sample*
  -> measurement: MeasurementEvent*
  -> derived_metric: DerivedMetric*
  -> external_reference: ExternalReference*
  -> run_status

ProcedureDefinition
  -> step: ProcedureStep*
  -> external_reference: ExternalReference*

MeasurementEvent
  -> raw_dataset: AnalyticalDataset
  -> result: MeasurementResult*
  -> external_reference: ExternalReference*

Sample
  -> represents_entity: ChemicalEntity
  -> located_in: Container
```

This kernel would already support:

- a proposed experiment
- a completed run
- a link to the intended reaction
- a reusable procedure
- concrete samples and containers
- measurement lineage
- objective-driven optimization

## Recommended Milestones

### Milestone 1: Add an Interop-First Experiment Kernel

Create a new extension schema with:

- `ExperimentCampaign`
- `ReactionExperiment`
- `ProcedureDefinition`
- `ProcedureExecution`
- `ProcedureStep`
- `Sample`
- `Container`
- `MeasurementEvent`
- `DerivedMetric`
- `Objective`
- `Constraint`
- `ExperimentRunStatusEnum`
- `ExternalReference`

Also add a reusable external-reference pattern instead of one slot per
ecosystem. Recommended minimum slots:

- `has_external_reference`
- `reference_system`
- `identifier`
- `uri`
- `artifact_role`
- `media_type`

This is a better first step than baking in dedicated `xdl_id`,
`ord_reaction_id`, `sila_feature_id`, `animl_uri`, `allotrope_uri`, and
`labop_id` slots because a single experiment may legitimately point to several
external artifacts across procedure, execution, device, and analytics layers.

This would be enough to make ChemROF a semantic hub without forcing it to own
every downstream payload.

### Milestone 2: Add Executed-Reaction Examples

Add a small example set in `src/data/examples/valid`, such as:

- `ReactionExperiment-aldol-optimization-run01.yaml`
- `ExperimentCampaign-electrochem-closed-loop.yaml`
- `ProcedureDefinition-simple-flow-screen.yaml`

The first examples should include:

- one successful run
- one failed or excluded run
- one suggested-but-not-yet-executed experiment

Negative and pending cases are important because closed-loop systems rely on
them operationally.

### Milestone 3: Align ReactionExperiment with ORD

The current schema already points toward ORD. The next concrete step is to make
that alignment explicit:

- use `Reaction` for the chemistry transformation
- use `ReactionExperiment` for executed records
- map inputs, conditions, workups, outcomes, and provenance to ORD concepts

This gives ChemROF a clear boundary:

- ChemROF core for entities and semantics
- ChemROF-AE for execution and campaign context
- ORD as a concrete exchange target for reaction records

### Milestone 4: Add Procedure Crosswalks to XDL and LabOP

Once the experiment kernel exists:

- store authoritative XDL or LabOP payloads externally
- project key steps, parameters, and execution status into ChemROF
- avoid lossy re-encoding of full procedures unless a strong use case appears

This is especially relevant to the seed paper, where literature procedures are
translated into XDL and executed on Chemputers.

### Milestone 5: Add Measurement Lineage and Quality Flags

After the first experiment examples land, extend the model for:

- raw analytical file linkage
- derived metric lineage
- uncertainty and confidence
- anomaly/exclusion tracking
- explicit indication of whether a result informed model updates

This is required for trustworthy closed-loop optimization.

## Integration Points with Existing Standards and Tools

| Standard or tool | What it does well | Recommended ChemROF relationship |
|---|---|---|
| XDL | Executable, hardware-independent procedure description for synthesis and optimization | Link to XDL payloads; normalize the minimum needed procedure and parameter metadata into ChemROF |
| ORD | Structured executed reaction records, including conditions, workups, outcomes, analyses, and provenance | Make `ReactionExperiment` the natural ORD-aligned layer |
| LabOP | RDF-native protocol definition and repeated execution histories with agents and parameter values | Use as a protocol-level interop target, especially outside pure synthesis |
| SiLA 2 | Device capability discovery plus commands and properties | Reference instrument capabilities and execution provenance; do not replace device control with ChemROF |
| AnIML | Analytical data exchange for instrument result data | Link raw analytical datasets and extract summary results into ChemROF |
| Allotrope | Rich analytical data plus metadata, instrument settings, and semantic description | Link to ADF payloads and reuse ChemROF only for campaign-level semantics and derived metrics |
| ChemOS 2.0 | Orchestration architecture for self-driving labs | Treat as an execution/orchestration peer system; ChemROF can provide semantic records for runs and objectives |
| HELAO / HELAO-async | Asynchronous orchestration over workflows, action servers, shared resources, and data streams | Use ChemROF to represent run state, samples, measurements, and campaign history exchanged with orchestrators |
| Atlas / Olympus | Ask-tell optimization over parameter spaces, observations, and trajectories | Align ChemROF objective, variable, suggestion, and historical-data classes with this interaction model |
| OntoRxn / OntoReaction / OntoDoE / OntoLab | Semantic-web representations of reactions, experiment conditions, goals, and lab digital twins | Reuse mappings where useful; current OntoRxn presence in the repo is already a good foothold |

## Boundary Recommendation

ChemROF should **not** try to become:

- a full scheduler
- a device-driver API
- an optimizer implementation
- a replacement for analytical file standards

ChemROF **should** become:

- a chemically precise semantic layer for experiment definitions and results
- a normalization layer across autonomous experimentation systems
- a validated interchange layer linking chemistry, procedure, measurement, and
  closed-loop campaign state

That boundary is both practical and repo-consistent.

## Concrete Next Step for This Repo

The next implementation step after this proposal should be a small PR that adds
the `chemrof-ae` kernel only, plus 2-3 examples. A reasonable first pass would
introduce:

- `ExperimentCampaign`
- `ReactionExperiment`
- `ProcedureDefinition`
- `ProcedureExecution`
- `ProcedureStep`
- `Sample`
- `Container`
- `MeasurementEvent`
- `DerivedMetric`
- `Objective`
- `Constraint`

with explicit reference slots to XDL, ORD, SiLA, and analytical datasets.

That would give ChemROF immediate value for autonomous experimentation without
locking the project into a monolithic lab ontology.

## Key Sources

- Pagel, Jirasek, Cronin. "Verification and execution of the scientific literature via chemputation augmented by large language models." Communications Chemistry (published 2026-04-03). https://www.nature.com/articles/s42004-026-01993-w
- Tom et al. "Self-Driving Laboratories for Chemistry and Materials Science." Chemical Reviews (2024). https://doi.org/10.1021/acs.chemrev.4c00055
- XDL 2.0 standard docs: https://croningroup.gitlab.io/chemputer/xdl/standard/index.html
- XDL procedure sections: https://croningroup.gitlab.io/chemputer/xdl/usage/procedure_sections.html
- XDL blueprints and parameters: https://croningroup.gitlab.io/chemputer/xdl/standard/xdl_blueprints.html and https://croningroup.gitlab.io/chemputer/xdl/standard/parameters.html
- ORD schema docs: https://docs.open-reaction-database.org/en/latest/schema.html
- ORD paper: Kearnes et al. "The open reaction database." JACS (2021). https://doi.org/10.1021/jacs.1c09820
- LabOP overview and execution model: https://bioprotocols.github.io/labop/ and https://github.com/Bioprotocols/labop
- SiLA 2 core specification: https://sila-standard.com/wp-content/uploads/2022/03/SiLA-2-Part-A-Overview-Concepts-and-Core-Specification-v1.1.pdf
- AnIML document structure overview: https://www.animl.org/an-animl-document
- Allotrope framework overview: https://www.allotrope.org/allotrope-framework
- Atlas ask-tell optimization interface: https://pubs.rsc.org/en/content/articlehtml/2025/dd/d4dd00115j
- ChemOS 2.0: Sim et al. "ChemOS 2.0: An orchestration architecture for chemical self-driving laboratories." Matter (2024). https://doi.org/10.1016/j.matt.2024.04.022
- HELAO-async: Guevarra et al. "Orchestrating nimble experiments across interconnected labs." Digital Discovery (2023). https://doi.org/10.1039/d3dd00166k
- Bai et al. "A dynamic knowledge graph approach to distributed self-driving laboratories." Nature Communications (2024). https://www.nature.com/articles/s41467-023-44599-9
- Autonomous closed-loop electrochemistry platform: https://www.nature.com/articles/s41467-024-47210-x
