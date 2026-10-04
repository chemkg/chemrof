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
from chemrof.converter.saturate import DEFAULT_GENERATORS
from chemrof.converter.siblings import DEFAULT_MAX_SIBLINGS

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

  chebi     -- Resolve atoms, monoatomic ions and isotopes to CHEBI ids
               (offline, from a bundled table). Replaces id and name.
               Other entity types are left unchanged.

  wikidata  -- (stub) Will resolve Wikidata QIDs via SPARQL.

Example: --enrichers pubchem"""

_CLASSES_HELP = """Target chemrof classes to generate (hint-based).

Pass a comma-separated list. Supported: RacemicMixture, Enantiomer, ChemicalSalt, Tautomer.
Implies --autochain. Requesting RacemicMixture automatically generates
Enantiomer entities and the chirality-agnostic form. ChemicalSalt decomposes
a salt into its cation and anion components. Tautomer enumerates tautomeric
forms and links them via tautomer_of.

Example: --classes RacemicMixture"""


_SIBLINGS_HELP = """Also generate the input's siblings.

For an atom (neutral, ion or isotope): every species of that element -- neutral
atom, naturally occurring isotopes, and the ions and isotopes known to ChEBI.
For a molecule with stereo elements: the stereo-agnostic parent and all
stereoisomers (Enantiomer when chiral, Stereoisomer otherwise), with each
mirror-image pair grouped as a RacemicMixture. Cannot be combined with
--classes or --autochain."""


def _do_convert(
    inputs: list[str],
    format: OutputFormat,
    enrichers: Optional[str],
    classes: Optional[str],
    autochain: bool,
    chemont_source: Optional[Path] = None,
    chemont_dictionary: Optional[Path] = None,
    siblings: bool = False,
    max_siblings: int = DEFAULT_MAX_SIBLINGS,
) -> None:
    """Shared implementation for convert and from-smiles commands."""
    if siblings and (classes or autochain):
        raise typer.BadParameter("--siblings cannot be combined with --classes or --autochain")
    enricher_instances = _build_enrichers(enrichers, chemont_source, chemont_dictionary)

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

        if siblings:
            from chemrof.converter.siblings import siblings as make_siblings

            all_results.extend(make_siblings(result, parsed.mol, max_siblings))
            continue

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
    _run_enrichers(all_results, enricher_instances)

    _emit(all_results, format)


def _build_enrichers(
    enrichers: Optional[str],
    chemont_source: Optional[Path] = None,
    chemont_dictionary: Optional[Path] = None,
) -> list:
    instances = []
    for name in (enrichers or "").split(","):
        name = name.strip()
        if not name:
            continue
        if name == "chemont":
            instances.append(
                ChemOntEnricher(source=chemont_source, dictionary_source=chemont_dictionary)
            )
        else:
            instances.append(get_enricher(name))
    return instances


def _run_enrichers(all_results: list[dict], enricher_instances: list) -> None:
    """Enrich every entity in place, keeping cross-references valid."""
    if not enricher_instances:
        return
    from chemrof.converter.enrichers.base import EnrichmentContext, rewrite_references

    id_remap: dict[str, str] = {}
    for i, obj in enumerate(all_results):
        old_id = obj.get("id", "")
        inchikey = old_id.replace("INCHIKEY:", "")
        context = EnrichmentContext(
            mol=None,
            inchikey=inchikey if obj.get("id", "").startswith("INCHIKEY:") else "",
            smiles=obj.get("smiles_string", ""),
            inchi=obj.get("inchi_string", ""),
        )
        for enricher in enricher_instances:
            obj = enricher.enrich(obj, context)
        all_results[i] = obj
        if obj.get("id") != old_id:
            id_remap[old_id] = obj["id"]

    # An enricher may have replaced ids (e.g. InChIKey -> CHEBI); keep links intact
    rewrite_references(all_results, id_remap)

    # Update RacemicMixture names from agnostic form's enriched name
    by_id = {r["id"]: r for r in all_results}
    for obj in all_results:
        if obj.get("type") == "chemrof:RacemicMixture":
            agnostic = by_id.get(obj.get("chirality_agnostic_form"))
            if agnostic and agnostic.get("name") != agnostic.get("empirical_formula"):
                obj["name"] = f"rac-{agnostic['name']}"


def _emit(all_results: list[dict], format: OutputFormat, output: Optional[Path] = None) -> None:
    """Write entities as YAML, JSON or OWL to *output* (stdout if None)."""

    def write(text: str) -> None:
        if output is None:
            typer.echo(text)
        else:
            output.write_text(text + "\n")

    if format == OutputFormat.owl:
        from chemrof.converter.owl_output import dicts_to_owl

        write(dicts_to_owl(all_results))
        return

    data = all_results if len(all_results) > 1 else all_results[0]

    if format == OutputFormat.json:
        write(json.dumps(data, indent=2))
    elif isinstance(data, list):
        # Multi-document YAML
        write(yaml.dump_all(data, default_flow_style=False, sort_keys=False).rstrip())
    else:
        write(yaml.dump(data, default_flow_style=False, sort_keys=False).rstrip())


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
    siblings: bool = typer.Option(False, "--siblings", help=_SIBLINGS_HELP),
    max_siblings: int = typer.Option(
        DEFAULT_MAX_SIBLINGS,
        "--max-siblings",
        min=1,
        help="With --siblings, the most stereoisomers to generate for one molecule.",
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

        chemrof convert "[Fe]" --siblings --enrichers chebi

        chemrof convert "CC(O)C(C)O" --siblings
    """
    _do_convert(
        inputs,
        format,
        enrichers,
        classes,
        autochain,
        chemont_source=chemont_source,
        chemont_dictionary=chemont_dictionary,
        siblings=siblings,
        max_siblings=max_siblings,
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


def _read_seeds(path: Path) -> list[dict]:
    """Read seed structures: one per line, ``structure[<TAB>name[<TAB>id]]``.

    Blank lines and lines starting with ``#`` are skipped. ``-`` reads stdin.
    """
    import sys

    text = sys.stdin.read() if str(path) == "-" else path.read_text()
    seeds = []
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        fields = line.rstrip("\n").split("\t")
        seed = {"structure": fields[0].strip()}
        if len(fields) > 1 and fields[1].strip():
            seed["name"] = fields[1].strip()
        if len(fields) > 2 and fields[2].strip():
            seed["id"] = fields[2].strip()
        seeds.append(seed)
    return seeds


_GENERATORS_HELP = """Comma-separated generators to saturate under.

  stereo       stereo-agnostic parent, stereoisomers and racemates of a
               molecule; neutral atom, isotopes and ions of an element
  salt         cationic and anionic components of a salt
  protonation  uncharged parent and pH 7.3 major microspecies, linked by
               has_major_microspecies_at_pH7_3 (and conjugate_acid_of /
               conjugate_base_of or tautomer_of where one step apart)
  tautomer     RDKit-enumerated tautomers (off by default; grows fast)"""


@app.command()
def saturate(
    seeds: Path = typer.Argument(
        help="File of seed structures, one SMILES or InChI per line, optionally "
        "followed by a tab and a name and a tab and an id to use (e.g. CHEBI:16977). '-' for stdin.",
    ),
    generators: str = typer.Option(
        ",".join(DEFAULT_GENERATORS), "--generators", "-g", help=_GENERATORS_HELP,
    ),
    max_entities: int = typer.Option(
        100_000, "--max-entities", min=1, help="Stop expanding past this many entities.",
    ),
    max_rounds: Optional[int] = typer.Option(
        None, "--max-rounds", min=0, help="Stop this many generations from the seeds "
        "(default: run to fixpoint).",
    ),
    max_siblings: int = typer.Option(
        DEFAULT_MAX_SIBLINGS, "--max-siblings", min=1,
        help="The most stereoisomers to generate for one molecule.",
    ),
    workers: int = typer.Option(
        1, "--workers", "-w", min=1,
        help="Processes to use. Seeds are split into chunks saturated independently "
        "and merged; --max-entities then applies per chunk.",
    ),
    format: OutputFormat = typer.Option(
        OutputFormat.yaml, "--format", "-f", help="Output format.",
    ),
    output: Optional[Path] = typer.Option(
        None, "--output", "-o", help="Write to a file instead of stdout.",
    ),
    enrichers: Optional[str] = typer.Option(
        None, "--enrichers", "-e", help=_ENRICHER_HELP,
    ),
    chemont_source: Optional[Path] = typer.Option(
        None, "--chemont-source", help="Local ChemOnt labels source (see convert).",
    ),
    chemont_dictionary: Optional[Path] = typer.Option(
        None, "--chemont-dictionary", help="Local ChemOnt dictionary (see convert).",
    ),
):
    """Generate a closed, ChEBI-like entity graph from seed structures.

    Every seed, and every structure generated from it, is run through the
    generators until no new structure appears: e.g. L-alanine yields D-alanine,
    alanine, rac-alanine and the zwitterion of each. Structures reached by
    several routes are merged by id (InChIKey; zwitterions, which share their
    uncharged form's InChIKey, get chemrof:zwitterion-<InChIKey>).

    Examples:

        chemrof saturate seeds.tsv -o graph.yaml

        chemrof saturate seeds.tsv -f owl -o graph.owl --enrichers chebi

        echo "OC(=O)CC(O)(CC(O)=O)C(O)=O" | chemrof saturate - -g protonation
    """
    import logging

    from rdkit import RDLogger

    from chemrof.converter.saturate import (
        ALL_GENERATORS,
        SaturationStats,
        saturate as do_saturate,
        saturate_parallel,
    )

    RDLogger.DisableLog("rdApp.*")
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")

    gens = [g.strip() for g in generators.split(",") if g.strip()]
    if set(gens) - set(ALL_GENERATORS):
        raise typer.BadParameter(f"unknown generators {sorted(set(gens) - set(ALL_GENERATORS))}; "
                                 f"choose from {', '.join(ALL_GENERATORS)}")
    kwargs = dict(
        generators=gens, max_entities=max_entities, max_rounds=max_rounds, max_siblings=max_siblings
    )
    stats = SaturationStats()
    seed_list = _read_seeds(seeds)
    if workers > 1:
        results = saturate_parallel(
            seed_list,
            workers,
            stats=stats,
            progress=lambda done, total: typer.echo(f"{done}/{total} seeds", err=True),
            **kwargs,
        )
    else:
        results = do_saturate(seed_list, stats=stats, **kwargs)
    if not results:
        raise typer.BadParameter("no parseable seed structures")

    _run_enrichers(results, _build_enrichers(enrichers, chemont_source, chemont_dictionary))
    _emit(results, format, output)
    typer.echo(
        f"{stats.seeds} seeds -> {len(results)} entities in {stats.rounds} rounds"
        + (f"; {len(stats.failed)} seeds unparseable" if stats.failed else "")
        + ("; truncated at --max-entities" if stats.truncated else ""),
        err=True,
    )


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
