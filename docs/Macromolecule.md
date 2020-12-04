
# Type: macromolecule




URI: [chemont:Macromolecule](https://w3id.org/chemont/Macromolecule)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Protein],[Polymer],[Peptide],[Copolymer]-%20has%20part%200..*>[Macromolecule&#124;id(i):string],[Polymer]-%20has%20part%200..1>[Macromolecule],[Macromolecule]^-[Protein],[Macromolecule]^-[Peptide],[Macromolecule]^-[Glycan],[ChemicalEntity]^-[Macromolecule],[Glycan],[Copolymer],[ChemicalEntity])

## Parents

 *  is_a: [ChemicalEntity](ChemicalEntity.md) - An entity that can be described using using chemical properties.

## Children

 * [Glycan](Glycan.md)
 * [Peptide](Peptide.md)
 * [Protein](Protein.md)

## Referenced by class

 *  **[Copolymer](Copolymer.md)** *[copolymer➞has part](copolymer_has_part.md)*  <sub>0..*</sub>  **[Macromolecule](Macromolecule.md)**
 *  **[Polymer](Polymer.md)** *[polymer➞has part](polymer_has_part.md)*  <sub>OPT</sub>  **[Macromolecule](Macromolecule.md)**

## Attributes


### Inherited from chemical entity:

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
