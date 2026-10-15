from chemrof.converter.protonation import RHEA_FITTED_RULES, predict_major_microspecies


def predict(smiles):
    return predict_major_microspecies(smiles, RHEA_FITTED_RULES)
