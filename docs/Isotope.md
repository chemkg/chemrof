
# Type: isotope


A specific subtype of an atom with a specified neutron number

URI: [chemont:Isotope](http://w3id.org/chemontIsotope)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Isotope]<decay%20product%200..1-++[Isotope&#124;neutron_number:count%20%3F;half_life:number_of_years%20%3F;decay_mode:string%20%3F;decay_energy:string%20%3F;mode_of_formation:string%20%3F;atomic_number(i):count%20%3F;symbol(i):string%20%3F;name(i):string%20%3F],[Isotope]<isotope%20of%200..1-++[Isotope],[Atom]^-[Isotope],[Atom])

## Parents

 *  is_a: [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.

## Referenced by class

 *  **[Isotope](Isotope.md)** *[decay product](decay_product.md)*  <sub>OPT</sub>  **[Isotope](Isotope.md)**
 *  **[Isotope](Isotope.md)** *[isotone of](isotone_of.md)*  <sub>OPT</sub>  **[Isotope](Isotope.md)**
 *  **[Isotope](Isotope.md)** *[isotope of](isotope_of.md)*  <sub>OPT</sub>  **[Isotope](Isotope.md)**
 *  **[Isotope](Isotope.md)** *[nuclear isomer of](nuclear_isomer_of.md)*  <sub>OPT</sub>  **[Isotope](Isotope.md)**

## Attributes


### Own

 * [decay energy](decay_energy.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [decay mode](decay_mode.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [decay product](decay_product.md)  <sub>OPT</sub>
    * range: [Isotope](Isotope.md)
 * [half life](half_life.md)  <sub>OPT</sub>
    * range: [NumberOfYears](types/NumberOfYears.md)
 * [isotope of](isotope_of.md)  <sub>OPT</sub>
    * Description: relationship that holds between two isotopes, always holds if the isotopes have the same atomic number and a different neutron number.
    * range: [Isotope](Isotope.md)
 * [mode of formation](mode_of_formation.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [neutron number](neutron_number.md)  <sub>OPT</sub>
    * Description: number of neutrons in an atom
    * range: [Count](types/Count.md)

### Inherited from atom:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of proteins in an atom
    * range: [Count](types/Count.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>OPT</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)
