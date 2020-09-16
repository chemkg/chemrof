
# Type: enantiomer


one of two stereoisomers of a chiral molecule that are mirror images. Example: R-thalidomide

URI: [chemont:Enantiomer](http://w3id.org/chemontEnantiomer)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[RacemicMixture],[Molecule],[Molecule]<enantiomer%20form%20of%200..1-%20[Enantiomer&#124;relative_configuration:string%20%3F;optical_configuration:string%20%3F;absolute_configuration:string%20%3F;has_part(i):string%20%3F;id(i):string],[RacemicMixture]-%20has%20left%20enantiomer%201..1>[Enantiomer],[RacemicMixture]-%20has%20right%20enantiomer%201..1>[Enantiomer],[Molecule]^-[Enantiomer],[AtomicBond],[AtomOccurrence],[Atom])

## Parents

 *  is_a: [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via bonds

## Referenced by class

 *  **None** *[has left enantiomer](has_left_enantiomer.md)*  <sub>REQ</sub>  **[Enantiomer](Enantiomer.md)**
 *  **None** *[has right enantiomer](has_right_enantiomer.md)*  <sub>REQ</sub>  **[Enantiomer](Enantiomer.md)**
 *  **[RacemicMixture](RacemicMixture.md)** *[racemic mixture➞has left enantiomer](racemic_mixture_has_left_enantiomer.md)*  <sub>REQ</sub>  **[Enantiomer](Enantiomer.md)**
 *  **[RacemicMixture](RacemicMixture.md)** *[racemic mixture➞has right enantiomer](racemic_mixture_has_right_enantiomer.md)*  <sub>REQ</sub>  **[Enantiomer](Enantiomer.md)**

## Attributes


### Own

 * [enantiomer➞absolute configuration](enantiomer_absolute_configuration.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [enantiomer➞enantiomer form of](enantiomer_enantiomer_form_of.md)  <sub>OPT</sub>
    * Description: Example:  R-thalidomide is the enantiomer form of 2-(2,6-dioxopiperidin-3-yl)-1H-isoindole-1,3(2H)-dione
    * range: [Molecule](Molecule.md)
 * [enantiomer➞optical configuration](enantiomer_optical_configuration.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [enantiomer➞relative configuration](enantiomer_relative_configuration.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from molecule:

 * [has atoms](has_atoms.md)  <sub>0..*</sub>
    * Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
    * range: [Atom](Atom.md)
 * [has submolecules](has_submolecules.md)  <sub>0..*</sub>
    * Description: Relation between a molecule and the molecules it is made from.
    * range: [Molecule](Molecule.md)
 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [molecule➞has atom occurrences](molecule_has_atom_occurrences.md)  <sub>0..*</sub>
    * range: [AtomOccurrence](AtomOccurrence.md)
 * [molecule➞has bonds](molecule_has_bonds.md)  <sub>0..*</sub>
    * range: [AtomicBond](AtomicBond.md)
 * [molecule➞has part](molecule_has_part.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
