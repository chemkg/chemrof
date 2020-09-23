
# Type: racemic mixture


a chemical compound that has equal amounts of left- and right-handed enantiomers of a chiral molecule. An example is Thalidomide

URI: [chemont:RacemicMixture](https://w3id.org/chemont/RacemicMixture)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Enantiomer]<has%20right%20enantiomer%201..1-%20[RacemicMixture&#124;id(i):string],[Enantiomer]<has%20left%20enantiomer%201..1-%20[RacemicMixture],[ChemicalEntity]^-[RacemicMixture],[Enantiomer],[ChemicalEntity])

## Parents

 *  is_a: [ChemicalEntity](ChemicalEntity.md) - An entity that can be described using using chemical properties.

## Referenced by class


## Attributes


### Own

 * [racemic mixture➞has left enantiomer](racemic_mixture_has_left_enantiomer.md)  <sub>REQ</sub>
    * range: [Enantiomer](Enantiomer.md)
 * [racemic mixture➞has right enantiomer](racemic_mixture_has_right_enantiomer.md)  <sub>REQ</sub>
    * range: [Enantiomer](Enantiomer.md)

### Inherited from chemical entity:

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
