
# Type: uncharged atom


An atom that has no charge

URI: [chemont:UnchargedAtom](http://w3id.org/chemontUnchargedAtom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedAtom&#124;elemental_charge(i):integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F;id(i):string]uses%20-.->[Uncharged],[AtomIonicForm]^-[UnchargedAtom],[Uncharged],[AtomIonicForm])

## Parents

 *  is_a: [AtomIonicForm](AtomIonicForm.md) - an atom type in which charge state is specified. Also known as (atom) ionic species

## Uses Mixins

 *  mixin: [Uncharged](Uncharged.md)

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
| **Mappings:** | | COB:0000043 |

