"""Backward-compatible SMILES converter imports.

The converter implementation now lives in ``chemrof.converter.convert`` and
accepts both SMILES and InChI inputs.
"""

from chemrof.converter.convert import ChemConverter, SmilesConverter

__all__ = ["ChemConverter", "SmilesConverter"]
