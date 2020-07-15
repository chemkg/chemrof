
# Type: atom anion


A charged atom that is negative

URI: [chemont:AtomAnion](http://w3id.org/chemontAtomAnion)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ChargedAtom],[AtomAnion&#124;elemental_charge:integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F]uses%20-.->[AnionState],[ChargedAtom]^-[AtomAnion],[AnionState])

## Parents

 *  is_a: [ChargedAtom](ChargedAtom.md)

## Uses Mixins

 *  mixin: [AnionState](AnionState.md)

## Referenced by class


## Attributes


### Own

 * [atom anion➞elemental charge](atom_anion_elemental_charge.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)

### Inherited from charged atom:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of proteins in an atom
    * range: [Count](types/Count.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)
