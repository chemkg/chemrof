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
molecular_formula: C6H12O6
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
## GroupingBySmarts-heme_o
### Input
```yaml
description: A heme that is heme a with a methyl group in place of the 17-formyl group;
  the biosynthetic precursor of heme a and the heme of cytochrome bo3 ubiquinol oxidase.
  The SMARTS pins every heavy atom of the iron-porphyrin skeleton and its substituents
  by element and heavy-atom degree, so no extra or missing substituents are allowed.
  Ring, Fe-N and C-O bonds are '~', so Kekule or aromatic, dative or charge-separated,
  and acid or carboxylate drawings all match. Acyclic C-C bonds keep their order.
  Iron is left unconstrained, so axial ligands are allowed and the grouping spans
  both oxidation states. Stereochemistry is not constrained.
genus: CHEBI:30413
id: CHEBI:24480
name: heme o
smarts_string: '[#6D1]-[#6D3](-[#6D1])=[#6D2]-[#6D2]-[#6D2]-[#6D3](-[#6D1])=[#6D2]-[#6D2]-[#6D2]-[#6D3](-[#6D1])=[#6D2]-[#6D2]-[#6D2]-[#6D3](~[#8D1])-[#6D3]1~[#6D3](-[#6D1])~[#6D3]2~[#6D2]~[#6D3]3~[#6D3](-[#6D1])~[#6D3](-[#6D2]-[#6D2]-[#6D3](~[#8D1])~[#8D1])~[#6D3]4~[#6D2]~[#6D3]5~[#6D3](-[#6D2]-[#6D2]-[#6D3](~[#8D1])~[#8D1])~[#6D3](-[#6D1])~[#6D3]6~[#6D2]~[#6D3]7~[#6D3](-[#6D2]=[#6D1])~[#6D3](-[#6D1])~[#6D3]8~[#6D2]~[#6D3]~1~[#7D3]~2~[Fe](~[#7D3]~3~4)(~[#7D3]~8~7)~[#7D3]~6~5'
subtype_of:
- CHEBI:30413

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
## Monosaccharide-N_acetyl_D_glucosamine
### Input
```yaml
IUPAC_name: 2-acetamido-2-deoxy-D-glucopyranose
anomeric_configuration: unknown
dl_configuration: D
empirical_formula: C8H15NO6
id: CHEBI:506227
inchi_chemical_sublayer: C8H15NO6
inchi_key_string: OVRNDRQMDRJTHS-RTRLPJTCSA-N
inchi_string: InChI=1S/C8H15NO6/c1-3(11)9-5-7(13)6(12)4(2-10)15-8(5)14/h4-8,10,12-14H,2H2,1H3,(H,9,11)/t4-,5-,6-,7-,8?/m1/s1
is_organic: true
molecular_formula: C8H15NO6
molecular_mass: 221.209
name: N-acetyl-D-glucosamine
ring_form: pyranose
smiles_string: CC(=O)N[C@H]1C(O)O[C@H](CO)[C@@H](O)[C@@H]1O
type: chemrof:Monosaccharide

