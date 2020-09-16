
# Type: atomic bond


A connection between two atoms. Note this is the reified form of 'atomically connected to'

URI: [chemont:AtomicBond](http://w3id.org/chemontAtomicBond)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Pattern],[Molecule],[AtomOccurrence]<has%20atom%20occurrences%200..*-++[AtomicBond&#124;bond_order:integer%20%3F;bond_type:string%20%3F],[Molecule]++-%20has%20bonds(i)%200..*>[AtomicBond],[Molecule]++-%20has%20bonds%200..*>[AtomicBond],[Pattern]^-[AtomicBond],[AtomOccurrence])

## Parents

 *  is_a: [Pattern](Pattern.md) - A pattern observed in nature. Instances of this class may be owl classes in a realist/OBO framework

## Referenced by class

 *  **[Molecule](Molecule.md)** *[has bonds](has_bonds.md)*  <sub>0..*</sub>  **[AtomicBond](AtomicBond.md)**
 *  **[Molecule](Molecule.md)** *[molecule➞has bonds](molecule_has_bonds.md)*  <sub>0..*</sub>  **[AtomicBond](AtomicBond.md)**

## Attributes


### Own

 * [atomic bond➞bond type](atomic_bond_bond_type.md)  <sub>OPT</sub>
    * Description: E.g. covalent, ionic
    * range: [String](types/String.md)
 * [atomic bond➞has atom occurrences](atomic_bond_has_atom_occurrences.md)  <sub>0..*</sub>
    * range: [AtomOccurrence](AtomOccurrence.md)
 * [bond order](bond_order.md)  <sub>OPT</sub>
    * Description: the number of electron pairs (bonds) between a pair of atoms
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | bond |
|  | | chemical bond |
| **Mappings:** | | CHEMINF:000063 |

