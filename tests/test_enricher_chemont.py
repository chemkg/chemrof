"""Tests for the local ClassyFire/ChemOnt enricher."""

import json

from typer.testing import CliRunner

from chemrof.cli.main import app
from chemrof.converter.enrichers.base import EnrichmentContext
from chemrof.converter.enrichers.chemont import (
    ChemOntEnricher,
    build_chemont_duckdb,
    build_chemont_parquet,
)


ETHANOL_INCHIKEY = "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"


def _write_chemont_inputs(tmp_path):
    labels = tmp_path / "labels.tsv"
    labels.write_text(
        "\t".join(
            [
                "inchikey",
                "cid",
                "zinc_id",
                "smiles",
                "chemont_tree_json",
                "chemont_other_json",
            ]
        )
        + "\n"
        + "\t".join(
            [
                ETHANOL_INCHIKEY,
                "702",
                "",
                "CCO",
                "[0,4707,323,1661,2450]",
                "{}",
            ]
        )
        + "\n"
    )
    dictionary = tmp_path / "chemont_dictionary.tsv"
    dictionary.write_text(
        "\t".join(
            [
                "numeric_id",
                "chemont_id",
                "name",
                "parent_numeric_id",
                "parent_name",
            ]
        )
        + "\n"
        + "\t".join(["2450", "CHEMONTID:0002450", "Alcohols", "323", "Organooxygen compounds"])
        + "\n"
    )
    return labels, dictionary


def test_chemont_enricher_from_indexed_duckdb(tmp_path):
    labels, dictionary = _write_chemont_inputs(tmp_path)
    db_path = build_chemont_duckdb(labels, dictionary, tmp_path / "chemont.duckdb")

    enricher = ChemOntEnricher(source=db_path)
    obj = {"id": f"INCHIKEY:{ETHANOL_INCHIKEY}", "name": "C2H6O"}
    ctx = EnrichmentContext(mol=None, inchikey=ETHANOL_INCHIKEY, smiles="CCO", inchi="")
    result = enricher.enrich(obj, ctx)

    assert result["classified_by"] == "CHEMONTID:0002450"


def test_chemont_enricher_from_parquet_directory(tmp_path):
    labels, dictionary = _write_chemont_inputs(tmp_path)
    parquet_dir = tmp_path / "parquet"
    build_chemont_parquet(labels, dictionary, parquet_dir)

    enricher = ChemOntEnricher(source=parquet_dir)
    obj = {"id": f"INCHIKEY:{ETHANOL_INCHIKEY}", "name": "C2H6O"}
    ctx = EnrichmentContext(mol=None, inchikey=ETHANOL_INCHIKEY, smiles="CCO", inchi="")
    result = enricher.enrich(obj, ctx)

    assert result["classified_by"] == "CHEMONTID:0002450"


def test_chemont_enricher_no_match_leaves_object_unchanged(tmp_path):
    labels, dictionary = _write_chemont_inputs(tmp_path)
    db_path = build_chemont_duckdb(labels, dictionary, tmp_path / "chemont.duckdb")
    enricher = ChemOntEnricher(source=db_path)
    obj = {"id": "INCHIKEY:missing", "name": "missing"}
    ctx = EnrichmentContext(mol=None, inchikey="missing", smiles="", inchi="")

    assert enricher.enrich(obj, ctx) == obj


def test_cli_from_smiles_can_use_chemont_source(tmp_path):
    labels, dictionary = _write_chemont_inputs(tmp_path)
    db_path = build_chemont_duckdb(labels, dictionary, tmp_path / "chemont.duckdb")

    result = CliRunner().invoke(
        app,
        [
            "from-smiles",
            "CCO",
            "--format",
            "json",
            "--enrichers",
            "chemont",
            "--chemont-source",
            str(db_path),
        ],
    )

    assert result.exit_code == 0, result.output
    data = json.loads(result.output)
    assert data["classified_by"] == "CHEMONTID:0002450"


def test_cli_prepare_chemont_builds_duckdb(tmp_path):
    labels, dictionary = _write_chemont_inputs(tmp_path)
    db_path = tmp_path / "prepared.duckdb"

    result = CliRunner().invoke(
        app,
        [
            "prepare-chemont",
            str(labels),
            str(dictionary),
            str(db_path),
        ],
    )

    assert result.exit_code == 0, result.output
    assert db_path.exists()
