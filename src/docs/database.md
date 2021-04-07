# Database

This project is primarily intended to provide a standardized
[schema](../schema/) for rigorous data modeling of chemical entities.

However, we also include a partial (currently *very* partial) set of
entries in the database, ETL-ed from different sources.

The database can be found in the
[database](https://github.com/cmungall/chem-schema/tree/master/database)
section

## ETL

The ETL is largely driven by SPARQL CONSTRUCT queries. See the
[sparql](https://github.com/cmungall/chem-schema/tree/master/sparql)
folder and the Makefile.

Note so far we have only ETL'd a very small set of datatypes for proof of principles:

 - ChemicalElement
 - Isotope
 - MonoatomicIon

## Identifiers

Rather than using incremental IDs as in OBO, we aim to use InChi
strings as identifiers for almost all ChemicalEntity classes (except
for the Atom branch). This facilitates integration between different
sources - e.g. whether we ingest from chembl, pubchem, chebi, or
wikidata.

For the Atom branch, we use the standard symbols and nomenclature, e.g. Cu/2-

For the ChemicalGrouping branch, there is no appropriate InChi, since
these group chemical entities via abstraction. Here we use CHEBI IDs.

## Database file organization

The database is organized according to the schema. We will provide the
following formats:

 * RDF/Turtle (`.ttl`)
 * JSON-LD (`.jsonld)
 * CSVs (todo)
 * YAML (todo)
 * SQL dumps (todo)

Depending on the serialization, the data may be available in different
files, one file per class/table in the schema.

For example:

 * [ChemicalElement.ttl](https://github.com/cmungall/chem-schema/blob/master/database/wd/ChemicalElement.ttl) from WikiData

## Example

the file ChemicalElement.ttl is derived from Wikidata and includes instances such as:

```turtle
chem:MonoatomicIon/Mn a chem:ChemicalElement ;
        rdfs:label "manganese"@en ;
        chem:symbol "Mn" ;
        chem:atomic_number 25.0 .
```

This is referenced in instances in the file MonoatomicIon.ttl is derived from CHEBI, e.g:

```turtle
chem:MonoatomicIon/Mn/+4       rdf:type        chem:MonoatomicIon ;
        rdfs:label      "manganese(4+)" ;
        ns1:chebi_iri   CHEBI:25158 ;
        ns1:charge      4 ;
        ns1:has_element chem:Mn ;
        ns1:inchi_string        "InChI=1S/Mn/q+4"^^xsd:string .
```

Similarly the file Isotope.ttl references the elements:

```turtle
chem:MonoatomicIon/Mn a chem:Isotope ;
        rdfs:label "manganese-46m"@en ;
        chem:neutron_number 21.0 ;
        chem:has_element <https://w3id.org/chemschema/ChemicalElement/Mn> .
```


## Merged Database

We also provide a file
[all-merged.owl](https://github.com/cmungall/chem-schema/blob/master/database/all-merged.owl)
that contains both the schema (as owl classes) and data (as
instances).

This data can be transformed into a more OBO-like OWL file, see next section.
