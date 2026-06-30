## MoleculeGroupingClass-phosphatidylinositol_3_phosphate_r1_r2
### Input
```yaml
cxsmiles_string: '[H][C@@](COC([*])=O)(COP(O)(=O)O[C@H]1[C@H](O)[C@@H](O)[C@H](O)[C@@H](OP(O)(O)=O)[C@H]1O)OC([*])=O
  |$;;;;;_R1;;;;;;;;;;;;;;;;;;;;;;;;;_R2$|'
id: wd:Q46220488
name: 1-phosphatidyl-1D-myo-inositol 3-phosphate (R1,R2)

```
## SmallMolecule-glucose-with-solubility
### Input
```yaml
IUPAC_name: (2R,3S,4R,5R)-2,3,4,5,6-pentahydroxyhexanal
empirical_formula: CH2O
id: CHEBI:17234
molecular_mass: 180.16
name: glucose
smiles_string: C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O
type: chemrof:SmallMolecule
water_solubility: 909.0

```
## MolecularAnion-acetate
### Input
```yaml
elemental_charge: -1
empirical_formula: C2H3O2
has_atom_occurrences:
- name: acetate-c1
  occurrence_of: C
- name: acetate-c2
  occurrence_of: C
- name: acetate-h1
  occurrence_of: H
- name: acetate-h2
  occurrence_of: H
- name: acetate-h3
  occurrence_of: H
- name: acetate-o1
  occurrence_of: O
- name: acetate-o2
  occurrence_of: O
has_atoms:
- C
- C
- H
- H
- H
- O
- O
has_bonds:
- bond_order: 1
  bond_type: covalent
  object: acetate-h1
  subject: acetate-c1
- bond_order: 1
  bond_type: covalent
  object: acetate-h2
  subject: acetate-c1
- bond_order: 1
  bond_type: covalent
  object: acetate-h3
  subject: acetate-c1
- bond_order: 1
  bond_type: covalent
  object: acetate-c2
  subject: acetate-c1
- bond_order: 2
  bond_type: covalent
  object: acetate-o1
  subject: acetate-c2
- bond_order: 1
  bond_type: covalent
  object: acetate-o2
  subject: acetate-c2
id: CHEBI:30089
is_organic: true
name: acetate
smiles_string: CC(=O)[O-]
type: chemrof:MolecularAnion

```
## Molecule-water
### Input
```yaml
empirical_formula: H2O
has_atom_occurrences:
- name: water-o1
  occurrence_of: O
- name: water-h1
  occurrence_of: H
- name: water-h2
  occurrence_of: H
has_atoms:
- H
- H
- O
has_bonds:
- bond_order: 1
  bond_type: polar covalent
  object: water-h1
  subject: water-o1
- bond_order: 1
  bond_type: polar covalent
  object: water-h2
  subject: water-o1
id: CHEBI:15377
is_organic: false
name: water
smiles_string: O
type: chemrof:Molecule

```
## AtomCation-sodium
### Input
```yaml
elemental_charge: 1
has_element: Na
id: CHEBI:29101
name: sodium (1+)
type: chemrof:AtomCation

```
## NaturalProduct-caffeine
### Input
```yaml
empirical_formula: C8H10N4O2
has_atoms:
- C
- C
- C
- C
- C
- C
- C
- C
- H
- H
- H
- H
- H
- H
- H
- H
- H
- H
- N
- N
- N
- N
- O
- O
id: CHEBI:27732
is_organic: true
name: caffeine
pka_ionization_constant:
- 10.4
smiles_string: CN1C=NC2=C1C(=O)N(C(=O)N2C)C
type: chemrof:NaturalProduct
water_solubility: 20.0

```
## ImpreciseChemicalMixture-wolfes_vitamin_mix
### Input
```yaml
has_proportional_parts:
- composed_of: CHEBI:16709
  concentration:
    unit: mg/L
    value: 10.0
- composed_of: CHEBI:30753
  concentration:
    unit: mg/L
    value: 5.0
- composed_of: CHEBI:30314
  concentration:
    unit: mg/L
    value: 5.0
- composed_of: CHEBI:15940
  concentration:
    unit: mg/L
    value: 5.0
- composed_of: CHEBI:17015
  concentration:
    unit: mg/L
    value: 5.0
- composed_of: CHEBI:49105
  concentration:
    unit: mg/L
    value: 5.0
- composed_of: CHEBI:7916
  concentration:
    unit: mg/L
    value: 5.0
- composed_of: CHEBI:15956
  concentration:
    unit: mg/L
    value: 2.0
- composed_of: CHEBI:27470
  concentration:
    unit: mg/L
    value: 2.0
- composed_of: CHEBI:17439
  concentration:
    unit: mg/L
    value: 0.1
id: ex:wolfes_vitamin_mix
name: Wolfe's vitamin mix
type: chemrof:ImpreciseChemicalMixture

```
## AtomAnion-fluoride
### Input
```yaml
elemental_charge: -1
has_element: F
id: CHEBI:17051
name: fluoride
type: chemrof:AtomAnion

```
## FunctionalGroup-hydroxyl
### Input
```yaml
empirical_formula: OH
id: CHEBI:43176
name: hydroxy group
type: chemrof:FunctionalGroup

```
## MoleculeGroupingClass-short_chain_fatty_acyl_coa
### Input
```yaml
description: A linear fatty acyl-CoA in which the fatty acyl group has a short (up
  to C5) carbon chain.
id: CHEBI:61905
name: short-chain fatty acyl-CoA
subtype_of:
- chemrof:LinearFattyAcylCoA

```
## AtomAnion-chloride
### Input
```yaml
atomic_number: 17
elemental_charge: -1
id: CHEBI:17996
name: chloride
symbol: Cl
type: chemrof:AtomAnion

```
## SubatomicParticle-electron
### Input
```yaml
id: CHEBI:10545
name: electron
subatomic_particle_type: electron
type: chemrof:SubatomicParticle

```
## Protein-insulin
### Input
```yaml
empirical_formula: C257H383N65O77S6
id: UniProtKB:P01308
is_organic: true
name: insulin
type: chemrof:Protein

```
## SmallMolecule-acetic-acid-with-pka
### Input
```yaml
IUPAC_name: acetic acid
empirical_formula: C2H4O2
id: CHEBI:15365
molecular_mass: 60.05
name: acetic acid
pka_ionization_constant:
- 4.74
smiles_string: CC(=O)O
type: chemrof:SmallMolecule
water_solubility: 1000000.0

```
## AtomCation-calcium2
### Input
```yaml
elemental_charge: 2
has_element: Ca
id: CHEBI:29108
inchi_chemical_sublayer: Ca
inchi_string: InChI=1S/Ca/q+2
name: calcium(2+)
type: chemrof:AtomCation

```
## ImpreciseChemicalMixture-RCH2_alphaKG_medium
### Input
```yaml
has_proportional_parts:
- composed_of: CHEBI:30915
  concentration:
    unit: mM
    value: 20.0
  has_ingredient_role:
    role_type: carbon_source
    source_element: CHEBI:27594
- composed_of: CHEBI:31206
  concentration:
    unit: g/L
    value: 0.25
  has_ingredient_role:
    role_type: nitrogen_source
    source_element: CHEBI:25555
- composed_of: CHEBI:32588
  concentration:
    unit: g/L
    value: 0.1
  has_ingredient_role:
    role_type: mineral
- composed_of: CHEBI:37585
  concentration:
    unit: g/L
    value: 0.6
  has_ingredient_role:
    role_type: phosphorus_source
    source_element: CHEBI:28659
- composed_of: CHEBI:44872
  concentration:
    unit: mM
    value: 30.0
  has_ingredient_role:
    role_type: buffer
- composed_of: ex:wolfes_mineral_mix
  has_ingredient_role:
    role_type: trace_element
- composed_of: ex:wolfes_vitamin_mix
  has_ingredient_role:
    role_type: vitamin
id: ex:RCH2_alphaKG_medium
name: RCH2 defined medium with alpha-ketoglutaric acid
ph: 7.0
type: chemrof:ImpreciseChemicalMixture

```
## ImpreciseChemicalMixture-wolfes_mineral_mix
### Input
```yaml
has_proportional_parts:
- composed_of: CHEBI:31795
  concentration:
    unit: g/L
    value: 3.0
- composed_of: CHEBI:44557
  concentration:
    unit: g/L
    value: 1.5
- composed_of: CHEBI:26710
  concentration:
    unit: g/L
    value: 1.0
- composed_of: CHEBI:86364
  concentration:
    unit: g/L
    value: 0.5
- composed_of: CHEBI:53503
  concentration:
    unit: g/L
    value: 0.1
- composed_of: CHEBI:32312
  concentration:
    unit: g/L
    value: 0.1
- composed_of: CHEBI:86158
  concentration:
    unit: g/L
    value: 0.1
- composed_of: CHEBI:75836
  concentration:
    unit: g/L
    value: 0.1
- composed_of: CHEBI:33118
  concentration:
    unit: g/L
    value: 0.01
- composed_of: CHEBI:75213
  concentration:
    unit: g/L
    value: 0.01
id: ex:wolfes_mineral_mix
name: Wolfe's mineral mix
type: chemrof:ImpreciseChemicalMixture

```
## Macromolecule-polyethylene
### Input
```yaml
empirical_formula: C2H4
has_submolecules:
- ethylene
id: CHEBI:60034
is_organic: true
name: polyethylene polymer
type: chemrof:Macromolecule

```
## MoleculeGroupingClass-odd_numbered_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA whose fatty acyl chain has an odd number of carbon atoms.
  Beta-oxidation yields acetyl-CoA plus a terminal propionyl-CoA.
