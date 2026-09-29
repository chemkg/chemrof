"""Write disagreements.tsv: rows where the rules and Rhea pick different ChEBI IDs."""
import pandas as pd
b = pd.read_csv('data/out_p_chemrof_all.tsv', sep='\t', dtype=str)
s = pd.read_csv('data/chebi_smiles.tsv', sep='\t', dtype=str).set_index('compound_id')
f = b[b.okid == 'False'].copy()
f['pred_name'] = f.pred_id.map(s.name)
f['kind'] = ['rules pick another ChEBI entity' if p != src else 'rules miss the change'
             for p, src in zip(f.pred_id, f.src)]
print(len(f)); print(f.kind.value_counts())
f[['src', 'src_name', 'tgt', 'tgt_name', 'pred_id', 'pred_name', 'kind', 'tgt_can', 'pred']].to_csv(
    'disagreements.tsv', sep='\t', index=False)
