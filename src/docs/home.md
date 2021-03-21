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

## Schema

Browse the schema here: [http://cmungall.github.io/chem-schema](http://cmungall.github.io/chem-schema)

The main division in the schema is between chemical *entities* and
chemical *groupings*. this distinction may be hard to grasp if you are
coming from an OBO realist ontologist philosophical perspective, but
this in fact allows us to serve a much wider variety of use cases than
a strict OBO-style approach.

See the [src/schema/](https://github.com/cmungall/chem-schema/tree/master/src/schema) folder

The source is in YAML (biolinkml)

Currently the main derived artefacts of interest are:

 - [JSON Schema](https://github.com/cmungall/chem-schema/tree/master/jsonschema)
 - [ShEx](https://github.com/cmungall/chem-schema/tree/master/shex)
 - [Python dataclasses](https://github.com/cmungall/chem-schema/tree/master/python)

With care, you also see:

 - [OWL](https://github.com/cmungall/chem-schema/tree/master/owl) -- note this should be read as a meta-ontology by OBO people

Schema: [chem-schema](http://cmungall.github.io/chem-schema)



## TODO

 - map slots to wikidata properties
 - Python code to saturate metaclass instances based on chemical database (e.g. Wikidata)
 - align with chebi
 - Add logical rules
 - Compilation down from biolinkml yaml to DOSDP or ROBOT - or custom OWLGen, e.g. using [funowl](https://github.com/hsolbrig/funowl)
