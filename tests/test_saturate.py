"""saturate: close seed structures under the stereo, salt and protonation generators."""

import doctest

import pytest
import yaml
from typer.testing import CliRunner

from chemrof.cli.main import app
from chemrof.converter import saturate as saturate_module
from chemrof.converter.saturate import SaturationStats, saturate

runner = CliRunner(mix_stderr=False)  # the run summary goes to stderr


def by_name(entities: list[dict]) -> dict[str, dict]:
    return {e["name"]: e for e in entities}


def test_doctests():
    assert doctest.testmod(saturate_module).failed == 0


def test_alanine_closes_over_stereo_and_zwitterions():
    graph = saturate([{"structure": "N[C@@H](C)C(O)=O", "name": "L-alanine"}])
    ids = {e["id"] for e in graph}
    assert len(ids) == len(graph) == 8
    names = by_name(graph)
    l_ala, zw = names["L-alanine"], names["L-alanine zwitterion"]
    assert zw["id"] == "chemrof:zwitterion-QNAYBMKLOCPYGJ-REOHCLBHSA-N"
    assert l_ala["has_major_microspecies_at_pH7_3"] == [zw["id"]]
    assert l_ala["tautomer_of"] == [zw["id"]]
    assert zw["tautomer_of"] == [l_ala["id"]]
    # the zwitterion has its own stereo family, not the neutral one's
    assert zw["enantiomer_form_of"] == "chemrof:zwitterion-QNAYBMKLOCPYGJ-UHFFFAOYSA-N"
    assert "chemrof:rac-zwitterion-QNAYBMKLOCPYGJ-UHFFFAOYSA-N" in ids
    # every reference points at an entity in the graph
    for e in graph:
        for slot in ("enantiomer_form_of", "has_left_enantiomer", "has_right_enantiomer",
                     "chirality_agnostic_form", "has_major_microspecies_at_pH7_3", "tautomer_of"):
            refs = e.get(slot, [])
            for ref in refs if isinstance(refs, list) else [refs]:
                assert ref in ids, (e["id"], slot)


def test_any_family_member_gives_the_same_graph():
    from_l = saturate(["N[C@@H](C)C(O)=O"])
    from_zwitterion_d = saturate(["[NH3+][C@H](C)C([O-])=O"])
    assert {e["id"] for e in from_l} == {e["id"] for e in from_zwitterion_d}


def test_one_proton_step_is_a_conjugate_pair():
    graph = by_name(saturate([{"structure": "CC(O)=O", "name": "acetic acid"}]))
    acid, base = graph["acetic acid"], graph["acetic acid(1-)"]
    assert base["conjugate_base_of"] == acid["id"]
    assert acid["conjugate_acid_of"] == base["id"]
    assert acid["has_major_microspecies_at_pH7_3"] == [base["id"]]
    assert base["type"] == "chemrof:MolecularAnion"
    assert base["elemental_charge"] == -1


def test_multi_proton_step_is_only_microspecies():
    graph = by_name(saturate([{"structure": "OC(=O)CC(O)(CC(O)=O)C(O)=O", "name": "citric acid"}]))
    acid = graph["citric acid"]
    assert acid["has_major_microspecies_at_pH7_3"] == [graph["citric acid(3-)"]["id"]]
    assert "conjugate_acid_of" not in acid


def test_salt_components_are_saturated():
    graph = saturate(["[Na+].CC([O-])=O"])
    types = {e["type"] for e in graph}
    assert "chemrof:ChemicalSalt" in types
    smiles = {e.get("smiles_string") for e in graph}
    # the acetate component, its acid, and sodium's element family
    assert {"CC(=O)[O-]", "CC(=O)O", "[Na+]", "[Na]"} <= smiles


def test_generators_can_be_chosen():
    graph = saturate(["N[C@@H](C)C(O)=O"], generators=["protonation"])
    assert len(graph) == 2  # L-alanine and its zwitterion, no stereo family
    with pytest.raises(ValueError, match="unknown generators"):
        saturate(["CCO"], generators=["bogus"])


def test_limits():
    stats = SaturationStats()
    graph = saturate(["N[C@@H](C)C(O)=O"], max_rounds=0, stats=stats)
    assert len(graph) == 1 and stats.rounds == 0
    stats = SaturationStats()
    saturate(["N[C@@H](C)C(O)=O"], max_entities=3, stats=stats)
    assert stats.truncated


def test_seed_id_replaces_inchikey_and_references():
    graph = saturate([{"structure": "N[C@@H](C)C(O)=O", "id": "CHEBI:16977"}])
    ids = {e["id"] for e in graph}
    assert "CHEBI:16977" in ids
    assert "INCHIKEY:QNAYBMKLOCPYGJ-REOHCLBHSA-N" not in ids
    rac = next(e for e in graph if e["type"] == "chemrof:RacemicMixture" and "zwitterion" not in e["id"])
    assert "CHEBI:16977" in (rac["has_left_enantiomer"], rac["has_right_enantiomer"])


def test_bad_seed_is_skipped():
    stats = SaturationStats()
    graph = saturate(["not a smiles", "CCO"], stats=stats)
    assert stats.failed == ["not a smiles"] and stats.seeds == 1
    assert len(graph) == 1


class TestSaturateCommand:
    def test_tsv_seeds(self, tmp_path):
        seeds = tmp_path / "seeds.tsv"
        seeds.write_text("# comment\nN[C@@H](C)C(O)=O\tL-alanine\tCHEBI:16977\n\nCC(O)=O\tacetic acid\n")
        result = runner.invoke(app, ["saturate", str(seeds)])
        assert result.exit_code == 0, result.output
        docs = [d for d in yaml.safe_load_all(result.stdout)]
        assert {"CHEBI:16977", "INCHIKEY:QTBSBXVTEAMEQO-UHFFFAOYSA-M"} <= {d["id"] for d in docs}
        assert "2 seeds -> 10 entities" in result.stderr

    def test_owl(self, tmp_path):
        seeds = tmp_path / "seeds.tsv"
        seeds.write_text("CC(O)=O\tacetic acid\n")
        out = tmp_path / "out.owl"
        result = runner.invoke(app, ["saturate", str(seeds), "-f", "owl", "-o", str(out)])
        assert result.exit_code == 0, result.output
        owl = out.read_text()
        assert "ObjectSomeValuesFrom(chemrof:conjugate_base_of" in owl
        assert "ObjectSomeValuesFrom(chemrof:has_major_microspecies_at_pH7_3" in owl

    def test_bad_generator(self, tmp_path):
        seeds = tmp_path / "seeds.tsv"
        seeds.write_text("CCO\n")
        result = runner.invoke(app, ["saturate", str(seeds), "-g", "bogus"])
        assert result.exit_code != 0


def test_parallel_matches_serial():
    from chemrof.converter.saturate import saturate_parallel

    seeds = [
        {"structure": "N[C@@H](C)C(O)=O", "name": "L-alanine", "id": "CHEBI:16977"},
        {"structure": "[NH3+][C@H](C)C([O-])=O"},  # D-alanine zwitterion: same families
        {"structure": "CC(O)=O", "name": "acetic acid"},
    ]
    serial = saturate([dict(s) for s in seeds])
    parallel = saturate_parallel([dict(s) for s in seeds], workers=2, chunk_size=1)
    assert sorted(serial, key=lambda e: e["id"]) == sorted(parallel, key=lambda e: e["id"])


def test_structure_without_inchi_gets_an_iri_safe_id():
    graph = saturate(["[NH3]->[Co+3]"], generators=[])
    assert graph[0]["id"].startswith("chemrof:smiles-")
