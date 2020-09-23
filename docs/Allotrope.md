
# Type: allotrope


A molecule consisting of atoms of the same element

URI: [chemont:Allotrope](https://w3id.org/chemont/Allotrope)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Molecule],[ChemicalElement],[AtomicBond],[AtomOccurrence],[Atom],[ChemicalElement]<allotrope%20of%201..1-%20[Allotrope&#124;has_bonding_structure:string;has_part(i):string%20%3F;id(i):string],[Molecule]^-[Allotrope])

## Parents

 *  is_a: [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via covalent bonds

## Referenced by class

 *  **[Allotrope](Allotrope.md)** *[allotropic analog of](allotropic_analog_of.md)*  <sub>OPT</sub>  **[Allotrope](Allotrope.md)**

## Attributes


### Own

 * [allotrope➞allotrope of](allotrope_allotrope_of.md)  <sub>REQ</sub>
    * range: [ChemicalElement](ChemicalElement.md)
 * [allotrope➞has bonding structure](allotrope_has_bonding_structure.md)  <sub>REQ</sub>
    * Description: The pattern in which the atoms are bonded; e.g. hexagonal lattice, sheets, etc
    * range: [String](types/String.md)

### Inherited from molecule:

 * [has atoms](has_atoms.md)  <sub>0..*</sub>
    * Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
    * range: [Atom](Atom.md)
 * [has submolecules](has_submolecules.md)  <sub>0..*</sub>
    * Description: Relation between a molecule and the molecules it is made from.
    * range: [Molecule](Molecule.md)
 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [molecule➞has atom occurrences](molecule_has_atom_occurrences.md)  <sub>0..*</sub>
    * range: [AtomOccurrence](AtomOccurrence.md)
 * [molecule➞has bonds](molecule_has_bonds.md)  <sub>0..*</sub>
    * Description: The set of all bonds connecting atoms in a molecule
    * range: [AtomicBond](AtomicBond.md)
 * [molecule➞has part](molecule_has_part.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Examples:** | | Example(value='diamond', description=None) |
|  | | Example(value='dioxygen', description=None) |

