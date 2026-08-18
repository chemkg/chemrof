"""chemrof CLI -- convert chemical structures to chemrof YAML/JSON/OWL."""

from __future__ import annotations

import json
import tempfile
from enum import Enum
from pathlib import Path
from typing import Optional

import typer
import yaml

from chemrof.converter.convert import ChemConverter
from chemrof.converter.enrichers.base import get_enricher
from chemrof.converter.enrichers.chemont import (
    ChemOntEnricher,
    build_chemont_duckdb,
    build_chemont_parquet,
    download_chemont_zenodo,
)
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

  chemont   -- Look up ClassyFire/ChemOnt labels by InChIKey from a
               local DuckDB, Parquet, or TSV source and fills classified_by.

  openclatura -- Derive a systematic IUPAC name locally from the structure
               (no network). Fills IUPAC_name. Requires `pip install openclatura`.

  chebi     -- (stub) Will resolve CHEBI identifiers via OLS.

  wikidata  -- (stub) Will resolve Wikidata QIDs via SPARQL.

Example: --enrichers pubchem"""

_CLASSES_HELP = """Target chemrof classes to generate (hint-based).

Pass a comma-separated list. Supported: RacemicMixture, Enantiomer, ChemicalSalt, Tautomer.
Implies --autochain. Requesting RacemicMixture automatically generates
Enantiomer entities and the chirality-agnostic form. ChemicalSalt decomposes
a salt into its cation and anion components. Tautomer enumerates tautomeric
forms and links them via tautomer_of.

