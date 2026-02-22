"""chemrof CLI -- convert chemical structures to chemrof YAML/JSON."""

from __future__ import annotations

import json
from enum import Enum
from typing import Optional

import typer
import yaml

from chemrof.converter.smiles import SmilesConverter
from chemrof.converter.enrichers.base import get_enricher, list_enrichers

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


@app.command()
def from_smiles(
    smiles: list[str] = typer.Argument(help="One or more SMILES strings to convert."),
    format: OutputFormat = typer.Option(OutputFormat.yaml, "--format", "-f", help="Output format."),
    enrichers: Optional[str] = typer.Option(
        None,
        "--enrichers",
        "-e",
        help="Comma-separated enricher names.",
    ),
):
    """Convert SMILES strings to chemrof-compliant YAML or JSON."""
    enricher_instances = []
    if enrichers:
        for name in enrichers.split(","):
            name = name.strip()
            enricher_instances.append(get_enricher(name))

    converter = SmilesConverter(enrichers=enricher_instances)

    results = []
    for smi in smiles:
        result = converter.convert(smi)
        results.append(result)

    output = results if len(results) > 1 else results[0]

    if format == OutputFormat.json:
        typer.echo(json.dumps(output, indent=2))
    else:
        typer.echo(yaml.dump(output, default_flow_style=False, sort_keys=False).rstrip())
