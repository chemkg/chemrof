"""Score a predictor module (with predict(smiles) -> smiles) on data/bench.tsv.

    python evalr.py p_chemrof --split dev
    python evalr.py p_candidate --split dev --compare p_chemrof   # accept/reject
    python evalr.py p_chemrof --split sealed --unseal              # final only

Scores:
  ID      predicted structure looked up in ChEBI (falls back to the source ID
          if absent, as Rhea does); compared with Rhea's target ID.
  STRUCT  exact canonical SMILES match with Rhea's target.
"changed" rows are those where Rhea maps to a different entity; ID-changed is
the primary metric. Intervals are 95% bootstrap CIs resampled by target ID.
"""
import argparse, datetime, importlib, pickle, time
from multiprocessing import Pool
import numpy as np, pandas as pd
from rdkit import Chem, RDLogger
RDLogger.DisableLog('rdApp.*')

N_BOOT = 1000
_mod = None


def _init(name):
    global _mod
    _mod = importlib.import_module(name)


def _run(smi):
    try:
        p = _mod.predict(smi)
        m = Chem.MolFromSmiles(p) if p else None
        return Chem.MolToSmiles(m) if m else None
    except Exception:
        return None


def predict(name, b):
    with Pool(4, initializer=_init, initargs=(name,)) as p:
        pred = p.map(_run, b.src_can.tolist(), chunksize=200)
    idx = pickle.load(open('data/chebi_can_idx.pkl', 'rb'))
    b = b.copy()
    b['pred'] = pred
    b['ok'] = b.pred == b.tgt_can
    b['pred_id'] = [tgt if tgt in idx.get(p, ()) else (sorted(idx[p])[0] if p in idx else src)
                    for p, src, tgt in zip(b.pred, b.src, b.tgt)]
    b['okid'] = b.pred_id == b.tgt
    return b


def boot(b, col, rng):
    """Point estimate and cluster-bootstrap CI of mean(col), clustered by target."""
    g = b.groupby('tgt')[col].agg(['sum', 'count'])
    s, c = g['sum'].to_numpy(float), g['count'].to_numpy(float)
    ix = rng.integers(0, len(g), (N_BOOT, len(g)))
    est = s[ix].sum(1) / c[ix].sum(1)
    return s.sum() / c.sum(), np.percentile(est, [2.5, 97.5])


def report(name, b, rng):
    ch = b[~b.identity]
    rows = [('ID changed (primary)', ch, 'okid'), ('ID all', b, 'okid'),
            ('STRUCT changed', ch, 'ok'), ('STRUCT all', b, 'ok')]
    print(f"{name}: n={len(b)} changed={len(ch)}")
    for label, d, col in rows:
        m, (lo, hi) = boot(d, col, rng)
        print(f"  {label:22s} {m:.4f}  [{lo:.4f}, {hi:.4f}]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('predictor')
    ap.add_argument('--split', default='train', choices=['train', 'dev', 'sealed', 'all'])
    ap.add_argument('--compare', help='baseline predictor for a paired comparison')
    ap.add_argument('--unseal', action='store_true', help='required to score the sealed split')
    a = ap.parse_args()
    if a.split == 'sealed':
        if not a.unseal:
            ap.error('the sealed split is for the final score only; pass --unseal')
        with open('data/unseal.log', 'a') as f:
            f.write(f"{datetime.datetime.now().isoformat()}\t{a.predictor}\t{a.compare or ''}\n")
    b = pd.read_csv('data/bench.tsv', sep='\t', dtype=str)
    b['identity'] = b.identity == 'True'
    # 'all' excludes sealed unless unsealed, so the disagreement list can't leak it
    b = b[b.split == a.split] if a.split != 'all' else (b if a.unseal else b[b.split != 'sealed'])
    rng = np.random.default_rng(0)
    t = time.time()
    r = predict(a.predictor, b)
    report(a.predictor, r, rng)
    r.to_csv(f'data/out_{a.predictor}_{a.split}.tsv', sep='\t', index=False)
    if a.compare:
        base = predict(a.compare, b)
        report(a.compare, base, rng)
        ch = ~r.identity
        d = pd.DataFrame({'tgt': r.tgt[ch], 'diff': r.okid[ch].astype(int) - base.okid[ch].astype(int)})
        m, (lo, hi) = boot(d, 'diff', rng)
        verdict = 'ACCEPT (beyond noise)' if lo > 0 else 'REJECT (worse)' if hi < 0 else 'NO CLEAR CHANGE (within noise)'
        print(f"  paired diff, ID changed: {m:+.4f}  [{lo:+.4f}, {hi:+.4f}]  -> {verdict}")
        print(f"  rows fixed: {int((d['diff'] > 0).sum())}  rows broken: {int((d['diff'] < 0).sum())}")
    print(f"  ({time.time() - t:.0f}s)")


if __name__ == '__main__':
    main()
