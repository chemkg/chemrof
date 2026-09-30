"""Grade predictors against measured pKa values (IUPAC Digitized pKa Dataset).

An external check that does not depend on Rhea/ChemAxon. For each molecule the
expected net charge at pH 7.3 is derived from its measured macro pKas:

    charge = #(pKaH > 7.3) - #(pKa < 7.3)

(pKaH = conjugate acid of a base, pKa = acid, as labelled in the dataset).
This checks the charge state, not which atom carries it.

The dataset is CC BY-NC 4.0 (IUPAC), so it is downloaded into data/ (gitignored)
and only aggregate scores are committed.

    uv run --with dimorphite_dl python iupac_eval.py
"""
import os, re, subprocess, pickle
import numpy as np, pandas as pd
from rdkit import Chem, RDLogger
from rdkit.Chem.MolStandardize import rdMolStandardize
RDLogger.DisableLog('rdApp.*')

PH, BAND = 7.3, 0.5
# Broad, rule-independent ionizable-group detector used only to flag molecules
# whose IUPAC entry lists fewer pKas than they have ionizable groups (the
# expected charge is then unreliable, e.g. terephthalic acid with one pKa).
SITES = [Chem.MolFromSmarts(s) for s in [
    '[OX2H1][CX3,SX4,PX4,AsX4]=O',          # carboxylic, sulfonic, phosphoric OH
    '[OX2H1]c', '[SX2H1]',                  # phenol, thiol
    '[NX3;!$(N[a]);!$(N[#6,#16,#15]=[#7,#8,#16]);!$(N[#7,#8])]',  # sp3 amine
    '[NX2]=[CX3][NX3]', '[nX2]',            # amidine/guanidine, aromatic N
    '[NX3H1](C=O)C=O',                      # imide
]]
REPO = 'https://github.com/IUPAC/Dissociation-Constants'
CSV = 'data/iupac/iupac_high-confidence_v2_4.csv'


def load():
    if not os.path.exists(CSV):
        subprocess.run(['git', 'clone', '-q', '--depth', '1', REPO, 'data/iupac'], check=True,
                       env={**os.environ, 'GIT_LFS_SKIP_SMUDGE': '1'})
    d = pd.read_csv(CSV, dtype=str)
    d['T'] = pd.to_numeric(d['T'], errors='coerce')
    d['pka_value'] = pd.to_numeric(d.pka_value, errors='coerce')
    d = d[d.pka_type.str.fullmatch(r'pKaH?\d*', na=False)]
    d = d[d['T'].between(20, 30) & d.cosolvent.isna() & (d.assessment != 'Uncertain')]
    d = d.dropna(subset=['pka_value', 'SMILES'])
    d['kind'] = np.where(d.pka_type.str.startswith('pKaH'), 'base', 'acid')
    # one value per molecule and pK label (median over measurements)
    g = d.groupby(['SMILES', 'pka_type', 'kind']).pka_value.median().reset_index()
    rows = []
    for smi, x in g.groupby('SMILES'):
        m = Chem.MolFromSmiles(smi)
        if m is None or any(a.GetFormalCharge() for a in m.GetAtoms()) and Chem.GetFormalCharge(m) != 0:
            continue
        if Chem.GetFormalCharge(m) != 0 or '.' in smi:
            continue
        pk = x.pka_value.to_numpy()
        q = int(((x.kind == 'base') & (x.pka_value > PH)).sum() - ((x.kind == 'acid') & (x.pka_value < PH)).sum())
        n_sites = sum(len(m.GetSubstructMatches(p)) for p in SITES)
        rows.append(dict(smiles=Chem.MolToSmiles(m), charge=q, n_pk=len(x), n_sites=n_sites,
                         complete=len(x) >= n_sites,
                         borderline=bool((abs(pk - PH) < BAND).any()),
                         inchikey=Chem.MolToInchiKey(m)))
    return pd.DataFrame(rows).drop_duplicates('smiles')


def charge(smi):
    m = Chem.MolFromSmiles(smi) if isinstance(smi, str) else None
    return Chem.GetFormalCharge(m) if m else None


