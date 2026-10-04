"""Saturate a set of seed structures into a closed, interlinked entity graph.

Each structure -- seed or generated -- is run through a set of generators, and
every structure a generator produces is fed back in, until nothing new appears
(or a limit is hit). Entities are keyed by id (InChIKey), so a structure reached
by several routes is one entity whose relations are merged.

Generators:

* ``stereo`` -- for a molecule with stereo elements: the stereo-agnostic parent,
  every stereoisomer and the racemates (:func:`chemrof.converter.siblings.siblings`).
  Past ``max_siblings`` stereoisomers, only the parent, the input's mirror
  image and their racemate. For an atom: the neutral atom, isotopes and ions
  of its element.
* ``salt`` -- a salt's cationic and anionic components.
* ``protonation`` -- the uncharged parent and the major microspecies at pH 7.3
  (:mod:`chemrof.converter.protonation`), linked by
  ``has_major_microspecies_at_pH7_3``. A pair one proton apart is also linked
  by ``conjugate_acid_of`` / ``conjugate_base_of``; a pair of equal net
  charge (an amino acid and its zwitterion) by ``tautomer_of``.
* ``tautomer`` -- RDKit tautomer enumeration, linked by ``tautomer_of``. Off by
  default: it multiplies the graph and most tautomers are not ChEBI classes.

>>> graph = saturate([{"structure": "N[C@@H](C)C(O)=O", "name": "L-alanine"}])
>>> len(graph)   # alanine, L-, D- and rac-alanine; and the zwitterion of each
8
>>> sorted(e["name"] for e in graph if e["name"].startswith("L-"))
['L-alanine', 'L-alanine zwitterion']
"""

from __future__ import annotations

import logging
from collections import deque
from dataclasses import dataclass, field
from typing import Callable, Iterable

from rdkit import Chem
from rdkit.Chem import EnumerateStereoisomers, FindMolChiralCenters, rdmolops
from rdkit.Chem.MolStandardize import rdMolStandardize

from chemrof.converter.atoms import is_single_atom
from chemrof.converter.autochain import _build_salt_graph, _build_tautomer_graph, _mol_to_entity
from chemrof.converter.classify import _is_salt, classify_entity
from chemrof.converter.convert import ChemConverter
from chemrof.converter.enrichers.base import rewrite_references
from chemrof.converter.parse import parse_input
from chemrof.converter.protonation import predict_major_microspecies
from chemrof.converter.siblings import DEFAULT_MAX_SIBLINGS, _mirror, siblings

logger = logging.getLogger(__name__)

_TYPE_PREFIX = "chemrof:"

ALL_GENERATORS = ("stereo", "salt", "protonation", "tautomer")
DEFAULT_GENERATORS = ("stereo", "salt", "protonation")

# Relation slots that hold a list of ids; values are unioned on merge.
# has_major_microspecies_at_pH7_3 says multivalued: false, but LinkML induces
# multivalued from its is_a parent acid_form_of, so the schema expects a list.
_LIST_SLOTS = {"tautomer_of", "has_major_microspecies_at_pH7_3"}
# Types a generator assigns on purpose, not to be overridden by reclassification
_STEREO_TYPES = {"Enantiomer", "Stereoisomer"}
_KEEP_TYPES = _STEREO_TYPES | {"RacemicMixture", "ChemicalSalt"}
_ION_TYPES = {"MolecularCation", "MolecularAnion"}


@dataclass
class SaturationStats:
    """Counts reported at the end of a run."""

    seeds: int = 0
    rounds: int = 0
    processed: int = 0
    failed: list[str] = field(default_factory=list)
    truncated: bool = False


