
# Type: molecular cation


A polyatomic ion that is positive

URI: [chemont:MolecularCation](http://w3id.org/chemontMolecularCation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PolyatomicIon],[MolecularCation&#124;elemental_charge(i):integer%20%3F]uses%20-.->[CationState],[PolyatomicIon]^-[MolecularCation],[CationState],[Atom])

## Parents

 *  is_a: [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).

## Uses Mixins

 *  mixin: [CationState](CationState.md)

## Attributes


### Inherited from polyatomic ion:

 * [has atoms](has_atoms.md)  <sub>OPT</sub>
    * range: [Atom](Atom.md)
