"""The offline ChEBI enricher for atoms, ions and isotopes."""

import yaml
from typer.testing import CliRunner

from chemrof.cli.main import app
from chemrof.converter.convert import ChemConverter
from chemrof.converter.enrichers.base import EnrichmentContext, get_enricher, rewrite_references
from chemrof.converter.enrichers.chebi import ChebiEnricher

runner = CliRunner()


def enriched(smiles: str) -> dict:
    return ChemConverter(enrichers=[ChebiEnricher()]).convert(smiles)


def test_registered():
    assert isinstance(get_enricher("chebi"), ChebiEnricher)


def test_neutral_atom():
    obj = enriched("[C]")
    assert (obj["id"], obj["name"]) == ("CHEBI:27594", "carbon atom")


def test_ion_and_anion():
    assert enriched("[Fe+3]")["id"] == "CHEBI:29034"
    assert enriched("[Cl-]")["id"] == "CHEBI:17996"


def test_isotope_and_charged_isotope():
    assert enriched("[13C]")["id"] == "CHEBI:36928"
    assert enriched("[57Fe+3]")["name"] == "iron-57(3+)"


def test_atom_without_chebi_class_is_untouched():
    obj = enriched("[56Fe]")  # ChEBI has iron-57 but no iron-56 class
    assert obj["id"].startswith("INCHIKEY:")
    assert obj["name"] == "56Fe"


def test_molecules_are_untouched():
    obj = enriched("CCO")
    assert obj["id"].startswith("INCHIKEY:")
    assert obj["name"] == "C2H6O"


def test_enrich_directly_without_mol():
    obj = {"id": "x", "name": "y", "atomic_number": 8, "elemental_charge": -2}
    out = ChebiEnricher().enrich(obj, EnrichmentContext(mol=None, inchikey="", smiles="", inchi=""))
    assert out["id"] == "CHEBI:29356"  # oxide(2-)


def test_rewrite_references_updates_strings_and_lists():
    objs = [
        {"id": "B", "has_cationic_component": "A", "name": "A"},
        {"id": "C", "tautomer_of": ["A", "B"]},
    ]
    rewrite_references(objs, {"A": "CHEBI:1"})
    assert objs[0]["has_cationic_component"] == "CHEBI:1"
    assert objs[1]["tautomer_of"] == ["CHEBI:1", "B"]
    assert objs[0]["id"] == "B"


def test_cli_keeps_salt_links_after_ids_change():
    result = runner.invoke(app, ["convert", "[Na+].[Cl-]", "--enrichers", "chebi"])
    assert result.exit_code == 0
    docs = list(yaml.safe_load_all(result.output))
    salt = next(d for d in docs if d["type"] == "chemrof:ChemicalSalt")
    assert salt["has_cationic_component"] == "CHEBI:29101"
    assert salt["has_anionic_component"] == "CHEBI:17996"
    assert {d["id"] for d in docs} >= {salt["has_cationic_component"], salt["has_anionic_component"]}
