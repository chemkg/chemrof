
# Type: fully specified atom


An atom (class) that has subatomic particle counts specified

URI: [chemont:FullySpecifiedAtom](http://w3id.org/chemontFullySpecifiedAtom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Atom]^-[FullySpecifiedAtom&#124;elemental_charge:integer%20%3F;neutron_number:count%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F],[Atom])

## Parents

 *  is_a: [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

## Attributes


### Own

 * [elemental charge](elemental_charge.md)  <sub>OPT</sub>
    * Description: number of protons minus number of electrons
    * range: [Integer](types/Integer.md)
 * [neutron number](neutron_number.md)  <sub>OPT</sub>
    * Description: number of neutrons in an atom
    * range: [Count](types/Count.md)

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