```
## NaturalProduct-caffeine
### Input
```yaml
empirical_formula: C4H5N2O
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
molecular_formula: C8H10N4O2
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
## NetUnchargedMolecule-ferroheme_a
### Input
```yaml
IUPAC_name: '[3,3''-{7-ethenyl-17-formyl-12-[(1S,4E,8E)-1-hydroxy-5,9,13-trimethyltetradeca-4,8,12-trien-1-yl]-3,8,13-trimethylporphyrin-2,18-diyl-kappa(4)N(21),N(22),N(23),N(24)}dipropanoato(2-)]iron'
classified_by:
- CHEBI:24479
- CHEBI:38573
elemental_charge: 0
has_atom_occurrences:
- coordination_number: 4
  name: ferroheme_a-fe1
  occurrence_of: Fe
  oxidation_number: 2
- name: ferroheme_a-n21
  occurrence_of: N
- name: ferroheme_a-n22
  occurrence_of: N
- name: ferroheme_a-n23
  occurrence_of: N
- name: ferroheme_a-n24
  occurrence_of: N
has_bonds:
- bond_order: 1
  object: ferroheme_a-n21
  subject: ferroheme_a-fe1
- bond_order: 1
  object: ferroheme_a-n22
  subject: ferroheme_a-fe1
- bond_order: 1
  object: ferroheme_a-n23
  subject: ferroheme_a-fe1
- bond_order: 1
  object: ferroheme_a-n24
  subject: ferroheme_a-fe1
id: CHEBI:36163
inchi_key_string: ZGGYGTCPXNDTRV-PRYGPKJJSA-L
inchi_string: InChI=1S/C49H58N4O6.Fe/c1-9-34-31(6)39-25-45-49(46(55)18-12-17-30(5)16-11-15-29(4)14-10-13-28(2)3)33(8)40(52-45)24-44-37(27-54)36(20-22-48(58)59)43(53-44)26-42-35(19-21-47(56)57)32(7)38(51-42)23-41(34)50-39;/h9,13,15,17,23-27,46,55H,1,10-12,14,16,18-22H2,2-8H3,(H4,50,51,52,53,54,56,57,58,59);/q;+2/p-2/b29-15+,30-17+,38-23-,39-25-,40-24-,41-23-,42-26-,43-26-,44-24-,45-25-;/t46-;/m0./s1
is_organic: true
molecular_formula: C49H56FeN4O6
molecular_mass: 852.854
name: ferroheme a
smiles_string: '[H]C(=O)C1=C(CCC(=O)O)C2=[N]3C1=Cc1c(C)c([C@@H](O)CC/C=C(\C)CC/C=C(\C)CCC=C(C)C)c4[n]1[Fe]31[N]3=C(C=c5c(C)c(CCC(=O)O)c([n]51)=C2)C(C=C)=C(C)C3=C4'
type: chemrof:NetUnchargedMolecule

```
## GroupingByGenusAndRangeRestriction-very_long_chain_fatty_acyl_coa
### Input
```yaml
description: A linear fatty acyl-CoA in which the fatty acyl group has a chain length
  greater than C22.
genus: CHEBI:37554
id: CHEBI:61910
min_value: 23
name: very long-chain fatty acyl-CoA
on_property: chemrof:carbon_number
subtype_of:
- chemrof:LinearFattyAcylCoA

```
## FunctionalGroup-hydroxyl
### Input
```yaml
empirical_formula: OH
id: CHEBI:43176
name: hydroxy group
type: chemrof:FunctionalGroup

```
## MolecularCation-ferriheme_b
### Input
```yaml
IUPAC_name: (protoporphyrinato)iron(III)
classified_by:
- CHEBI:26355
- CHEBI:38574
elemental_charge: 1
has_atom_occurrences:
- coordination_number: 4
  name: ferriheme_b-fe1
  occurrence_of: Fe
  oxidation_number: 3
- name: ferriheme_b-n21
  occurrence_of: N
- name: ferriheme_b-n22
  occurrence_of: N
- name: ferriheme_b-n23
  occurrence_of: N
- name: ferriheme_b-n24
  occurrence_of: N
has_bonds:
- bond_order: 1
  object: ferriheme_b-n21
  subject: ferriheme_b-fe1
- bond_order: 1
  object: ferriheme_b-n22
  subject: ferriheme_b-fe1
- bond_order: 1
  object: ferriheme_b-n23
  subject: ferriheme_b-fe1
- bond_order: 1
  object: ferriheme_b-n24
  subject: ferriheme_b-fe1
id: CHEBI:36144
inchi_key_string: GGIDWJQWCUJYRY-RGGAHWMASA-L
inchi_string: InChI=1S/C34H34N4O4.Fe/c1-7-21-17(3)25-13-26-19(5)23(9-11-33(39)40)31(37-26)16-32-24(10-12-34(41)42)20(6)28(38-32)15-30-22(8-2)18(4)27(36-30)14-29(21)35-25;/h7-8,13-16H,1-2,9-12H2,3-6H3,(H4,35,36,37,38,39,40,41,42);/q;+3/p-2/b25-13-,26-13-,27-14-,28-15-,29-14-,30-15-,31-16-,32-16-;
is_organic: true
molecular_formula: C34H32FeN4O4
molecular_mass: 616.499
name: ferriheme b
smiles_string: C=CC1=C(C)C2=Cc3c(C=C)c(C)c4[n]3[Fe+]35[N]2=C1C=c1c(C)c(CCC(=O)O)c([n]13)=CC1=[N]5C(=C4)C(C)=C1CCC(=O)O
type: chemrof:MolecularCation

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
## GroupingBySmarts-fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA results from the formal condensation of the thiol group
  of coenzyme A with the carboxy group of a fatty acid. It is the genus for the fatty
  acid beta-oxidation substrate classification; membership is recognised structurally
  by the coenzyme A thioester substructure.
genus: CHEBI:17984
id: CHEBI:37554
name: fatty acyl-CoA
smarts_string: '[#6]C(=O)SCCNC(=O)CCNC(=O)C(O)C(C)(C)COP(O)(O)=O'

```
## GroupingByGenusAndRangeRestriction-saturated_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA in which the fatty acyl chain contains no carbon-carbon
  double bonds.
