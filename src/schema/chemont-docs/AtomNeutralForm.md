
# Type: atom neutral form




URI: [chemont:AtomNeutralForm](http://w3id.org/chemontAtomNeutralForm)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AtomIonicForm]^-[AtomNeutralForm&#124;elemental_charge:integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F],[AtomIonicForm])

## Parents

 *  is_a: [AtomIonicForm](AtomIonicForm.md) - an atom type in which charge state is specified. Also known as (atom) ionic species

## Referenced by class


## Attributes


### Own

 * [atom neutral form➞elemental charge](atom_neutral_form_elemental_charge.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)

### Inherited from atom ionic form:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of proteins in an atom
    * range: [Count](types/Count.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)
