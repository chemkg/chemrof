"""chemrof CLI -- convert chemical structures to chemrof YAML/JSON."""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from typing import Optional

import typer
import yaml

from chemrof.converter.enrichers.chemont import (
    ChemOntEnricher,
    build_chemont_duckdb,
    build_chemont_parquet,
)
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
    owl = "owl"


_ENRICHER_HELP = """Optionally pull extra data from external databases.

Pass a comma-separated list of source names. Available sources:

  pubchem   -- Look up the compound in PubChem by InChIKey.
               Fills in the preferred IUPAC name and PubChem CID.

  chemont   -- Look up ClassyFire/ChemOnt labels by InChIKey from a
               local DuckDB, Parquet, or TSV source and fills classified_by.

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
    chemont_source: Optional[Path] = typer.Option(
        None,
        "--chemont-source",
        help="Local ChemOnt labels source: indexed DuckDB, Parquet, or Zenodo TSV/ZST.",
    ),
    chemont_dictionary: Optional[Path] = typer.Option(
        None,
        "--chemont-dictionary",
        help="Local ChemOnt dictionary TSV/Parquet, required unless bundled in the DuckDB.",
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
            if name == "chemont":
                enricher_instances.append(
                    ChemOntEnricher(
                        source=chemont_source,
                        dictionary_source=chemont_dictionary,
                    )
                )
            else:
                enricher_instances.append(get_enricher(name))

    converter = SmilesConverter(enrichers=enricher_instances)

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


class ChemOntStoreFormat(str, Enum):
    duckdb = "duckdb"
    parquet = "parquet"


@app.command()
def prepare_chemont(
    enriched_tsv: Path = typer.Argument(
        help="Zenodo classyfire_dedup_inchikey_smiles.enriched.tsv.zst or TSV file.",
    ),
    dictionary_tsv: Path = typer.Argument(
        help="Zenodo chemont_dictionary.tsv file.",
    ),
    output: Path = typer.Argument(
        help="Output DuckDB file or Parquet directory.",
    ),
    format: ChemOntStoreFormat = typer.Option(
        ChemOntStoreFormat.duckdb,
        "--format",
        "-f",
        help="Storage format to create.",
    ),
    overwrite: bool = typer.Option(
        False,
        "--overwrite",
        help="Replace an existing output file.",
    ),
):
    """Prepare the ClassyFire/ChemOnt Zenodo table for fast local lookups."""
    if format == ChemOntStoreFormat.duckdb:
        path = build_chemont_duckdb(
            enriched_tsv,
            dictionary_tsv,
            output,
            overwrite=overwrite,
        )
        typer.echo(str(path))
        return

    labels_path, dictionary_path = build_chemont_parquet(
        enriched_tsv,
        dictionary_tsv,
        output,
        overwrite=overwrite,
    )
    typer.echo(str(labels_path))
    typer.echo(str(dictionary_path))
