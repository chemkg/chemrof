
# Type: molecule




URI: [chemont:Molecule](http://w3id.org/chemontMolecule)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UnchargedMolecule],[PolyatomicIon],[NonSpeciesMolecule],[Atom]<has%20atoms%200..1-++[Molecule],[Molecule]^-[UnchargedMolecule],[Molecule]^-[PolyatomicIon],[Molecule]^-[NonSpeciesMolecule],[Molecule]^-[MolecularSpecies],[ChemicalEnitity]^-[Molecule],[MolecularSpecies],[ChemicalEnitity],[Atom])

## Parents

 *  is_a: [ChemicalEnitity](ChemicalEnitity.md) - An entity that can be described using using chemical properties.

## Children

 * [MolecularSpecies](MolecularSpecies.md) - A molecule in which the units are identical. Example: methyl
 * [NonSpeciesMolecule](NonSpeciesMolecule.md) - A molecule in which the units are not identical. Example: sodium chloride
 * [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).
 * [UnchargedMolecule](UnchargedMolecule.md) - A molecule that in uncharged charge

## Referenced by class


## Attributes


### Own

 * [has atoms](has_atoms.md)  <sub>OPT</sub>
    * range: [Atom](Atom.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | molecular entity |
| **Mappings:** | | COB:0000013 |

