"""audit.py SMARTS [SMARTS...]: for reliable train targets, tally the charge Rhea gives atom :1 (matched on the neutralised target)."""
import sys, pandas as pd, collections
from rdkit import Chem, RDLogger; RDLogger.DisableLog('rdApp.*')
from rdkit.Chem.MolStandardize import rdMolStandardize
U=rdMolStandardize.Uncharger()
b=pd.read_csv('data/bench.tsv',sep='\t',dtype=str); b=b[b.split=='train']
multi=b.tgt.value_counts(); b=b[b.tgt.map(multi)>=2].drop_duplicates('tgt')
mols=[(t,n,Chem.MolFromSmiles(s)) for t,n,s in zip(b.tgt,b.tgt_name,b.tgt_can)]
mols=[(t,n,m,U.uncharge(m)) for t,n,m in mols if m]
print('reliable targets:',len(mols))
for sma in sys.argv[1:]:
    p=Chem.MolFromSmarts(sma); mi=[a.GetIdx() for a in p.GetAtoms() if a.GetAtomMapNum()==1]; mi=mi[0] if mi else 0
    c=collections.Counter(); ex=collections.defaultdict(list)
    for t,n,m,u in mols:
        seen=set()
        for mt in u.GetSubstructMatches(p,uniquify=False):
            if mt[mi] in seen: continue
            seen.add(mt[mi])
            q=m.GetAtomWithIdx(mt[mi]).GetFormalCharge(); c[q]+=1
            if len(ex[q])<3: ex[q].append(f"{t}:{n[:40]}")
    print(f"{sma}\n   {dict(c)}  ex: {dict(ex)}")
