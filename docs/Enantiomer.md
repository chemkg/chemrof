
# Type: enantiomer


one of two stereoisomers that are mirror images. Example: R-thalidomide

URI: [chemont:Enantiomer](http://w3id.org/chemontEnantiomer)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[RacemicMixture],[Molecule],[RacemicMixture]++-%20has%20left%20enantiomer(i)%201..1>[Enantiomer],[RacemicMixture]++-%20has%20right%20enantiomer(i)%201..1>[Enantiomer],[Molecule]^-[Enantiomer],[AtomicBond],[AtomOccurrence])

## Parents

 *  is_a: [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via bonds

## Referenced by class

 *  **[RacemicMixture](RacemicMixture.md)** *[has left enantiomer](has_left_enantiomer.md)*  <sub>REQ</sub>  **[Enantiomer](Enantiomer.md)**
 *  **[RacemicMixture](RacemicMixture.md)** *[has right enantiomer](has_right_enantiomer.md)*  <sub>REQ</sub>  **[Enantiomer](Enantiomer.md)**

## Attributes


### Inherited from molecule:

 * [molecule➞has atom occurrences](molecule_has_atom_occurrences.md)  <sub>0..*</sub>
    * range: [AtomOccurrence](AtomOccurrence.md)
 * [molecule➞has bonds](molecule_has_bonds.md)  <sub>0..*</sub>
    * range: [AtomicBond](AtomicBond.md)
