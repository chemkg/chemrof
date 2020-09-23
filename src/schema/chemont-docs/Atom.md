
# Type: atom


A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

URI: [chemont:Atom](https://w3id.org/chemont/Atom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Nuclide],[Molecule],[Isotope],[FullySpecifiedAtom],[ChemicalEntity],[ChemicalElement],[AtomOccurrence],[AtomIonicForm],[AtomOccurrence]-%20has%20atom%200..1>[Atom&#124;atomic_number:count%20%3F;symbol(pk):string;name:string%20%3F;id(i):string],[Molecule]-%20has%20atoms%200..*>[Atom],[Atom]^-[Nuclide],[Atom]^-[Isotope],[Atom]^-[FullySpecifiedAtom],[Atom]^-[ChemicalElement],[Atom]^-[AtomIonicForm],[ChemicalEntity]^-[Atom])

## Parents

 *  is_a: [ChemicalEntity](ChemicalEntity.md) - An entity that can be described using using chemical properties.

## Children

 * [AtomIonicForm](AtomIonicForm.md) - an atom type in which charge state is specified. Also known as (atom) ionic species
 * [ChemicalElement](ChemicalElement.md) - generic form of an atom, with unspecified neutron or charge
 * [FullySpecifiedAtom](FullySpecifiedAtom.md) - An atom (class) that has subatomic particle counts specified
 * [Isotope](Isotope.md) - A specific subtype of an atom with a specified neutron number
 * [Nuclide](Nuclide.md) - an atomic species characterized by the specific constitution of its nucleus

## Referenced by class

 *  **[AtomOccurrence](AtomOccurrence.md)** *[atom occurrence➞has atom](atom_occurrence_has_atom.md)*  <sub>OPT</sub>  **[Atom](Atom.md)**
 *  **None** *[has atom](has_atom.md)*  <sub>OPT</sub>  **[Atom](Atom.md)**
 *  **[Molecule](Molecule.md)** *[has atoms](has_atoms.md)*  <sub>0..*</sub>  **[Atom](Atom.md)**

## Attributes


### Own

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of protons in an atom
    * range: [Count](types/Count.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>REQ</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)

### Inherited from chemical entity:

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | atomic species |
| **Mappings:** | | COB:0000011 |

