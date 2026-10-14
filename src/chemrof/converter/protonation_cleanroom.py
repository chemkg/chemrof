"""Clean-room pH 7.3 rules: derived without Rhea or ChemAxon output.

:mod:`chemrof.converter.protonation` was first written against Rhea's
``chebi_pH7_3_mapping.tsv``, whose changed rows are all computed (reportedly
by ChemAxon). This module keeps the same engine but re-derives every rule
from two sources only:

* measured pKa values from the raw ChEMBL25 and DataWarrior extracts of
  Baltruschat & Czodrowski (CC BY 4.0, doi:10.5281/zenodo.7884512). Only the
  raw files are used; the authors' cleaned files were filtered and
  site-labelled with ChemAxon Marvin. The statistic is the median pKa over
  molecules in which the group is the only ionizable group
  (``chebi-scratch/ph73/cleanroom/audit_exp.py``);
* textbook group pKa values, cited per rule.

Each rule's evidence is in :data:`PROVENANCE`. Rhea is used only as an outside
comparison, never to choose a rule.

>>> predict_major_microspecies("OC(=O)CC(O)(CC(O)=O)C(O)=O")  # citric acid
'O=C([O-])CC(O)(CC(=O)[O-])C(=O)[O-]'
>>> predict_major_microspecies("O=c1cc(-c2ccccc2)oc2cc(O)ccc12")  # 7-hydroxyflavone, pKa ~7.4
'O=c1cc(-c2ccccc2)oc2cc(O)ccc12'
>>> predict_major_microspecies("Cn1cnc2c(c1=N)ncn2C")  # 1,9-dimethyladenine, pKaH ~8.3
'Cn1cnc2c(ncn2C)c1=[NH2+]'
"""

from typing import Optional

from chemrof.converter import protonation as _p
from chemrof.converter.protonation import RuleSet

# Evidence per rule. "exp" = measured pKa in the CC BY 4.0 raw extracts:
# n single-site molecules, median pKa, share ionized at pH 7.3.
PROVENANCE = {
    "carboxylic acid": "exp n=1005, median 3.97, 98% ionized",
    "carbonic acid": "textbook pKa1 6.35, pKa2 10.3: hydrogencarbonate",
    "phosphate ester / anhydride OH": "exp n=1 (4.1); textbook monoester pKa1 ~1.5, pKa2 ~6.0-6.5; diester pKa ~1.5",
    "phosphoric acid OH": "textbook H3PO4 pKa 2.1, 7.2, 12.3: HPO4(2-) slightly dominant at 7.3",
    "phosphonic / phosphinic OH": "exp n=22, median 3.25 (pKa1); textbook pKa2 ~7.5-8: monoanion",
    "sulfonic / sulfuric OH": "exp n=5, median -6.9",
    "sulfinic OH": "exp n=15, median 2.05",
    "thiophosphate SH": "textbook: thiophosphoric acids are stronger than phosphoric acid",
    "thiophosphate OH": "exp n=2, median 6.6",
    "arsonic OH": "exp n=2, median 6.4 (pKa1); textbook pKa2 ~8.5-9: monoanion",
    "nitric acid": "textbook pKa -1.4",
    "thio / dithio acid SH": "exp n=14, median 2.9",
    "thiophenol (benzene ring, pKa ~6.6)": "exp n=17, median 5.8, 100% ionized",
    "tetrazole NH": "textbook 5-substituted tetrazoles pKa ~4.5-5",
    "acyl sulfonamide NH": "exp n=44, median 4.97, 100% ionized",
    "o/p-nitrophenol": "exp n=20, median 6.9, 80% ionized",
    "o-nitrophenol": "exp n=28, median 4.8, 89% ionized",
    "2,6-dihalophenol": "exp n=20, median 5.9, 85% ionized",
    "aza- / nitro-imide NH (azauracils, 5-nitrouracils)": "exp n=1 (5.7); textbook 6-azauracil ~7.0, 5-nitrouracil ~5.3 (weak evidence)",
    "gem-dinitro C-H (pKa ~5)": "exp n=10, median 5.5, 90% ionized",
    "vinylogous acid (1,3-dicarbonyl enol)": "exp n=57, median 4.35, 86% ionized",
    "inorganic phosphoric acid keeps one OH": "textbook H3PO4 pKa3 12.3; H4P2O7 pKa4 ~9.4",
    "amine": "exp n=1781, median 8.9, 81% protonated",
    "morpholine": "exp n=78, median 6.8, 22% protonated",
    "alpha-cyano amine": "exp n=19, median 4.2, 0% protonated",
    "aminal N-C-N": "textbook hexamethylenetetramine pKaH 4.9 (weak evidence)",
    "beta,beta-difluoro amine": "exp n=23, median 5.8, 9% protonated",
    "two beta electron-withdrawing groups": "exp n=7, median 6.5, 0% protonated",
    "amidine / guanidine": "exp n=111, median 10.5, 90% protonated",
    "formamidine": "textbook amidines pKaH 11-12",
    "exocyclic ring imine": "textbook 1-methylcytosine-type imines and 1-methyladenosine pKaH ~8.3-8.8",
    "4-aminopyridine": "textbook 4-aminopyridine 9.2, 4-dimethylaminopyridine 9.6",
    "1,2-diamine: one N": "textbook ethylenediamine pKa2 6.9, piperazine pKa2 5.3",
    "cyclic 1,3-diketone": "exp n=20, median 5.2, 90% ionized",
    "tropolone": "exp n=19, median 6.7, 74% ionized; not when another anion is present (electrostatic suppression of a second ionization)",
}

# Rules dropped because nothing but Rhea supported them
DROPPED = {
    "flavone / isoflavone 7-OH": "exp n=3, median 7.35, 33% ionized: too close to 7.3 to call",
    "flavone 5-OH when 7-O is substituted": "no data; textbook: H-bonded to C4=O, pKa ~11",
    "imino acid (C=N alpha to carboxylate)": "no experimental or textbook support found",
    "non-fused restriction on ring imines": "1-methyladenosine pKaH ~8.3-8.8: fused ring imines are basic too",
}

_ACIDS = [a for a in _p.ACIDS if a[0] not in DROPPED]

_RING_IMINE = "[NX2;+0;!$(N[#7,#8,#16]);!$(NC=O):1]=c:n"

CLEANROOM_RULES = RuleSet(
    acids=_ACIDS,
    phosphoric_keep=_p.PHOSPHORIC_KEEP,
    amine=_p.AMINE,
    weak_amines=_p.WEAK_AMINES,
    amidines=[_p.AMIDINES[0], _p.AMIDINES[1], _RING_IMINE, _p.AMIDINES[4]],
    cyclic_diketone=_p.CYCLIC_DIKETONE,
    tropolone=_p.TROPOLONE,
    imino_acid=None,
)


def predict_major_microspecies(smiles: str) -> Optional[str]:
    """Predict the major microspecies at pH 7.3 with the clean-room rules."""
    return _p.predict_major_microspecies(smiles, CLEANROOM_RULES)
