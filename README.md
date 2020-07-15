# Chemical Ontology Metaclasses

This repo includes schema/datamodel for a chemical ontology

Instances of the classes in the data model are chemical ontology classes, e.g.

 - nickel atom
 - nickel anion
 - carbon 14

See

 - https://docs.google.com/presentation/d/1xCHnJqGp_8jb8Btf6-JX5M_pt5j1NFiYhQFMASFanGM/edit

For driving use case see:

 - https://github.com/EnvironmentOntology/envo/issues/989

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
 - Compilation down from biolinkml yaml to DOSDP or ROBOT - or custom OWLGen, e.g. using owlgen
