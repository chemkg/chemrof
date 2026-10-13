"""Generate the "siblings" of a chemical input: the other members of its family.

* **Atoms** (neutral, ionic or isotope-labelled): every species of the same
  element -- the neutral atom, the monoatomic ions and the isotopes known to
  ChEBI (see :mod:`chemrof.converter.species`), plus the naturally occurring
  isotopes.
* **Molecules** with stereo elements: the stereo-agnostic parent and every
  stereoisomer of it. Chiral stereoisomers become ``Enantiomer`` entities
  (linked to the parent by ``enantiomer_form_of``); achiral ones (meso forms,
  cis/trans isomers) become ``Stereoisomer``. Each mirror-image pair is grouped
  in a ``RacemicMixture``.

The input need not be one of the siblings' canonical forms: any member of the
family yields the whole family.

>>> from chemrof.converter.convert import ChemConverter
>>> from chemrof.converter.parse import parse_input
>>> parsed = parse_input("[Fe+3]")
>>> family = siblings(ChemConverter().convert_parsed(parsed), parsed.mol)
>>> [e["name"] for e in family][:4]
['Fe', '54Fe', '56Fe', '57Fe']
>>> parsed = parse_input("CC(O)C(C)O")   # butane-2,3-diol: (R,R)/(S,S) pair + meso
>>> family = siblings(ChemConverter().convert_parsed(parsed), parsed.mol)
>>> sorted(e["type"].split(":")[1] for e in family)
['Enantiomer', 'Enantiomer', 'RacemicMixture', 'SmallMolecule', 'Stereoisomer']
"""

from __future__ import annotations

import logging

from rdkit import Chem
from rdkit.Chem import EnumerateStereoisomers, FindMolChiralCenters, inchi

from chemrof.converter.atoms import is_single_atom
from chemrof.converter.autochain import _mol_to_entity, _strip_stereo
from chemrof.converter.classify import _is_salt
from chemrof.converter.convert import ChemConverter
from chemrof.converter.parse import parse_input
from chemrof.converter.species import species_of_element

logger = logging.getLogger(__name__)

DEFAULT_MAX_SIBLINGS = 64
_TYPE_PREFIX = "chemrof:"


def siblings(entity: dict, mol: Chem.Mol, max_siblings: int = DEFAULT_MAX_SIBLINGS) -> list[dict]:
    """Return the entity's whole family as a list of chemrof dicts.

    Falls back to ``[entity]`` (with a warning) when the input has no siblings
    to generate, e.g. an achiral molecule or a salt.

    Args:
        entity: The chemrof dict from the converter.
        mol: The RDKit Mol it came from.
        max_siblings: Cap on generated stereoisomers (``2**n`` grows quickly).
    """
    if is_single_atom(mol):
        return _element_siblings(entity, mol)
    if _is_salt(mol):
        logger.warning("--siblings does not apply to salts; use --classes ChemicalSalt")
        return [entity]
    return _stereo_siblings(entity, mol, max_siblings)


# -- atoms -----------------------------------------------------------------


def _element_siblings(entity: dict, mol: Chem.Mol) -> list[dict]:
    """The neutral atom, natural isotopes, and ChEBI-known ions/isotopes of the element."""
    z = mol.GetAtomWithIdx(0).GetAtomicNum()
    symbol = mol.GetAtomWithIdx(0).GetSymbol()
    pt = Chem.GetPeriodicTable()

    smiles: dict[str, tuple] = {f"[{symbol}]": (0, 0, 0)}  # neutral, unlabelled atom first
    for mass in range(1, 400):
        if pt.GetAbundanceForIsotope(z, mass) > 0:
            smiles[f"[{mass}{symbol}]"] = (1, mass, 0)
    for sp in species_of_element(z):
        smiles.setdefault(sp.smiles, (1 if sp.charge == 0 else 2, sp.mass_number or 0, sp.charge))

    converter = ChemConverter()
    results, seen = [], set()
    for smi in sorted(smiles, key=smiles.get):
        obj = converter.convert(smi)
        if obj["id"] not in seen:
            seen.add(obj["id"])
            results.append(obj)

    if entity["id"] not in seen:  # e.g. a charge state ChEBI has no class for
        results.append(entity)
    return results


