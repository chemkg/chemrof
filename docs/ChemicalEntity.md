
# Type: chemical entity


An entity that can be described using using chemical properties.

URI: [chemont:ChemicalEntity](http://w3id.org/chemontChemicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SubatomicParticle],[Salt],[RacemicMixture],[Pattern],[Molecule],[ChemicalEntity&#124;id:string]^-[SubatomicParticle],[ChemicalEntity]^-[Salt],[ChemicalEntity]^-[RacemicMixture],[ChemicalEntity]^-[Molecule],[ChemicalEntity]^-[Atom],[Pattern]^-[ChemicalEntity],[Atom])

## Parents

 *  is_a: [Pattern](Pattern.md) - A pattern observed in nature. Instances of this class may be owl classes in a realist/OBO framework

## Children

 * [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.
 * [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via bonds
 * [RacemicMixture](RacemicMixture.md) - a chemical compound that has equal amounts of left- and right-handed enantiomers of a chiral molecule. An example is Thalidomide
 * [Salt](Salt.md) - a chemical compound consisting of an ionic assembly of cations and anions.
 * [SubatomicParticle](SubatomicParticle.md) - A chemical entity below the granularity of an atom.

## Referenced by class

 *  **[ChemicalEntity](ChemicalEntity.md)** *[alternate form of](alternate_form_of.md)*  <sub>OPT</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[isobar of](isobar_of.md)*  <sub>OPT</sub>  **[ChemicalEntity](ChemicalEntity.md)**

## Attributes


### Own

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | CHEBI:24431 |
|  | | CHEMINF:000000 |

