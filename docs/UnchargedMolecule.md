
# Type: uncharged molecule


A molecule that in uncharged charge

URI: [chemont:UnchargedMolecule](http://w3id.org/chemontUnchargedMolecule)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedMolecule&#124;elemental_charge:integer%20%3F]uses%20-.->[Uncharged],[Molecule]^-[UnchargedMolecule],[Uncharged],[Molecule],[Atom])

## Parents

 *  is_a: [Molecule](Molecule.md)

## Uses Mixins

 *  mixin: [Uncharged](Uncharged.md)

## Attributes


### Inherited from molecule:

 * [has atoms](has_atoms.md)  <sub>OPT</sub>
    * range: [Atom](Atom.md)

### Mixed in from uncharged:

 * [uncharged➞elemental charge](uncharged_elemental_charge.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)
