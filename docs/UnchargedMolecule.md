
# Type: uncharged molecule


A molecule that has no charge

URI: [chemont:UnchargedMolecule](http://w3id.org/chemontUnchargedMolecule)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedMolecule&#124;elemental_charge:integer%20%3F;has_part(i):string%20%3F;id(i):string]uses%20-.->[Uncharged],[Molecule]^-[UnchargedMolecule],[Uncharged],[Molecule],[AtomicBond],[AtomOccurrence],[Atom])

## Parents

 *  is_a: [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via bonds

## Uses Mixins

 *  mixin: [Uncharged](Uncharged.md)

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

### Mixed in from uncharged:

 * [uncharged➞elemental charge](uncharged_elemental_charge.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)
