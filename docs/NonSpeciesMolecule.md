
# Type: non species molecule


A molecule in which the units are not identical. Example: sodium chloride

URI: [chemont:NonSpeciesMolecule](http://w3id.org/chemontNonSpeciesMolecule)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Molecule]^-[NonSpeciesMolecule&#124;has_part(i):string%20%3F;id(i):string],[Molecule],[AtomicBond],[AtomOccurrence],[Atom])

## Parents

 *  is_a: [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via bonds

## Attributes


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
    * range: [AtomicBond](AtomicBond.md)
 * [molecule➞has part](molecule_has_part.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