id: chemrof:OddNumberedFattyAcylCoA
name: odd-numbered fatty acyl-CoA
subtype_of:
- CHEBI:37554

```
## Isotope-deuterium
### Input
```yaml
atomic_number: 1
has_element: H
id: CHEBI:29237
isotope_of: CHEBI:49637
name: deuterium atom
neutron_number: 1
symbol: H
type: chemrof:Isotope

```
## MoleculeGroupingClass-branched_chain_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA whose fatty acyl chain carries one or more alkyl substituents.
  Branched-chain fatty acyl-CoAs are processed by peroxisomal (partial) beta-oxidation.
id: CHEBI:61912
name: branched-chain fatty acyl-CoA
subtype_of:
- CHEBI:37554

```
## Isotope-protium
### Input
```yaml
atomic_number: 1
has_element: H
id: CHEBI:29236
isotope_of: CHEBI:49637
name: protium atom
neutron_number: 0
symbol: H
type: chemrof:Isotope

```
## AtomCation-helium2
### Input
```yaml
atomic_number: 2
elemental_charge: 2
id: CHEBI:33316
name: helium(2+)
symbol: He
type: chemrof:AtomCation

```
## MolecularCation-methylammonium
### Input
```yaml
elemental_charge: 1
empirical_formula: CH6N
has_atom_occurrences:
- name: methylammonium-c1
  occurrence_of: C
- name: methylammonium-n1
  occurrence_of: N
- name: methylammonium-h1
  occurrence_of: H
- name: methylammonium-h2
  occurrence_of: H
- name: methylammonium-h3
  occurrence_of: H
- name: methylammonium-h4
  occurrence_of: H
- name: methylammonium-h5
  occurrence_of: H
- name: methylammonium-h6
  occurrence_of: H
has_atoms:
- C
- H
- H
- H
- N
- H
- H
- H
has_bonds:
- bond_order: 1
  bond_type: covalent
  object: methylammonium-h1
  subject: methylammonium-c1
- bond_order: 1
  bond_type: covalent
  object: methylammonium-h2
  subject: methylammonium-c1
- bond_order: 1
  bond_type: covalent
  object: methylammonium-h3
  subject: methylammonium-c1
- bond_order: 1
  bond_type: covalent
  object: methylammonium-n1
  subject: methylammonium-c1
- bond_order: 1
  bond_type: polar covalent
  object: methylammonium-h4
  subject: methylammonium-n1
- bond_order: 1
  bond_type: polar covalent
  object: methylammonium-h5
  subject: methylammonium-n1
- bond_order: 1
  bond_type: polar covalent
  object: methylammonium-h6
  subject: methylammonium-n1
id: CHEBI:59338
is_organic: true
name: methylammonium
smiles_string: C[NH3+]
type: chemrof:MolecularCation

```
## MoleculeGroupingClass-medium_chain_fatty_acyl_coa
### Input
```yaml
description: A linear fatty acyl-CoA in which the fatty acyl group has a medium-length
  (C6 to C12) carbon chain.
id: CHEBI:61907
name: medium-chain fatty acyl-CoA
subtype_of:
- chemrof:LinearFattyAcylCoA

```
## MoleculeGroupingClass-long_chain_fatty_acyl_coa
### Input
```yaml
description: A linear fatty acyl-CoA in which the fatty acyl group has a long (C13
  to C22) carbon chain.
id: CHEBI:33184
name: long-chain fatty acyl-CoA
subtype_of:
- chemrof:LinearFattyAcylCoA

```
## Molecule-citric_acid_with_pka_context
### Input
```yaml
empirical_formula: C6H8O7
id: CHEBI:30769
inchi_string: InChI=1S/C6H8O7/c7-3(8)1-6(13,5(11)12)2-4(9)10/h13H,1-2H2,(H,7,8)(H,9,10)(H,11,12)
molecular_mass: 192.124
name: citric acid
pka_ionic_strength: 0.0
pka_ionization_constant:
- 3.13
- 4.76
- 6.4
pka_pressure: 1.0
pka_solvent: water
pka_temperature: 25.0
smiles_string: OC(=O)CC(O)(C(=O)O)CC(=O)O
type: chemrof:Molecule

```
## SubatomicParticle-proton
### Input
```yaml
id: CHEBI:24636
name: proton
subatomic_particle_type: proton
type: chemrof:SubatomicParticle

```
## MoleculeGroupingClass-saturated_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA in which the fatty acyl chain contains no carbon-carbon
  double bonds.
