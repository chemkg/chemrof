"""Patch the ontology header of the gen-owl output.

Interim workaround for three gaps in the LinkML OWL generator (owlgen), as of
linkml 1.12.1. Delete this script once owlgen covers them:

  * the schema `version` is emitted only as pav:version; this adds
    owl:versionInfo, which registries and FAIR checkers look for
  * the schema `license` is emitted as a string literal; this turns it into
    an IRI when it is one
  * the owl:Ontology block lands wherever the serializer puts it (byte ~220k
    of ~360k for chemrof); this writes it first, because checkers such as
    SchemaScope read only the head of the artefact

Everything else in the header (title, description, source, see_also) comes
from the schema's own metadata.

Usage: python scripts/finalize_owl.py IN.owl.ttl OUT.owl.ttl --version 0.4.1
"""

import argparse

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF

ONTOLOGY_IRI = URIRef("https://w3id.org/chemrof")


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

    for lic in list(g.objects(ont, DCTERMS.license)):
        if isinstance(lic, Literal) and str(lic).startswith(("http://", "https://")):
            g.remove((ont, DCTERMS.license, lic))
            g.add((ont, DCTERMS.license, URIRef(str(lic))))

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
