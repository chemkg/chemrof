
# Type: molecular anion


A polyatomic ion that is negative

URI: [chemont:MolecularAnion](http://w3id.org/chemontMolecularAnion)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PolyatomicIon],[Molecule],[MolecularAnion&#124;elemental_charge(i):integer%20%3F;has_part(i):string%20%3F;id(i):string]uses%20-.->[AnionState],[PolyatomicIon]^-[MolecularAnion],[AtomicBond],[AtomOccurrence],[Atom],[AnionState])

## Parents

 *  is_a: [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).

## Uses Mixins

 *  mixin: [AnionState](AnionState.md)

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
    * range: [AtomicBond](AtomicBond.md)
 * [molecule➞has part](molecule_has_part.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