id: CHEBI:231546
name: saturated fatty acyl-CoA
subtype_of:
- CHEBI:37554

```
## Ester-ethyl_acetate
### Input
```yaml
empirical_formula: C4H8O2
has_atoms:
- C
- C
- C
- C
- H
- H
- H
- H
- H
- H
- H
- H
- O
- O
id: CHEBI:27750
is_organic: true
name: ethyl acetate
smiles_string: CC(=O)OCC
type: chemrof:Ester

```
## ChemicalElement-berkelium
### Input
```yaml
atomic_number: 97
id: CHEBI:33391
inchi_string: InChI=1S/Bk
name: berkelium
smiles_string: '[Bk]'
symbol: Bk

```
## AtomCation-copper2
### Input
```yaml
IUPAC_name: cupric ion
elemental_charge: 2
has_element: Cu
id: CHEBI:29036
inchi_chemical_sublayer: Cu
inchi_string: InChI=1S/Cu/q+2
name: copper(2+)
type: chemrof:AtomCation

```
## ChemicalSalt-sodium_carbonate
### Input
```yaml
empirical_formula: Na2CO3
id: CHEBI:29377
name: sodium carbonate
type: chemrof:ChemicalSalt

```
## Collection-methionine_cycle_excerpt
### Input
```yaml
entities:
- id: INCHIKEY:FFEARJCKVFRZRR-BYPYZUCNSA-N
  inchi_key_string: FFEARJCKVFRZRR-BYPYZUCNSA-N
  name: methionine
  type: chemrof:SmallMolecule
