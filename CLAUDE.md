# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## LinkML Source

The source is here: `src/chemrof/schema/chemrof.yaml`

DO NOT edit other files in src/chemrof/schema, these are all auto-generated from the yaml, as is standard for LinkML repos.

## Build & Development Commands
- `make gen` - Generate all project files from schema (equivalent to `make project`)
- `make test` - Run tests on examples (equivalent to `make gen test-examples`)
- `make gendoc` - generate markdown docs in `docs/`. These might be useful to explore the schema

## Example instances

Following LinkML best practice, this repo has examples in `src/data/examples/valid`. These all have the filename:

- `ClassName-instanceName.yaml`

The example should have all required slots filled in. Use web search if you are unsure of correct values.
ALWAYS run `make test-examples` after touching an example, iterating until it conforms to the schema.


## Useful yq Queries for Schema Analysis

The source is quite large so you may want to use tools like `yq` and `grep` to find things of interest.

- `yq '.classes | keys | length' src/chemrof/schema/chemrof.yaml` - Count total classes
- `yq '.classes | to_entries | map(select(.value.description == null)) | .[].key' src/chemrof/schema/chemrof.yaml` - Find classes without descriptions
- `yq '.classes.ClassName.description' src/chemrof/schema/chemrof.yaml` - Read a specific class description
- `yq '.classes.ClassName.description = "New description"' -i src/chemrof/schema/chemrof.yaml` - Add/update description

## Using the docs for search

This schema makes use of a lot of linkml features like inheritance. This means that you need to follow
class hierarchies to see applicable slots. The generated markdown docs materialized everything, to make it easier
for humans (and AIs like yourself). Run `make gendoc` to generate `docs/*.md`. These can be examined like any
other markdown. Do not edit these

## Schema Editing Workflow Comparison

### For Adding Class Descriptions:

**Direct YAML Editing (Recommended for single edits):**
1. Use `grep -n "^  ClassName:" src/chemrof/schema/chemrof.yaml` to find line number
2. Use Read tool to view the class structure 
3. Use Edit tool to add description field with proper indentation
4. ✅ Pros: Precise control, maintains formatting, easy to see context
5. ❌ Cons: Manual for each class

**yq Approach (Better for bulk operations):**
1. Use `yq '.classes.ClassName.description = "Description text"' -i file.yaml`
2. ✅ Pros: Good for scripting, bulk operations
3. ❌ Cons: Less precise formatting control

**Best Practice:** Use direct editing for careful, one-by-one additions. Use yq for discovery and bulk operations.

## Creating Examples - Lessons Learned

When creating examples for ionic species:

1. **Use `elemental_charge` not `charge`**: The schema uses `elemental_charge` as the slot name for ionic charge values
2. **Match filename to type**: Example filenames must match the declared type (e.g., `MonoatomicIon-copper2.yaml` requires `type: chemrof:MonoatomicIon`)
4. **Use web search for chemical data**: Search for CHEBI IDs and chemical properties to ensure accurate example data
5. 

## Common Schema Investigation Commands
- `grep -A 20 "ClassName:" schema.yaml` - See class definition with slots
- `grep -A 10 -B 5 "SlotName:" schema.yaml` - Find slot definitions
- Use `grep` to find mixins and inheritance relationships before creating examples (or look at generated docs)

