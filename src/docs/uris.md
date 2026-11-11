# URI Encoding of InChIs

CHEMROF uses [InChI](https://www.iupac.org/inchi) strings as the identifier for
individual chemical entities, so a valid entity IRI is the w3id.org base plus the
percent-encoded form of the InChI:

```text
https://w3id.org/chemrof/ChemicalEntity/<InChI percent-encoded>
```

Because an InChI contains characters such as `=`, `/`, `,`, `+`, `#` and `(`
that are not permitted in an IRI, they are percent-encoded using
[SPARQL `ENCODE_FOR_URI`](https://www.w3.org/TR/sparql11-query/#func-encode-for-uri).

## Example

Take the InChI for ascorbic acid (vitamin C):

```text
InChI=1S/C6H8O6/c7-1-2(8)5-3(9)4(10)6(11)12-5/h2,5,7-8,10-11H,1H2/t2-,5+/m0/s1
```

The following SPARQL query performs the encoding:

```sparql
SELECT ?x WHERE {
  BIND(ENCODE_FOR_URI('InChI=1S/C6H8O6/c7-1-2(8)5-3(9)4(10)6(11)12-5/h2,5,7-8,10-11H,1H2/t2-,5+/m0/s1') as ?x)
}
```

which returns the percent-encoded string:

```text
InChI%3D1S%2FC6H8O6%2Fc7-1-2%288%295-3%289%294%2810%296%2811%2912-5%2Fh2%2C5%2C7-8%2C10-11H%2C1H2%2Ft2-%2C5%2B%2Fm0%2Fs1
```

Note that `-`, `_` and `.` are left unencoded, as they are valid in an IRI path
segment.

Putting the two together gives the entity IRI:

```text
https://w3id.org/chemrof/ChemicalEntity/InChI%3D1S%2FC6H8O6%2Fc7-1-2%288%295-3%289%294%2810%296%2811%2912-5%2Fh2%2C5%2C7-8%2C10-11H%2C1H2%2Ft2-%2C5%2B%2Fm0%2Fs1
```

Decoding is the reverse operation: apply
[SPARQL `IRI`, `CONCAT` or percent-decoding](https://www.w3.org/TR/sparql11-query/#func-iri)
to recover the original InChI.
