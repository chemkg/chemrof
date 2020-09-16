
# Chemont schema


A data model describing metaclasses for chemical ontology classes


### Classes

 * [GroupingClass](GroupingClass.md) - A non-specific entity. For example "amino acid" is a grouping for "serine", "leucine" etc; ester is a grouping for nitroglycerin; alkane is a grouping for pentane, butane, methane, etc
 * [Pattern](Pattern.md) - A pattern observed in nature. Instances of this class may be owl classes in a realist/OBO framework
    * [AtomOccurrence](AtomOccurrence.md) - An occurrence of an atom in the context of a particular molecule. For example, one of two occurrences of oxygen in nitrate
    * [AtomicBond](AtomicBond.md) - A connection between two atoms. Note this is the reified form of 'atomically connected to'
    * [ChemicalEntity](ChemicalEntity.md) - An entity that can be described using using chemical properties.
       * [Atom](Atom.md) - A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.
          * [AtomIonicForm](AtomIonicForm.md) - an atom type in which charge state is specified. Also known as (atom) ionic species
             * [MonoatomicIon](MonoatomicIon.md) - An atom that has a charge
                * [AtomAnion](AtomAnion.md) - A monoatomic ion that is negative
                * [AtomCation](AtomCation.md) - A monoatomic ion that is positive
             * [UnchargedAtom](UnchargedAtom.md) - An atom that has no charge
          * [FullySpecifiedAtom](FullySpecifiedAtom.md) - An atom (class) that has subatomic particle counts specified
          * [GenericAtom](GenericAtom.md) - generic form of an atom, with unspecified neutron or charge
          * [Isotope](Isotope.md) - A specific subtype of an atom with a specified neutron number
          * [Nuclide](Nuclide.md) - an atomic species characterized by the specific constitution of its nucleus
             * [Radionuclide](Radionuclide.md) - an atom that has excess nuclear energy, making it unstable
       * [Molecule](Molecule.md) - A chemical entity that consists of two or more atoms where all atoms are connected via bonds
          * [Acid](Acid.md)
          * [Enantiomer](Enantiomer.md) - one of two stereoisomers of a chiral molecule that are mirror images. Example: R-thalidomide
          * [MolecularSpecies](MolecularSpecies.md) - A molecule in which the units are identical. Example: methyl
          * [NonSpeciesMolecule](NonSpeciesMolecule.md) - A molecule in which the units are not identical. Example: sodium chloride
          * [PolyatomicIon](PolyatomicIon.md) - A molecule that has a charge. For example, nitrate (NO3-).
             * [MolecularAnion](MolecularAnion.md) - A polyatomic ion that is negative
             * [MolecularCation](MolecularCation.md) - A polyatomic ion that is positive
          * [UnchargedMolecule](UnchargedMolecule.md) - A molecule that has no charge
       * [RacemicMixture](RacemicMixture.md) - a chemical compound that has equal amounts of left- and right-handed enantiomers of a chiral molecule. An example is Thalidomide
       * [Salt](Salt.md) - a chemical compound consisting of an ionic assembly of cations and anions.
       * [SubatomicParticle](SubatomicParticle.md) - A chemical entity below the granularity of an atom.
          * [Electron](Electron.md)
          * [Nucleon](Nucleon.md) - A neutron or proton
             * [Neutron](Neutron.md)
             * [Proton](Proton.md)

### Mixins

 * [AnionState](AnionState.md)
 * [CationState](CationState.md)
 * [ChargeState](ChargeState.md) - Applies to entities that have a charge state, which may be positive, negative, or neutral
    * [Charged](Charged.md)
    * [Uncharged](Uncharged.md)
 * [Charged](Charged.md)
 * [Uncharged](Uncharged.md)

