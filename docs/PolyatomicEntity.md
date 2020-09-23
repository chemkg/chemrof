
# Type: polyatomic entity


Any chemical entity consisting of more than one atom.

URI: [chemont:PolyatomicEntity](https://w3id.org/chemont/PolyatomicEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Salt],[PolyatomicEntity&#124;id(i):string]^-[Salt],[PolyatomicEntity]^-[MoleculePart],[PolyatomicEntity]^-[Molecule],[ChemicalEntity]^-[PolyatomicEntity],[MoleculePart],[Molecule],[ChemicalEntity])

## Parents

 *  is_a: [ChemicalEntity](ChemicalEntity.md) - An entity that can be described using using chemical properties.

## Children

 * [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via covalent bonds
 * [MoleculePart](MoleculePart.md)
 * [Salt](Salt.md) - a chemical compound consisting of an ionic assembly of cations and anions.

## Referenced by class


## Attributes


### Inherited from chemical entity:

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