genus: CHEBI:37554
id: CHEBI:231546
max_value: 0
min_value: 0
name: saturated fatty acyl-CoA
on_property: chemrof:carbon_carbon_double_bond_number
subtype_of:
- CHEBI:37554

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
## NetUnchargedMolecule-ferroheme_b
### Input
```yaml
IUPAC_name: (protoporphyrinato)iron(II)
classified_by:
- CHEBI:26355
- CHEBI:38573
elemental_charge: 0
has_atom_occurrences:
- coordination_number: 4
  name: ferroheme_b-fe1
  occurrence_of: Fe
  oxidation_number: 2
- name: ferroheme_b-n21
  occurrence_of: N
- name: ferroheme_b-n22
  occurrence_of: N
- name: ferroheme_b-n23
  occurrence_of: N
- name: ferroheme_b-n24
  occurrence_of: N
has_bonds:
- bond_order: 1
  object: ferroheme_b-n21
  subject: ferroheme_b-fe1
- bond_order: 1
  object: ferroheme_b-n22
  subject: ferroheme_b-fe1
- bond_order: 1
  object: ferroheme_b-n23
  subject: ferroheme_b-fe1
- bond_order: 1
  object: ferroheme_b-n24
  subject: ferroheme_b-fe1
has_major_microspecies_at_pH7_3:
- CHEBI:60344
id: CHEBI:17627
inchi_key_string: KABFMIBPWCXCRK-RGGAHWMASA-L
inchi_string: InChI=1S/C34H34N4O4.Fe/c1-7-21-17(3)25-13-26-19(5)23(9-11-33(39)40)31(37-26)16-32-24(10-12-34(41)42)20(6)28(38-32)15-30-22(8-2)18(4)27(36-30)14-29(21)35-25;/h7-8,13-16H,1-2,9-12H2,3-6H3,(H4,35,36,37,38,39,40,41,42);/q;+2/p-2/b25-13-,26-13-,27-14-,28-15-,29-14-,30-15-,31-16-,32-16-;
is_organic: true
molecular_formula: C34H32FeN4O4
molecular_mass: 616.499
name: ferroheme b
smiles_string: C=CC1=C(C)C2=Cc3c(C=C)c(C)c4[n]3[Fe-2]35[n]6c(c(C)c(CCC(=O)O)c6=CC6=[N+]3C(=C4)C(C)=C6CCC(=O)O)=CC1=[N+]25
type: chemrof:NetUnchargedMolecule

```
## GroupingBySmarts-heme_a
### Input
```yaml
description: A heme whose porphyrin carries a formyl group at position 17 and a (1S,4E,8E)-1-hydroxy-5,9,13-trimethyltetradeca-4,8,12-trien-1-yl
  (hydroxyethylfarnesyl) chain at position 12; the heme of cytochrome c oxidase (cytochromes
  a and a3). The oxidation-state-neutral parent of ferroheme a and ferriheme a. The
  SMARTS pins every heavy atom of the iron-porphyrin skeleton and its substituents
  by element and heavy-atom degree, so no extra or missing substituents are allowed.
  Ring, Fe-N and C-O bonds are '~', so Kekule or aromatic, dative or charge-separated,
  and acid or carboxylate drawings all match. Acyclic C-C bonds keep their order.
  Iron is left unconstrained, so axial ligands are allowed and the grouping spans
  both oxidation states. Stereochemistry is not constrained.
genus: CHEBI:30413
id: CHEBI:24479
name: heme a
smarts_string: '[#6D1]-[#6D3](-[#6D1])=[#6D2]-[#6D2]-[#6D2]-[#6D3](-[#6D1])=[#6D2]-[#6D2]-[#6D2]-[#6D3](-[#6D1])=[#6D2]-[#6D2]-[#6D2]-[#6D3](~[#8D1])-[#6D3]1~[#6D3](-[#6D1])~[#6D3]2~[#6D2]~[#6D3]3~[#6D3](-[#6D2]~[#8D1])~[#6D3](-[#6D2]-[#6D2]-[#6D3](~[#8D1])~[#8D1])~[#6D3]4~[#6D2]~[#6D3]5~[#6D3](-[#6D2]-[#6D2]-[#6D3](~[#8D1])~[#8D1])~[#6D3](-[#6D1])~[#6D3]6~[#6D2]~[#6D3]7~[#6D3](-[#6D2]=[#6D1])~[#6D3](-[#6D1])~[#6D3]8~[#6D2]~[#6D3]~1~[#7D3]~2~[Fe](~[#7D3]~3~4)(~[#7D3]~8~7)~[#7D3]~6~5'
subtype_of:
- CHEBI:30413

```
## GroupingByGenusAndRangeRestriction-short_chain_fatty_acyl_coa
### Input
```yaml
description: A linear fatty acyl-CoA in which the fatty acyl group has a short (up
  to C5) carbon chain.
genus: CHEBI:37554
id: CHEBI:61905
max_value: 5
min_value: 2
name: short-chain fatty acyl-CoA
on_property: chemrof:carbon_number
subtype_of:
- chemrof:LinearFattyAcylCoA

```
## SmallMolecule-acetic-acid-with-pka
### Input
```yaml
IUPAC_name: acetic acid
empirical_formula: CH2O
id: CHEBI:15365
molecular_formula: C2H4O2
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
empirical_formula: CH2
has_submolecules:
- ethylene
id: CHEBI:60034
is_organic: true
name: polyethylene polymer
type: chemrof:Macromolecule

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
## GroupingByGenusAndRangeRestriction-monounsaturated_fatty_acyl_coa
### Input
```yaml
description: An unsaturated fatty acyl-CoA in which the fatty acyl chain contains
  exactly one carbon-carbon double bond (e.g. oleoyl-CoA, 18:1).
