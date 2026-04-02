"""Convert chemical inputs to chemrof-compliant dicts.

>>> converter = ChemConverter()
>>> result = converter.convert("CCO")
>>> result["type"]
'chemrof:SmallMolecule'
>>> result["empirical_formula"]
'C2H6O'
>>> result = converter.convert("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3")
>>> result["type"]
'chemrof:SmallMolecule'
"""

from __future__ import annotations

from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors, inchi, FindMolChiralCenters

from chemrof.converter.classify import classify_entity
from chemrof.converter.enrichers.base import Enricher, EnrichmentContext
from chemrof.converter.inchi import parse_inchi_sublayers
from chemrof.converter.parse import ParsedInput, parse_input


# chemrof type URI prefix
_TYPE_PREFIX = "chemrof:"

# Types where elemental_charge applies
_ION_TYPES = {"AtomCation", "AtomAnion", "MolecularCation", "MolecularAnion"}
_MONOATOMIC_TYPES = {"AtomCation", "AtomAnion", "UnchargedAtom"}


class ChemConverter:
    """Converts chemical input strings to chemrof-compliant dicts.

    Accepts SMILES or InChI strings (auto-detected).

    >>> ChemConverter().convert("[Ca+2]")["type"]
    'chemrof:AtomCation'
    """

    def __init__(self, enrichers: list[Enricher] | None = None):
        self.enrichers: list[Enricher] = enrichers or []

    def convert(self, raw: str) -> dict:
        """Parse an input string and return a chemrof dict.

        Args:
            raw: A SMILES or InChI string.

        Returns:
            A dict with chemrof slots populated.

        Raises:
            ValueError: If RDKit cannot parse the input.
        """
        parsed = parse_input(raw)
        return self.convert_parsed(parsed)

    def convert_parsed(self, parsed: ParsedInput) -> dict:
        """Convert a pre-parsed input to a chemrof dict."""
        entity_type = classify_entity(parsed.mol)
        obj = self._populate(parsed, entity_type)

        # Run enricher pipeline
        inchikey = obj.get("id", "").replace("INCHIKEY:", "")
        context = EnrichmentContext(
            mol=parsed.mol,
            inchikey=inchikey,
            smiles=obj.get("smiles_string", ""),
            inchi=obj.get("inchi_string", ""),
        )
        for enricher in self.enrichers:
            obj = enricher.enrich(obj, context)

        return obj

    def _populate(self, parsed: ParsedInput, entity_type: str) -> dict:
        """Fill chemrof slots from the parsed input."""
        mol = parsed.mol

        # Canonical SMILES
        canonical = Chem.MolToSmiles(mol)

        # InChI and InChIKey
        inchi_str = inchi.MolToInchi(mol) or ""
        inchikey = inchi.InchiToInchiKey(inchi_str) if inchi_str else ""

        # Molecular formula
        formula = rdMolDescriptors.CalcMolFormula(mol)

        # Molecular mass (exact)
        mass = Descriptors.ExactMolWt(mol)

        # Net formal charge
        charge = sum(atom.GetFormalCharge() for atom in mol.GetAtoms())

        # Radical check
        has_radical = any(atom.GetNumRadicalElectrons() > 0 for atom in mol.GetAtoms())

        # Is organic (contains carbon)
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

        # InChI sublayers
        sublayers = parse_inchi_sublayers(inchi_str)
        obj.update(sublayers)

        # Charge-related slots
        if entity_type in _ION_TYPES:
            obj["elemental_charge"] = charge

        # Monoatomic: has_element
        if entity_type in _MONOATOMIC_TYPES:
            obj["has_element"] = mol.GetAtomWithIdx(0).GetSymbol()

        # Boolean flags
        if has_carbon:
            obj["is_organic"] = True
        if has_radical:
            obj["is_radical"] = True

        # Enantiomer-specific slots
        if entity_type == "Enantiomer":
            obj["isomeric_smiles_string"] = Chem.MolToSmiles(mol, isomericSmiles=True)
            chiral_centers = FindMolChiralCenters(mol)
            if len(chiral_centers) == 1:
                obj["absolute_configuration"] = f"({chiral_centers[0][1]})"

        return obj


# Backwards-compatible alias
SmilesConverter = ChemConverter
