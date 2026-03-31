"""Parse InChI strings into chemrof sublayer slots.

InChI format: InChI=1S/<formula>/c<connections>/h<hydrogens>/q<charge>/p<proton>/...

Reference: https://www.inchi-trust.org/technical-faq/

>>> parse_inchi_sublayers("InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3")
{'inchi_chemical_sublayer': 'C2H6O', 'inchi_atom_connections_sublayer': '1-2-3', 'inchi_hydrogen_connections_sublayer': '3H,2H2,1H3'}
"""

from __future__ import annotations

import re

# Map InChI layer prefix to chemrof slot name
_LAYER_MAP = {
    "c": "inchi_atom_connections_sublayer",
    "h": "inchi_hydrogen_connections_sublayer",
    "q": "inchi_charge_sublayer",
    "p": "inchi_proton_sublayer",
    "b": "inchi_stereochemical_double_bond_sublayer",
    "t": "inchi_tetrahedral_stereochemical_sublayer",
    "s": "inchi_stereochemical_type_sublayer",
    "i": "inchi_isotopic_layer",
}


def parse_inchi_sublayers(inchi: str) -> dict[str, str]:
    """Decompose an InChI string into chemrof sublayer slots.

    Returns a dict with only the sublayers present in the input.
    Returns empty dict for invalid or empty input.

    >>> parse_inchi_sublayers("InChI=1S/Ca/q+2")
    {'inchi_chemical_sublayer': 'Ca', 'inchi_charge_sublayer': '+2'}

    >>> parse_inchi_sublayers("")
    {}
    """
    if not inchi or not inchi.startswith("InChI="):
        return {}

    # Strip "InChI=1S/" or "InChI=1/" prefix
    body = re.sub(r"^InChI=1S?/", "", inchi)

    # Split on "/" to get layers
    layers = body.split("/")
    if not layers:
        return {}

    result: dict[str, str] = {}

    # First layer is always the chemical formula (no prefix letter)
    result["inchi_chemical_sublayer"] = layers[0]

    # Remaining layers have single-letter prefixes
    for layer in layers[1:]:
        if not layer:
            continue
        prefix = layer[0]
        value = layer[1:]
        slot = _LAYER_MAP.get(prefix)
        if slot:
            result[slot] = value

    return result
