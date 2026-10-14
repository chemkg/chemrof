"""Rule-based prediction of the major microspecies at pH 7.3.

An open alternative to the ChemAxon-computed rows of Rhea's
``chebi_pH7_3_mapping.tsv``. The rules are SMARTS patterns plus a few
interaction heuristics. The input is neutralised first, then acidic groups
are deprotonated and basic groups protonated.

Two rule sets share one engine:

* :data:`CLEANROOM_RULES` (the default) are derived only from measured pKa
  values (raw ChEMBL25 and DataWarrior extracts, CC BY 4.0) and textbook group
  pKas; Rhea is used only as an outside comparison. Each rule's evidence is in
  :data:`PROVENANCE`.
* :data:`RHEA_FITTED_RULES` were written against Rhea's mapping, whose changed
  rows are all computed (reportedly by ChemAxon), then hill-climbed against
  measured pKa. Kept for comparison.

See ``chebi-scratch/ph73/README.md`` and ``chebi-scratch/ph73/cleanroom/README.md``
for the benchmarks and scores.

>>> predict_major_microspecies("OC(=O)CC(O)(CC(O)=O)C(O)=O")  # citric acid
'O=C([O-])CC(O)(CC(=O)[O-])C(=O)[O-]'
>>> predict_major_microspecies("NCC(O)=O")  # glycine
'[NH3+]CC(=O)[O-]'
>>> predict_major_microspecies("CC(O)COP(O)(O)=O")  # phosphate monoester
'CC(O)COP(=O)([O-])[O-]'
>>> predict_major_microspecies("CP(O)(O)=O")  # phosphonate
'CP(=O)([O-])O'
>>> predict_major_microspecies("C1CNCCN1")  # piperazine: one N only
'C1C[NH2+]CCN1'
"""

from dataclasses import dataclass
from functools import lru_cache
from typing import Optional, Sequence, Tuple

from rdkit import Chem
from rdkit.Chem.MolStandardize import rdMolStandardize

PH = 7.3

# Acids: (name, SMARTS, max per centre). Atom 0 is the OH/SH/NH to deprotonate,
# atom 1 the central atom. ``max per centre`` caps how many protons one centre
# loses, e.g. phosphonate -> 1-, carbonic acid -> hydrogencarbonate.
ACIDS = [
    ("carboxylic acid", "[OX2H1:1][CX3;!$(C([OH])[OH])]=[OX1]", None),
    ("carbonic acid", "[OX2H1:1][CX3]([OX2H1])=[OX1]", 1),
    ("phosphate ester / anhydride OH", "[OX2H1:1][PX4;!$(P[#6])](=[OX1])[OX2;!H1]", None),
    ("phosphoric acid OH", "[OX2H1:1][PX4;!$(P[#6])](=[OX1])([OX2H1])[OX2H1]", None),
    ("phosphonic / phosphinic OH", "[OX2H1:1][PX4](=[OX1])[#6,#1]", 1),
    ("sulfonic / sulfuric OH", "[OX2H1:1][SX4](=[OX1])=[OX1]", None),
    ("sulfinic OH", "[OX2H1:1][SX3]=[OX1]", None),
    ("thiophosphate SH", "[SX2H1:1][PX4]=[SX1,OX1]", None),
    ("thiophosphate OH", "[OX2H1:1][PX4]=[SX1]", None),
    ("arsonic OH", "[OX2H1:1][As](=[OX1])", 1),
    ("nitric acid", "[OX2H1:1][N+](=O)[O-]", None),
    ("thio / dithio acid SH", "[SX2H1:1]C=[O,S]", None),
    ("thiophenol (benzene ring, pKa ~6.6)", "[SX2H1:1]c1ccccc1", None),
    ("tetrazole NH", "[nH:1]1nnnc1", None),
    ("acyl sulfonamide NH", "[NX3H1:1](C=O)S(=O)=O", None),
    ("flavone / isoflavone 7-OH", "[OX2H1:1]c1ccc2c(c1)occc2=O", None),
    ("flavone 5-OH when 7-O is substituted", "[OX2H1:1]c1cc(O[#6,S])cc2occc(=O)c12", None),
    ("o/p-nitrophenol", "[OX2H1:1]c1ccc(cc1)[N+](=O)[O-]", None),
    ("o-nitrophenol", "[OX2H1:1]c1ccccc1[N+](=O)[O-]", None),
    ("2,6-dihalophenol", "[OX2H1:1]c1c([Cl,Br,I])cccc1[Cl,Br,I]", None),
    ("aza- / nitro-imide NH (azauracils, 5-nitrouracils)",
     "[nH;$([nH](c=O)c=O);$([nH]1:c:[nX2,$(c[N+](=O)[O-])]:*:*:*:1),$([nH]1:c:*:[nX2,$(c[N+](=O)[O-])]:*:*:1),"
     "$([nH]1:c:*:*:[nX2,$(c[N+](=O)[O-])]:*:1):1]c=O", None),
    ("gem-dinitro C-H (pKa ~5)", "[CX4H1:1]([N+](=O)[O-])[N+](=O)[O-]", None),
    ("vinylogous acid (1,3-dicarbonyl enol)", "[OX2H1:1][CX3]=[CX3][CX3]=[OX1]", None),
]

