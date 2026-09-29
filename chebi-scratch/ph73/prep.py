import pandas as pd, csv, sys
csv.field_size_limit(sys.maxsize)
s=pd.read_csv('data/structures.tsv.gz',sep='\t',usecols=['compound_id','smiles','standard_inchi_key','default_structure'],dtype=str,engine='python')
s=s[s.default_structure.str.lower().isin(['t','true','1'])] if s.default_structure.notna().any() else s
s=s.dropna(subset=['smiles']).drop_duplicates('compound_id')
c=pd.read_csv('data/compounds.tsv.gz',sep='\t',usecols=['id','name'],dtype=str)
s=s.merge(c,left_on='compound_id',right_on='id',how='left')[['compound_id','name','smiles','standard_inchi_key']]
s.to_csv('data/chebi_smiles.tsv',sep='\t',index=False)
print(len(s)); print(s.head())
