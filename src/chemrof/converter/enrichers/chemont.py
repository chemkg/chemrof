"""ChemOnt enricher backed by the ClassyFire/ChemOnt InChIKey table."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path
from typing import Any

import duckdb
import httpx

from chemrof.converter.enrichers.base import EnrichmentContext

CHEMONT_SOURCE_ENV = "CHEMROF_CHEMONT_SOURCE"
CHEMONT_DICTIONARY_ENV = "CHEMROF_CHEMONT_DICTIONARY"

ZENODO_RECORD_ID = "20200447"
ZENODO_LABELS_FILE = "classyfire_dedup_inchikey_smiles.enriched.tsv.zst"
ZENODO_DICTIONARY_FILE = "chemont_dictionary.tsv"
ZENODO_FILES_URL = f"https://zenodo.org/api/records/{ZENODO_RECORD_ID}/files"

LABELS_TABLE = "chemont_labels"
DICTIONARY_TABLE = "chemont_dictionary"


def download_chemont_zenodo(
    download_dir: str | Path,
    *,
    overwrite: bool = False,
) -> tuple[Path, Path]:
    """Download the ChemOnt Zenodo files needed to build a local lookup store."""
    download_dir = Path(download_dir)
    download_dir.mkdir(parents=True, exist_ok=True)

    labels_path = download_dir / ZENODO_LABELS_FILE
    dictionary_path = download_dir / ZENODO_DICTIONARY_FILE

    _download_file(_zenodo_file_url(ZENODO_LABELS_FILE), labels_path, overwrite=overwrite)
    _download_file(
        _zenodo_file_url(ZENODO_DICTIONARY_FILE),
        dictionary_path,
        overwrite=overwrite,
    )

    return labels_path, dictionary_path


def build_chemont_duckdb(
    enriched_tsv: str | Path,
    dictionary_tsv: str | Path,
    output_db: str | Path,
    *,
    overwrite: bool = False,
) -> Path:
    """Build an indexed DuckDB database from the Zenodo TSV files.

    The full ClassyFire/ChemOnt table is large enough that an indexed DuckDB file is
    the best format for repeated point lookups by InChIKey. Parquet is still useful
    for scans and bulk joins, but the CLI enricher benefits from this index.
    """
    output_db = Path(output_db)
    _prepare_output(output_db, overwrite=overwrite)
    temp_db = output_db.with_name(f".{output_db.name}.tmp")
    _prepare_output(temp_db, overwrite=True)

    try:
        con = duckdb.connect(str(temp_db))
        try:
            con.execute(
                f"""
                CREATE TABLE {LABELS_TABLE} AS
                SELECT
                  inchikey,
                  cid,
                  zinc_id,
                  smiles,
                  chemont_tree_json,
                  chemont_other_json
                FROM {_source_relation(enriched_tsv)}
                """
            )
            con.execute(
                f"CREATE INDEX {LABELS_TABLE}_inchikey_idx ON {LABELS_TABLE}(inchikey)"
            )
            con.execute(
                f"""
                CREATE TABLE {DICTIONARY_TABLE} AS
                SELECT
                  CAST(numeric_id AS INTEGER) AS numeric_id,
                  chemont_id,
                  name,
                  {_parent_numeric_id_expression()} AS parent_numeric_id,
                  parent_name
                FROM {_source_relation(dictionary_tsv)}
                """
            )
            con.execute(
                f"CREATE UNIQUE INDEX {DICTIONARY_TABLE}_numeric_id_idx "
                f"ON {DICTIONARY_TABLE}(numeric_id)"
            )
        finally:
            con.close()
        temp_db.replace(output_db)
    except Exception:
        if temp_db.exists():
            temp_db.unlink()
        raise

    return output_db


def _parent_numeric_id_expression() -> str:
    return "TRY_CAST(NULLIF(parent_numeric_id, 'null') AS INTEGER)"


def build_chemont_parquet(
    enriched_tsv: str | Path,
    dictionary_tsv: str | Path,
    output_dir: str | Path,
    *,
    overwrite: bool = False,
) -> tuple[Path, Path]:
    """Build Parquet copies of the Zenodo TSV files for scan-heavy workflows."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    labels_path = output_dir / "chemont_labels.parquet"
    dictionary_path = output_dir / "chemont_dictionary.parquet"
    _prepare_output(labels_path, overwrite=overwrite)
    _prepare_output(dictionary_path, overwrite=overwrite)

    con = duckdb.connect()
    try:
        con.execute(
            f"""
            COPY (
              SELECT
                inchikey,
                cid,
                zinc_id,
                smiles,
                chemont_tree_json,
                chemont_other_json
              FROM {_source_relation(enriched_tsv)}
            )
            TO {_sql_literal(labels_path)}
            (FORMAT PARQUET, COMPRESSION ZSTD)
            """
        )
        con.execute(
            f"""
            COPY (
              SELECT
                CAST(numeric_id AS INTEGER) AS numeric_id,
                chemont_id,
                name,
                {_parent_numeric_id_expression()} AS parent_numeric_id,
                parent_name
              FROM {_source_relation(dictionary_tsv)}
            )
            TO {_sql_literal(dictionary_path)}
            (FORMAT PARQUET, COMPRESSION ZSTD)
            """
        )
    finally:
        con.close()

    return labels_path, dictionary_path