# Inorganic phosphoric / diphosphoric acid keep one OH (HPO4 2-, HP2O7 3-)
PHOSPHORIC_KEEP = [
    "[OX2H1:1][PX4](=[OX1])([OX2H1])[OX2H1]",
    "[OX2H1:1][PX4](=[OX1])([OX2H1])[OX2][PX4](=[OX1])([OX2H1])[OX2H1]",
]

AMINE = (
    "[NX3;H2,H1,H0;+0;!$(N[a]);!$(N[#6,#16,#15]=[#7,#8,#16]);!$(N[#7,#8]);"
    "!$(NC=[C,N,S]);!$(N#*);!$(N=*);!$(NS);!$(NP);!$(NC#N);!$(NC[F,Cl]);!$(NC(F)F):1]"
)
# Amines whose pKa is pushed below 7.3
WEAK_AMINES = [
    "[N;R1:1]1CCOCC1",  # morpholine
    "[N:1]CC#N",
    "[N:1][CX4][NX3;!$(NC=O)]",  # aminal N-C-N
    "[N:1]CC(F)(F)",
    # two beta electron-withdrawing groups, e.g. bis(2-chloroethyl)amines
    "[N:1](CC[Cl,Br,$(C#N),$([N+](=O)[O-])])CC[Cl,Br,$(C#N),$([N+](=O)[O-])]",
]
# Cationic bases protonated on an sp2 N (atom 0), atom 1 is the carbon
AMIDINES = [
    # amidine / guanidine / isothiourea
    "[NX2;+0;!$(N[#8,#7]);!$(N[S,P]);!$(NC=O);!$(N[a]);!$(N=C[a;!n]);!$(N=C-C=O):1]"
    "=[CX3;!$(C=O);!$(C[OX2])]([#6,#7,#16,#1;!$([#7]C=O)])[NX3;!$(NC=O);!$(N[S,P])]",
    # formamidine
    "[NX2;+0;!$(N[#8,#7]);!$(N[S,P]);!$(NC=O);!$(N[a]):1]=[CX3H1][NX3;!$(NC=O);!$(N[S,P])]",
    # exocyclic imine on a non-fused azine/azole ring (2-iminopyrimidine etc.);
    # fused systems (N1-substituted adenines) are left neutral as in Rhea
    "[NX2;+0;!$(N[#7,#8,#16]);!$(NC=O):1]=c1:[n;R1]:[a;R1]:[a;R1]:[a;R1]:[a;R1]:1",
    "[NX2;+0;!$(N[#7,#8,#16]);!$(NC=O):1]=c1:[n;R1]:[a;R1]:[a;R1]:[a;R1]:1",
    # 4-aminopyridine-type ring N
    "[nX2;+0;r6:1]1:c:c:c(-[NX3;+0;H2,H1,H0;!$(NC=O);!$(NS)]):c:c:1",
]
# Cyclic 1,3-diketone (keto form, pKa ~4-5): C-H between two ring ketones
CYCLIC_DIKETONE = "[CX4;H1,H2;R:1]([CX3;R](=[OX1])[#6])[CX3;R](=[OX1])[#6]"
# Weak acids (pKa ~6.7) ionized only when the molecule has no other anion
TROPOLONE = "[OX2H1:1]c1cccccc1=O"
IMINO_ACID = "[NX2;+0;!$(N[#7,#8]):1]=[CX3]C(=O)[O-,OH]"



