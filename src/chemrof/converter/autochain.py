"""Generate interlinked entity graphs from a single chemical input.

Given a chemrof entity dict and a set of target classes, autochain
generates dependent entities (enantiomers, racemic mixtures) with
proper relationship slots populated.

>>> from chemrof.converter.convert import ChemConverter
>>> from rdkit import Chem
>>> entity = ChemConverter().convert("CC(N)C(=O)O")
>>> mol = Chem.MolFromSmiles("CC(N)C(=O)O")
>>> results = autochain(entity, {"RacemicMixture"}, mol)
>>> len(results)
4
"""

from __future__ import annotations

import logging

from rdkit import Chem
from rdkit.Chem import (
    Descriptors,
    EnumerateStereoisomers,
    FindMolChiralCenters,
    inchi,
    rdMolDescriptors,
    rdmolops,
)

from chemrof.converter.classify import classify_entity
from chemrof.converter.inchi import parse_inchi_sublayers

logger = logging.getLogger(__name__)

_TYPE_PREFIX = "chemrof:"


def autochain(entity: dict, target_classes: set[str], mol: Chem.Mol) -> list[dict]:
    """Generate dependent entities for target classes.

    Returns a list of chemrof dicts including the original entity
    and all generated dependents, with relationship slots populated.

    Args:
        entity: The chemrof dict from the converter.
        target_classes: Set of chemrof class names (e.g. ``{"RacemicMixture"}``).
        mol: The RDKit Mol for the input.

    Returns:
        List of interlinked chemrof dicts.
    """
    # Salt autochain
    if "ChemicalSalt" in target_classes or entity.get("type") == "chemrof:ChemicalSalt":
        return _build_salt_graph(entity, mol)

    wants_racemate = "RacemicMixture" in target_classes
    wants_enantiomers = "Enantiomer" in target_classes or wants_racemate

    if not wants_enantiomers:
        return [entity]

    # Check stereocenter count — v1 only supports single stereocenter
    chiral_centers = FindMolChiralCenters(mol, includeUnassigned=True)
    if len(chiral_centers) == 0:
        logger.warning("No stereocenters found — cannot generate enantiomers")
        return [entity]
    if len(chiral_centers) > 1:
        logger.warning(
            "Multiple stereocenters (%d) — autochain v1 only supports single stereocenter",
            len(chiral_centers),
        )
        return [entity]

    return _build_stereo_graph(entity, mol, wants_racemate)


def _strip_stereo(mol: Chem.Mol) -> Chem.Mol:
    """Return a copy of mol with all stereochemistry removed."""
    mol_copy = Chem.RWMol(mol)
    Chem.RemoveStereochemistry(mol_copy)
    return mol_copy.GetMol()


def _mol_to_entity(mol: Chem.Mol, entity_type: str) -> dict:
    """Build a basic chemrof dict from an RDKit mol."""
    canonical = Chem.MolToSmiles(mol)
    inchi_str = inchi.MolToInchi(mol) or ""
    inchikey = inchi.InchiToInchiKey(inchi_str) if inchi_str else ""
    formula = rdMolDescriptors.CalcMolFormula(mol)
    mass = Descriptors.ExactMolWt(mol)
    has_carbon = any(atom.GetAtomicNum() == 6 for atom in mol.GetAtoms())

    obj: dict = {
        "id": f"INCHIKEY:{inchikey}" if inchikey else f"smiles:{canonical}",
        "name": formula,
        "type": f"{_TYPE_PREFIX}{entity_type}",
        "smiles_string": canonical,
        "inchi_string": inchi_str,
        "empirical_formula": formula,
        "molecular_mass": round(mass, 4),
    }

    sublayers = parse_inchi_sublayers(inchi_str)
    obj.update(sublayers)

    if has_carbon:
        obj["is_organic"] = True

    return obj


def _build_stereo_graph(entity: dict, mol: Chem.Mol, include_mixture: bool) -> list[dict]:
    """Build the full stereoisomer entity graph for a single-stereocenter molecule."""
    # Step 1: Get the agnostic form
    agnostic_mol = _strip_stereo(mol)
    agnostic = _mol_to_entity(agnostic_mol, "SmallMolecule")

    # Step 2: Enumerate enantiomers from the agnostic mol
    opts = EnumerateStereoisomers.StereoEnumerationOptions(unique=True)
    isomers = list(EnumerateStereoisomers.EnumerateStereoisomers(agnostic_mol, options=opts))

    enantiomers = []
    for iso_mol in isomers:
        enantiomer = _mol_to_entity(iso_mol, "Enantiomer")
        enantiomer["enantiomer_form_of"] = agnostic["id"]
        enantiomer["isomeric_smiles_string"] = Chem.MolToSmiles(iso_mol, isomericSmiles=True)

        centers = FindMolChiralCenters(iso_mol)
        if len(centers) == 1:
            enantiomer["absolute_configuration"] = f"({centers[0][1]})"

        enantiomers.append(enantiomer)

    results = [agnostic] + enantiomers

    # Step 3: Build RacemicMixture if requested
    if include_mixture and len(enantiomers) == 2:
        agnostic_inchikey = agnostic["id"].replace("INCHIKEY:", "")
        mixture: dict = {
            "id": f"chemrof:rac-{agnostic_inchikey}",
            "name": f"rac-{agnostic['name']}",
            "type": f"{_TYPE_PREFIX}RacemicMixture",
            "has_left_enantiomer": enantiomers[0]["id"],
            "has_right_enantiomer": enantiomers[1]["id"],
            "chirality_agnostic_form": agnostic["id"],
        }
        results.append(mixture)

    return results


def _build_salt_graph(entity: dict, mol: Chem.Mol) -> list[dict]:
    """Decompose a salt into cation/anion component entities plus the salt entity.

    Returns [cation, anion, ..., salt] where:
    - Each fragment becomes a typed entity (AtomCation, MolecularAnion, etc.)
    - The salt entity links to components via has_cationic_component / has_anionic_component

    >>> from rdkit import Chem
    >>> from chemrof.converter.convert import ChemConverter
    >>> entity = ChemConverter().convert("[Na+].[Cl-]")
    >>> results = _build_salt_graph(entity, Chem.MolFromSmiles("[Na+].[Cl-]"))
    >>> len(results)
    3
    >>> results[-1]["type"]
    'chemrof:ChemicalSalt'
    """
    frags = rdmolops.GetMolFrags(mol, asMols=True)
    cations = []
    anions = []
    components = []

    for frag in frags:
        frag_charge = sum(a.GetFormalCharge() for a in frag.GetAtoms())
        frag_type = classify_entity(frag)
        comp = _mol_to_entity(frag, frag_type)
        if frag_type in ("AtomCation", "AtomAnion", "UnchargedAtom"):
            comp["has_element"] = frag.GetAtomWithIdx(0).GetSymbol()
        if frag_charge > 0:
            comp["elemental_charge"] = frag_charge
            cations.append(comp)
        elif frag_charge < 0:
            comp["elemental_charge"] = frag_charge
            anions.append(comp)
        components.append(comp)

    # Build the salt entity — it keeps the full salt's structural data
    salt = dict(entity)
    salt["type"] = f"{_TYPE_PREFIX}ChemicalSalt"
    salt["elemental_charge"] = 0
    if cations:
        salt["has_cationic_component"] = cations[0]["id"]
    if anions:
        salt["has_anionic_component"] = anions[0]["id"]

    return components + [salt]