@dataclass
class _Graph:
    entities: dict[str, dict] = field(default_factory=dict)
    # links a generator wants made once the entities it returned are added
    pending_links: list[tuple[str, str, str]] = field(default_factory=list)
    # (generator, family key) pairs already expanded; any member of a family
    # yields the whole family, so the other members need not be run again
    expanded: set[tuple[str, str]] = field(default_factory=set)

    def first_visit(self, generator: str, key: str) -> bool:
        if (generator, key) in self.expanded:
            return False
        self.expanded.add((generator, key))
        return True

    def add(self, entity: dict) -> bool:
        """Add or merge *entity*; return True if its id is new."""
        _normalize(entity)
        existing = self.entities.get(entity["id"])
        if existing is None:
            self.entities[entity["id"]] = entity
            return True
        _merge(existing, entity)
        return False

    def link(self, source_id: str, slot: str, target_id: str) -> None:
        source = self.entities[source_id]
        if slot in _LIST_SLOTS:
            values = source.setdefault(slot, [])
            if target_id not in values:
                values.append(target_id)
        elif source.get(slot, target_id) != target_id:
            logger.warning(
                "%s: keeping %s=%s, not %s", source_id, slot, source[slot], target_id
            )
        else:
            source[slot] = target_id


def is_zwitterion(mol: Chem.Mol) -> bool:
    """True for a net-neutral, charge-separated form that InChI drops.

    Standard InChI normalises a zwitterion to its uncharged tautomer, so the two
    share an InChIKey. ChEBI keeps them apart (L-alanine and L-alanine
    zwitterion), so they need different ids here. Formal charges InChI keeps,
    such as a nitro group's or a betaine's, don't count.

    >>> is_zwitterion(Chem.MolFromSmiles("[NH3+]CC([O-])=O"))
    True
    >>> is_zwitterion(Chem.MolFromSmiles("NCC(O)=O"))
    False
    >>> is_zwitterion(Chem.MolFromSmiles("C[N+](C)(C)CC([O-])=O"))   # betaine
    False
    """
    if Chem.GetFormalCharge(mol) != 0 or not any(a.GetFormalCharge() for a in mol.GetAtoms()):
        return False
    roundtrip = Chem.MolFromInchi(Chem.MolToInchi(mol))
    charged = sum(1 for a in mol.GetAtoms() if a.GetFormalCharge())
    return roundtrip is not None and charged > sum(
        1 for a in roundtrip.GetAtoms() if a.GetFormalCharge()
    )


def _assign_id(entity: dict, mol: Chem.Mol) -> None:
    """Re-key a zwitterion so it does not collide with its uncharged form."""
    eid = entity.get("id", "")
    if eid.startswith("INCHIKEY:") and is_zwitterion(mol):
        entity["id"] = f"chemrof:zwitterion-{eid.removeprefix('INCHIKEY:')}"


def _normalize(entity: dict) -> None:
    """Give generated entities the type the converter would, and their charge.

    Generators build some entities with a fixed type (a stereo-agnostic parent
    is always ``SmallMolecule``), which is wrong for an ion.
    """
    smiles = entity.get("smiles_string")
    typ = entity.get("type", "").removeprefix(_TYPE_PREFIX)
    if not smiles or typ in _KEEP_TYPES:
        return
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return
    typ = classify_entity(mol)
    if typ == "Enantiomer" and Chem.MolToSmiles(_mirror(mol)) == Chem.MolToSmiles(mol):
        typ = "Stereoisomer"  # meso: every centre assigned, but achiral
    entity["type"] = f"{_TYPE_PREFIX}{typ}"
    if typ in _ION_TYPES:
        entity["elemental_charge"] = Chem.GetFormalCharge(mol)


def _merge(into: dict, other: dict) -> None:
    """Merge *other* into *into*: fill missing slots, union list slots.

    A stereo type (set by the stereo generator, which knows an isolated
    cis/trans isomer is a ``Stereoisomer``) wins over a charge-based one.
    """
    if _type(other) in _STEREO_TYPES and _type(into) not in _STEREO_TYPES:
        into["type"] = other["type"]
    for key, value in other.items():
        if key not in into:
            into[key] = value
        elif key in _LIST_SLOTS:
            into[key] = list(dict.fromkeys([*into[key], *value]))


