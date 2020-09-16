
# Type: polyatomic ion


A molecule that has a charge. For example, nitrate (NO3-).

URI: [chemont:PolyatomicIon](http://w3id.org/chemontPolyatomicIon)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PolyatomicIon&#124;elemental_charge:integer%20%3F;has_part(i):string%20%3F;id(i):string]uses%20-.->[Charged],[PolyatomicIon]^-[MolecularCation],[PolyatomicIon]^-[MolecularAnion],[Molecule]^-[PolyatomicIon],[Molecule],[MolecularCation],[MolecularAnion],[Charged],[AtomicBond],[AtomOccurrence],[Atom])

## Parents

 *  is_a: [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via bonds

## Uses Mixins

 *  mixin: [Charged](Charged.md)

## Children

 * [MolecularAnion](MolecularAnion.md) - A polyatomic ion that is negative
 * [MolecularCation](MolecularCation.md) - A polyatomic ion that is positive

## Referenced by class


## Attributes


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

### Mixed in from charge state:

 * [elemental charge](elemental_charge.md)  <sub>OPT</sub>
    * Description: number of protons minus number of electrons
    * range: [Integer](types/Integer.md)