genus: CHEBI:37554
id: chemrof:MonounsaturatedFattyAcylCoA
max_value: 1
min_value: 1
name: monounsaturated fatty acyl-CoA
on_property: chemrof:carbon_carbon_double_bond_number
smarts_string: '[CX3;!$(C=O)]=[CX3;!$(C=O)]'
subtype_of:
- CHEBI:51006

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
## MoleculeGroupingClass-ferriheme
### Input
```yaml
description: Any iron(III)-porphyrin coordination complex. The differentia is the
  +3 oxidation state of the iron. This cannot be read from a SMILES string (ChEBI
  draws ferriheme b with a formally Fe(+1) centre), and it is not a molecule-level
  property, so no current grouping meta-pattern can define this class. Members state
  it on their iron AtomOccurrence via oxidation_number.
id: CHEBI:38574
name: ferriheme
subtype_of:
- CHEBI:30413

```
## MoleculeGroupingClass-ferroheme
### Input
```yaml
description: Any iron(II)-porphyrin coordination complex. The differentia is the +2
  oxidation state of the iron. This cannot be read from a SMILES string (ChEBI draws
  ferroheme b with a formally Fe(-2) centre and ferroheme a with a neutral one), and
  it is not a molecule-level property, so no current grouping meta-pattern can define
  this class. Members state it on their iron AtomOccurrence via oxidation_number.
id: CHEBI:38573
name: ferroheme
subtype_of:
- CHEBI:30413

```
## GroupingByGenusAndPropertyValue-branched_chain_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA whose fatty acyl chain carries one or more alkyl substituents.
  Processed by peroxisomal (partial) beta-oxidation.
