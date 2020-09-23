
# Type: molecular species


A molecule in which the units are identical. Example: methyl

URI: [chemont:MolecularSpecies](https://w3id.org/chemont/MolecularSpecies)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Molecule],[Molecule]^-[MolecularSpecies&#124;has_part(i):string%20%3F;id(i):string],[AtomicBond],[AtomOccurrence],[Atom])

## Parents

 *  is_a: [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via covalent bonds

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
    * Description: The set of all bonds connecting atoms in a molecule
    * range: [AtomicBond](AtomicBond.md)
 * [molecule➞has part](molecule_has_part.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
