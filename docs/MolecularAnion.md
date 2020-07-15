
# Type: molecular anion


A polyatomic ion that is negative

URI: [chemont:MolecularAnion](http://w3id.org/chemontMolecularAnion)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PolyatomicIon],[MolecularAnion&#124;elemental_charge(i):integer%20%3F]uses%20-.->[AnionState],[PolyatomicIon]^-[MolecularAnion],[Atom],[AnionState])

## Parents

 *  is_a: [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).

## Uses Mixins

 *  mixin: [AnionState](AnionState.md)

## Attributes


### Inherited from polyatomic ion:

 * [has atoms](has_atoms.md)  <sub>OPT</sub>
    * range: [Atom](Atom.md)
