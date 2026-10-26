"""Post-process the gen-owl output so the ontology header is machine-findable.

gen-owl writes the owl:Ontology block wherever rdflib's serializer puts it,
which for chemrof is near the end of a ~330 KB file, and it records the
version only as pav:version. Registries and FAIR checkers (e.g. SchemaScope)
read just the head of the artefact and look for owl:versionInfo /
owl:versionIRI, so they report the version as "not declared inside the
artefact".

This script:
  * adds owl:versionInfo (and keeps pav:version) for the given version
  * turns the dcterms:license literal into an IRI
  * adds homepage / source repository metadata
  * writes the ontology header block first, followed by the rest of the graph

Usage: python scripts/finalize_owl.py IN.owl.ttl OUT.owl.ttl --version 0.4.1
"""

import argparse

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import DCTERMS, FOAF, OWL, RDF

ONTOLOGY_IRI = URIRef("https://w3id.org/chemrof")
LICENSE = URIRef("https://creativecommons.org/publicdomain/zero/1.0/")
HOMEPAGE = URIRef("https://chemkg.github.io/chemrof")
REPOSITORY = URIRef("https://github.com/chemkg/chemrof")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    g = Graph()
    g.parse(args.input, format="turtle")

    ont = ONTOLOGY_IRI
    if (ont, RDF.type, OWL.Ontology) not in g:
        raise SystemExit(f"{args.input}: no owl:Ontology {ont}")

    version = args.version.lstrip("v")
    pav_version = URIRef("http://purl.org/pav/version")
    g.remove((ont, pav_version, None))
    g.add((ont, pav_version, Literal(version)))
    g.remove((ont, OWL.versionInfo, None))
    g.add((ont, OWL.versionInfo, Literal(version)))
    g.remove((ont, DCTERMS.license, None))
    g.add((ont, DCTERMS.license, LICENSE))
    g.add((ont, FOAF.homepage, HOMEPAGE))
    g.add((ont, DCTERMS.source, REPOSITORY))

    header = Graph(namespace_manager=g.namespace_manager)
    for triple in g.triples((ont, None, None)):
        header.add(triple)
    body = Graph(namespace_manager=g.namespace_manager)
    for triple in g:
        if triple[0] != ont:
            body.add(triple)

    # Turtle allows repeated @prefix declarations, so the two serializations
    # concatenate into one valid document with the header first.
    with open(args.output, "w") as out:
        out.write(header.serialize(format="turtle"))
        out.write("\n")
        out.write(body.serialize(format="turtle"))


if __name__ == "__main__":
    main()
