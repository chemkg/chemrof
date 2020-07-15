
# Type: uncharged atom


An atom that has no charge

URI: [chemont:UnchargedAtom](http://w3id.org/chemontUnchargedAtom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedAtom&#124;elemental_charge:integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F]uses%20-.->[Uncharged],[Atom]^-[UnchargedAtom],[Uncharged],[Atom])

## Parents

 *  is_a: [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

## Uses Mixins

 *  mixin: [Uncharged](Uncharged.md)

## Attributes


### Inherited from atom:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of proteins in an atom
    * range: [Count](types/Count.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)

### Mixed in from uncharged:

 * [uncharged➞elemental charge](uncharged_elemental_charge.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | COB:0000043 |