genus: CHEBI:37554
id: CHEBI:61912
name: branched-chain fatty acyl-CoA
on_property: chemrof:is_branched
subtype_of:
- CHEBI:37554
value: 'true'
value_datatype: xsd:boolean

```
## GroupingBySmarts-heme
### Input
```yaml
description: 'A heme is any tetrapyrrolic chelate of iron. Membership is recognised
  structurally: an iron atom bonded to four five-membered-ring nitrogens. The SMARTS
  does not constrain the oxidation state, formal charges or axial ligands of the iron,
  nor how the Fe-N bonds are drawn, so it matches ferrohemes, ferrihemes, hemin and
  hematin alike, while zinc, magnesium and cobalt tetrapyrroles, free-base porphyrins
  and ferrocene do not match.'
genus: CHEBI:33892
id: CHEBI:30413
name: heme
smarts_string: '[Fe](~[#7;r5])(~[#7;r5])(~[#7;r5])~[#7;r5]'

```
## GroupingByGenusAndRangeRestriction-long_chain_fatty_acyl_coa
### Input
```yaml
description: A linear fatty acyl-CoA in which the fatty acyl group has a long (C13
  to C22) carbon chain.
genus: CHEBI:37554
id: CHEBI:33184
max_value: 22
min_value: 13
name: long-chain fatty acyl-CoA
on_property: chemrof:carbon_number
subtype_of:
- chemrof:LinearFattyAcylCoA

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
## GroupingByGenusAndRangeRestriction-unsaturated_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA in which the fatty acyl chain contains one or more carbon-carbon
  double bonds.
genus: CHEBI:37554
id: CHEBI:51006
min_value: 1
name: unsaturated fatty acyl-CoA
on_property: chemrof:carbon_carbon_double_bond_number
smarts_string: '[CX3;!$(C=O)]=[CX3;!$(C=O)]'
subtype_of:
- CHEBI:37554