- id: INCHIKEY:ZKHQWZAMYRWXGA-KQYNXXCUSA-J
  inchi_key_string: ZKHQWZAMYRWXGA-KQYNXXCUSA-J
  name: adenosine triphosphate
  type: chemrof:SmallMolecule
- id: INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O
  inchi_key_string: MEFKEPWMEQBLKI-AIRLBKTGSA-O
  name: S-adenosyl-L-methionine
  type: chemrof:SmallMolecule
- direction: l->r
  has_competitive_inhibition:
  - effector: INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O
    regulated_enzyme: MAT1
  id: RHEA:21080
  left_participants:
  - participant: INCHIKEY:FFEARJCKVFRZRR-BYPYZUCNSA-N
    stoichiometry: 1.0
  - participant: INCHIKEY:ZKHQWZAMYRWXGA-KQYNXXCUSA-J
    stoichiometry: 1.0
  name: methionine adenosyltransferase reaction
  reaction_mechanism: irreversible_michaelis_menten
  right_participants:
  - participant: INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O
    stoichiometry: 1.0
  type: chemrof:Reaction

```
## Molecule-dioxygen
### Input
```yaml
empirical_formula: O2
has_atom_occurrences:
- name: dioxygen-o1
  occurrence_of: O
- name: dioxygen-o2
  occurrence_of: O
has_atoms:
- O
- O
has_bonds:
- bond_order: 2
  bond_type: covalent
  object: dioxygen-o2
  subject: dioxygen-o1
id: CHEBI:15379
is_organic: false
name: dioxygen
smiles_string: O=O
type: chemrof:Molecule

