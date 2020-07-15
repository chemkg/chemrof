
# Type: charged




URI: [chemont:Charged](http://w3id.org/chemontCharged)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PolyatomicIon]uses%20-.->[Charged&#124;elemental_charge(i):integer%20%3F],[MonoatomicIon]uses%20-.->[Charged],[ChargeState]^-[Charged],[PolyatomicIon],[MonoatomicIon],[ChargeState])

## Parents

 *  is_a: [ChargeState](ChargeState.md)

## Mixin for

 * [MonoatomicIon](MonoatomicIon.md) (mixin)  - An atom that has a charge
 * [PolyatomicIon](PolyatomicIon.md) (mixin)  - A molecule that has a charge. For example, nitrate (NO3-).

## Referenced by class


## Attributes


### Inherited from charge state:

 * [elemental charge](elemental_charge.md)  <sub>OPT</sub>
    * Description: number of protons minus number of electrons
    * range: [Integer](types/Integer.md)