```
## Ester-ethyl_acetate
### Input
```yaml
empirical_formula: C2H4O
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
molecular_formula: C4H8O2
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
## Monosaccharide-alpha_D_glucopyranose
### Input
```yaml
IUPAC_name: alpha-D-glucopyranose
anomeric_configuration: alpha
dl_configuration: D
empirical_formula: CH2O
id: CHEBI:17925
inchi_chemical_sublayer: C6H12O6
inchi_key_string: WQZGKKKJIJFFOK-DVKNGEFBSA-N
inchi_string: InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6+/m1/s1
is_organic: true
molecular_formula: C6H12O6
molecular_mass: 180.156
name: alpha-D-glucopyranose
ring_form: pyranose
smiles_string: OC[C@H]1O[C@H](O)[C@H](O)[C@@H](O)[C@@H]1O
type: chemrof:Monosaccharide

```
## Reaction-atp_phosphohydrolase
### Input
```yaml
direction: l->r
has_thermodynamic_estimate:
- estimation_method: component_contribution
  ionic_strength: 0.25
  p_h: 7.5
  p_mg: 3.0
  quantity_type: standard_transformed_gibbs_free_energy_change
  source: eQuilibrator (equilibrator-api 0.8.1)
  standard_error: 0.304278
  temperature: 298.15
  unit: kJ/mol
  value: -29.641753
- estimation_method: component_contribution
  ionic_strength: 0.25
  p_h: 7.5
  p_mg: 3.0
  quantity_type: physiological_transformed_gibbs_free_energy_change
  source: eQuilibrator (equilibrator-api 0.8.1)
  standard_error: 0.304278
  temperature: 298.15
  unit: kJ/mol
  value: -46.756591
- estimation_method: component_contribution
  ionic_strength: 0.25
  p_h: 7.5
  p_mg: 3.0
  quantity_type: ln_reversibility_index
  source: eQuilibrator (equilibrator-api 0.8.1)
  standard_error: 0.081873
  temperature: 298.15
  value: -12.581017
id: RHEA:13065
is_balanced: true
left_participants:
- participant: CHEBI:30616
  stoichiometry: 1.0
- participant: CHEBI:15377
  stoichiometry: 1.0
name: ATP phosphohydrolase reaction
reaction_type: hydrolysis
right_participants:
- participant: CHEBI:456216
  stoichiometry: 1.0
- participant: CHEBI:43474
  stoichiometry: 1.0
type: chemrof:Reaction

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
## GroupingByGenusAndPropertyValue-odd_numbered_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA whose fatty acyl chain has an odd number of carbon atoms.
  Beta-oxidation yields acetyl-CoA plus a terminal propionyl-CoA.
genus: CHEBI:37554
id: chemrof:OddNumberedFattyAcylCoA
name: odd-numbered fatty acyl-CoA
on_property: chemrof:carbon_number_parity
subtype_of:
- CHEBI:37554
value: odd

```
## NetUnchargedMolecule-ferroheme_c
### Input
```yaml
IUPAC_name: '{3,3''-[3,7,12,17-tetramethyl-8,13-bis(1-sulfanylethyl)porphyrin-2,18-diyl-kappa(4)N(21),N(22),N(23),N(24)]dipropanoato(2-)}iron'
classified_by:
- CHEBI:38573
elemental_charge: 0
has_atom_occurrences:
- coordination_number: 4
  name: ferroheme_c-fe1
  occurrence_of: Fe
  oxidation_number: 2
- name: ferroheme_c-n21
  occurrence_of: N
- name: ferroheme_c-n22
  occurrence_of: N
- name: ferroheme_c-n23
  occurrence_of: N
- name: ferroheme_c-n24
  occurrence_of: N
has_bonds:
- bond_order: 1
  object: ferroheme_c-n21
  subject: ferroheme_c-fe1
- bond_order: 1
  object: ferroheme_c-n22
  subject: ferroheme_c-fe1
- bond_order: 1
  object: ferroheme_c-n23
  subject: ferroheme_c-fe1
- bond_order: 1
  object: ferroheme_c-n24
  subject: ferroheme_c-fe1
has_major_microspecies_at_pH7_3:
- CHEBI:61717
id: CHEBI:60562
inchi_key_string: XSWPXBWSKQRBRZ-IDTMDVKXSA-L
inchi_string: InChI=1S/C34H38N4O4S2.Fe/c1-15-21(7-9-31(39)40)27-14-28-22(8-10-32(41)42)16(2)24(36-28)12-29-34(20(6)44)18(4)26(38-29)13-30-33(19(5)43)17(3)25(37-30)11-23(15)35-27;/h11-14,19-20H,7-10H2,1-6H3,(H6,35,36,37,38,39,40,41,42,43,44);/q;+2/p-2/b23-11-,24-12-,25-11-,26-13-,27-14-,28-14-,29-12-,30-13-;
is_organic: true
molecular_formula: C34H36FeN4O4S2
molecular_mass: 684.665
name: ferroheme c
smiles_string: CC1=C(CCC(=O)O)C2=[N+]3C1=Cc1c(C)c(C(C)S)c4[n]1[Fe-2]31[n]3c(c(C)c(CCC(=O)O)c3=C2)=CC2=[N+]1C(=C4)C(C)=C2C(C)S
type: chemrof:NetUnchargedMolecule

```
## Molecule-dioxygen
### Input
```yaml
empirical_formula: O
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
molecular_formula: O2
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
## NetUnchargedMolecule-ferroheme_o
### Input
```yaml
IUPAC_name: '[3,3''-{7-ethenyl-12-[(1S,4E,8E)-1-hydroxy-5,9,13-trimethyltetradeca-4,8,12-trien-1-yl]-3,8,13,17-tetramethylporphyrin-2,18-diyl-kappa(4)N(21),N(22),N(23),N(24)}dipropanoato(2-)]iron'
classified_by:
- CHEBI:24480
- CHEBI:38573
elemental_charge: 0
has_atom_occurrences:
- coordination_number: 4
  name: ferroheme_o-fe1
  occurrence_of: Fe
  oxidation_number: 2
