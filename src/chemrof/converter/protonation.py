"""Rule-based prediction of the major microspecies at pH 7.3.

An open replacement for the ChemAxon-computed rows of Rhea's
``chebi_pH7_3_mapping.tsv``. The rules are SMARTS patterns plus a few
interaction heuristics. Each rule was checked against the Rhea mapping;
see ``chebi-scratch/ph73/README.md`` for the benchmark and scores.

The input is neutralised first, then acidic groups are deprotonated and
basic groups protonated according to Rhea's conventions at pH 7.3.

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

from functools import lru_cache
from typing import Optional

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
    ("thiophosphate SH", "[SX2H1:1][PX4]=[SX1,OX1]", None),
    ("thiophosphate OH", "[OX2H1:1][PX4]=[SX1]", None),
    ("arsonic OH", "[OX2H1:1][As](=[OX1])", 1),
    ("nitric acid", "[OX2H1:1][N+](=O)[O-]", None),
    ("thio / dithio acid SH", "[SX2H1:1]C=[O,S]", None),
    ("tetrazole NH", "[nH:1]1nnnc1", None),
    ("acyl sulfonamide NH", "[NX3H1:1](C=O)S(=O)=O", None),
    ("flavone / isoflavone 7-OH", "[OX2H1:1]c1ccc2c(c1)occc2=O", None),
    ("flavone 5-OH when 7-O is substituted", "[OX2H1:1]c1cc(O[#6,S])cc2occc(=O)c12", None),
    ("o/p-nitrophenol", "[OX2H1:1]c1ccc(cc1)[N+](=O)[O-]", None),
    ("o-nitrophenol", "[OX2H1:1]c1ccccc1[N+](=O)[O-]", None),
    ("2,6-dihalophenol", "[OX2H1:1]c1c([Cl,Br,I])cccc1[Cl,Br,I]", None),
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
]
# Cationic bases protonated on an sp2 N (atom 0), atom 1 is the carbon
AMIDINES = [
    # amidine / guanidine / isothiourea
    "[NX2;+0;!$(N[#8,#7]);!$(N[S,P]);!$(NC=O);!$(N[a]);!$(N=C[a;!n]);!$(N=C-C=O):1]"
    "=[CX3;!$(C=O);!$(C[OX2])]([#6,#7,#16,#1;!$([#7]C=O)])[NX3;!$(NC=O);!$(N[S,P])]",
    # formamidine
    "[NX2;+0;!$(N[#8,#7]);!$(N[S,P]);!$(NC=O);!$(N[a]):1]=[CX3H1][NX3;!$(NC=O);!$(N[S,P])]",
    # 4-aminopyridine-type ring N
    "[nX2;+0;r6:1]1:c:c:c(-[NX3;H2,H1,H0;!$(NC=O);!$(NS)]):c:c:1",
]
IMINO_ACID = "[NX2;+0;!$(N[#7,#8]):1]=[CX3]C(=O)[O-,OH]"

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


def ionize(mol: Chem.Mol) -> Chem.Mol:
    """Apply the pH 7.3 rules to a neutral molecule."""
    mol = Chem.RWMol(mol)
    keep = {
        mol.GetSubstructMatch(_pat(s))[0] for s in PHOSPHORIC_KEEP if mol.HasSubstructMatch(_pat(s))
    }
    done = set()
    for _, smarts, max_per_centre in ACIDS:
        per_centre = {}
        # uniquify=False: equivalent OH groups on one centre share an atom set
        for match in mol.GetSubstructMatches(_pat(smarts), uniquify=False):
            site, centre = match[0], match[1]
            if site in done or site in keep:
                continue
            if max_per_centre is not None and per_centre.get(centre, 0) >= max_per_centre:
                continue
            per_centre[centre] = per_centre.get(centre, 0) + 1
            _shift(mol.GetAtomWithIdx(site), -1)
            done.add(site)

    weak = {m[0] for s in WEAK_AMINES for m in mol.GetSubstructMatches(_pat(s))}

    # amidines etc.: protonate the imine N, once per conjugated system
    used = set()
    for smarts in AMIDINES:
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
    for match in mol.GetSubstructMatches(_pat(IMINO_ACID)):
        atom = mol.GetAtomWithIdx(match[0])
        if atom.GetFormalCharge() == 0:
            _shift(atom, +1)

    # amines: protonate, but only one N of a 1,2-diamine (piperazine etc.)
    charged = []
    for match in mol.GetSubstructMatches(_pat(AMINE)):
        site = match[0]
        if site in weak or site in used:
            continue
        if any(len(Chem.GetShortestPath(mol, site, j)) - 1 <= 3 for j in charged):
            continue
        _shift(mol.GetAtomWithIdx(site), +1)
        charged.append(site)

    Chem.SanitizeMol(mol)
    return mol


def predict_major_microspecies(smiles: str) -> Optional[str]:
    """Predict the canonical SMILES of the major microspecies at pH 7.3.

    Returns None if the SMILES cannot be parsed. Single atoms and
    metal-containing species are returned unchanged (canonicalised).

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
    return Chem.MolToSmiles(ionize(_uncharger.uncharge(mol)))
