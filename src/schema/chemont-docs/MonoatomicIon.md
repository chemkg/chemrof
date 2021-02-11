
# Type: monoatomic ion


An atom that has a charge

URI: [chemont:MonoatomicIon](https://w3id.org/chemont/MonoatomicIon)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MonoatomicIon&#124;elemental_charge(i):integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F;id(i):string]uses%20-.->[Charged],[MonoatomicIon]^-[AtomCation],[MonoatomicIon]^-[AtomAnion],[AtomIonicForm]^-[MonoatomicIon],[Charged],[AtomIonicForm],[AtomCation],[AtomAnion])

## Parents

 *  is_a: [AtomIonicForm](AtomIonicForm.md) - an atom type in which charge state is specified. Also known as (atom) ionic species

## Uses Mixins

 *  mixin: [Charged](Charged.md)

## Children

 * [AtomAnion](AtomAnion.md) - A monoatomic ion that is negative
 * [AtomCation](AtomCation.md) - A monoatomic ion that is positive

## Referenced by class


## Attributes


### Inherited from atom ionic form:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of protons in an atom
    * range: [Count](types/Count.md)
 * [elemental charge](elemental_charge.md)  <sub>OPT</sub>
    * Description: number of protons minus number of electrons
    * range: [Integer](types/Integer.md)
 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | charged atom |
| **Mappings:** | | COB:0000042 |
|  | | CHEBI:24867 |

