
# Type: atom


A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

URI: [chemont:Atom](http://w3id.org/chemontAtom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedAtom],[Nuclide],[MonoatomicIon],[Isotope],[GenericAtom],[FullySpecifiedAtom],[ChemicalEntity],[AtomOccurrence],[AtomIonicForm],[AtomOccurrence]++-%20of%20atom(i)%200..1>[Atom&#124;atomic_number:count%20%3F;symbol:string%20%3F;name:string%20%3F],[Atom]^-[UnchargedAtom],[Atom]^-[Nuclide],[Atom]^-[MonoatomicIon],[Atom]^-[Isotope],[Atom]^-[GenericAtom],[Atom]^-[FullySpecifiedAtom],[Atom]^-[AtomIonicForm],[ChemicalEntity]^-[Atom])

## Parents

 *  is_a: [ChemicalEntity](ChemicalEntity.md) - An entity that can be described using using chemical properties.

## Children

 * [AtomIonicForm](AtomIonicForm.md) - an atom type in which charge state is specified. Also known as (atom) ionic species
 * [FullySpecifiedAtom](FullySpecifiedAtom.md) - An atom (class) that has subatomic particle counts specified
 * [GenericAtom](GenericAtom.md) - generic form of an atom, with unspecified neutron or charge
 * [Isotope](Isotope.md) - A specific subtype of an atom with a specified neutron number
 * [MonoatomicIon](MonoatomicIon.md) - An atom that has a charge
 * [Nuclide](Nuclide.md) - an atomic species characterized by the specific constitution of its nucleus
 * [UnchargedAtom](UnchargedAtom.md) - An atom that has no charge

## Referenced by class

 *  **[AtomOccurrence](AtomOccurrence.md)** *[of atom](of_atom.md)*  <sub>OPT</sub>  **[Atom](Atom.md)**

## Attributes


### Own

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of proteins in an atom
    * range: [Count](types/Count.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | atomic species |
| **Mappings:** | | COB:0000011 |

