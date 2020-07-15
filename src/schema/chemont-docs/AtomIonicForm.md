
# Type: atom ionic form




URI: [chemont:AtomIonicForm](http://w3id.org/chemontAtomIonicForm)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ChargedAtom],[AtomNeutralForm],[AtomIonicForm&#124;elemental_charge:integer%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F]^-[ChargedAtom],[AtomIonicForm]^-[AtomNeutralForm],[Atom]^-[AtomIonicForm],[Atom])

## Parents

 *  is_a: [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

## Children

 * [AtomNeutralForm](AtomNeutralForm.md)
 * [ChargedAtom](ChargedAtom.md)

## Referenced by class


## Attributes


### Own

 * [elemental charge](elemental_charge.md)  <sub>OPT</sub>
    * Description: number of protons minus number of electrons
    * range: [Integer](types/Integer.md)

### Inherited from atom:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of proteins in an atom
    * range: [Count](types/Count.md)
 * [name](name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