def _type(entity: dict) -> str:
    return entity.get("type", "").removeprefix(_TYPE_PREFIX)


# -- generators -------------------------------------------------------------
#
# A generator takes (entity, mol, graph) and returns the entities it found;
# the driver merges them into the graph and queues the new ones. A generator
# may also queue links between them on ``graph.pending_links``.


def _gen_stereo(entity: dict, mol: Chem.Mol, graph: _Graph, max_siblings: int) -> list[dict]:
    if is_single_atom(mol):
        element = mol.GetAtomWithIdx(0).GetAtomicNum()
        return siblings(entity, mol, max_siblings) if graph.first_visit("element", str(element)) else []
    if _is_salt(mol) or len(rdmolops.GetMolFrags(mol)) > 1:
        return []
    stripped = Chem.RWMol(mol)
    Chem.RemoveStereochemistry(stripped)
    stripped = stripped.GetMol()
    count = EnumerateStereoisomers.GetStereoisomerCount(stripped)
    if count <= 1:
        return []
    if count > max_siblings:
        # A sample of a huge family would be noise; keep the input's own lineage
        return _mirror_family(entity, mol, stripped)
    if not graph.first_visit("stereo", Chem.MolToSmiles(stripped)):
        return []
    return siblings(entity, mol, max_siblings)


def _mirror_family(entity: dict, mol: Chem.Mol, stripped: Chem.Mol) -> list[dict]:
    """The stereo-agnostic parent, and for a chiral input its mirror image and racemate.

    Used for molecules with more stereoisomers than ``max_siblings``. Ids match
    what :func:`~chemrof.converter.siblings.siblings` gives the same entities.
    """
    agnostic = _mol_to_entity(stripped, "SmallMolecule")
    unassigned = FindMolChiralCenters(mol, includeUnassigned=True, useLegacyImplementation=False)
    smiles = Chem.MolToSmiles(mol)
    mirror_mol = _mirror(mol)
    if any(c[1] == "?" for c in unassigned) or Chem.MolToSmiles(mirror_mol) == smiles:
        return [agnostic]  # partly specified, or achiral
    family = [agnostic]
    for m in (mol, mirror_mol):
        ent = _mol_to_entity(m, "Enantiomer")
        ent["isomeric_smiles_string"] = Chem.MolToSmiles(m)
        ent["enantiomer_form_of"] = agnostic["id"]
        centers = FindMolChiralCenters(m)
        if len(centers) == 1:
            ent["absolute_configuration"] = f"({centers[0][1]})"
        family.append(ent)
    left, right = sorted(family[1:], key=lambda e: e["id"])
    family.append(
        {
            "id": f"chemrof:rac-{left['id'].removeprefix('INCHIKEY:')}",
            "name": f"rac-{agnostic['name']}",
            "type": f"{_TYPE_PREFIX}RacemicMixture",
            "has_left_enantiomer": left["id"],
            "has_right_enantiomer": right["id"],
            "chirality_agnostic_form": agnostic["id"],
        }
    )
    return family


def _gen_salt(entity: dict, mol: Chem.Mol, graph: _Graph) -> list[dict]:
    if not _is_salt(mol):
        return []
    return _build_salt_graph(entity, mol)


def _gen_tautomer(entity: dict, mol: Chem.Mol, graph: _Graph) -> list[dict]:
    if is_single_atom(mol) or len(rdmolops.GetMolFrags(mol)) > 1:
        return []
    return _build_tautomer_graph(entity, mol)


_uncharger = rdMolStandardize.Uncharger()


