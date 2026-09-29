import sys,pandas as pd
from rdkit import Chem, RDLogger; RDLogger.DisableLog('rdApp.*')
b=pd.read_csv(sys.argv[1],sep='\t',dtype=str); f=b[b.okid=='False']
def chg(s):
    m=Chem.MolFromSmiles(s) if isinstance(s,str) else None
    if not m: return None
    return (sum(a.GetFormalCharge()>0 for a in m.GetAtoms()), sum(a.GetFormalCharge()<0 for a in m.GetAtoms()))
f=f.assign(pc=f.pred.map(chg),tc=f.tgt_can.map(chg))
f['kind']=[('pos' if p[0]>t[0] else 'POS' if p[0]<t[0] else '')+('neg' if p[1]>t[1] else 'NEG' if p[1]<t[1] else '') if p and t else 'err' for p,t in zip(f.pc,f.tc)]
print(f.groupby(['identity','kind']).size().sort_values(ascending=False).head(15))
n=int(sys.argv[3]) if len(sys.argv)>3 else 8
for k in sys.argv[2].split(','):
    idn,kind=k.split(':')
    print('=====',k)
    print(f[(f.identity==idn)&(f.kind==kind)].sample(n,random_state=1)[['src','src_name','pred','tgt_can']].to_string(max_colwidth=90))
