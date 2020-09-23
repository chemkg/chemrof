
# Type: radionuclide


an atom that has excess nuclear energy, making it unstable

URI: [chemont:Radionuclide](https://w3id.org/chemont/Radionuclide)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Nuclide]^-[Radionuclide&#124;energy_level(i):string%20%3F;atomic_number(i):count%20%3F;symbol(pk)(i):string;name(i):string%20%3F;id(i):string],[Nuclide])

## Parents

 *  is_a: [Nuclide](Nuclide.md) - an atomic species characterized by the specific constitution of its nucleus

## Attributes


### Inherited from nuclide:

 * [atomic number](atomic_number.md)  <sub>OPT</sub>
    * Description: number of protons in an atom
    * range: [Count](types/Count.md)
 * [energy level](energy_level.md)  <sub>OPT</sub>
    * Description: e.g. ground, stable
    * range: [String](types/String.md)
 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: name of chemical entity. E.g. nickel, carbon-16
    * range: [String](types/String.md)
 * [symbol](symbol.md)  <sub>REQ</sub>
    * Description: short symbol for chemical entity, e.g. K, C-16
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | radioactive nuclide |
|  | | radioactive isotope |
| **Examples:** | | Example(value='radioactive isotope', description=None) |

