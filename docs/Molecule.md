
# Type: molecule


A chemical entity that consists of two or more atoms where all atoms are connected via bonds

URI: [chemont:Molecule](http://w3id.org/chemontMolecule)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedMolecule],[PolyatomicIon],[NonSpeciesMolecule],[AtomicBond]<has%20bonds%200..*-++[Molecule],[AtomOccurrence]<has%20atom%20occurrences%200..*-++[Molecule],[Enantiomer]++-%20enantiomer%20form%20of(i)%200..1>[Molecule],[Molecule]^-[UnchargedMolecule],[Molecule]^-[PolyatomicIon],[Molecule]^-[NonSpeciesMolecule],[Molecule]^-[MolecularSpecies],[Molecule]^-[Enantiomer],[Molecule]^-[Acid],[ChemicalEntity]^-[Molecule],[MolecularSpecies],[Enantiomer],[ChemicalEntity],[AtomicBond],[AtomOccurrence],[Acid])

## Parents

 *  is_a: [ChemicalEntity](ChemicalEntity.md) - An entity that can be described using using chemical properties.

## Children

 * [Acid](Acid.md)
 * [Enantiomer](Enantiomer.md) - one of two stereoisomers that are mirror images. Example: R-thalidomide
 * [MolecularSpecies](MolecularSpecies.md) - A molecule in which the units are identical. Example: methyl
 * [NonSpeciesMolecule](NonSpeciesMolecule.md) - A molecule in which the units are not identical. Example: sodium chloride
 * [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).
 * [UnchargedMolecule](UnchargedMolecule.md) - A molecule that in uncharged charge

## Referenced by class

 *  **[Molecule](Molecule.md)** *[chemical isomer of](chemical_isomer_of.md)*  <sub>OPT</sub>  **[Molecule](Molecule.md)**
 *  **[Enantiomer](Enantiomer.md)** *[enantiomer form of](enantiomer_form_of.md)*  <sub>OPT</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[enantiomer of](enantiomer_of.md)*  <sub>OPT</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[stereoisomer of](stereoisomer_of.md)*  <sub>OPT</sub>  **[Molecule](Molecule.md)**
 *  **[Molecule](Molecule.md)** *[structural isomer of](structural_isomer_of.md)*  <sub>OPT</sub>  **[Molecule](Molecule.md)**

## Attributes


### Own

 * [molecule➞has atom occurrences](molecule_has_atom_occurrences.md)  <sub>0..*</sub>
    * range: [AtomOccurrence](AtomOccurrence.md)
 * [molecule➞has bonds](molecule_has_bonds.md)  <sub>0..*</sub>
    * range: [AtomicBond](AtomicBond.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | molecular entity |
| **Mappings:** | | COB:0000013 |