def _gen_protonation(entity: dict, mol: Chem.Mol, graph: _Graph) -> list[dict]:
    """The uncharged parent and its pH 7.3 major microspecies, linked."""
    if is_single_atom(mol) or len(rdmolops.GetMolFrags(mol)) > 1:
        return []
    parent_mol = _uncharger.uncharge(mol)
    if not graph.first_visit("protonation", Chem.MolToSmiles(parent_mol)):
        return []
    converter = ChemConverter()
    parent = converter.convert(Chem.MolToSmiles(parent_mol))
    _assign_id(parent, parent_mol)  # the uncharger keeps some zwitterions
    ms_smiles = predict_major_microspecies(parent["smiles_string"])
    if ms_smiles is None:
        return []
    microspecies = converter.convert(ms_smiles)
    _assign_id(microspecies, Chem.MolFromSmiles(ms_smiles))
    if microspecies["id"] == parent["id"]:
        return [parent]

    links = [(parent["id"], "has_major_microspecies_at_pH7_3", microspecies["id"])]
    dq = Chem.GetFormalCharge(Chem.MolFromSmiles(ms_smiles)) - Chem.GetFormalCharge(parent_mol)
    if dq == 0:
        links += [
            (parent["id"], "tautomer_of", microspecies["id"]),
            (microspecies["id"], "tautomer_of", parent["id"]),
        ]
    elif abs(dq) == 1:
        base, acid = (microspecies, parent) if dq < 0 else (parent, microspecies)
        links += [
            (base["id"], "conjugate_base_of", acid["id"]),
            (acid["id"], "conjugate_acid_of", base["id"]),
        ]
    graph.pending_links.extend(links)
    return [parent, microspecies]


def _rekey(batch: list[dict]) -> list[dict]:
    """Apply :func:`_assign_id` to a generator's output, keeping its links valid.

    Generators that know nothing of zwitterions (stereo, salt) give one the
    InChIKey id of its uncharged form. Within one batch the zwitterion forms
    all come from the same input, so a plain old->new id map is unambiguous.
    """
    remap = {}
    for entity in batch:
        smiles = entity.get("smiles_string")
        mol = Chem.MolFromSmiles(smiles) if smiles else None
        if mol is None:
            continue
        old = entity["id"]
        _assign_id(entity, mol)
        if entity["id"] != old:
            remap[old] = entity["id"]
    rewrite_references(batch, remap)
    for entity in batch:  # racemates are keyed by an enantiomer's or the parent's key
        for old, new in remap.items():
            key, new_key = old.removeprefix("INCHIKEY:"), new.removeprefix("chemrof:")
            if entity["id"] == f"chemrof:rac-{key}":
                entity["id"] = f"chemrof:rac-{new_key}"
    return batch


def _net_charge(entity: dict) -> int:
    """Net charge from the SMILES (stereo classes have no ``elemental_charge`` slot)."""
    if "elemental_charge" in entity:
        return entity["elemental_charge"]
    mol = Chem.MolFromSmiles(entity.get("smiles_string", ""))
    return Chem.GetFormalCharge(mol) if mol is not None else 0


def _charge_suffix(charge: int) -> str:
    """ChEBI's charge suffix: ``(3-)``, ``(1+)``."""
    return f"({abs(charge)}{'-' if charge < 0 else '+'})"


def derive_names(entities: list[dict]) -> None:
    """Name unnamed entities after a named relative, ChEBI style (in place).

    An entity counts as unnamed while its name is its formula (the converter's
    default). Repeats until nothing changes, so names flow along chains, e.g.
    L-alanine -> L-alanine zwitterion.

    >>> ents = [
    ...     {"id": "a", "name": "citric acid", "has_major_microspecies_at_pH7_3": ["b"]},
    ...     {"id": "b", "name": "C6H5O7-3", "empirical_formula": "C6H5O7-3", "elemental_charge": -3},
    ... ]
    >>> derive_names(ents)
    >>> ents[1]["name"]
    'citric acid(3-)'
    """
    by_id = {e["id"]: e for e in entities}
    acid_of = {
        microspecies: e["id"]
        for e in entities
        for microspecies in e.get("has_major_microspecies_at_pH7_3", [])
    }

    def named(eid):
        e = by_id.get(eid)
        return e["name"] if e and e.get("name") and e.get("name") != e.get("empirical_formula") else None

    def unnamed(e):
        name = e.get("name")
        if _type(e) == "RacemicMixture":  # named rac-<formula> when generated
            agnostic = by_id.get(e.get("chirality_agnostic_form"), {})
            return not name or name == f"rac-{agnostic.get('empirical_formula')}"
        return not name or name == e.get("empirical_formula")

    changed = True
    while changed:
        changed = False
        for e in entities:
            if not unnamed(e):
                continue
            name = None
            if e["id"].startswith("chemrof:zwitterion-"):
                partner = next((t for t in e.get("tautomer_of", []) if named(t)), None)
                name = f"{named(partner)} zwitterion" if partner else None
            elif _type(e) == "RacemicMixture":
                agnostic = named(e.get("chirality_agnostic_form"))
                name = f"rac-{agnostic}" if agnostic else None
            elif _type(e) == "Enantiomer" and e.get("absolute_configuration"):
                agnostic = named(e.get("enantiomer_form_of"))
                name = f"{e['absolute_configuration']}-{agnostic}" if agnostic else None
            if name is None and named(acid_of.get(e["id"])):
                charge = _net_charge(e)
                if charge:
                    name = f"{named(acid_of[e['id']])}{_charge_suffix(charge)}"
            if name:
                e["name"] = name
                changed = True


