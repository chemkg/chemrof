
# Type: molecular cation


A polyatomic ion that is positive

URI: [chemont:MolecularCation](https://w3id.org/chemont/MolecularCation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PolyatomicIon],[Molecule],[MolecularCation&#124;elemental_charge(i):integer%20%3F;has_part(i):string%20%3F;id(i):string]uses%20-.->[CationState],[PolyatomicIon]^-[MolecularCation],[CationState],[AtomicBond],[AtomOccurrence],[Atom])

## Parents

 *  is_a: [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).

## Uses Mixins

 *  mixin: [CationState](CationState.md)

## Attributes


### Inherited from polyatomic ion:

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
    * Description: The set of all bonds connecting atoms in a molecule
    * range: [AtomicBond](AtomicBond.md)
 * [molecule➞has part](molecule_has_part.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
