
# Type: molecule


A chemical entity that consists of two or more atoms where all atoms are connected via bonds

URI: [chemont:Molecule](http://w3id.org/chemontMolecule)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedMolecule],[PolyatomicIon],[NonSpeciesMolecule],[Atom]<has%20atoms%200..*-%20[Molecule&#124;has_part:string%20%3F;id(i):string],[Molecule]<has%20submolecules%200..*-%20[Molecule],[AtomicBond]<has%20bonds%200..*-++[Molecule],[AtomOccurrence]<has%20atom%20occurrences%200..*-++[Molecule],[Enantiomer]-%20enantiomer%20form%20of%200..1>[Molecule],[Molecule]^-[UnchargedMolecule],[Molecule]^-[PolyatomicIon],[Molecule]^-[NonSpeciesMolecule],[Molecule]^-[MolecularSpecies],[Molecule]^-[Enantiomer],[Molecule]^-[Acid],[ChemicalEntity]^-[Molecule],[MolecularSpecies],[Enantiomer],[ChemicalEntity],[AtomicBond],[AtomOccurrence],[Atom],[Acid])

## Parents

 *  is_a: [ChemicalEntity](ChemicalEntity.md) - An entity that can be described using using chemical properties.

## Children

 * [Acid](Acid.md)
 * [Enantiomer](Enantiomer.md) - one of two stereoisomers of a chiral molecule that are mirror images. Example: R-thalidomide
 * [MolecularSpecies](MolecularSpecies.md) - A molecule in which the units are identical. Example: methyl
 * [NonSpeciesMolecule](NonSpeciesMolecule.md) - A molecule in which the units are not identical. Example: sodium chloride
 * [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).
 * [UnchargedMolecule](UnchargedMolecule.md) - A molecule that has no charge

## Referenced by class

 *  **[Molecule](Molecule.md)** *[chemical isomer of](chemical_isomer_of.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**
 *  **None** *[enantiomer form of](enantiomer_form_of.md)*  <sub>OPT</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[enantiomer of](enantiomer_of.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**
 *  **[Enantiomer](Enantiomer.md)** *[enantiomer➞enantiomer form of](enantiomer_enantiomer_form_of.md)*  <sub>OPT</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[functional isomer of](functional_isomer_of.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**
 *  **[Atom](Atom.md)** *[has group](has_group.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[has submolecules](has_submolecules.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[next in homologous series from](next_in_homologous_series_from.md)*  <sub>OPT</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[position isomer of](position_isomer_of.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[skeletal isomer of](skeletal_isomer_of.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[stereoisomer of](stereoisomer_of.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[structural isomer of](structural_isomer_of.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[tautomer of](tautomer_of.md)*  <sub>0..*</sub>  **[Molecule](Molecule.md)**

## Attributes


### Own

 * [has atoms](has_atoms.md)  <sub>0..*</sub>
    * Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
    * range: [Atom](Atom.md)
 * [has submolecules](has_submolecules.md)  <sub>0..*</sub>
    * Description: Relation between a molecule and the molecules it is made from.
    * range: [Molecule](Molecule.md)
 * [molecule➞has atom occurrences](molecule_has_atom_occurrences.md)  <sub>0..*</sub>
    * range: [AtomOccurrence](AtomOccurrence.md)
 * [molecule➞has bonds](molecule_has_bonds.md)  <sub>0..*</sub>
    * range: [AtomicBond](AtomicBond.md)
 * [molecule➞has part](molecule_has_part.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from chemical entity:

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | molecular entity |
| **Mappings:** | | COB:0000013 |

