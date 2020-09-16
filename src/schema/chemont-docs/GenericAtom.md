
# Type: generic atom


generic form of an atom, with unspecified neutron or charge

URI: [chemont:GenericAtom](http://w3id.org/chemontGenericAtom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Atom]^-[GenericAtom&#124;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F;id(i):string],[Atom])

## Parents

 *  is_a: [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

## Attributes


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
| **Aliases:** | | element |
|  | | chemical element |
| **Examples:** | | Example(value='carbon', description=None) |
|  | | Example(value='nickel', description=None) |

