
# Type: molecular anion


A polyatomic ion that is negative

URI: [chemont:MolecularAnion](http://w3id.org/chemontMolecularAnion)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PolyatomicIon],[MolecularAnion&#124;elemental_charge(i):integer%20%3F]uses%20-.->[AnionState],[PolyatomicIon]^-[MolecularAnion],[AtomicBond],[AtomOccurrence],[AnionState])

## Parents

 *  is_a: [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).

## Uses Mixins

 *  mixin: [AnionState](AnionState.md)

## Attributes


### Inherited from polyatomic ion:

 * [molecule➞has atom occurrences](molecule_has_atom_occurrences.md)  <sub>0..*</sub>
    * range: [AtomOccurrence](AtomOccurrence.md)
 * [molecule➞has bonds](molecule_has_bonds.md)  <sub>0..*</sub>
    * range: [AtomicBond](AtomicBond.md)