@dataclass(frozen=True)
class RuleSet:
    """The rule tables :func:`ionize` applies. Empty or None disables a step."""

    acids: Sequence[Tuple[str, str, Optional[int]]]
    phosphoric_keep: Sequence[str]
    amine: str
    weak_amines: Sequence[str]
    amidines: Sequence[str]
    cyclic_diketone: Optional[str]
    tropolone: Optional[str]
    imino_acid: Optional[str]


RHEA_FITTED_RULES = RuleSet(
    acids=ACIDS,
    phosphoric_keep=PHOSPHORIC_KEEP,
    amine=AMINE,
    weak_amines=WEAK_AMINES,
    amidines=AMIDINES,
    cyclic_diketone=CYCLIC_DIKETONE,
    tropolone=TROPOLONE,
    imino_acid=IMINO_ACID,
)

# Evidence for each clean-room rule. "exp" = measured pKa in the raw ChEMBL25 and
# DataWarrior extracts of Baltruschat & Czodrowski (doi:10.5281/zenodo.7884512,
# CC BY 4.0; their ChemAxon-filtered files are not used): n molecules in which
# the group is the only ionizable one, median pKa, share ionized at pH 7.3.
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
    "tropolone": "exp n=19, median 6.7, 74% ionized; not when another anion is present "
                 "(electrostatic suppression of a second ionization)",
}

# Rhea-fitted rules left out of the clean-room set, because nothing but Rhea supported them
DROPPED = {
    "flavone / isoflavone 7-OH": "exp n=3, median 7.35, 33% ionized: too close to 7.3 to call",
    "flavone 5-OH when 7-O is substituted": "no data; textbook: H-bonded to C4=O, pKa ~11",
    "imino acid (C=N alpha to carboxylate)": "no experimental or textbook support found",
    "non-fused restriction on ring imines": "1-methyladenosine pKaH ~8.3-8.8: fused ring imines are basic too",
}

RING_IMINE = "[NX2;+0;!$(N[#7,#8,#16]);!$(NC=O):1]=c:n"

CLEANROOM_RULES = RuleSet(
    acids=[a for a in ACIDS if a[0] not in DROPPED],
    phosphoric_keep=PHOSPHORIC_KEEP,
    amine=AMINE,
    weak_amines=WEAK_AMINES,
    amidines=[AMIDINES[0], AMIDINES[1], RING_IMINE, AMIDINES[4]],
    cyclic_diketone=CYCLIC_DIKETONE,
    tropolone=TROPOLONE,
    imino_acid=None,
)

DEFAULT_RULES = CLEANROOM_RULES

# Species containing anything else (metals etc.) are left unchanged
NONMETALS = {1, 5, 6, 7, 8, 9, 14, 15, 16, 17, 33, 34, 35, 52, 53}

_uncharger = rdMolStandardize.Uncharger()


@lru_cache(maxsize=None)
def _pat(smarts: str) -> Chem.Mol:
    pat = Chem.MolFromSmarts(smarts)
    if pat is None:
        raise ValueError(f"Invalid SMARTS: {smarts}")
    return pat


def _shift(atom: Chem.Atom, dq: int) -> None:
    """Add (dq=+1) or remove (dq=-1) a proton."""
    h = atom.GetTotalNumHs()
    atom.SetFormalCharge(atom.GetFormalCharge() + dq)
    atom.SetNumExplicitHs(h + dq)
    atom.SetNoImplicit(True)


def _to_terminal_iminium(mol: Chem.RWMol, site: int, centre: int) -> None:
    """Draw amidinium / guanidinium as C=[NH2+] on a terminal NH2 (Rhea convention)."""
    for bond in mol.GetAtomWithIdx(centre).GetBonds():
        other = bond.GetOtherAtom(mol.GetAtomWithIdx(centre))
        if (
            other.GetIdx() != site
            and other.GetAtomicNum() == 7
            and other.GetFormalCharge() == 0
            and other.GetTotalNumHs() == 2
            and bond.GetBondType() == Chem.BondType.SINGLE
            and not mol.GetAtomWithIdx(site).GetTotalNumHs() == 2
        ):
            imine = mol.GetAtomWithIdx(site)
            mol.GetBondBetweenAtoms(site, centre).SetBondType(Chem.BondType.SINGLE)
            bond.SetBondType(Chem.BondType.DOUBLE)
            imine.SetFormalCharge(0)
            other.SetFormalCharge(1)
            return


