"""Convert SMILES strings to chemrof-compliant dicts.

>>> converter = SmilesConverter()
>>> result = converter.convert("CCO")
>>> result["type"]
'chemrof:SmallMolecule'
>>> result["empirical_formula"]
'C2H6O'
"""

from __future__ import annotations

from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors, inchi

from chemrof.converter.classify import classify_entity
from chemrof.converter.enrichers.base import Enricher, EnrichmentContext
from chemrof.converter.inchi import parse_inchi_sublayers


# chemrof type URI prefix
_TYPE_PREFIX = "chemrof:"

# Types where elemental_charge applies
_ION_TYPES = {"AtomCation", "AtomAnion", "MolecularCation", "MolecularAnion"}
_MONOATOMIC_TYPES = {"AtomCation", "AtomAnion", "UnchargedAtom"}


class SmilesConverter:
    """Converts SMILES strings to chemrof-compliant dicts.

    Attributes:
        enrichers: Ordered list of Enricher instances to run after
            structural slot population.
    """

    def __init__(self, enrichers: list[Enricher] | None = None):
        self.enrichers: list[Enricher] = enrichers or []

    def convert(self, smiles: str) -> dict:
        """Parse a SMILES string and return a chemrof dict.

        Args:
            smiles: A SMILES string.

        Returns:
            A dict with chemrof slots populated.

        Raises:
            ValueError: If RDKit cannot parse the SMILES.
        """
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            raise ValueError(f"RDKit could not parse SMILES: {smiles!r}")

        entity_type = classify_entity(mol)
        obj = self._populate(mol, smiles, entity_type)

        # Run enricher pipeline
        inchikey = obj.get("id", "").replace("INCHIKEY:", "")
        context = EnrichmentContext(
            mol=mol,
            inchikey=inchikey,
            smiles=smiles,
            inchi=obj.get("inchi_string", ""),
        )
        for enricher in self.enrichers:
            obj = enricher.enrich(obj, context)

        return obj

    def _populate(self, mol: Chem.Mol, smiles: str, entity_type: str) -> dict:
        """Fill chemrof slots from the RDKit mol."""
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

        # Boolean flags (only include if True, following existing example style)
        if has_carbon:
            obj["is_organic"] = True
        if has_radical:
            obj["is_radical"] = True

        return obj
