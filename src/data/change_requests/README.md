# Upstream change requests

This directory holds changes that chemrof asks external resources to make, written in
[KGCL](https://github.com/INCATools/kgcl) (Knowledge Graph Change Language). KGCL makes a
request exact: which term, which edge or annotation, and the old and new values.

There is one directory per resource, and one file per topic, e.g. `chebi/heme.kgcl`.

## Format

- One KGCL command per line.
- Blank lines and lines starting with `#` are comments. Use them to give the evidence for each
  command: what was checked, against which release, with which tool versions.
- A new term gets a placeholder ID of the form `CHEBI:NEW_<slug>`, created with
  `create node` in the same file before it is used.
- For ChEBI, `is_a` is `rdfs:subClassOf`, and structure annotations use the `chemrof:`
  predicates of ChEBI's ontology release (`chemrof:smiles_string`,
  `chemrof:generalized_empirical_formula`, ...).

This is the format `runoak apply --changes-format kgcl` reads. `tests/test_change_requests.py`
checks that every command parses, that runoak reads the same commands, and that every
placeholder ID is created in the file that uses it.

## Trying a change locally

`runoak apply` applies a file to a local copy of the ontology, for example an OBO extract:

```bash
uv run runoak -i simpleobo:extract.obo apply \
  --changes-input src/data/change_requests/chebi/heme.kgcl --changes-format kgcl -o patched.obo
```

oaklib (0.6.23) applies `create node`, `add definition` and `create edge`. No oaklib adapter
implements `change annotation` yet, so remove those lines before applying. They are still
valid KGCL, and the test still parses them.

## Workflow

1. Open an issue with the **Upstream change request** form. It records the evidence and
   impact. See [#101](https://github.com/chemkg/chemrof/issues/101) for an example.
2. If the change can be written in KGCL, add it to a file here in the same pull request as the
   work that found it, and link the issue in the file's header comment.
3. Forward the issue to the resource's own tracker, include the KGCL lines, and record the link
   in the issue.
4. When a release of the resource includes the change, delete the lines (or the file).

## What KGCL can't express

Some requests have no KGCL form. Describe them in the issue text only, and note them as
comments in the `.kgcl` file if they belong to the same topic:

- removing an annotation value, such as a structure that shouldn't be on a grouping class;
- rows in data tables, such as Rhea's `chebi_pH7_3_mapping.tsv`;
- defects in an export or API that affect many terms, such as
  [#101](https://github.com/chemkg/chemrof/issues/101).
