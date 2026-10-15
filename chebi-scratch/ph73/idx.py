import pandas as pd, pickle
from multiprocessing import Pool
from rdkit import Chem, RDLogger; RDLogger.DisableLog('rdApp.*')
def can(s):
    m=Chem.MolFromSmiles(s) if isinstance(s,str) else None
    return Chem.MolToSmiles(m) if m else None
if __name__=='__main__':
    s=pd.read_csv('data/chebi_smiles.tsv',sep='\t',dtype=str)
    with Pool(4) as p: s['can']=p.map(can,s.smiles.tolist(),chunksize=500)
    idx={}
    for i,c in zip(s.compound_id,s.can):
        if c: idx.setdefault(c,set()).add(i)
    pickle.dump(idx,open('data/chebi_can_idx.pkl','wb')); print(len(idx))
