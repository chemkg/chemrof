"""Build data/exp_pka.tsv from the raw ChEMBL25 and DataWarrior pKa extracts.

Source: Baltruschat & Czodrowski, "Machine learning meets pKa" datasets
(CC BY 4.0, doi:10.5281/zenodo.7884512). Only the two RAW extracts are used.
Their cleaned/combined files are NOT used: that pipeline filtered and
site-labelled the data with ChemAxon Marvin.

    uv run python exp_data.py
"""
import os, subprocess
import pandas as pd
from rdkit import Chem, RDLogger
from rdkit.Chem.MolStandardize import rdMolStandardize
RDLogger.DisableLog('rdApp.*')

REPO = 'https://github.com/czodrowskilab/Machine-learning-meets-pKa'
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
SRC = os.path.join(DATA, 'mlpka')
U = rdMolStandardize.Uncharger()


def main():
    if not os.path.exists(f'{SRC}/datasets/chembl25.sdf'):
        subprocess.run(['git', 'clone', '-q', '--depth', '1', REPO, SRC], check=True)
    rows = []
    for name in ('chembl25', 'datawarrior'):
        for m in Chem.SDMolSupplier(f'{SRC}/datasets/{name}.sdf'):
            if m is None or not m.HasProp('pKa'):
                continue
            try:
                pka = float(m.GetProp('pKa'))
            except ValueError:
                continue
            kind = m.GetProp('basicOrAcidic').strip().lower() if m.HasProp('basicOrAcidic') else ''
            m = U.uncharge(Chem.RemoveHs(m))
            if Chem.GetFormalCharge(m) != 0 or len(Chem.GetMolFrags(m)) > 1:
                continue
            rows.append(dict(source=name, smiles=Chem.MolToSmiles(m), inchikey=Chem.MolToInchiKey(m),
                             pka=pka, kind={'acidic': 'acid', 'basic': 'base'}.get(kind, '')))
    d = pd.DataFrame(rows)
    d.to_csv(os.path.join(DATA, 'exp_pka.tsv'), sep='\t', index=False)
    print(d.groupby('source').agg(records=('pka', 'size'), molecules=('inchikey', 'nunique')))
    print('typed acid/base:', (d.kind != '').sum())


if __name__ == '__main__':
    main()
