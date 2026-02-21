# About this repo

This repo is for the chemrof schema. It is primarily a schema repo rather than code repo,
and code should be reviewed accordingly.

## LinkML Source

The source is here: `src/chemrof/schema/chemrof.yaml`

The source is in LinkML. Other formats like JSON-Schema are derived.

This should follow LinkML best practice

- new elements SHOULD have descriptions
- when creating a new class, we recommend adding an example to src/data/examples/valid
- enum permissible values should be linked to ontology terms via `meaning` where appropriate

## Example instances

Following LinkML best practice, this repo has examples in `src/data/examples/valid`. These all have the filename:

- `ClassName-instanceName.yaml`

The example should have all required slots filled in. Use web search if you are unsure of correct values.
ALWAYS run `make test-examples` after touching an example, iterating until it conforms to the schema.

