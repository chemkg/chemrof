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
## Protein-insulin
### Input
```yaml
empirical_formula: C257H383N65O77S6
id: UniProtKB:P01308
is_organic: true
name: insulin
type: chemrof:Protein

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
## SubatomicParticle-electron
### Input
```yaml
id: CHEBI:10545
name: electron
subatomic_particle_type: electron
type: chemrof:SubatomicParticle

```
## FunctionalGroup-hydroxyl
### Input
```yaml
empirical_formula: OH
id: CHEBI:43176
name: hydroxy group
type: chemrof:FunctionalGroup

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
## MonoatomicIon-copper2
### Input
```yaml
elemental_charge: 2
has_element: Cu
id: CHEBI:29036
name: copper(2+)
type: chemrof:MonoatomicIon

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
## SubatomicParticle-neutron
### Input
```yaml
id: CHEBI:30222
name: neutron
subatomic_particle_type: neutron
type: chemrof:SubatomicParticle

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
smiles_string: CN1C=NC2=C1C(=O)N(C(=O)N2C)C
type: chemrof:NaturalProduct

```
## ChemicalSalt-sodium_carbonate
### Input
```yaml
empirical_formula: Na2CO3
id: CHEBI:29377
name: sodium carbonate
type: chemrof:ChemicalSalt

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
## SubatomicParticle-proton
### Input
```yaml
id: CHEBI:24636
name: proton
subatomic_particle_type: proton
type: chemrof:SubatomicParticle

```
## FunctionalGroup-carboxyl
### Input
```yaml
empirical_formula: CO2H
id: CHEBI:46883
name: carboxy group
type: chemrof:FunctionalGroup

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