def rhea_charges(mols):
    """Charge of Rhea's pH 7.3 target for molecules found in ChEBI by InChIKey."""
    s = pd.read_csv('data/chebi_smiles.tsv', sep='\t', dtype=str)
    r = pd.read_csv('data/chebi_pH7_3_mapping.tsv', sep='\t', dtype=str)
    tgt = dict(zip(r.CHEBI, r.CHEBI_PH7_3))
    smiles = dict(zip(s.compound_id, s.smiles))
    by_key = {}
    for cid, k in zip(s.compound_id, s.standard_inchi_key):
        if isinstance(k, str) and cid in tgt:
            by_key.setdefault(k, cid)
    out = []
    for k in mols.inchikey:
        cid = by_key.get(k)
        out.append(charge(smiles.get(tgt[cid])) if cid else None)
    return out


N_BOOT = 1000


def score(y, p, rng, n_boot=N_BOOT):
    ok = (np.asarray(p, dtype=float) == np.asarray(y, dtype=float)).astype(float)
    ix = rng.integers(0, len(ok), (n_boot, len(ok)))
    lo, hi = np.percentile(ok[ix].mean(1), [2.5, 97.5])
    return f"{ok.mean():.3f} [{lo:.3f}, {hi:.3f}]"


def main():
    import sys
    sys.path.insert(0, '../../src')
    from chemrof.converter.protonation import predict_major_microspecies
    preds = {'identity': lambda s: s, 'chemrof rules': predict_major_microspecies}
    try:
        from dimorphite_dl import protonate_smiles
        preds['Dimorphite-DL'] = lambda s: (protonate_smiles(s, ph_min=PH, ph_max=PH, precision=0.0,
                                                             max_variants=1) or [s])[0]
    except ImportError:
        print('(dimorphite_dl not installed; skipping)')
    mols = load()
    for name, f in preds.items():
        mols[name] = [charge(f(s)) for s in mols.smiles]
    mols['Rhea (ChemAxon)'] = rhea_charges(mols)
    mols.to_csv('data/iupac_scored.tsv', sep='\t', index=False)
    rng = np.random.default_rng(0)
    names = list(preds) + ['Rhea (ChemAxon)']
    clear = mols[~mols.borderline]
    for label, sub in (('all molecules with no pK within 0.5 of 7.3', clear),
                       ('...and pKa list complete (n_pk >= ionizable groups)', clear[clear.complete])):
        print(f"\n== {label}")
        table(sub, names, rng)
    # paired: rules vs Rhea on the same molecules
    p = clear[clear.complete & clear['Rhea (ChemAxon)'].notna()]
    d = ((p['chemrof rules'] == p.charge).astype(int) - (p['Rhea (ChemAxon)'] == p.charge).astype(int)).to_numpy()
    lo, hi = np.percentile(d[rng.integers(0, len(d), (N_BOOT, len(d)))].mean(1), [2.5, 97.5])
    print(f"\npaired rules - Rhea (complete, in Rhea, n={len(d)}): {d.mean():+.3f} [{lo:+.3f}, {hi:+.3f}]  "
          f"only rules right: {(d > 0).sum()}  only Rhea right: {(d < 0).sum()}")


def table(mols, names, rng):
    in_rhea = mols[mols['Rhea (ChemAxon)'].notna()]
    subsets = [('all', mols), ('charged', mols[mols.charge != 0]),
               ('in Rhea', in_rhea), ('in Rhea, charged', in_rhea[in_rhea.charge != 0])]
    print(f"{'':16s}" + ''.join(f"{s:>26s}" for s, d in subsets))
    print(f"{'n':16s}" + ''.join(f"{len(d):>26d}" for s, d in subsets))
    for n in names:
        cells = [score(d.charge, d[n], rng) if d[n].notna().all() else '-' for _, d in subsets]
        print(f"{n:16s}" + ''.join(f"{c:>26s}" for c in cells))


if __name__ == '__main__':
    main()