class ChemOntEnricher:
    """Add ClassyFire/ChemOnt tree classes as ``classified_by``."""

    name = "chemont"

    def __init__(
        self,
        source: str | Path | None = None,
        dictionary_source: str | Path | None = None,
    ):
        source = source or os.getenv(CHEMONT_SOURCE_ENV)
        dictionary_source = dictionary_source or os.getenv(CHEMONT_DICTIONARY_ENV)
        if not source:
            raise ValueError(
                "ChemOntEnricher requires a source path. Pass --chemont-source "
                f"or set {CHEMONT_SOURCE_ENV}."
            )

        self.source = Path(source)
        self.dictionary_source = (
            Path(dictionary_source)
            if dictionary_source
            else _default_dictionary_source(self.source)
        )
        self._source_is_duckdb = _is_duckdb(self.source)
        self._dictionary: dict[int, dict[str, Any]] | None = None

        if self.dictionary_source and _is_csv_like(self.dictionary_source):
            self._dictionary = _load_dictionary_tsv(self.dictionary_source)

    def enrich(self, obj: dict, context: EnrichmentContext) -> dict:
        if not context.inchikey:
            return obj

        numeric_ids = self._lookup_tree_classes(context.inchikey)
        if not numeric_ids:
            return obj

        obj["classified_by"] = [
            self._classification_curie(numeric_id) for numeric_id in numeric_ids
        ]
        return obj

    def _lookup_tree_classes(self, inchikey: str) -> list[int]:
        row = self._fetch_label_row(inchikey)
        if not row:
            return []
        return _tree_classes(row[0])

    def _fetch_label_row(self, inchikey: str) -> tuple[Any, ...] | None:
        con = (
            duckdb.connect(str(self.source), read_only=True)
            if self._source_is_duckdb
            else duckdb.connect()
        )
        try:
            if self._source_is_duckdb:
                return con.execute(
                    f"""
                    SELECT chemont_tree_json
                    FROM {LABELS_TABLE}
                    WHERE inchikey = ?
                    LIMIT 1
                    """,
                    [inchikey],
                ).fetchone()
            return con.execute(
                f"""
                SELECT chemont_tree_json
                FROM {_source_relation(self.source)}
                WHERE inchikey = ?
                LIMIT 1
                """,
                [inchikey],
            ).fetchone()
        finally:
            con.close()

    def _classification_curie(self, numeric_id: int) -> str:
        row = self._lookup_dictionary_row(numeric_id)
        if row and row.get("chemont_id"):
            return row["chemont_id"]
        return _chemont_id(numeric_id)

    def _lookup_dictionary_row(self, numeric_id: int) -> dict[str, Any] | None:
        if self._dictionary is not None:
            return self._dictionary.get(numeric_id)

        if self._source_is_duckdb:
            con = duckdb.connect(str(self.source), read_only=True)
            try:
                row = con.execute(
                    f"""
                    SELECT chemont_id, name, parent_numeric_id, parent_name
                    FROM {DICTIONARY_TABLE}
                    WHERE numeric_id = ?
                    LIMIT 1
                    """,
                    [numeric_id],
                ).fetchone()
            except duckdb.CatalogException:
                return None
            finally:
                con.close()
            return _dictionary_row_from_tuple(row) if row else None

        if self.dictionary_source:
            con = duckdb.connect()
            try:
                row = con.execute(
                    f"""
                    SELECT chemont_id, name, parent_numeric_id, parent_name
                    FROM {_source_relation(self.dictionary_source)}
                    WHERE numeric_id = ?
                    LIMIT 1
                    """,
                    [numeric_id],
                ).fetchone()
            finally:
                con.close()
            return _dictionary_row_from_tuple(row) if row else None

        return None


