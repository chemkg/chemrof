# Ontology Generation

The **primary objective** of this schema is to provide a data model for
representing chemical entities and their groupings, where these are
database instances, and to use this for aligning across different
chemical databases.

A **secondary objective** is to be able to generate an OBO-style ontology from the
data model, and to use this to help advance the development of CHEBI.

## Download OWL

The [ontology](https://github.com/chemkg/chemrof/tree/main/ontology)
folder on GitHub holds a proof-of-concept ontology generated in 2022
from the exemplar [database](database.md). It is a frozen snapshot: the
pipeline that produced it has been retired (see below).

## OWL generation

The basic idea is to transform instance data (where for example
`carbon` is an instance of the ChemicalElement class, and `carbon-12`
is an instance of the sibling Isotope class) into OWL classes, and to
use reasoning to classify.

This is done with [linkml-owl](https://linkml.io/linkml-owl): the
`chemrof convert` command produces instances from SMILES and can emit
them as OWL with `--format owl` (see the [CLI reference](cli.md)).
Classes carrying an `owl.template` annotation in the schema
(MonoatomicIon, Enantiomer, RacemicMixture) become `EquivalentClasses`
axioms; other classes produce annotation assertions.

An earlier pipeline (2021–2024) reached the same result with SPARQL
CONSTRUCT queries run over an ETL'd instance database. It was retired
in September 2026 and can be found in git history (`etl.mk`,
`sparql/owlgen/`).

## Example

Mn(+4) is represented in the database as an individual of type MonoatomicIon

```turtle
chem:MonoatomicIon/Mn/+4       rdf:type        chem:MonoatomicIon ;
        rdfs:label      "manganese(4+)" ;
        ns1:chebi_iri   CHEBI:25158 ;
        ns1:charge      4 ;
        ns1:has_element chem:Mn ;
        ns1:inchi_string        "InChI=1S/Mn/q+4"^^xsd:string .
```

This is translated to class-level (via the `owl.template` annotation on MonoatomicIon):

```turtle
chem:MonoatomicIon/Mn/+4
        a                    owl:Class ;
        rdfs:label           "manganese(4+)" ;
        owl:equivalentClass
              [ owl:intersectionOf
                          ( chem:ChemicalElement/Mn
                            [ a               owl:Restriction ;
                              owl:hasValue    4 ;
                              owl:onProperty  chem:charge
                            ]
                          ) ] .
```

This will autoclassify to "manganese ion" etc

here is an example of the atom hierarchy in protege, showing automatic classification:

![image](https://user-images.githubusercontent.com/50745/113934643-de047280-97aa-11eb-859a-5c3650871cb5.png)


## Two-level representation

One thing that may seem unintuitive is that *instances* at the LinkML level are *classes* at the OBO level. This is illustrated here:

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTtQv4MLicg0nW1ehl7v9-ga3OCDB8Cr4Pf7M8B-YkvEoaUypuOYRSqqDCavADIr28KlZ6TwatcqQV_/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Relationship to templating systems

One way to view this project is:

 - the schema is a hierarchical collection of DOSDP templates or ROBOT templates
 - the database are the TSVs/spreadsheets that are inputs to the templates to generate OWL

Using LinkML as the modeling system provides some advantages. Rather
than a collection of denormalized tables, the inputs to the OWL
generation are objects/instances/rows conforming to a full object
model/schema, allowing for both rigorous modeling and powerful programmatic transformations.
