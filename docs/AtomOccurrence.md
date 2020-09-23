
# Type: atom occurrence


An occurrence of an atom in the context of a particular molecule. For example, one of two occurrences of oxygen in nitrate

URI: [chemont:AtomOccurrence](https://w3id.org/chemont/AtomOccurrence)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Pattern],[Molecule],[AtomicBond],[Atom]<has%20atom%200..1-%20[AtomOccurrence&#124;valence:integer%20%3F],[AtomicBond]++-%20has%20atom%20occurrences%200..*>[AtomOccurrence],[Molecule]++-%20has%20atom%20occurrences(i)%200..*>[AtomOccurrence],[AtomicBond]++-%20has%20atom%20occurrences(i)%200..*>[AtomOccurrence],[Molecule]++-%20has%20atom%20occurrences%200..*>[AtomOccurrence],[Pattern]^-[AtomOccurrence],[Atom])

## Parents

 *  is_a: [Pattern](Pattern.md) - A pattern observed in nature. Instances of this class may be owl classes in a realist/OBO framework

## Referenced by class

 *  **[AtomicBond](AtomicBond.md)** *[atomic bond➞has atom occurrences](atomic_bond_has_atom_occurrences.md)*  <sub>0..*</sub>  **[AtomOccurrence](AtomOccurrence.md)**
 *  **[AtomOccurrence](AtomOccurrence.md)** *[atomically connected to](atomically_connected_to.md)*  <sub>0..*</sub>  **[AtomOccurrence](AtomOccurrence.md)**
 *  **None** *[has atom occurrences](has_atom_occurrences.md)*  <sub>0..*</sub>  **[AtomOccurrence](AtomOccurrence.md)**
 *  **[Molecule](Molecule.md)** *[molecule➞has atom occurrences](molecule_has_atom_occurrences.md)*  <sub>0..*</sub>  **[AtomOccurrence](AtomOccurrence.md)**

## Attributes


### Own

 * [atom occurrence➞has atom](atom_occurrence_has_atom.md)  <sub>OPT</sub>
    * range: [Atom](Atom.md)
 * [atom occurrence➞valence](atom_occurrence_valence.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)