- name: ferroheme_o-n21
  occurrence_of: N
- name: ferroheme_o-n22
  occurrence_of: N
- name: ferroheme_o-n23
  occurrence_of: N
- name: ferroheme_o-n24
  occurrence_of: N
has_bonds:
- bond_order: 1
  object: ferroheme_o-n21
  subject: ferroheme_o-fe1
- bond_order: 1
  object: ferroheme_o-n22
  subject: ferroheme_o-fe1
- bond_order: 1
  object: ferroheme_o-n23
  subject: ferroheme_o-fe1
- bond_order: 1
  object: ferroheme_o-n24
  subject: ferroheme_o-fe1
id: CHEBI:36301
inchi_key_string: FISPASSVCDRERW-ARQJTVBPSA-L
inchi_string: InChI=1S/C49H60N4O5.Fe/c1-10-35-31(6)40-26-45-49(46(54)19-13-18-30(5)17-12-16-29(4)15-11-14-28(2)3)34(9)41(53-45)24-38-32(7)36(20-22-47(55)56)43(51-38)27-44-37(21-23-48(57)58)33(8)39(52-44)25-42(35)50-40;/h10,14,16,18,24-27,46,54H,1,11-13,15,17,19-23H2,2-9H3,(H4,50,51,52,53,55,56,57,58);/q;+2/p-2/b29-16+,30-18+,38-24-,39-25-,40-26-,41-24-,42-25-,43-27-,44-27-,45-26-;/t46-;/m0./s1
is_organic: true
molecular_formula: C49H58FeN4O5
molecular_mass: 838.871
name: ferroheme o
smiles_string: C=CC1=C(C)C2=Cc3c([C@@H](O)CC/C=C(\C)CC/C=C(\C)CCC=C(C)C)c(C)c4[n]3[Fe]35[N]2=C1C=c1c(C)c(CCC(=O)O)c([n]13)=CC1=[N]5C(=C4)C(C)=C1CCC(=O)O
type: chemrof:NetUnchargedMolecule

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
## Glycan-lewis_x
### Input
```yaml
IUPAC_name: beta-D-Galp-(1->4)[alpha-L-Fucp-(1->3)]-D-GlcNAc
empirical_formula: C20H35NO15
has_glycosidic_linkages:
- acceptor_position: 3
  anomeric_configuration: alpha
  donor_position: 1
  object: chemrof:lewis_x.GlcNAc
  subject: chemrof:lewis_x.Fuc
- acceptor_position: 4
  anomeric_configuration: beta
  donor_position: 1
  object: chemrof:lewis_x.GlcNAc
  subject: chemrof:lewis_x.Gal
has_monosaccharide_residues:
- anomeric_configuration: unknown
  dl_configuration: D
  id: chemrof:lewis_x.GlcNAc
  name: GlcNAc
  residue_of: CHEBI:506227
  ring_form: pyranose
  type: chemrof:MonosaccharideResidue
- anomeric_configuration: alpha
  dl_configuration: L
  id: chemrof:lewis_x.Fuc
  name: Fuc
  residue_of: CHEBI:42548
  ring_form: pyranose
  type: chemrof:MonosaccharideResidue
- anomeric_configuration: beta
  dl_configuration: D
  id: chemrof:lewis_x.Gal
  name: Gal
  residue_of: CHEBI:27667
  ring_form: pyranose
  type: chemrof:MonosaccharideResidue
has_reducing_end: chemrof:lewis_x.GlcNAc
id: GLYTOUCAN:G39995KJ
inchi_chemical_sublayer: C20H35NO15
is_branched: true
is_organic: true
iupac_condensed_representation: Gal(b1-4)[Fuc(a1-3)]GlcNAc
molecular_formula: C20H35NO15
molecular_mass: 529.49
name: Lewis X trisaccharide
type: chemrof:Glycan
wurcs_representation: WURCS=2.0/3,3,2/[u2122h_2*NCC/3=O][a1221m-1a_1-5][a2112h-1b_1-5]/1-2-3/a3-b1_a4-c1

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
## GroupingByGenusAndPropertyValue-even_numbered_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA whose fatty acyl chain has an even number of carbon
  atoms. Complete beta-oxidation yields acetyl-CoA only.
genus: CHEBI:37554
id: chemrof:EvenNumberedFattyAcylCoA
name: even-numbered fatty acyl-CoA
on_property: chemrof:carbon_number_parity
subtype_of:
- CHEBI:37554
value: even

```
## GroupingByGenusAndRangeRestriction-polyunsaturated_fatty_acyl_coa
### Input
```yaml
description: An unsaturated fatty acyl-CoA in which the fatty acyl chain contains
  two or more carbon-carbon double bonds (e.g. linolenoyl-CoA, 18:3).
genus: CHEBI:37554
id: chemrof:PolyunsaturatedFattyAcylCoA
min_value: 2
name: polyunsaturated fatty acyl-CoA
on_property: chemrof:carbon_carbon_double_bond_number
smarts_string: '[CX3;!$(C=O)]=[CX3;!$(C=O)]'
subtype_of:
- CHEBI:51006

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
## SubatomicParticle-neutron
### Input
```yaml
id: CHEBI:30222
name: neutron
subatomic_particle_type: neutron
type: chemrof:SubatomicParticle

