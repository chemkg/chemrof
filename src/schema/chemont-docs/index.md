
# Chemont schema


A data model describing metaclasses for chemical ontology classes


### Classes

 * [GenericAtom](GenericAtom.md) - generic form of an atom, with unspecified neutron or charge
 * [Pattern](Pattern.md) - A pattern observed in nature. Instances of this class may be owl classes in a realist/OBO framework
    * [ChemicalEnitity](ChemicalEnitity.md) - An entity that can be described using using chemical properties.
       * [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.
          * [AtomIonicForm](AtomIonicForm.md) - an atom type in which charge state is specified. Also known as (atom) ionic species
             * [AtomNeutralForm](AtomNeutralForm.md)
             * [ChargedAtom](ChargedAtom.md)
                * [AtomAnion](AtomAnion.md) - A charged atom that is negative
                * [AtomCation](AtomCation.md) - A charged atom that is positive
          * [FullySpecifiedAtom](FullySpecifiedAtom.md)
          * [Isotope](Isotope.md) - A specific subtype of an atom with a specified neutron number
          * [MonoatomicIon](MonoatomicIon.md) - An atom that has a charge
          * [Nuclide](Nuclide.md) - an atomic species characterized by the specific constitution of its nucleus
             * [Radionuclide](Radionuclide.md) - an atom that has excess nuclear energy, making it unstable
          * [UnchargedAtom](UnchargedAtom.md) - An atom that has no charge
       * [Molecule](Molecule.md)
          * [MolecularSpecies](MolecularSpecies.md) - A molecule in which the units are identical. Example: methyl
          * [NonSpeciesMolecule](NonSpeciesMolecule.md) - A molecule in which the units are not identical. Example: sodium chloride
          * [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).
             * [MolecularAnion](MolecularAnion.md) - A polyatomic ion that is negative
             * [MolecularCation](MolecularCation.md) - A polyatomic ion that is positive
          * [UnchargedMolecule](UnchargedMolecule.md) - A molecule that in uncharged charge
       * [SubatomicParticle](SubatomicParticle.md) - A chemical entity below the granularity of an atom.
          * [Electron](Electron.md)
          * [Nucleon](Nucleon.md) - A neutron or proton
             * [Neutron](Neutron.md)
             * [Proton](Proton.md)

### Mixins

 * [AnionState](AnionState.md)
 * [CationState](CationState.md)
 * [ChargeState](ChargeState.md)
    * [Charged](Charged.md)
    * [Uncharged](Uncharged.md)
 * [Charged](Charged.md)
 * [Uncharged](Uncharged.md)

### Slots

 * [atomic number](atomic_number.md) - number of proteins in an atom
 * [decay energy](decay_energy.md)
 * [decay mode](decay_mode.md)
 * [decay product](decay_product.md)
 * [elemental charge](elemental_charge.md) - number of protons minus number of electrons
    * [anion state➞elemental charge](anion_state_elemental_charge.md)
    * [atom anion➞elemental charge](atom_anion_elemental_charge.md)
    * [atom cation➞elemental charge](atom_cation_elemental_charge.md)
    * [atom neutral form➞elemental charge](atom_neutral_form_elemental_charge.md)
    * [cation state➞elemental charge](cation_state_elemental_charge.md)
    * [uncharged➞elemental charge](uncharged_elemental_charge.md)
 * [energy level](energy_level.md) - e.g. ground, stable
 * [half life](half_life.md)
 * [has atoms](has_atoms.md)
 * [isobar of](isobar_of.md) - equal mass number (Z1 + N1 = Z2 + N2)
 * [isotone of](isotone_of.md) - relationship that holds between two isotones, always holds if the isotones have a different atomic number and the same neutron number.
 * [isotope of](isotope_of.md) - relationship that holds between two isotopes, always holds if the isotopes have the same atomic number and a different neutron number.
 * [mode of formation](mode_of_formation.md)
 * [name](name.md) - name of chemical entity. E.g. nickel, carbon-16
 * [neutron number](neutron_number.md) - number of neutrons in an atom
 * [nuclear isomer of](nuclear_isomer_of.md) - relationship that holds between two nuclear isomers, always holds if the isomers have the same nucleon number but different energy states
 * [nucleon number](nucleon_number.md) - number of nucleons in an atom. proton number plus neutral number.
 * [symbol](symbol.md) - short symbol for chemical entity, e.g. K, C-16

### Types


#### Built in

 * **Bool**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Count](types/Count.md)  (**int**) 
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [NumberOfYears](types/NumberOfYears.md)  (**int**) 
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