```
## Reaction-methionine_adenosyltransferase
### Input
```yaml
direction: l->r
has_allosteric_regulation:
- effector: INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O
  modification_type: activation
  regulated_enzyme: MAT3
has_competitive_inhibition:
- effector: INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O
  regulated_enzyme: MAT1
id: RHEA:21080
left_participants:
- participant: INCHIKEY:FFEARJCKVFRZRR-BYPYZUCNSA-N
  stoichiometry: 1.0
- participant: INCHIKEY:ZKHQWZAMYRWXGA-KQYNXXCUSA-J
  stoichiometry: 1.0
name: methionine adenosyltransferase reaction
reaction_mechanism: irreversible_michaelis_menten
right_participants:
- participant: INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O
  stoichiometry: 1.0
- participant: INCHIKEY:NBIIXXVUZAFLBC-UHFFFAOYSA-L
  stoichiometry: 1.0
- participant: INCHIKEY:XPPKVPWEQAFLFU-UHFFFAOYSA-K
  stoichiometry: 1.0
type: chemrof:Reaction

```
## MonoatomicIon-copper2
### Input
```yaml
elemental_charge: 2
has_element: Cu
id: CHEBI:29036
name: copper(2+)
type: chemrof:MonoatomicIon

```
## MoleculeGroupingClass-very_long_chain_fatty_acyl_coa
### Input
```yaml
description: A linear fatty acyl-CoA in which the fatty acyl group has a chain length
  greater than C22. Very long-chain fatty acyl-CoAs are shortened by peroxisomal (partial)
  beta-oxidation before completion in the mitochondrion.
id: CHEBI:61910
name: very long-chain fatty acyl-CoA
subtype_of:
- chemrof:LinearFattyAcylCoA

```
## ChemicalElement-carbon
### Input
```yaml
atomic_number: 6
id: CHEBI:27594
inchi_string: InChI=1S/C
name: carbon
smiles_string: '[C]'
symbol: C

```
## AtomCation-copper1
### Input
```yaml
IUPAC_name: cuprous ion
elemental_charge: 1
has_element: Cu
id: CHEBI:49552
inchi_chemical_sublayer: Cu
inchi_string: InChI=1S/Cu/q+1
name: copper(1+)
type: chemrof:AtomCation

```
## MoleculeGroupingClass-even_numbered_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA whose fatty acyl chain has an even number of carbon
  atoms. Complete beta-oxidation yields acetyl-CoA only.
id: chemrof:EvenNumberedFattyAcylCoA
name: even-numbered fatty acyl-CoA
subtype_of:
- CHEBI:37554

```
## MoleculeGroupingClass-linear_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA whose fatty acyl chain is unbranched. Linear fatty acyl-CoAs
  are the canonical substrates of mitochondrial fatty acid beta-oxidation.
id: chemrof:LinearFattyAcylCoA
name: linear fatty acyl-CoA
subtype_of:
- CHEBI:37554

```
## NeutralMolecule-water
### Input
```yaml
elemental_charge: 0
has_atoms:
- H
- H
- O
id: CHEBI:15377
is_organic: false
name: water
type: chemrof:NeutralMolecule

```
## UnchargedAtom-hydrogen
### Input
```yaml
atomic_number: 1
elemental_charge: 0
id: CHEBI:49637
name: hydrogen atom
symbol: H
type: chemrof:UnchargedAtom

```
## MoleculeGroupingClass-monounsaturated_fatty_acyl_coa
### Input
```yaml
description: An unsaturated fatty acyl-CoA in which the fatty acyl chain contains
  exactly one carbon-carbon double bond (e.g. oleoyl-CoA, 18:1).
id: chemrof:MonounsaturatedFattyAcylCoA
name: monounsaturated fatty acyl-CoA
subtype_of:
- CHEBI:51006

```
## SubatomicParticle-neutron
### Input
```yaml
id: CHEBI:30222
name: neutron
subatomic_particle_type: neutron
type: chemrof:SubatomicParticle

