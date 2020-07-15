
# Type: monoatomic ion


An atom that has a charge

URI: [chemont:MonoatomicIon](http://w3id.org/chemontMonoatomicIon)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MonoatomicIon&#124;elemental_charge:integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F]uses%20-.->[Charged],[Atom]^-[MonoatomicIon],[Charged],[Atom])

## Parents

 *  is_a: [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

## Uses Mixins

 *  mixin: [Charged](Charged.md)

## Attributes


### Inherited from atom:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of proteins in an atom
    * range: [Count](types/Count.md)
 * [name](name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Mixed in from charge state:

 * [elemental charge](elemental_charge.md)  <sub>OPT</sub>
    * Description: number of protons minus number of electrons
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | COB:0000042 |
|  | | CHEBI:24867 |

