
# Type: molecule part




URI: [chemont:MoleculePart](https://w3id.org/chemont/MoleculePart)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PolyatomicEntity],[MoleculePart&#124;id(i):string]^-[Moiety],[MoleculePart]^-[FunctionalGroup],[PolyatomicEntity]^-[MoleculePart],[Moiety],[FunctionalGroup])

## Parents

 *  is_a: [PolyatomicEntity](PolyatomicEntity.md) - Any chemical entity consisting of more than one atom.

## Children

 * [FunctionalGroup](FunctionalGroup.md)
 * [Moiety](Moiety.md) - a named part of a molecule. In some instances moieties may be composed of yet smaller moieties and functional groups

## Referenced by class


## Attributes


### Inherited from polyatomic entity:

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
