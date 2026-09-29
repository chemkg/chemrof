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
r['split']=r.tgt.map(lambda x: 'test' if int(hashlib.md5(x.encode()).hexdigest(),16)%5==0 else 'train')
r['identity']=r.src==r.tgt
print(n0,len(r)); print(r.groupby(['split','identity']).size()); print(r.origin.value_counts())
r.to_csv('data/bench.tsv',sep='\t',index=False)
