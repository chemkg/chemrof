"""audit_exp.py SMARTS [SMARTS...]: measured pKa for a group, from molecules
where it is the ONLY ionizable group (so the value must belong to it).

Uses data/exp_pka.tsv (CC BY 4.0 raw extracts, no ChemAxon). Atom :1 marks the
group's ionizable atom; the broad detector below decides "only ionizable group".
"""
import os, sys
import numpy as np, pandas as pd
from rdkit import Chem, RDLogger
RDLogger.DisableLog('rdApp.*')

PH = 7.3
# Deliberately broad, rule-independent ionizable-site detector: (smarts, acid/base)
SITES = [(Chem.MolFromSmarts(s), k) for s, k in [
    ('[OX2H1][CX3,SX4,SX3,PX4,AsX4]=[O,S]', 'acid'),  # carboxylic, sulfonic, sulfinic, phosphorus OH
    ('[SX2H1][#6,P]', 'acid'),                        # thiols, thioacids
    ('[OX2H1]c', 'acid'),                             # phenols
    ('[OX2H1][CX3]=[CX3]', 'acid'),                   # enols
    ('[OX2H1][NX3,NX2]', 'acid'),                     # hydroxamic acids, oximes
    # activated N-H only; plain amide, pyrrole and imidazole N-H have pKa > 12
    ('[NX3H1;$(N(C=O)C=O),$(NS(=O)=O)]', 'acid'),     # imide, sulfonamide NH
    ('[nH;$([nH](c=O)c=O),$([nH]1nnnc1),$([nH]1nncc1),$([nH]1ncnc1)]', 'acid'),  # ring imide, tetrazole, triazole
    ('[CX4H1,CX4H2;$(C([N+](=O)[O-])[N+](=O)[O-]),$(C(C=O)C=O)]', 'acid'),  # C-H acids
    ('[NX3;H2,H1,H0;+0;!$(N[a]);!$(N[#6,#16,#15]=[#7,#8,#16]);!$(N[#7,#8])]', 'base'),  # sp3 amine
    ('[NX3;H2,H1,H0;+0;$(Nc);!$(N[#6,#16]=[#7,#8,#16])]', 'base'),  # aniline-type N
    ('[NX2;+0;!$(N[#8,#7])]=[CX3]', 'base'),          # imines, amidines, guanidines
    ('[nX2;+0]', 'base'),                              # pyridine-type N
]]


def sites(m):
    out = set()
    for p, k in SITES:
        for mt in m.GetSubstructMatches(p):
            out.add((mt[0], k))
    return out


def load():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'exp_pka.tsv')
    d = pd.read_csv(path, sep='\t', dtype={'kind': str}, keep_default_na=False)
    d['mol'] = [Chem.MolFromSmiles(s) for s in d.smiles]
    d = d[d.mol.notna()].copy()
    d['sites'] = [sites(m) for m in d.mol]
    return d[[len(s) == 1 for s in d.sites]]


def audit(d, smarts):
    p = Chem.MolFromSmarts(smarts)
    mi = next((a.GetIdx() for a in p.GetAtoms() if a.GetAtomMapNum() == 1), 0)
    hits = []
    for r in d.itertuples():
        (site, kind), = r.sites
        if any(mt[mi] == site for mt in r.mol.GetSubstructMatches(p)):
            if r.kind and r.kind != kind:
                continue  # dataset says the value belongs to the other type
            hits.append((r.pka, kind, r.smiles))
    if not hits:
        return f'{smarts}\n   no single-site measurements'
    v = np.array([h[0] for h in hits]); kind = hits[0][1]
    ion = (v < PH) if kind == 'acid' else (v > PH)
    q = np.percentile(v, [10, 50, 90])
    ex = sorted(hits, key=lambda h: h[0])
    exs = ', '.join(f'{s} {x:.1f}' for x, _, s in (ex[:2] + ex[len(ex)//2:len(ex)//2+1] + ex[-2:]))[:300]
    return (f'{smarts}\n   n={len(v)} {kind}  median {q[1]:.2f} [p10 {q[0]:.2f}, p90 {q[2]:.2f}]  '
            f'ionized at 7.3: {ion.mean():.0%}\n   e.g. {exs}')


if __name__ == '__main__':
    d = load()
    print(f'single-site molecules: {len(d)} of the measured set')
    for s in sys.argv[1:]:
        print(audit(d, s))
