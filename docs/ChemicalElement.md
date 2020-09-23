
# Type: chemical element


generic form of an atom, with unspecified neutron or charge

URI: [chemont:ChemicalElement](https://w3id.org/chemont/ChemicalElement)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Allotrope]-%20allotrope%20of%201..1>[ChemicalElement&#124;symbol(pk):string;periodic_table_group:string%20%3F;periodic_table_block:string%20%3F;boiling_point_in_celcius:float%20%3F;melting_point_in_celcius:float%20%3F;standard_atomic_weight:float%20%3F;electron_configuration:string%20%3F;atomic_number(i):count%20%3F;name(i):string%20%3F;id(i):string],[Atom]^-[ChemicalElement],[Atom],[Allotrope])

## Parents

 *  is_a: [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

## Referenced by class

 *  **None** *[allotrope of](allotrope_of.md)*  <sub>REQ</sub>  **[ChemicalElement](ChemicalElement.md)**
 *  **[Allotrope](Allotrope.md)** *[allotrope➞allotrope of](allotrope_allotrope_of.md)*  <sub>REQ</sub>  **[ChemicalElement](ChemicalElement.md)**

## Attributes


### Own

 * [chemical element➞boiling point in celcius](chemical_element_boiling_point_in_celcius.md)  <sub>OPT</sub>
    * range: [Float](types/Float.md)
 * [chemical element➞electron configuration](chemical_element_electron_configuration.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [chemical element➞melting point in celcius](chemical_element_melting_point_in_celcius.md)  <sub>OPT</sub>
    * range: [Float](types/Float.md)
 * [chemical element➞periodic table block](chemical_element_periodic_table_block.md)  <sub>OPT</sub>
    * Description: block of periodic table unified by the orbitals their valence electrons or vacancies lie in
    * range: [String](types/String.md)
 * [chemical element➞periodic table group](chemical_element_periodic_table_group.md)  <sub>OPT</sub>
    * Description: which number in periodic table column
    * range: [String](types/String.md)
 * [chemical element➞standard atomic weight](chemical_element_standard_atomic_weight.md)  <sub>OPT</sub>
    * range: [Float](types/Float.md)
 * [chemical element➞symbol](chemical_element_symbol.md)  <sub>REQ</sub>
    * Description: E.g. O, K, Ge
    * range: [String](types/String.md)

### Inherited from atom:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of protons in an atom
    * range: [Count](types/Count.md)
 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | element |
|  | | generic atom |
| **Examples:** | | Example(value='carbon', description=None) |
|  | | Example(value='nickel', description=None) |
| **See also:** | | https://en.wikipedia.org/wiki/Chemical_element |

