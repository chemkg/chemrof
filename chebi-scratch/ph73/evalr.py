"""Evaluate a predictor module (predict(smiles)->smiles) on bench.tsv."""
import sys, importlib, time, pandas as pd
from multiprocessing import Pool
from rdkit import Chem, RDLogger; RDLogger.DisableLog('rdApp.*')
mod=importlib.import_module(sys.argv[1]); split=sys.argv[2] if len(sys.argv)>2 else 'train'
limit=int(sys.argv[3]) if len(sys.argv)>3 else 0
def run(smi):
    try:
        p=mod.predict(smi); m=Chem.MolFromSmiles(p) if p else None
        return Chem.MolToSmiles(m) if m else None
    except Exception as e:
        return None
if __name__=='__main__':
    b=pd.read_csv('data/bench.tsv',sep='\t',dtype=str)
    b['identity']=b.identity=='True'
    if split!='all': b=b[b.split==split]
    if limit: b=b.sample(limit,random_state=0)
    t=time.time()
    with Pool(4) as p: b['pred']=p.map(run,b.src_can.tolist(),chunksize=200)
    b['ok']=b.pred==b.tgt_can
    import pickle; idx=pickle.load(open('data/chebi_can_idx.pkl','rb'))
    b['pred_id']=[ (tgt if tgt in idx.get(p,()) else (sorted(idx[p])[0] if p in idx else src)) for p,src,tgt in zip(b.pred,b.src,b.tgt)]
    b['okid']=b.pred_id==b.tgt
    print(f"ID-level: all={b.okid.mean():.4f} changed={b[~b.identity].okid.mean():.4f} unchanged={b[b.identity].okid.mean():.4f}")
    print(f"STRUCT {sys.argv[1]} [{split}] n={len(b)} {time.time()-t:.0f}s  all={b.ok.mean():.4f}  changed={b[~b.identity].ok.mean():.4f} ({(~b.identity).sum()})  unchanged={b[b.identity].ok.mean():.4f} ({b.identity.sum()})")
    b.to_csv(f'data/out_{sys.argv[1]}_{split}.tsv',sep='\t',index=False)
