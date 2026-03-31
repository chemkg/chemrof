"""chemrof CLI -- convert chemical structures to chemrof YAML/JSON/OWL."""

from __future__ import annotations

import json
from enum import Enum
from typing import Optional

import typer
import yaml

from chemrof.converter.convert import ChemConverter
from chemrof.converter.enrichers.base import get_enricher
from chemrof.converter.parse import parse_input

app = typer.Typer(
    name="chemrof",
    help="Chemical Entities, Materials, and Reactions Ontological Framework -- CLI tools.",
    no_args_is_help=True,
    invoke_without_command=True,
)


@app.callback()
def _main_callback() -> None:
    """chemrof CLI entry point."""


class OutputFormat(str, Enum):
    yaml = "yaml"
    json = "json"
    owl = "owl"


_ENRICHER_HELP = """Optionally pull extra data from external databases.

Pass a comma-separated list of source names. Available sources:

  pubchem   -- Look up the compound in PubChem by InChIKey.
               Fills in the preferred IUPAC name and PubChem CID.

  chebi     -- (stub) Will resolve CHEBI identifiers via OLS.

  wikidata  -- (stub) Will resolve Wikidata QIDs via SPARQL.

Example: --enrichers pubchem"""

_CLASSES_HELP = """Target chemrof classes to generate (hint-based).

Pass a comma-separated list. Supported: RacemicMixture, Enantiomer.
Implies --autochain. Requesting RacemicMixture automatically generates
Enantiomer entities and the chirality-agnostic form.

Example: --classes RacemicMixture"""


def _do_convert(
    inputs: list[str],
    format: OutputFormat,
    enrichers: Optional[str],
    classes: Optional[str],
    autochain: bool,
) -> None:
    """Shared implementation for convert and from-smiles commands."""
    enricher_instances = []
    if enrichers:
        for name in enrichers.split(","):
            enricher_instances.append(get_enricher(name.strip()))

    target_classes: set[str] = set()
    if classes:
        target_classes = {c.strip() for c in classes.split(",")}
        autochain = True

    converter = ChemConverter(enrichers=enricher_instances)

    all_results = []
    for raw in inputs:
        parsed = parse_input(raw)

        # Non-standard racemic InChI auto-triggers autochain
        if parsed.is_racemic:
            target_classes.add("RacemicMixture")
            autochain = True

        result = converter.convert_parsed(parsed)

        if autochain and target_classes:
            from chemrof.converter.autochain import autochain as do_autochain

            chain = do_autochain(result, target_classes, parsed.mol)
            all_results.extend(chain)
        else:
            all_results.append(result)

    if format == OutputFormat.owl:
        from chemrof.converter.owl_output import dicts_to_owl

        typer.echo(dicts_to_owl(all_results))
        return

    output = all_results if len(all_results) > 1 else all_results[0]

    if format == OutputFormat.json:
        typer.echo(json.dumps(output, indent=2))
    else:
        if isinstance(output, list):
            # Multi-document YAML
            typer.echo(yaml.dump_all(output, default_flow_style=False, sort_keys=False).rstrip())
        else:
            typer.echo(yaml.dump(output, default_flow_style=False, sort_keys=False).rstrip())


@app.command()
def convert(
    inputs: list[str] = typer.Argument(
        help="One or more SMILES or InChI strings.",
    ),
    format: OutputFormat = typer.Option(
        OutputFormat.yaml, "--format", "-f", help="Output format.",
    ),
    enrichers: Optional[str] = typer.Option(
        None, "--enrichers", "-e", help=_ENRICHER_HELP,
    ),
    classes: Optional[str] = typer.Option(
        None, "--classes", "-c", help=_CLASSES_HELP,
    ),
    autochain: bool = typer.Option(
        False, "--autochain", help="Generate interlinked dependent entities.",
    ),
):
    """Convert chemical inputs to chemrof data.

    Parses each input string (SMILES or InChI, auto-detected) with RDKit,
    classifies the entity type, and outputs chemrof-compliant records.

    Examples:

        chemrof convert CCO

        chemrof convert "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3" --format json

        chemrof convert "CC(N)C(=O)O" --classes RacemicMixture

        chemrof convert "[Ca+2]" --enrichers pubchem
    """
    _do_convert(inputs, format, enrichers, classes, autochain)


@app.command(hidden=True)
def from_smiles(
    smiles: list[str] = typer.Argument(
        help="One or more SMILES strings.",
    ),
    format: OutputFormat = typer.Option(
        OutputFormat.yaml, "--format", "-f", help="Output format.",
    ),
    enrichers: Optional[str] = typer.Option(
        None, "--enrichers", "-e", help=_ENRICHER_HELP,
    ),
):
    """(Deprecated) Convert SMILES to chemrof data. Use 'convert' instead."""
    _do_convert(smiles, format, enrichers, classes=None, autochain=False)
