"""Score the clean-room rules against measured pKa (test) and Rhea (comparison).

Test set: IUPAC molecules (no pK within 0.5 of 7.3, complete pKa list) that are
NOT in the CC BY training extracts (matched by InChIKey). Run from chebi-scratch/ph73:

    PYTHONPATH=../../src uv run python cleanroom/evaluate.py
"""
import sys
import numpy as np, pandas as pd
sys.path.insert(0, '.')
import iupac_eval as ie

NAMES = {'p_cleanroom': 'clean-room rules', 'p_chemrof': 'current rules', 'p_original': 'first rules (Rhea-fitted)'}


def ci(ok, rng, n=2000):
    ok = np.asarray(ok, float)
    lo, hi = np.percentile(ok[rng.integers(0, len(ok), (n, len(ok)))].mean(1), [2.5, 97.5])
    return f'{ok.mean():.3f} [{lo:.3f}, {hi:.3f}]'


def main():
    rng = np.random.default_rng(0)
    mols = ie.load()
    train = set(pd.read_csv('data/exp_pka.tsv', sep='\t', usecols=['inchikey']).inchikey)
    mols['in_training'] = mols.inchikey.isin(train)
    test = mols[~mols.in_training].copy()
    print(f'IUPAC usable: {len(mols)}; overlapping the CC BY training data: {mols.in_training.sum()}; test: {len(test)}')
    for n in NAMES:
        test[n] = ie.charges(n, test.smiles)
    test['rhea'] = ie.rhea_charges(test)
    subsets = [('all test', test), ('charged', test[test.charge != 0]),
               ('IUPAC sealed half', test[test.split == 'sealed']), ('in ChEBI+Rhea', test[test.rhea.notna()])]
    print(f"\n{'measured-pKa match':28s}" + ''.join(f'{s:>24s}' for s, _ in subsets))
    print(f"{'n':28s}" + ''.join(f'{len(d):>24d}' for _, d in subsets))
    for n, label in list(NAMES.items()) + [('rhea', 'ChemAxon (Rhea)')]:
        cells = [ci(d[n] == d.charge, rng) if d[n].notna().all() else '-' for _, d in subsets]
        print(f'{label:28s}' + ''.join(f'{c:>24s}' for c in cells))
    d = test[test.rhea.notna()]
    diff = (d.p_cleanroom == d.charge).astype(int) - (d.rhea == d.charge).astype(int)
    print(f'\npaired clean-room - ChemAxon (in Rhea, n={len(d)}): {ci(diff, rng)}  '
          f'only clean-room right: {(diff > 0).sum()}  only ChemAxon right: {(diff < 0).sum()}')
    diff = (test.p_cleanroom == test.charge).astype(int) - (test.p_chemrof == test.charge).astype(int)
    print(f'paired clean-room - current (all test, n={len(test)}): {ci(diff, rng)}  '
          f'fixed: {(diff > 0).sum()}  broken: {(diff < 0).sum()}')


if __name__ == '__main__':
    main()
