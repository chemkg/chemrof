# Ontology Generation

The **primary objective** of this schema is to provide a data model for
representing chemical entities and their groupings, where these are
database instances, and to use this for aligning across different
chemical databases.

A **secondary objective** is to be able to generate an ontology from the
datamodel, and to use this to help advance the development of CHEBI.


## OWL generation

See
[Makefile.etl](https://github.com/cmungall/chem-schema/tree/master/Makefile.etl)
for specific details.

The basic idea is to transform the turtle instance data (where for
example `carbon` is an instance of the ChemicalElement class, and
`carbon-12` is an instance of the sibling Isotope class) into classes,
and to use reasoning to classify.

Currently this is done via SPARQL construct but later this will be
done by generating equivalence axioms from compound keys in the
database.

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

This is translated to class-level:

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
