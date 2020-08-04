
# Type: molecular species


A molecule in which the units are identical. Example: methyl

URI: [chemont:MolecularSpecies](http://w3id.org/chemontMolecularSpecies)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Molecule],[Molecule]^-[MolecularSpecies],[AtomicBond],[AtomOccurrence])

## Parents

 *  is_a: [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via bonds

## Attributes


### Inherited from molecule:

 * [molecule➞has atom occurrences](molecule_has_atom_occurrences.md)  <sub>0..*</sub>
    * range: [AtomOccurrence](AtomOccurrence.md)
 * [molecule➞has bonds](molecule_has_bonds.md)  <sub>0..*</sub>
    * range: [AtomicBond](AtomicBond.md)
