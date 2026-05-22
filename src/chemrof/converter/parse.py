"""Detect input format (SMILES vs InChI) and parse to RDKit Mol.

>>> parse_input("CCO").input_format
'smiles'
>>> parse_input("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3").input_format
'inchi'
>>> parse_input("InChI=1/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/s3").is_racemic
True
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rdkit.Chem import Mol


@dataclass
class ParsedInput:
    """Result of parsing a chemical input string.

    Attributes:
        mol: RDKit Mol object.
        input_format: Detected format — ``"smiles"`` or ``"inchi"``.
        original: The raw input string.
        inchi_stereo_type: The ``/s`` layer value (e.g. ``"s1"``, ``"s3"``), or ``""`` if absent.
        is_racemic: True when ``inchi_stereo_type`` is ``"s3"``.
    """

    mol: Mol
    input_format: str
    original: str
    inchi_stereo_type: str = ""
    is_racemic: bool = False


def _extract_inchi_stereo_type(inchi: str) -> str:
    """Extract the /s layer from an InChI string.

    >>> _extract_inchi_stereo_type("InChI=1S/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/m1/s1")
    's1'
    >>> _extract_inchi_stereo_type("InChI=1/C3H7NO2/c1-2(4)3(5)6/h2H,4H2,1H3,(H,5,6)/t2-/s3")
    's3'
    >>> _extract_inchi_stereo_type("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3")
    ''
    """
    match = re.search(r"/(s\d+)", inchi)
    return match.group(1) if match else ""


def parse_input(raw: str) -> ParsedInput:
    """Parse a SMILES or InChI string into a ``ParsedInput``.

    Raises:
        ValueError: If the string cannot be parsed by RDKit.
    """
    if raw.startswith("InChI="):
        return _parse_inchi(raw)
    return _parse_smiles(raw)


def _parse_smiles(smiles: str) -> ParsedInput:
    from rdkit import Chem

    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"RDKit could not parse SMILES: {smiles!r}")
    return ParsedInput(mol=mol, input_format="smiles", original=smiles)


def _parse_inchi(inchi: str) -> ParsedInput:
    from rdkit.Chem import inchi as rdkit_inchi

    stereo_type = _extract_inchi_stereo_type(inchi)
    mol = rdkit_inchi.MolFromInchi(inchi)
    if mol is None:
        raise ValueError(f"RDKit could not parse InChI: {inchi!r}")
    return ParsedInput(
        mol=mol,
        input_format="inchi",
        original=inchi,
        inchi_stereo_type=stereo_type,
        is_racemic=(stereo_type == "s3"),
    )
