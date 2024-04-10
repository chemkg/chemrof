# CHEMROF: Chemical Entities Mixtures Reactions Ontological Framework

GitHub: [chemkg/chemrof](https://github.com/chemkg/chemrof)

This project provides a LinkML schema/datamodel to represent chemical entities and other related entities.

It also includes as a proof of concept:

 - small database of entities conforming to the model
 - a translation of this database to an ontology (OWL TBox)

## Core Datamodel

Some example classes and their instances:

 - [Atoms](https://w3id.org/chemrof/Atom):
    - [Elements](https://w3id.org/chemrof/ChemicalElement): nickel atom, carbon atom, ...
    - [Monoatomic Ions](https://w3id.org/chemrof/MonoatomicIon): copper(2+), ...
    - [Isotopes](https://w3id.org/chemrof/Isotope): carbon-14, carbon-12, ...
    - [Fully Specified Atoms](https://w3id.org/chemrof/FullySpecifiedAtom): Helium-4(2+), ...
 - [Molecules](https://w3id.org/chemrof/Molecule):
    - [Enantiomers](https://w3id.org/chemrof/Enantiomer): L-serine
    - [Racemic Mixtures](https://w3id.org/chemrof/RacemicMixture): thalidomide, ...

Note that in a chemical ontology like CHEBI, concepts such as "nickel
atom" are treated as classes. In this primary chemrof representation,
they are instances, but can be later translated to OWL classes.

## Schema

The schema and overall framework uses [LinkML](https://linkml.io/linkml)

 * Browse the schema here: [http://chemkg.github.io/chemrof](http://chemkg.github.io/chemrof)
 * See the yaml source in the [src/schema](https://github.com/chemkg/chemrof/blob/master/src/schema) directory

### Schema Organization

The main division is between:

 * [ChemicalEntity](/ChemicalEntity/) - essentially things you can write a formula/inchi for, and
 * [GroupingClass](/GroupingClass/) - generalizations/sets of chemical entities

This distinction may be hard to grasp if you are coming from an OBO
realist ontologist philosophical perspective, but this in fact allows
us to serve a much wider variety of use cases than a strict OBO-style
approach. At the same time we can generate an OBO-style ontology from this representation

### Example

Enantiomers are mirror-image stereoisomers.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Thalidomide_enantiomers.svg/400px-Thalidomide_enantiomers.svg.png)

The [Enantiomer class](/Enantiomer) represents a chemical entity that has a form (e.g L/D) specified.

[Racemic mixtures](/Racemic mixture) are compounds with equal amounts left and right-handed enantiomers. 

=== "Schema"

    ```yaml
    racemic mixture:
      aliases:
        - racemate
        - racemic mixture of enantiomers
      is_a: precise chemical mixture
      description: >-
        a chemical compound that has equal amounts of left- and right-handed enantiomers of a chiral molecule. An example is Thalidomide
      slot_usage:
        has left enantiomer:
          required: true
          range: enantiomer
        has right enantiomer:
          required: true
          range: enantiomer
        chirality agnostic form:
          recommended: true
          required: false
          range: molecule
        IUPAC name:
          pattern: "^rac-"
      defining_slots:
        - has left enantiomer
        - has right enantiomer
      exact_mappings:
        - CHEBI:60911
        - NCIT:C103198
        - wdeschema:E47
        - wd:Q467717
        - goldbook:R05025
      see_also:
        - https://github.com/ebi-chebi/ChEBI/issues/3245
    ```

=== "Example Data (Turtle)"

    ```turtle
    ChemicalEntity:InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29%2Fs3
            a chem:RacemicMixture ;
            rdfs:label "thalidomide" ;
            chem:chebi_iri obo:CHEBI_9513 ;
            chem:chirality_agnostic_form ChemicalEntity:InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29 ;
            chem:has_left_enantiomer ChemicalEntity:InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29%2Ft9-%2Fm0%2Fs1 ;
            chem:has_right_enantiomer ChemicalEntity:InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29%2Ft9-%2Fm1%2Fs1 .
    ```

=== "Example Data (YAML)"

    ```yaml
      id: "ChemicalEntity:InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29%2Fs3"
      type: "RacemicMixture"
      label: "thalidomide"
      chebi_iri: "CHEBI:9513"
      chirality_agnostic_form: "ChemicalEntity:InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29"
      has_left_enantiomer: "ChemicalEntity:InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29%2Ft9-%2Fm0%2Fs1"
      has_right_enantiomer: "ChemicalEntity:InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%291
   ``````

=== "OWL (TBox)"

    ```xml
    <owl:Class rdf:about="https://w3id.org/chemrof/ChemicalEntity/InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29%2Fs3">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="https://w3id.org/chemrof/RacemicMixture"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="https://w3id.org/chemrof/chirality_agnostic_form"/>
                        <owl:someValuesFrom rdf:resource="https://w3id.org/chemrof/ChemicalEntity/InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29"/>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="https://w3id.org/chemrof/RacemicMixture"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="https://w3id.org/chemrof/has_left_enantiomer"/>
                        <owl:someValuesFrom rdf:resource="https://w3id.org/chemrof/ChemicalEntity/InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29%2Ft9-%2Fm0%2Fs1"/>
                    </owl:Restriction>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="https://w3id.org/chemrof/has_right_enantiomer"/>
                        <owl:someValuesFrom rdf:resource="https://w3id.org/chemrof/ChemicalEntity/InChI%3D1S%2FC13H10N2O4%2Fc16-10-6-5-9%2811%2817%2914-10%2915-12%2818%297-3-1-2-4-8%287%2913%2815%2919%2Fh1-4%2C9H%2C5-6H2%2C%28H%2C14%2C16%2C17%29%2Ft9-%2Fm1%2Fs1"/>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:subClassOf rdf:resource="https://w3id.org/chemrof/RacemicMixture"/>
        <rdfs:label>thalidomide</rdfs:label>
    </owl:Class>
    ```

Note that a class "Enantiomer" does not really make sense at an OBO level where all chemical entities are classes; it is a metaclass.

## Mappings

 - [SSSOM](https://github.com/chemkg/chemrof/tree/master/schema/sssom)

Example mappings:

|subject_id|subject_label|predicate_id|object_id|match_type|subject_source|
|---|---|---|---|---|---|
|chemrof:bond_type_enum#covalent|covalent|skos:exactMatch|gc:NormalBond|skos:exactMatch|https://w3id.org/chemrof|
|chemrof:bond_type_enum#aromatic|aromatic|skos:exactMatch|gc:AromaticBond|skos:exactMatch|https://w3id.org/chemrof|
|chemrof:element_metallic_classification#Metallic|Metallic|skos:exactMatch|damlpt:Metallic|skos:exactMatch|https://w3id.org/chemrof|
|chemrof:nanostructure_morphology_enum#nanotube|nanotube|skos:exactMatch|CHEBI:50796|skos:exactMatch|https://w3id.org/chemrof|
|chemrof:periodic_table_block_enum#s-block|s-block|skos:exactMatch|CHEBI:33674|skos:exactMatch|https://w3id.org/chemrof|
|chemrof:Enantiomer|enantiomer|skos:exactMatch|SIO:010777|skos:exactMatch|https://w3id.org/chemrof|


## Derived artefacts

Currently the main derived artefacts of interest are:

 - [JSON Schema](https://github.com/chemkg/chemrof/tree/master/schema/jsonschema)
 - [ShEx](https://github.com/chemkg/chemrof/tree/master/schema/shex)
 - [SHACL](https://github.com/chemkg/chemrof/tree/master/schema/shacl)

With care, you also see:

 - [OWL](https://github.com/chemkg/chemrof/tree/master/schema/owl) -- note this should be read as a meta-ontology by OBO people

## Comparison with CHEBI and Wikidata

TODO
