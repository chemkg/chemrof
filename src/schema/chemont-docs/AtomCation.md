
# Type: atom cation


A monoatomic ion that is positive

URI: [chemont:AtomCation](https://w3id.org/chemont/AtomCation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MonoatomicIon],[CationState],[AtomCation&#124;elemental_charge:integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F;id(i):string]uses%20-.->[CationState],[MonoatomicIon]^-[AtomCation])

## Parents

 *  is_a: [MonoatomicIon](MonoatomicIon.md) - An atom that has a charge

## Uses Mixins

 *  mixin: [CationState](CationState.md)

## Referenced by class


## Attributes


### Own

 * [atom cation➞elemental charge](atom_cation_elemental_charge.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)

### Inherited from monoatomic ion:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of protons in an atom
    * range: [Count](types/Count.md)
 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)