```
## GroupingBySmarts-heme_b
### Input
```yaml
description: A heme in which iron is chelated by protoporphyrin IX (3,8,13,17-tetramethyl-7,12-divinylporphyrin-2,18-dipropanoate);
  the most abundant heme and the oxidation-state-neutral parent of ferroheme b and
  ferriheme b. The SMARTS pins every heavy atom of the iron-porphyrin skeleton and
  its substituents by element and heavy-atom degree, so no extra or missing substituents
  are allowed. Ring, Fe-N and C-O bonds are '~', so Kekule or aromatic, dative or
  charge-separated, and acid or carboxylate drawings all match. Acyclic C-C bonds
  keep their order. Iron is left unconstrained, so axial ligands are allowed and the
  grouping spans both oxidation states. Vinyl (not ethyl) at positions 7 and 12 distinguishes
  it from mesoheme.
genus: CHEBI:30413
id: CHEBI:26355
name: heme b
smarts_string: '[#6D1]-[#6D3]1~[#6D3]2~[#6D2]~[#6D3]3~[#6D3](-[#6D1])~[#6D3](-[#6D2]=[#6D1])~[#6D3]4~[#6D2]~[#6D3]5~[#6D3](-[#6D1])~[#6D3](-[#6D2]=[#6D1])~[#6D3]6~[#6D2]~[#6D3]7~[#6D3](-[#6D1])~[#6D3](-[#6D2]-[#6D2]-[#6D3](~[#8D1])~[#8D1])~[#6D3]8~[#6D2]~[#6D3](~[#6D3]~1-[#6D2]-[#6D2]-[#6D3](~[#8D1])~[#8D1])~[#7D3]~2~[Fe](~[#7D3]~5~6)(~[#7D3]~3~4)~[#7D3]~7~8'
subtype_of:
- CHEBI:30413

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
## FunctionalGroup-carboxyl
### Input
```yaml
empirical_formula: CO2H
id: CHEBI:46883
name: carboxy group
type: chemrof:FunctionalGroup

```
## GroupingByGenusAndRangeRestriction-medium_chain_fatty_acyl_coa
### Input
```yaml
description: A linear fatty acyl-CoA in which the fatty acyl group has a medium-length
  (C6 to C12) carbon chain.
genus: CHEBI:37554
id: CHEBI:61907
max_value: 12
min_value: 6
name: medium-chain fatty acyl-CoA
on_property: chemrof:carbon_number
subtype_of:
- chemrof:LinearFattyAcylCoA

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
## GroupingByGenusAndPropertyValue-linear_fatty_acyl_coa
### Input
```yaml
description: A fatty acyl-CoA whose fatty acyl chain is unbranched. The canonical
  substrate of mitochondrial fatty acid beta-oxidation.
genus: CHEBI:37554
id: chemrof:LinearFattyAcylCoA
name: linear fatty acyl-CoA
on_property: chemrof:is_branched
subtype_of:
- CHEBI:37554
value: 'false'
value_datatype: xsd:boolean

```
