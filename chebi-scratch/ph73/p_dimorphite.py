from dimorphite_dl import protonate_smiles
def predict(s):
    o=protonate_smiles(s,ph_min=7.3,ph_max=7.3,precision=0.0,max_variants=1)
    return o[0] if o else s