# -- driver -----------------------------------------------------------------


def saturate(
    seeds: Iterable[str | dict],
    generators: Iterable[str] = DEFAULT_GENERATORS,
    max_entities: int = 100_000,
    max_rounds: int | None = None,
    max_siblings: int = DEFAULT_MAX_SIBLINGS,
    stats: SaturationStats | None = None,
    progress: Callable[[int, int], None] | None = None,
    finish: bool = True,
) -> list[dict]:
    """Close *seeds* under *generators*; return the entities in discovery order.

    Args:
        seeds: SMILES/InChI strings, or dicts with a ``structure`` key plus any
            slots to set on the seed entity, such as ``name``. An ``id`` (e.g. a
            CHEBI id) replaces the computed one once saturation is done.
        generators: Names from :data:`ALL_GENERATORS`.
        max_entities: Stop expanding past this many entities. Entities found
            after the limit are kept but not run through the generators.
        max_rounds: Stop after this many generations away from the seeds
            (``None``: run to fixpoint). Round 0 is the seeds themselves.
        max_siblings: Cap on stereoisomers per molecule.
        stats: Filled in with run counts, if given.
        progress: Called as ``progress(processed, total_entities)``.
        finish: If False, return ``(entities, seed_ids)`` without applying the
            seeds' ids or deriving names (for merging partial graphs).

    >>> ids = [e["id"] for e in saturate(["OC(=O)CC(O)(CC(O)=O)C(O)=O"])]  # citric acid
    >>> len(ids)   # citric acid and citrate(3-)
    2
    >>> saturate(["CCO"], generators=["protonation"])[0]["name"]
    'C2H6O'
    """
    generators = list(generators)
    unknown = set(generators) - set(ALL_GENERATORS)
    if unknown:
        raise ValueError(f"unknown generators: {sorted(unknown)}; choose from {ALL_GENERATORS}")
    stats = stats if stats is not None else SaturationStats()

    def run_generators(entity: dict, mol: Chem.Mol) -> list[dict]:
        found: list[dict] = []
        for name in generators:
            try:
                if name == "stereo":
                    batch = _gen_stereo(entity, mol, graph, max_siblings)
                elif name == "salt":
                    batch = _gen_salt(entity, mol, graph)
                elif name == "protonation":
                    batch = _gen_protonation(entity, mol, graph)
                else:
                    batch = _gen_tautomer(entity, mol, graph)
                found += _rekey(batch)
            except Exception as exc:  # one bad structure must not stop a large run
                logger.warning("%s generator failed on %s: %s", name, entity["id"], exc)
        return found

    graph = _Graph()
    converter = ChemConverter()
    queue: deque[tuple[str, int]] = deque()
    given_ids: dict[str, str] = {}

    for seed in seeds:
        extra = {}
        if isinstance(seed, dict):
            extra = {k: v for k, v in seed.items() if k != "structure" and v}
            seed = seed["structure"]
        try:
            entity = converter.convert_parsed(parse_input(seed))
        except Exception as exc:
            logger.warning("cannot parse seed %r: %s", seed, exc)
            stats.failed.append(seed)
            continue
        _assign_id(entity, Chem.MolFromSmiles(entity["smiles_string"]))
        if "id" in extra:
            given_ids[entity["id"]] = extra.pop("id")
        entity.update(extra)
        stats.seeds += 1
        if graph.add(entity):
            queue.append((entity["id"], 0))

    while queue:
        entity_id, depth = queue.popleft()
        stats.rounds = max(stats.rounds, depth)
        entity = graph.entities[entity_id]
        smiles = entity.get("isomeric_smiles_string") or entity.get("smiles_string")
        mol = Chem.MolFromSmiles(smiles) if smiles else None
        stats.processed += 1
        if progress:
            progress(stats.processed, len(graph.entities))
        if mol is None or (max_rounds is not None and depth >= max_rounds):
            continue
        for found in run_generators(entity, mol):
            if graph.add(found) and "smiles_string" in found:
                if len(graph.entities) >= max_entities:
                    stats.truncated = True
                    continue
                queue.append((found["id"], depth + 1))
        for link in graph.pending_links:
            graph.link(*link)
        graph.pending_links.clear()

    if stats.truncated:
        logger.warning("stopped enqueuing at %d entities (raise --max-entities)", max_entities)
    if not finish:
        return list(graph.entities.values()), given_ids
    return _finish(list(graph.entities.values()), given_ids)


