
# Type: charged atom




URI: [chemont:ChargedAtom](http://w3id.org/chemontChargedAtom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ChargedAtom&#124;elemental_charge(i):integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F]^-[AtomCation],[ChargedAtom]^-[AtomAniom],[AtomIonicForm]^-[ChargedAtom],[AtomIonicForm],[AtomCation],[AtomAniom])

## Parents

 *  is_a: [AtomIonicForm](AtomIonicForm.md)

## Children

 * [AtomAniom](AtomAniom.md)
 * [AtomCation](AtomCation.md)

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
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
