
# Type: polyatomic ion


A molecule that has a charge. For example, nitrate (NO3-).

URI: [chemont:PolyatomicIon](http://w3id.org/chemontPolyatomicIon)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PolyatomicIon&#124;elemental_charge:integer%20%3F]uses%20-.->[Charged],[PolyatomicIon]^-[MolecularCation],[PolyatomicIon]^-[MolecularAnion],[Molecule]^-[PolyatomicIon],[Molecule],[MolecularCation],[MolecularAnion],[Charged],[Atom])

## Parents

 *  is_a: [Molecule](Molecule.md)

## Uses Mixins

 *  mixin: [Charged](Charged.md)

## Children

 * [MolecularAnion](MolecularAnion.md) - A polyatomic ion that is negative
 * [MolecularCation](MolecularCation.md) - A polyatomic ion that is positive

## Referenced by class


## Attributes


### Inherited from molecule:

 * [has atoms](has_atoms.md)  <sub>OPT</sub>
    * range: [Atom](Atom.md)

### Mixed in from charge state:

 * [elemental charge](elemental_charge.md)  <sub>OPT</sub>
    * Description: number of protons minus number of electrons
    * range: [Integer](types/Integer.md)
