# Design: extending ChemROF toward autonomous experimentation

**Date:** 2026-04-04
**Branch:** `feat/autonomous-experimentation-scout`
**Status:** Scouting proposal

## Context

ChemROF already provides a strong semantic layer for chemical identity: atoms,
molecules, mixtures, roles, and reactions are modeled in LinkML and can be
rendered into JSON Schema, SHACL, OWL, and other artifacts. That is a useful
starting point for autonomous experimentation, but it is only one layer of the
stack.

Recent autonomous experimentation systems consistently separate at least five
concerns:

1. stable identification of chemicals and formulations
2. executable procedure definitions
3. concrete experiment executions on hardware
4. measurements, observations, and derived outcomes
5. campaign-level goals, constraints, and closed-loop decisions

The seed paper on literature verification via chemputation and LLMs reinforces
this layering: the system extracts procedures from papers, translates them into
XDL, simulates execution on a target platform, and finally executes them on a
robotic system. In other words, autonomous experimentation is not just about
reactions; it is about the path from text to executable procedure to measured
run to optimization loop.

## Repo-Relevant Readout

ChemROF is already useful for autonomous experimentation in the following ways:

- `ChemicalEntity`, `Material`, mixture classes, `IngredientRole`, and
  `Concentration` provide a chemical identity layer for reagents, solvents,
  additives, and stock formulations.
- `Reaction` and `ReactionParticipant` already give a conceptual reaction layer,
  and the schema explicitly carries a TODO to align with ORD.
- The schema already values assay precision, as shown in
  `docs/explanations/clinical-assays.md`; that same distinction between
  analyte, measurement, and interpretation is central to autonomous workflows.
- The CLI converter can normalize SMILES/InChI into ChemROF instances, which is
  directly useful for reconciling reagent identities coming from procedure text,
  robot software, or analytical pipelines.
- LinkML generation gives ChemROF a practical validation path for future
  autonomous-experiment records.

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
- `external_record`

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
- `external_xdl_step_id`
- `external_labop_node_id`

Do not start by modeling every XDL primitive as a dedicated ChemROF class.
Instead:

- begin with a small number of generic step families
- support step typing via enums or a shallow hierarchy
- preserve links to external XDL/LabOP identifiers

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
  -> run_status

ProcedureDefinition
  -> step: ProcedureStep*

MeasurementEvent
  -> raw_dataset: AnalyticalDataset
  -> result: MeasurementResult*

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

Also add generic external reference slots for:

- `xdl_id`
- `ord_reaction_id`
- `sila_feature_id`
- `animl_uri`
- `allotrope_uri`
- `labop_id`

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

- Seed paper: Pagel, Jirasek, Cronin. "Verification and execution of the scientific literature via chemputation augmented by large language models." Communications Chemistry (2026). https://www.nature.com/articles/s42004-026-01993-w
- XDL standard docs: https://croningroup.gitlab.io/chemputer/xdl/standard/index.html
- XDL procedure sections: https://croningroup.gitlab.io/chemputer/xdl/usage/procedure_sections.html
- ORD schema docs: https://docs.open-reaction-database.org/en/latest/schema.html
- ORD paper: Kearnes et al. "The open reaction database." JACS (2021). https://doi.org/10.1021/jacs.1c09820
- LabOP repository and execution model: https://github.com/Bioprotocols/labop
- SiLA 2 core specification: https://sila-standard.com/wp-content/uploads/2022/03/SiLA-2-Part-A-Overview-Concepts-and-Core-Specification-v1.1.pdf
- AnIML overview: https://www.animl.org/files/pdf/2012_gwk_about_animl.pdf
- Allotrope framework overview: https://www.allotrope.org/allotrope-framework
- Atlas ask-tell optimization interface: https://pubs.rsc.org/en/content/articlehtml/2025/dd/d4dd00115j
- ChemOS 2.0 DOI: https://doi.org/10.1016/j.matt.2024.04.022
- HELAO-async preprint: https://chemrxiv.org/engage/chemrxiv/article-details/64e7b1c63fdae147fabf71f2
- Dynamic knowledge graph for distributed self-driving laboratories: https://pmc.ncbi.nlm.nih.gov/articles/PMC10805810/
- Autonomous closed-loop electrochemistry platform: https://www.nature.com/articles/s41467-024-47210-x
