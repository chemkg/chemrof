"""chemrof CLI -- convert chemical structures to chemrof YAML/JSON."""

from __future__ import annotations

import json
from enum import Enum
from typing import Optional

import typer
import yaml

from chemrof.converter.convert import ChemConverter
from chemrof.converter.enrichers.base import get_enricher

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


@app.command()
def from_smiles(
    smiles: list[str] = typer.Argument(
        help="One or more SMILES strings (e.g. 'CCO' for ethanol, '[Ca+2]' for calcium ion).",
    ),
    format: OutputFormat = typer.Option(
        OutputFormat.yaml, "--format", "-f", help="Output format.",
    ),
    enrichers: Optional[str] = typer.Option(
        None,
        "--enrichers",
        "-e",
        help=_ENRICHER_HELP,
    ),
):
    """Convert SMILES to chemrof data.

    Parses each SMILES string with RDKit, auto-detects the entity type
    (SmallMolecule, AtomCation, MolecularAnion, etc.), and outputs a
    chemrof-compliant record with structural properties filled in:
    InChI, molecular formula, exact mass, and more.

    Examples:

        chemrof from-smiles CCO

        chemrof from-smiles CCO c1ccccc1 --format json

        chemrof from-smiles "[Ca+2]" --enrichers pubchem
    """
    enricher_instances = []
    if enrichers:
        for name in enrichers.split(","):
            name = name.strip()
            enricher_instances.append(get_enricher(name))

    converter = ChemConverter(enrichers=enricher_instances)

    results = []
    for smi in smiles:
        result = converter.convert(smi)
        results.append(result)

    if format == OutputFormat.owl:
        from chemrof.converter.owl_output import dicts_to_owl

        typer.echo(dicts_to_owl(results))
        return

    output = results if len(results) > 1 else results[0]

    if format == OutputFormat.json:
        typer.echo(json.dumps(output, indent=2))
    else:
        typer.echo(yaml.dump(output, default_flow_style=False, sort_keys=False).rstrip())
