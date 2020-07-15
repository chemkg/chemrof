
# Type: charged atom




URI: [chemont:ChargedAtom](http://w3id.org/chemontChargedAtom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ChargedAtom&#124;elemental_charge(i):integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F]^-[AtomCation],[ChargedAtom]^-[AtomAnion],[AtomIonicForm]^-[ChargedAtom],[AtomIonicForm],[AtomCation],[AtomAnion])

## Parents

 *  is_a: [AtomIonicForm](AtomIonicForm.md) - an atom type in which charge state is specified. Also known as (atom) ionic species

## Children

 * [AtomAnion](AtomAnion.md) - A charged atom that is negative
 * [AtomCation](AtomCation.md) - A charged atom that is positive

## Referenced by class


## Attributes


### Inherited from atom ionic form:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of proteins in an atom
    * range: [Count](types/Count.md)
 * [elemental charge](elemental_charge.md)  <sub>OPT</sub>
    * Description: number of protons minus number of electrons
    * range: [Integer](types/Integer.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)
