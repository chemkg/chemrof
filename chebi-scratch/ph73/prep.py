"""Build data/chebi_smiles.tsv: one SMILES per ChEBI compound.

The ChEBI flat-file SMILES drop the H on some aromatic NH atoms (indoles,
purines, pterins...), so ~6k Rhea-mapped entries do not parse. For those the
SMILES is regenerated from the molfile, which keeps the hydrogens.
"""
import csv, sys
import pandas as pd
from rdkit import Chem, RDLogger
RDLogger.DisableLog('rdApp.*')
csv.field_size_limit(sys.maxsize)

s = pd.read_csv('data/structures.tsv.gz', sep='\t', dtype=str, engine='python',
                usecols=['compound_id', 'molfile', 'smiles', 'standard_inchi_key', 'default_structure'])
if s.default_structure.notna().any():
    s = s[s.default_structure.str.lower().isin(['t', 'true', '1'])]
s = s.drop_duplicates('compound_id')


def fix(row):
    smi = row.smiles if isinstance(row.smiles, str) else None
    if smi and Chem.MolFromSmiles(smi) is not None:
        return smi, 'smiles'
    m = Chem.MolFromMolBlock(row.molfile) if isinstance(row.molfile, str) else None
    if m is not None:
        return Chem.MolToSmiles(m), 'molfile'
    return smi, 'unparsed'


s[['smiles', 'smiles_source']] = [fix(r) for r in s.itertuples()]
s = s.dropna(subset=['smiles'])
c = pd.read_csv('data/compounds.tsv.gz', sep='\t', usecols=['id', 'name'], dtype=str)
s = s.merge(c, left_on='compound_id', right_on='id', how='left')
s = s[['compound_id', 'name', 'smiles', 'standard_inchi_key', 'smiles_source']]
s.to_csv('data/chebi_smiles.tsv', sep='\t', index=False)
print(len(s)); print(s.smiles_source.value_counts())
