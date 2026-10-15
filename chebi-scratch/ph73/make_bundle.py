"""Package the pH 7.3 benchmark and predictions for sharing (Parquet + data card).

Run after:
    evalr.py p_chemrof     --split all --unseal   # default (clean-room) rules
    evalr.py p_rhea_fitted --split all --unseal
    evalr.py p_original    --split all --unseal

    uv run --with pyarrow python make_bundle.py [VERSION]

Writes data/release/ph73-<VERSION>/ and a .tar of it. IUPAC-derived data is
deliberately left out (CC BY-NC 4.0).
"""
import gzip, hashlib, os, shutil, subprocess, sys, tarfile
import pandas as pd

VERSION = sys.argv[1] if len(sys.argv) > 1 else '2026-10-14'
OUT = f'data/release/ph73-{VERSION}'
COMMIT = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()


def curie(s):
    return 'CHEBI:' + s.astype(str)


def predictions(name):
    p = pd.read_csv(f'data/out_{name}_all.tsv', sep='\t', dtype=str, keep_default_na=False)
    return p.set_index(['src', 'tgt'])[['pred', 'pred_id', 'ok', 'okid']]


def main():
    os.makedirs(OUT, exist_ok=True)
    b = pd.read_csv('data/bench.tsv', sep='\t', dtype=str, keep_default_na=False)
    bench = pd.DataFrame({
        'chebi_id': curie(b.src), 'chebi_name': b.src_name,
        'rhea_ph7_3_id': curie(b.tgt), 'rhea_ph7_3_name': b.tgt_name,
        'rhea_origin': b.origin, 'split': b.split, 'changed': b.identity != 'True',
        'smiles': b.src_can, 'rhea_ph7_3_smiles': b.tgt_can,
    })
    key = list(zip(b.src, b.tgt))
    for name, label in (('p_chemrof', 'default'), ('p_rhea_fitted', 'rhea_fitted'), ('p_original', 'original')):
        p = predictions(name).reindex(key)
        bench[f'pred_{label}_smiles'] = p.pred.to_numpy()
        bench[f'pred_{label}_id'] = ['CHEBI:' + x if x else '' for x in p.pred_id.fillna('')]
        bench[f'{label}_matches_rhea_structure'] = (p.ok == 'True').to_numpy()
        bench[f'{label}_matches_rhea_id'] = (p.okid == 'True').to_numpy()
    bench.to_parquet(f'{OUT}/benchmark.parquet', index=False, compression='zstd')

    d = bench[~bench.default_matches_rhea_id].copy()
    d['kind'] = ['rules pick another ChEBI entity' if p != c else 'rules miss the change'
                 for p, c in zip(d.pred_default_id, d.chebi_id)]
    d = d[['chebi_id', 'chebi_name', 'rhea_ph7_3_id', 'rhea_ph7_3_name', 'pred_default_id', 'kind', 'split',
           'smiles', 'rhea_ph7_3_smiles', 'pred_default_smiles']]
    d.to_parquet(f'{OUT}/disagreements.parquet', index=False, compression='zstd')

    s = pd.read_csv('data/chebi_smiles.tsv', sep='\t', dtype=str, keep_default_na=False)
    s = s.assign(chebi_id=curie(s.compound_id))[['chebi_id', 'name', 'smiles', 'standard_inchi_key', 'smiles_source']]
    s.to_parquet(f'{OUT}/chebi_structures.parquet', index=False, compression='zstd')

    u = pd.read_csv('chebi_unparseable_smiles.tsv', sep='\t', dtype=str, keep_default_na=False)
    u.to_parquet(f'{OUT}/chebi_unparseable_smiles.parquet', index=False, compression='zstd')

    with open('data/chebi_pH7_3_mapping.tsv', 'rb') as f, gzip.open(f'{OUT}/rhea_chebi_pH7_3_mapping.tsv.gz', 'wb') as g:
        shutil.copyfileobj(f, g)

    counts = {n: len(x) for n, x in (('benchmark', bench), ('disagreements', d), ('chebi_structures', s),
                                     ('chebi_unparseable_smiles', u))}
    with open('make_bundle_datacard.md') as f:
        card = f.read().format(version=VERSION, commit=COMMIT, **counts,
                               changed=int(bench.changed.sum()),
                               default_id=bench[bench.changed].default_matches_rhea_id.mean(),
                               rhea_fitted_id=bench[bench.changed].rhea_fitted_matches_rhea_id.mean(),
                               original_id=bench[bench.changed].original_matches_rhea_id.mean())
    with open(f'{OUT}/DATACARD.md', 'w') as f:
        f.write(card)

    files = sorted(x for x in os.listdir(OUT) if x != 'SHA256SUMS')
    with open(f'{OUT}/SHA256SUMS', 'w') as f:
        for x in files:
            f.write(f"{hashlib.sha256(open(f'{OUT}/{x}', 'rb').read()).hexdigest()}  {x}\n")
    with tarfile.open(f'{OUT}.tar', 'w') as t:
        t.add(OUT, arcname=os.path.basename(OUT))
    for x in files + ['SHA256SUMS']:
        print(f"{os.path.getsize(f'{OUT}/{x}') / 1e6:8.1f} MB  {x}")
    print(f"{os.path.getsize(f'{OUT}.tar') / 1e6:8.1f} MB  {OUT}.tar")


if __name__ == '__main__':
    main()