# -- molecules -------------------------------------------------------------


def _mirror(mol: Chem.Mol) -> Chem.Mol:
    """The mirror image: every tetrahedral center inverted."""
    mirror = Chem.RWMol(mol)
    for atom in mirror.GetAtoms():
        tag = atom.GetChiralTag()
        if tag == Chem.ChiralType.CHI_TETRAHEDRAL_CW:
            atom.SetChiralTag(Chem.ChiralType.CHI_TETRAHEDRAL_CCW)
        elif tag == Chem.ChiralType.CHI_TETRAHEDRAL_CCW:
            atom.SetChiralTag(Chem.ChiralType.CHI_TETRAHEDRAL_CW)
    return mirror.GetMol()


def _stereo_siblings(entity: dict, mol: Chem.Mol, max_siblings: int) -> list[dict]:
    agnostic_mol = _strip_stereo(mol)
    total = EnumerateStereoisomers.GetStereoisomerCount(agnostic_mol)
    if total <= 1:
        logger.warning("No stereo elements found -- no stereoisomers to generate")
        return [entity]
    if total > max_siblings:
        logger.warning(
            "%d stereoisomers possible; generating only the first %d (raise --max-siblings)",
            total,
            max_siblings,
        )

    agnostic = _mol_to_entity(agnostic_mol, "SmallMolecule")
    opts = EnumerateStereoisomers.StereoEnumerationOptions(
        unique=True, tryEmbedding=False, maxIsomers=max_siblings
    )
    isomer_mols = list(EnumerateStereoisomers.EnumerateStereoisomers(agnostic_mol, options=opts))
    by_smiles = {Chem.MolToSmiles(m): m for m in isomer_mols}

    isomers: dict[str, dict] = {}  # isomeric SMILES -> entity
    for smiles, iso_mol in by_smiles.items():
        chiral = Chem.MolToSmiles(_mirror(iso_mol)) != smiles
        ent = _mol_to_entity(iso_mol, "Enantiomer" if chiral else "Stereoisomer")
        ent["isomeric_smiles_string"] = smiles
        if chiral:
            ent["enantiomer_form_of"] = agnostic["id"]
            centers = FindMolChiralCenters(iso_mol)
            if len(centers) == 1:
                ent["absolute_configuration"] = f"({centers[0][1]})"
        isomers[smiles] = ent

    # Group each mirror-image pair (both members present) in a racemic mixture
    pairs = []
    for smiles, ent in isomers.items():
        mirror_smiles = Chem.MolToSmiles(_mirror(by_smiles[smiles]))
        if mirror_smiles != smiles and mirror_smiles in isomers:
            left, right = sorted((ent, isomers[mirror_smiles]), key=lambda e: e["id"])
            if (left["id"], right["id"]) not in {(p[0]["id"], p[1]["id"]) for p in pairs}:
                pairs.append((left, right))

    agnostic_key = agnostic["id"].replace("INCHIKEY:", "")
    mixtures = []
    for left, right in pairs:
        # a lone enantiomer pair keeps the id `--classes RacemicMixture` gives it; with
        # more stereoisomers there are several racemates, each keyed by its left
        # enantiomer. Depends on `total`, not on the cap, so ids don't change with it.
        key = agnostic_key if total == 2 else left["id"].replace("INCHIKEY:", "")
        mixtures.append(
            {
                "id": f"chemrof:rac-{key}",
                "name": f"rac-{agnostic['name']}",
                "type": f"{_TYPE_PREFIX}RacemicMixture",
                "has_left_enantiomer": left["id"],
                "has_right_enantiomer": right["id"],
                "chirality_agnostic_form": agnostic["id"],
            }
        )
    return [agnostic, *isomers.values(), *mixtures]