def _prepare_output(path: Path, *, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if not overwrite:
            raise FileExistsError(f"{path} already exists")
        path.unlink()


def _download_file(url: str, path: Path, *, overwrite: bool) -> Path:
    if path.exists() and not overwrite:
        return path

    _prepare_output(path, overwrite=True)
    temp_path = path.with_name(f"{path.name}.tmp")
    if temp_path.exists():
        temp_path.unlink()

    timeout = httpx.Timeout(30.0, read=None)
    try:
        with httpx.stream(
            "GET",
            url,
            follow_redirects=True,
            timeout=timeout,
        ) as response:
            response.raise_for_status()
            with temp_path.open("wb") as stream:
                for chunk in response.iter_bytes():
                    if chunk:
                        stream.write(chunk)
        temp_path.replace(path)
    finally:
        if temp_path.exists():
            temp_path.unlink()

    return path


def _zenodo_file_url(filename: str) -> str:
    return f"{ZENODO_FILES_URL}/{filename}/content"


def _source_relation(path: str | Path) -> str:
    path = Path(path)
    if path.is_dir():
        labels_path = path / "chemont_labels.parquet"
        if labels_path.exists():
            return f"read_parquet({_sql_literal(labels_path)})"
        return f"read_parquet({_sql_literal(path / '**' / '*.parquet')})"
    if path.suffix.lower() in {".parquet", ".parq"}:
        return f"read_parquet({_sql_literal(path)})"
    return f"read_csv_auto({_sql_literal(path)}, delim='\\t', header=true)"


def _sql_literal(path: str | Path) -> str:
    return "'" + str(path).replace("'", "''") + "'"


def _is_duckdb(path: Path) -> bool:
    return path.suffix.lower() in {".duckdb", ".ddb", ".db"}


def _is_csv_like(path: Path) -> bool:
    suffixes = {suffix.lower() for suffix in path.suffixes}
    return bool(suffixes & {".tsv", ".csv"})


def _default_dictionary_source(source: Path) -> Path | None:
    if source.is_dir():
        for name in ("chemont_dictionary.parquet", "chemont_dictionary.tsv"):
            candidate = source / name
            if candidate.exists():
                return candidate
    return None


def _load_dictionary_tsv(path: Path) -> dict[int, dict[str, Any]]:
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        return {
            int(row["numeric_id"]): {
                "chemont_id": row["chemont_id"],
                "name": row["name"],
                "parent_numeric_id": _optional_int(row.get("parent_numeric_id")),
                "parent_name": _optional_str(row.get("parent_name")),
            }
            for row in reader
            if row.get("numeric_id")
        }


def _dictionary_row_from_tuple(row: tuple[Any, ...]) -> dict[str, Any]:
    return {
        "chemont_id": row[0],
        "name": row[1],
        "parent_numeric_id": row[2],
        "parent_name": row[3],
    }


def _tree_classes(tree_json: Any) -> list[int]:
    if tree_json is None:
        return []
    tree = json.loads(tree_json) if isinstance(tree_json, str) else tree_json
    classes = []
    seen = set()
    for value in tree:
        if value is None:
            continue
        numeric_id = int(value)
        if numeric_id not in seen:
            classes.append(numeric_id)
            seen.add(numeric_id)
    return classes


def _chemont_id(numeric_id: int) -> str:
    return f"CHEMONTID:{numeric_id:07d}"


def _optional_int(value: Any) -> int | None:
    return int(value) if value not in (None, "", "null") else None


def _optional_str(value: Any) -> str | None:
    return value if value not in (None, "", "null") else None
