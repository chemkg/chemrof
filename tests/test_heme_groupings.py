"""Check the heme grouping examples against the heme molecule examples.

The GroupingBySmarts examples for heme, heme a, heme b and heme o carry a
SMARTS that is meant to recognise exactly the molecules that ChEBI files under
each class. Each molecule example states its direct groupings in
``classified_by``; the groupings state their parents in ``subtype_of``. This
test checks that, for every heme molecule example, the set of SMARTS groupings
that match its SMILES is exactly the set implied by ``classified_by`` closed
over ``subtype_of``, and that close non-members (other metals, free-base
porphyrin, ferrocene, mesoheme) match none of them.
"""

from pathlib import Path

import pytest
import yaml
from rdkit import Chem

EXAMPLES = Path(__file__).parent.parent / "src" / "data" / "examples" / "valid"

HEME_MOLECULES = [
    "NetUnchargedMolecule-ferroheme_a.yaml",
    "NetUnchargedMolecule-ferroheme_b.yaml",
    "NetUnchargedMolecule-ferroheme_c.yaml",
    "NetUnchargedMolecule-ferroheme_o.yaml",
    "MolecularCation-ferriheme_b.yaml",
]

HEME_GROUPINGS = [
    "GroupingBySmarts-heme.yaml",
    "GroupingBySmarts-heme_a.yaml",
    "GroupingBySmarts-heme_b.yaml",
    "GroupingBySmarts-heme_o.yaml",
    "MoleculeGroupingClass-ferroheme.yaml",
    "MoleculeGroupingClass-ferriheme.yaml",
]


def _load(name):
    with open(EXAMPLES / name) as f:
        return yaml.safe_load(f)


def _mol(smiles):
    mol = Chem.MolFromSmiles(smiles)
    assert mol is not None, smiles
    return mol


@pytest.fixture(scope="module")
def groupings():
    return {g["id"]: g for g in map(_load, HEME_GROUPINGS)}


@pytest.fixture(scope="module")
def smarts(groupings):
    out = {}
    for gid, g in groupings.items():
        if "smarts_string" in g:
            query = Chem.MolFromSmarts(g["smarts_string"])
            assert query is not None, f"{gid} SMARTS does not parse"
            out[gid] = query
    return out


def _closure(direct, groupings):
    seen, todo = set(), list(direct)
    while todo:
        gid = todo.pop()
        if gid in seen:
            continue
        seen.add(gid)
        todo.extend(groupings.get(gid, {}).get("subtype_of", []))
    return seen


@pytest.mark.parametrize("filename", HEME_MOLECULES)
def test_smarts_matches_asserted_groupings(filename, groupings, smarts):
    m = _load(filename)
    mol = _mol(m["smiles_string"])
    matched = {gid for gid, q in smarts.items() if mol.HasSubstructMatch(q)}
    expected = _closure(m["classified_by"], groupings) & set(smarts)
    assert matched == expected, f"{m['name']}: matched {matched}, expected {expected}"


@pytest.mark.parametrize("filename", HEME_MOLECULES)
def test_iron_oxidation_state_agrees_with_grouping(filename):
    """ferroheme members have Fe(II), ferriheme members Fe(III)."""
    m = _load(filename)
    fe = [a for a in m["has_atom_occurrences"] if a["occurrence_of"] == "Fe"]
    assert len(fe) == 1
    expected = {"CHEBI:38573": 2, "CHEBI:38574": 3}
    asserted = [expected[c] for c in m["classified_by"] if c in expected]
    assert asserted == [fe[0]["oxidation_number"]]


@pytest.mark.parametrize(
    "name, smiles",
    [
        # ChEBI:28783, same ligand as heme b but zinc
        ("zinc protoporphyrin",
         "C=CC1=C(C)C2=Cc3c(C=C)c(C)c4[n]3[Zn]35[N]2=C1C=c1c(C)c(CCC(=O)O)"
         "c([n]13)=CC1=[N]5C(=C4)C(C)=C1CCC(=O)O"),
        # ChEBI:15430, free-base ligand, no metal
        ("protoporphyrin",
         "C=CC1=C(C)c2cc3nc(cc4nc(cc5nc(cc1n2)c(C)c5CCC(=O)O)C(CCC(=O)O)=C4C)"
         "c(C)c3C=C"),
        # ChEBI:30672, iron bonded to carbon, not nitrogen
        ("ferrocene",
         "[CH]12[CH]3[CH]4[CH]5[CH]1[Fe]23451678[CH]2[CH]1[CH]6[CH]7[CH]28"),
        ("iron(2+)", "[Fe+2]"),
    ],
)
def test_non_hemes_match_no_heme_grouping(name, smiles, smarts):
    mol = _mol(smiles)
    assert not any(mol.HasSubstructMatch(q) for q in smarts.values()), name


def test_mesoheme_is_heme_but_not_heme_b(smarts):
    """Ethyl in place of vinyl: still a heme, no longer heme b."""
    ferroheme_b = _load("NetUnchargedMolecule-ferroheme_b.yaml")["smiles_string"]
    mesoheme = ferroheme_b.replace("C=CC1", "CCC1").replace("c(C=C)", "c(CC)")
    assert mesoheme != ferroheme_b
    mol = _mol(mesoheme)
    assert mol.HasSubstructMatch(smarts["CHEBI:30413"])
    assert not mol.HasSubstructMatch(smarts["CHEBI:26355"])