### Slots

 * [absolute configuration](absolute_configuration.md)
    * [enantiomer➞absolute configuration](enantiomer_absolute_configuration.md)
 * [acidity](acidity.md)
 * [alternate form of](alternate_form_of.md) - A relationship between two entities of the same type
    * [chemical isomer of](chemical_isomer_of.md) - a relationship that holds between two forms of a parent molecule with identical chemical formulas but distinct arrangements of atoms in space
       * [stereoisomer of](stereoisomer_of.md) - a relationship that holds between two forms of the 'same' molecule with identical chemical formulas but different bonds
          * [enantiomer of](enantiomer_of.md) - a stereoisomer relationship where the two forms are mirror images of one another
       * [structural isomer of](structural_isomer_of.md) - a relationship that holds between two forms of the 'same' molecule with identical chemical formulas but different bonding patterns
          * [functional isomer of](functional_isomer_of.md) - structural isomers that have the same molecular formula (that is, the same number of atoms of the same elements), but the atoms are connected in different ways so that the groupings are dissimilar.
          * [position isomer of](position_isomer_of.md) - a functional group or other substituent changes position on a parent structure.
          * [skeletal isomer of](skeletal_isomer_of.md) - components of the (usually carbon) skeleton are distinctly re-ordered to create different structures. Pentane exists as three isomers: n-pentane (often called simply "pentane"), isopentane (2-methylbutane) and neopentane (dimethylpropane).
          * [tautomer of](tautomer_of.md) - structural isomers (constitutional isomers) of chemical compounds that readily interconvert. Examples: a neutral amino acid and its zwitterion
    * [isobar of](isobar_of.md) - equal mass number (Z1 + N1 = Z2 + N2)
    * [isotone of](isotone_of.md) - relationship that holds between two isotones, always holds if the isotones have a different atomic number and the same neutron number.
    * [isotope of](isotope_of.md) - relationship that holds between two isotopes, always holds if the isotopes have the same atomic number and a different neutron number.
    * [nuclear isomer of](nuclear_isomer_of.md) - relationship that holds between two nuclear isomers, always holds if the isomers have the same nucleon number but different energy states
 * [atomic number](atomic_number.md) - number of protons in an atom
 * [atomically connected to](atomically_connected_to.md)
 * [bond energy](bond_energy.md) - the measure of bond strength in a chemical bond.
 * [bond length](bond_length.md) - the average distance between nuclei of two bonded atoms in a molecule
 * [bond order](bond_order.md) - the number of electron pairs (bonds) between a pair of atoms
 * [bond type](bond_type.md) - E.g. covalent, ionic
    * [atomic bond➞bond type](atomic_bond_bond_type.md)
 * [chemical formula](chemical_formula.md) - A generic grouping for miolecular formulae and empirican formulae
    * [empirical formula](empirical_formula.md) - A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
    * [molecular formula](molecular_formula.md) - A chemical formula where numbers denote atom count. E.g. C6H12O6  for glucose
    * [smiles string](smiles_string.md) - A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
 * [decay energy](decay_energy.md)
 * [decay mode](decay_mode.md)
 * [decay product](decay_product.md)
 * [elemental charge](elemental_charge.md) - number of protons minus number of electrons
    * [anion state➞elemental charge](anion_state_elemental_charge.md)
       * [atom anion➞elemental charge](atom_anion_elemental_charge.md)
    * [cation state➞elemental charge](cation_state_elemental_charge.md)
       * [atom cation➞elemental charge](atom_cation_elemental_charge.md)
    * [salt➞elemental charge](salt_elemental_charge.md)
    * [uncharged➞elemental charge](uncharged_elemental_charge.md)
 * [enantiomer form of](enantiomer_form_of.md) - Example:  R-thalidomide is the enantiomer form of 2-(2,6-dioxopiperidin-3-yl)-1H-isoindole-1,3(2H)-dione
    * [enantiomer➞enantiomer form of](enantiomer_enantiomer_form_of.md)
 * [energy level](energy_level.md) - e.g. ground, stable
 * [half life](half_life.md)
 * [has atom occurrences](has_atom_occurrences.md)
    * [atomic bond➞has atom occurrences](atomic_bond_has_atom_occurrences.md)
    * [molecule➞has atom occurrences](molecule_has_atom_occurrences.md)
 * [has bonds](has_bonds.md)
    * [molecule➞has bonds](molecule_has_bonds.md)
 * [has cyclic structure](has_cyclic_structure.md) - true if the molecule possesses a cycle in the atom connectivity graph
 * [has left enantiomer](has_left_enantiomer.md)
    * [racemic mixture➞has left enantiomer](racemic_mixture_has_left_enantiomer.md)
 * [has part](has_part.md) - basic parthood relations
    * [has atoms](has_atoms.md) - Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
    * [has submolecules](has_submolecules.md) - Relation between a molecule and the molecules it is made from.
       * [has group](has_group.md) - Relation between a molecule and the groups it contains
    * [molecule➞has part](molecule_has_part.md)
 * [has right enantiomer](has_right_enantiomer.md)
    * [racemic mixture➞has right enantiomer](racemic_mixture_has_right_enantiomer.md)
 * [id](id.md)
 * [mode of formation](mode_of_formation.md)
 * [name](name.md) - name of chemical entity. E.g. nickel, carbon-16
 * [neutron number](neutron_number.md) - number of neutrons in an atom
 * [next in homologous series from](next_in_homologous_series_from.md) - Next in a sequence of compounds with the same functional group and similar chemical properties in which the members of the series can be branched or unbranched. E.g.  ethane (C2H6) next in homologous series from methane (CH4)
 * [nucleon number](nucleon_number.md) - number of nucleons in an atom. proton number plus neutral number.
 * [of atom](of_atom.md)
    * [atom occurrence➞of atom](atom_occurrence_of_atom.md)
 * [optical configuration](optical_configuration.md)
    * [enantiomer➞optical configuration](enantiomer_optical_configuration.md)
 * [relative configuration](relative_configuration.md)
    * [enantiomer➞relative configuration](enantiomer_relative_configuration.md)
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
 * [ChemicalEncoding](types/ChemicalEncoding.md)  (**str**) 
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
