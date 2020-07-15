# Chemical Ontology Metaclasses

This repo includes schema/datamodel for a chemical ontology

Instances of the classes in the data model are chemical ontology classes, e.g.

 - nickel atom
 - nickel anion
 - carbon 14

Preliminary slides showing the idea:

 - https://docs.google.com/presentation/d/1xCHnJqGp_8jb8Btf6-JX5M_pt5j1NFiYhQFMASFanGM/edit

For driving use case and why we need aan alternatibe to existing chebi atom / simple molecule representation see:

 - https://github.com/EnvironmentOntology/envo/issues/989

Schema: [chemistry-ontology](http://cmungall.github.io/chemistry-ontology)

## Basic idea

We need an alternative classification of chemical atoms and elements
that is different than the existing CHEBI. There are deep problems
with classification of atms and molecular entities in CHEBI. These
problems arise from a basic confusion about classes and
metaclasses. Sources like IUPAC represent chemical *species*,
instances of which are chemical *elements*, __NOT__ instances in the
OBO sense. This fundamental confusion means CHEBI does not work for
OBO.

The idea here is to provide a *schema* in which the instances are
classes in a chemical ontology. The schema could be thought of as an
ontology of metaclasses, but care must be taken here due to mixing of
different metamodel formalisms (this schema is closed-world and thus
not well represented in OWL).

The schema language used here is
[biolinkml](https://github.com/biolink/biolinkml/), which provides
powerful modeling framework that incorporates aspects of UML, ShEx,
and OWL, and is semantic-web ready.

The goal is to create instances of these schema classes
(e.g. carbon-14) which would be OWL classes, auto-populated with
standardized names and logical axioms. This could be done via a
compilation to dospd or robot, or direcly within the biolinkml
framework (see [this
issue](https://github.com/INCATools/dead_simple_owl_design_patterns/issues/51)
). TBD.

## Schema

Browse the schema here: [http://cmungall.github.io/chemistry-ontology](http://cmungall.github.io/chemistry-ontology)

See the [src/schema/](src/schema/) folder

The source is in YAML (biolinkml)

Currently the main derived artefacts of interest are:

 - [JSON Schema](src/schema/chemont.schema.json)
 - [ShEx](src/schema/chemont.shex)
 - [Python dataclasses](src/schema/chemont_datamodel.py)

## TODO

 - Python code to saturate metaclass instances based on chemical database (e.g. Wikidata)
 - align with chebi
 - Compilation down from biolinkml yaml to DOSDP or ROBOT - or custom OWLGen, e.g. using [funowl](https://github.com/hsolbrig/funowl)
