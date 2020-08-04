
# Type: atom aniom




URI: [chemont:AtomAniom](http://w3id.org/chemontAtomAniom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ChargedAtom],[ChargedAtom]^-[AtomAniom&#124;elemental_charge:integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F])

## Parents

 *  is_a: [ChargedAtom](ChargedAtom.md)

## Referenced by class


## Attributes


### Own

 * [atom aniom➞elemental charge](atom_aniom_elemental_charge.md)  <sub>OPT</sub>
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