def ionize(mol: Chem.Mol, rules: Optional[RuleSet] = None) -> Chem.Mol:
    """Apply the pH 7.3 rules (default: :data:`DEFAULT_RULES`) to a neutral molecule."""
    rules = rules or DEFAULT_RULES
    mol = Chem.RWMol(mol)
    keep = {
        mol.GetSubstructMatch(_pat(s))[0] for s in rules.phosphoric_keep if mol.HasSubstructMatch(_pat(s))
    }
    done = set()
    for _, smarts, max_per_centre in rules.acids:
        per_centre = {}
        # uniquify=False: equivalent OH groups on one centre share an atom set
        for match in mol.GetSubstructMatches(_pat(smarts), uniquify=False):
            site, centre = match[0], match[1]
            # the H may be an explicit (e.g. deuterium) atom; leave those alone
            if site in done or site in keep or mol.GetAtomWithIdx(site).GetTotalNumHs() == 0:
                continue
            if max_per_centre is not None and per_centre.get(centre, 0) >= max_per_centre:
                continue
            per_centre[centre] = per_centre.get(centre, 0) + 1
            _shift(mol.GetAtomWithIdx(site), -1)
            done.add(site)

    # cyclic 1,3-diketones: draw as the enolate C=C-[O-]
    for match in mol.GetSubstructMatches(_pat(rules.cyclic_diketone)) if rules.cyclic_diketone else ():
        c_alpha, c_carbonyl, oxygen = (mol.GetAtomWithIdx(i) for i in match[:3])
        if c_alpha.GetTotalNumHs() == 0 or oxygen.GetFormalCharge() != 0:
            continue
        c_alpha.SetNumExplicitHs(c_alpha.GetTotalNumHs() - 1)
        c_alpha.SetNoImplicit(True)
        mol.GetBondBetweenAtoms(match[0], match[1]).SetBondType(Chem.BondType.DOUBLE)
        mol.GetBondBetweenAtoms(match[1], match[2]).SetBondType(Chem.BondType.SINGLE)
        oxygen.SetFormalCharge(-1)

    if rules.tropolone and not any(a.GetFormalCharge() < 0 for a in mol.GetAtoms()):
        match = mol.GetSubstructMatch(_pat(rules.tropolone))
        if match:
            _shift(mol.GetAtomWithIdx(match[0]), -1)

    weak = {m[0] for s in rules.weak_amines for m in mol.GetSubstructMatches(_pat(s))}

    # amidines etc.: protonate the imine N, once per conjugated system
    used = set()
    for smarts in rules.amidines:
        for match in mol.GetSubstructMatches(_pat(smarts)):
            site, centre = match[0], match[1]
            atom = mol.GetAtomWithIdx(site)
            if centre in used or atom.GetFormalCharge() != 0:
                continue
            _shift(atom, +1)
            _to_terminal_iminium(mol, site, centre)
            used.add(centre)
            used.update(n.GetIdx() for n in mol.GetAtomWithIdx(centre).GetNeighbors())

    # imino acids: C=N alpha to a carboxylate (1-pyrroline-2-carboxylate etc.)
    for match in mol.GetSubstructMatches(_pat(rules.imino_acid)) if rules.imino_acid else ():
        atom = mol.GetAtomWithIdx(match[0])
        if atom.GetFormalCharge() == 0:
            _shift(atom, +1)

    # amines: protonate, but only one N of a 1,2-diamine (piperazine etc.)
    charged = []
    for match in mol.GetSubstructMatches(_pat(rules.amine)):
        site = match[0]
        if site in weak or site in used:
            continue
        if any(len(Chem.GetShortestPath(mol, site, j)) - 1 <= 3 for j in charged):
            continue
        _shift(mol.GetAtomWithIdx(site), +1)
        charged.append(site)

    Chem.SanitizeMol(mol)
    return mol


def predict_major_microspecies(smiles: str, rules: Optional[RuleSet] = None) -> Optional[str]:
    """Predict the canonical SMILES of the major microspecies at pH 7.3.

    Returns None if the SMILES cannot be parsed. Single atoms and
    metal-containing species are returned unchanged (canonicalised).
    ``rules`` selects a rule set (default: :data:`DEFAULT_RULES`).

    >>> predict_major_microspecies("[Na+]")
    '[Na+]'
    >>> predict_major_microspecies("not a smiles") is None
    True
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    if mol.GetNumHeavyAtoms() == 1 or any(a.GetAtomicNum() not in NONMETALS for a in mol.GetAtoms()):
        return Chem.MolToSmiles(mol)
    return Chem.MolToSmiles(ionize(_uncharger.uncharge(mol), rules))