```
## MoleculeGroupingClass-fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA results from the formal condensation of the thiol group
  of coenzyme A with the carboxy group of a fatty acid. It is the root grouping class
  for the fatty acid beta-oxidation substrate classification.
id: CHEBI:37554
name: fatty acyl-CoA

```
## PolyatomicIon-ammonium
### Input
```yaml
conjugate_base_of: CHEBI:16134
empirical_formula: NH+4
has_atom_occurrences:
- name: ammonium-n
  occurrence_of: N
- name: ammonium-h1
  occurrence_of: H
- name: ammonium-h2
  occurrence_of: H
- name: ammonium-h3
  occurrence_of: H
- name: ammonium-h4
  occurrence_of: H
has_bonds:
- bond_order: 1
  bond_type: polar covalent
  object: ammonium-h1
  subject: ammonium-n
- bond_order: 1
  bond_type: polar covalent
  object: ammonium-h2
  subject: ammonium-n
- bond_order: 1
  bond_type: polar covalent
  object: ammonium-h3
  subject: ammonium-n
- bond_order: 1
  bond_type: polar covalent
  object: ammonium-h4
  subject: ammonium-n
id: CHEBI:28938
name: ammonium
smiles_string: '[NH4+]'
type: chemrof:PolyatomicIon

```
## IsomeraseReaction-glucose_isomerase
### Input
```yaml
id: RHEA:28549
name: glucose isomerase reaction
type: chemrof:IsomeraseReaction

```
## SmallMolecule-glucose
### Input
```yaml
has_atoms:
- C
- C
- C
- C
- C
- C
- H
- H
- H
- H
- H
- H
- H
- H
- H
- H
- H
- H
- O
- O
- O
- O
- O
- O
id: CHEBI:17234
is_organic: true
name: glucose
type: chemrof:SmallMolecule

```
## MoleculeGroupingClass-unsaturated_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA in which the fatty acyl chain contains one or more carbon-carbon
  double bonds.
id: CHEBI:51006
name: unsaturated fatty acyl-CoA
subtype_of:
- CHEBI:37554

```
## FunctionalGroup-carboxyl
### Input
```yaml
empirical_formula: CO2H
id: CHEBI:46883
name: carboxy group
type: chemrof:FunctionalGroup

```
## Collection-nitrites
### Input
```yaml
entities:
- empirical_formula: "NO\u22122"
  has_atom_occurrences:
  - name: _:nitrite-o1
    occurrence_of: oxygen
  - name: _:nitrite-o2
    occurrence_of: oxygen
  - name: _:nitrite-n1
    occurrence_of: nitrogen
  has_bonds:
  - bond_order: 2
    bond_type: sigma
    object: _:nitrite-n1
    subject: _:nitrite-o1
  - bond_order: 1
    bond_type: sigma
    object: _:nitrite-n1
    subject: _:nitrite-o2
  id: CHEBI:16301
  molecular_mass: 46.005
  name: nitrite
  smiles_string: N(=O)[O-]
  type: chemrof:PolyatomicIon
- empirical_formula: HNO2
  has_atom_occurrences:
  - name: _:nitrous_acid-o1
    occurrence_of: oxygen
  - name: _:nitrous_acid-o2
    occurrence_of: oxygen
  - name: _:nitrous_acid-n1
    occurrence_of: nitrogen
  - name: _:nitrous_acid-h1
    occurrence_of: hydrogen
  has_bonds:
  - bond_order: 2
    object: _:nitrous_acid-n1
    subject: _:nitrous_acid-o1
  - bond_order: 1
    object: _:nitrous_acid-n1
    subject: _:nitrous_acid-o2
  - bond_order: 1
    object: _:nitrous_acid-h1
    subject: _:nitrous_acid-o2
  id: CHEBI:25567
  molecular_mass: 47.013
  name: nitrous acid
  smiles_string: N(=O)O
  type: chemrof:PolyatomicIon

```
## Peptide-glycylglycine
### Input
```yaml
empirical_formula: C4H8N2O3
has_atoms:
- C
- C
- C
- C
- H
- H
- H
- H
- H
- H
- H
- H
- N
- N
- O
- O
- O
id: CHEBI:17201
is_organic: true
name: glycylglycine
smiles_string: C(C(=O)NCC(=O)O)N
type: chemrof:Peptide

```
## MoleculeGroupingClass-polyunsaturated_fatty_acyl_coa
### Input
```yaml
description: An unsaturated fatty acyl-CoA in which the fatty acyl chain contains
  two or more carbon-carbon double bonds (e.g. linolenoyl-CoA, 18:3).
id: chemrof:PolyunsaturatedFattyAcylCoA
name: polyunsaturated fatty acyl-CoA
subtype_of:
- CHEBI:51006

```
