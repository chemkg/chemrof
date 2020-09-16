
# Type: uncharged molecule


A molecule that has no charge

URI: [chemont:UnchargedMolecule](http://w3id.org/chemontUnchargedMolecule)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedMolecule&#124;elemental_charge:integer%20%3F]uses%20-.->[Uncharged],[Molecule]^-[UnchargedMolecule],[Uncharged],[Molecule],[AtomicBond],[AtomOccurrence])

## Parents

 *  is_a: [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via bonds

## Uses Mixins

 *  mixin: [Uncharged](Uncharged.md)

## Attributes


### Inherited from molecule:

 * [molecule➞has atom occurrences](molecule_has_atom_occurrences.md)  <sub>0..*</sub>
    * range: [AtomOccurrence](AtomOccurrence.md)
 * [molecule➞has bonds](molecule_has_bonds.md)  <sub>0..*</sub>
    * range: [AtomicBond](AtomicBond.md)

### Mixed in from uncharged:

 * [uncharged➞elemental charge](uncharged_elemental_charge.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)
