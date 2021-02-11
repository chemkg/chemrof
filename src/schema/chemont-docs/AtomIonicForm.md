
# Type: atom ionic form


an atom type in which charge state is specified. Also known as (atom) ionic species

URI: [chemont:AtomIonicForm](https://w3id.org/chemont/AtomIonicForm)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedAtom],[MonoatomicIon],[AtomIonicForm&#124;elemental_charge:integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F;id(i):string]^-[UnchargedAtom],[AtomIonicForm]^-[MonoatomicIon],[Atom]^-[AtomIonicForm],[Atom])

## Parents

 *  is_a: [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

## Children

 * [MonoatomicIon](MonoatomicIon.md) - An atom that has a charge
 * [UnchargedAtom](UnchargedAtom.md) - An atom that has no charge

## Referenced by class


## Attributes


### Own

 * [elemental charge](elemental_charge.md)  <sub>OPT</sub>
    * Description: number of protons minus number of electrons
    * range: [Integer](types/Integer.md)

### Inherited from atom:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | atom ionic species |
| **Examples:** | | Example(value='chloride Cl-', description=None) |

