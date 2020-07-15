
# Type: atom


A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

URI: [chemont:Atom](http://w3id.org/chemontAtom)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedAtom],[Nuclide],[MonoatomicIon],[Molecule],[Isotope],[FullySpecifiedAtom],[ChemicalEnitity],[AtomIonicForm],[Molecule]++-%20has%20atoms%200..1>[Atom&#124;atomic_number:count%20%3F;symbol:string%20%3F;name:string%20%3F],[Atom]^-[UnchargedAtom],[Atom]^-[Nuclide],[Atom]^-[MonoatomicIon],[Atom]^-[Isotope],[Atom]^-[FullySpecifiedAtom],[Atom]^-[AtomIonicForm],[ChemicalEnitity]^-[Atom])

## Parents

 *  is_a: [ChemicalEnitity](ChemicalEnitity.md)

## Children

 * [AtomIonicForm](AtomIonicForm.md)
 * [FullySpecifiedAtom](FullySpecifiedAtom.md)
 * [Isotope](Isotope.md) - A specific subtype of an atom with a specified neutron number
 * [MonoatomicIon](MonoatomicIon.md) - An atom that has a charge
 * [Nuclide](Nuclide.md) - an atomic species characterized by the specific constitution of its nucleus
 * [UnchargedAtom](UnchargedAtom.md) - An atom that has no charge

## Referenced by class

 *  **[Molecule](Molecule.md)** *[has atoms](has_atoms.md)*  <sub>OPT</sub>  **[Atom](Atom.md)**

## Attributes


### Own

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of proteins in an atom
    * range: [Count](types/Count.md)
 * [name](name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | atomic species |
| **Mappings:** | | COB:0000011 |