Example: --classes RacemicMixture"""


def _do_convert(
    inputs: list[str],
    format: OutputFormat,
    enrichers: Optional[str],
    classes: Optional[str],
    autochain: bool,
    chemont_source: Optional[Path] = None,
    chemont_dictionary: Optional[Path] = None,
) -> None:
    """Shared implementation for convert and from-smiles commands."""
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

    target_classes: set[str] = set()
    if classes:
        target_classes = {c.strip() for c in classes.split(",")}
        autochain = True

    # Don't pass enrichers to converter — we run them after autochain
    # so that generated entities also get enriched
    converter = ChemConverter()

    all_results = []
    for raw in inputs:
        parsed = parse_input(raw)

        # Non-standard racemic InChI auto-triggers autochain
        if parsed.is_racemic:
            target_classes.add("RacemicMixture")
            autochain = True

        result = converter.convert_parsed(parsed)

        # Salt input auto-triggers autochain
        if result.get("type") == "chemrof:ChemicalSalt":
            target_classes.add("ChemicalSalt")
            autochain = True

        if autochain and target_classes:
            from chemrof.converter.autochain import autochain as do_autochain

            chain = do_autochain(result, target_classes, parsed.mol)
            all_results.extend(chain)
        else:
            all_results.append(result)

    # Run enrichers on all entities (including autochain-generated ones)
    if enricher_instances:
        from chemrof.converter.enrichers.base import EnrichmentContext

        for i, obj in enumerate(all_results):
            inchikey = obj.get("id", "").replace("INCHIKEY:", "")
            context = EnrichmentContext(
                mol=None,
                inchikey=inchikey if obj.get("id", "").startswith("INCHIKEY:") else "",
                smiles=obj.get("smiles_string", ""),
                inchi=obj.get("inchi_string", ""),
            )
            for enricher in enricher_instances:
                obj = enricher.enrich(obj, context)
            all_results[i] = obj

        # Update RacemicMixture names from agnostic form's enriched name
        for obj in all_results:
            if obj.get("type") == "chemrof:RacemicMixture":
                agnostic_id = obj.get("chirality_agnostic_form")
                agnostic = next(
                    (r for r in all_results if r["id"] == agnostic_id), None
                )
                if agnostic and agnostic.get("name") != agnostic.get("empirical_formula"):
                    obj["name"] = f"rac-{agnostic['name']}"

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
    """Convert chemical inputs to chemrof data.

    Parses each input string (SMILES or InChI, auto-detected) with RDKit,
    classifies the entity type, and outputs chemrof-compliant records.

    Examples:

        chemrof convert CCO

        chemrof convert "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3" --format json

        chemrof convert "CC(N)C(=O)O" --classes RacemicMixture

        chemrof convert "[Ca+2]" --enrichers pubchem
    """
    _do_convert(
        inputs,
        format,
        enrichers,
        classes,
        autochain,
        chemont_source=chemont_source,
        chemont_dictionary=chemont_dictionary,
    )


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
    """(Deprecated) Convert SMILES to chemrof data. Use 'convert' instead."""
    _do_convert(
        smiles,
        format,
        enrichers,
        classes=None,
        autochain=False,
        chemont_source=chemont_source,
        chemont_dictionary=chemont_dictionary,
    )


@app.command(name="convert-maud")
def convert_maud(
    input: Path = typer.Argument(
        help="A Maud kinetic-model TOML file, or a Maud config.toml that "
        "references one via 'kinetic_model_file'.",
    ),
    format: OutputFormat = typer.Option(
        OutputFormat.yaml, "--format", "-f", help="Output format (yaml or json).",
    ),
    output: Optional[Path] = typer.Option(
        None, "--output", "-o", help="Write to a file instead of stdout.",
    ),
):
    """Convert a Maud kinetic model (TOML) into a chemrof Collection.

    Maps metabolites to SmallMolecule (keyed by InChIKey), reactions to Reaction
    with left/right ReactionParticipants, the reaction mechanism, and any
    allosteric / competitive-inhibition regulation. Bayesian priors and
    experiment measurements are not part of this structural mapping.

    Example:

        chemrof convert-maud data/methionine/methionine_cycle.toml
    """
    from chemrof.converter.maud import MaudConverter

    if format == OutputFormat.owl:
        raise typer.BadParameter("convert-maud supports only yaml or json output.")

    collection = MaudConverter().convert_file(input)
    if format == OutputFormat.json:
        text = json.dumps(collection, indent=2)
    else:
        text = yaml.safe_dump(collection, sort_keys=False)

    if output is not None:
        output.write_text(text)
    else:
        typer.echo(text)


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


@app.command()
def prepare_chemont_from_zenodo(
    output: Path = typer.Argument(
        help="Output DuckDB file or Parquet directory.",
    ),
    format: ChemOntStoreFormat = typer.Option(
        ChemOntStoreFormat.duckdb,
        "--format",
        "-f",
        help="Storage format to create.",
    ),
    download_dir: Optional[Path] = typer.Option(
        None,
        "--download-dir",
        help="Directory for downloaded Zenodo files. Defaults to a temporary directory.",
    ),
    overwrite: bool = typer.Option(
        False,
        "--overwrite",
        help="Replace an existing output and re-download existing files.",
    ),
):
    """Download the ChemOnt Zenodo release and prepare a local lookup store."""
    if download_dir is None:
        with tempfile.TemporaryDirectory(prefix="chemrof-chemont-") as temp_dir:
            _prepare_downloaded_chemont(
                Path(temp_dir),
                output,
                format=format,
                overwrite=overwrite,
            )
        return

    _prepare_downloaded_chemont(
        download_dir,
        output,
        format=format,
        overwrite=overwrite,
    )


def _prepare_downloaded_chemont(
    download_dir: Path,
    output: Path,
    *,
    format: ChemOntStoreFormat,
    overwrite: bool,
) -> None:
    labels_path, dictionary_path = download_chemont_zenodo(
        download_dir,
        overwrite=overwrite,
    )
    if format == ChemOntStoreFormat.duckdb:
        path = build_chemont_duckdb(
            labels_path,
            dictionary_path,
            output,
            overwrite=overwrite,
        )
        typer.echo(str(path))
        return

    labels_parquet, dictionary_parquet = build_chemont_parquet(
        labels_path,
        dictionary_path,
        output,
        overwrite=overwrite,
    )
    typer.echo(str(labels_parquet))
    typer.echo(str(dictionary_parquet))
