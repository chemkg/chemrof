# Chem: Schema for chemistry data models and ontologies

GitHub: [cmungall/chem-schema](https://github.com/cmungall/chem-schema)

This repo includes schema/datamodel for a chemical ontology

Instances of the classes in the data model are chemical ontology classes, e.g.

 - nickel atom
 - nickel anion
 - carbon 14
 - nitrate
 - L-serine

Preliminary slides showing the idea:

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTtQv4MLicg0nW1ehl7v9-ga3OCDB8Cr4Pf7M8B-YkvEoaUypuOYRSqqDCavADIr28KlZ6TwatcqQV_/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Basic idea

We need an alternative classification of chemical atoms and elements
that is different than the existing CHEBI. There are deep problems
with classification of atoms and molecular entities in CHEBI. These
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

Browse the schema here: [http://cmungall.github.io/chem-schema](http://cmungall.github.io/chem-schema)

Realist pedants be advised to assume the suffix 'species', 'class', or 'type' on the end of these (meta)class names

See the [src/schema/](https://github.com/cmungall/chem-schema/tree/master/src/schema) folder

The source is in YAML (biolinkml)

Currently the main derived artefacts of interest are:

 - [JSON Schema](https://github.com/cmungall/chem-schema/tree/master/jsonschema)
 - [ShEx](https://github.com/cmungall/chem-schema/tree/master/shex)
 - [Python dataclasses](https://github.com/cmungall/chem-schema/tree/master/python)

With care, you also see:

 - [OWL](https://github.com/cmungall/chem-schema/tree/master/owl) -- note this should be read as a meta-ontology by OBO people

## Motivation

For driving use case and why we need aan alternatibe to existing chebi atom / simple molecule representation see:

 - https://github.com/EnvironmentOntology/envo/issues/989

Schema: [chem-schema](http://cmungall.github.io/chem-schema)



## TODO

 - map slots to wikidata properties
 - Python code to saturate metaclass instances based on chemical database (e.g. Wikidata)
 - align with chebi
 - Add logical rules
 - Compilation down from biolinkml yaml to DOSDP or ROBOT - or custom OWLGen, e.g. using [funowl](https://github.com/hsolbrig/funowl)
