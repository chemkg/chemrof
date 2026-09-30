import pandas as pd, hashlib
from rdkit import Chem, RDLogger; RDLogger.DisableLog('rdApp.*')
s=pd.read_csv('data/chebi_smiles.tsv',sep='\t',dtype=str).set_index('compound_id')
r=pd.read_csv('data/chebi_pH7_3_mapping.tsv',sep='\t',dtype=str)
r.columns=['src','tgt','origin']
def can(smi):
    m=Chem.MolFromSmiles(smi) if isinstance(smi,str) else None
    return Chem.MolToSmiles(m) if m else None
r['src_name']=r.src.map(s.name); r['tgt_name']=r.tgt.map(s.name)
r['src_smiles']=r.src.map(s.smiles); r['tgt_smiles']=r.tgt.map(s.smiles)
n0=len(r); r=r.dropna(subset=['src_smiles','tgt_smiles'])
r['src_can']=r.src_smiles.map(can); r['tgt_can']=r.tgt_smiles.map(can)
r=r.dropna(subset=['src_can','tgt_can'])
# skip polymers / R-groups / wildcard atoms: can't be protonated meaningfully
r=r[~r.src_can.str.contains(r'\*') & ~r.tgt_can.str.contains(r'\*')]
# Split by target ID so every protonation form of a compound lands together.
# train (80%): rules may be written from it and its failures read.
# The original 20% test split had its aggregate score checked ~5 times while the
# first rule set was developed, but its failures were never read. From
# 2026-09-30 it is halved: dev drives accept/reject decisions, sealed is
# scored only via `evalr.py --unseal` (each use is logged).
def split(tgt):
    if int(hashlib.md5(tgt.encode()).hexdigest(), 16) % 5:
        return 'train'
    return 'sealed' if int(hashlib.sha1(('sealed:' + tgt).encode()).hexdigest(), 16) % 2 else 'dev'
r['split']=r.tgt.map(split)
r['identity']=r.src==r.tgt
print(n0,len(r)); print(r.groupby(['split','identity']).size()); print(r.origin.value_counts())
r.to_csv('data/bench.tsv',sep='\t',index=False)
