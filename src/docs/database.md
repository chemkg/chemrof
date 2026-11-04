# Database

This project is primarily intended to provide a standardized
[schema](../schema/) for rigorous data modeling of chemical entities.

However, we also include a partial (*very* partial) set of exemplar
entries in the database, ETL-ed from different sources.

The database can be found in the
[database](https://github.com/chemkg/chemrof/tree/main/database)
directory of the GitHub repo.

## ETL

The files in `database/` were produced between 2021 and 2024 by a
pipeline of SPARQL CONSTRUCT queries against Wikidata and CHEBI. That
pipeline was retired in September 2026 (it lives on in git history as
`etl.mk` and `sparql/`), so the files are a frozen snapshot.

Only a very small set of types was ETL'd, as a proof of principle:

 - [ChemicalElement](ChemicalElement.md)
 - Isotope
 - MonoatomicIon

The current route from external data into chemrof instances is the
`chemrof convert` command, which builds instances from SMILES strings
and can enrich them from PubChem and ChemOnt; see the
[converter](converter.md) and [CLI](cli.md) pages.

## Identifiers

Rather than using numeric IDs as in OBO, we aim to use InChi
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

 * [ChemicalElement.ttl](https://github.com/chemkg/chemrof/blob/main/database/wd/ChemicalElement.ttl) from WikiData

## Example

the file ChemicalElement.ttl is derived from Wikidata and includes instances such as:

```turtle
chem:MonoatomicIon/Mn a chem:ChemicalElement ;
        rdfs:label "manganese"@en ;
        chem:symbol "Mn" ;
        chem:atomic_number 25.0 .
```

This is referenced in instances in the file MonoatomicIon.ttl, which is derived from CHEBI.
For example:

```turtle
chem:MonoatomicIon/Mn/+4       rdf:type        chem:MonoatomicIon ;
        rdfs:label      "manganese(4+)" ;
        chem:chebi_iri   CHEBI:25158 ;
        chem:charge      4 ;
        chem:has_element chem:Mn ;
        chem:inchi_string        "InChI=1S/Mn/q+4"^^xsd:string .
```

Similarly the file Isotope.ttl references the elements:

```turtle
chem:Isotope/Mn/21 a chem:Isotope ;
        rdfs:label "manganese-46m"@en ;
        chem:neutron_number 21.0 ;
        chem:has_element <https://w3id.org/chemrof/ChemicalElement/Mn> .
```


## Merged Database

The per-source files are merged into a single
[all.jsonld](https://github.com/chemkg/chemrof/blob/main/database/all.jsonld).

This data can be transformed into a more OBO-like OWL file, see the
[ontology](ontology.md) page.