def _finish(results: list[dict], given_ids: dict[str, str]) -> list[dict]:
    """Swap in the seeds' own ids and name what can be named."""
    for entity in results:
        entity["id"] = given_ids.get(entity["id"], entity["id"])
    rewrite_references(results, given_ids)
    derive_names(results)
    return results


def _saturate_chunk(args: tuple) -> tuple[list[dict], dict[str, str], SaturationStats]:
    seeds, kwargs = args
    from rdkit import RDLogger

    RDLogger.DisableLog("rdApp.*")
    stats = SaturationStats()
    entities, given_ids = saturate(seeds, stats=stats, finish=False, **kwargs)
    return entities, given_ids, stats


def saturate_parallel(
    seeds: list[str | dict],
    workers: int,
    chunk_size: int = 100,
    stats: SaturationStats | None = None,
    progress: Callable[[int, int], None] | None = None,
    **kwargs,
) -> list[dict]:
    """:func:`saturate`, with the seeds split into chunks run in *workers* processes.

    Chunks are saturated independently and their graphs merged by id, so a
    family reached from seeds in two chunks is built twice but stored once.
    ``max_entities`` applies per chunk.

    Args:
        progress: Called as ``progress(seeds_done, total_seeds)``.
    """
    from multiprocessing import Pool

    stats = stats if stats is not None else SaturationStats()
    chunks = [seeds[i : i + chunk_size] for i in range(0, len(seeds), chunk_size)]
    graph = _Graph()
    given_ids: dict[str, str] = {}
    done = 0
    with Pool(workers) as pool:
        for entities, chunk_ids, chunk_stats in pool.imap(
            _saturate_chunk, [(chunk, kwargs) for chunk in chunks]
        ):
            for entity in entities:
                existing = graph.entities.get(entity["id"])
                if existing is None:
                    graph.entities[entity["id"]] = entity
                else:
                    _merge(existing, entity)
            given_ids.update(chunk_ids)
            stats.seeds += chunk_stats.seeds
            stats.processed += chunk_stats.processed
            stats.rounds = max(stats.rounds, chunk_stats.rounds)
            stats.failed += chunk_stats.failed
            stats.truncated = stats.truncated or chunk_stats.truncated
            done += chunk_stats.seeds + len(chunk_stats.failed)
            if progress:
                progress(done, len(seeds))
    return _finish(list(graph.entities.values()), given_ids)
