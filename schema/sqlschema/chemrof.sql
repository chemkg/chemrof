-- # Class: "Collection" Description: ""
--     * Slot: id Description: 
-- # Abstract Class: "DomainEntity" Description: "A discrete, specific named entity in the domain of chemistry."
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: Collection_id Description: Autocreated FK slot
-- # Abstract Class: "PhysicochemicalEntity" Description: "A discrete chemical structure, material structure, or subatomic particle type"
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
-- # Abstract Class: "ChemicalEntity" Description: "A discrete structure that is one or more atoms that can be described by a chemical formula."
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "SubatomicParticle" Description: "A chemical entity below the granularity of an atom."
--     * Slot: subatomic_particle_type Description: 
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
-- # Class: "OwlClass" Description: "instances of this class mixin are OWL Classes"
--     * Slot: id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "GroupingClass" Description: "Instances of this class represent generic  concepts that can be used to group more specific concepts, or to classify entities"
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "PhysicochemicalEntityGroupingClass" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "ChemicalGroupingClass" Description: "Instances of this class represent generic chemical concepts that can be used to group more specific concepts, or to classify entities. For example "amino acid" is a grouping for "serine", "leucine" etc; ester is a grouping for nitroglycerin; alkane is a grouping for pentane, butane, methane, etc"
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ReactionGroupingClass" Description: "A grouping class for reactions, for example, dehalogenase; breaking of covalent bond"
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MaterialGroupingClass" Description: "A grouping class that classifies materials"
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ChemicalGroupingByCharge" Description: "A grouping class that refines a charge-neutral entity"
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MoleculeGroupingClass" Description: "A grouping class that classifies molecules. Example: carbohydrate, monosaccharide, amino acid, polyacrylamide"
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MolecularComponentGroupingClass" Description: "A grouping class that classifies molecular components. Example: inorganic anion group"
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MolecularDerivativeGroupingClass" Description: "A grouping class defined as a derivative of another molecule or molecular grouping class"
--     * Slot: derivative_of Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MoleculeGroupingClassDefinedByComponents" Description: "A grouping class defined as an exhaustive list of components"
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: has_part_id Description: basic parthood relations
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MoleculeGroupingClassDefinedByAdditionOfAGroup" Description: "A grouping class defined in terms of a derivative of a molecule and the addition of a group"
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ChemicalSaltGroupingClass" Description: "A grouping class for a chemical salt"
--     * Slot: has_anionic_component Description: 
--     * Slot: has_cationic_component Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ChemicalSaltByCation" Description: "A grouping class for a chemical salt named by cation"
--     * Slot: has_cationic_component Description: 
--     * Slot: has_anionic_component Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ChemicalSaltByAnion" Description: "A grouping class for a chemical salt named by anion"
--     * Slot: has_anionic_component Description: 
--     * Slot: has_cationic_component Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "GeneralizedMolecularStructureClass" Description: "A molecule grouping class that can be written using a chemical formula using variables (e.g. n), or arithmetic expressions uing variables (e.g. 2n+2), plus optionally constraints on those variables (e.g. n>3). An example is alkane; CnH2n+2, which groups specific molecules such as methane"
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MonomericPolymericGroupingClass" Description: ""
--     * Slot: has_repeat_unit Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "GroupingClassForAcidsOrBases" Description: ""
--     * Slot: conjugate_base_of Description: connects the base form of an acid to an acid. Also connects the different charge states of the base. Example: the different charge states of lactate (CHEBI:24996) conjugate base of lactic acid (CHEBI:28358)
--     * Slot: conjugate_acid_of Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AcidAnionGroupingClass" Description: "A molecule grouping class that groups the different ion forms of the base of an acid"
--     * Slot: conjugate_base_of Description: connects the base form of an acid to an acid. Also connects the different charge states of the base. Example: the different charge states of lactate (CHEBI:24996) conjugate base of lactic acid (CHEBI:28358)
--     * Slot: conjugate_acid_of Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "GeneralAcidBaseGroupingClass" Description: "A molecule grouping class that can groups an acid together with all its conjugate bases. physiological"
--     * Slot: conjugate_base_of Description: connects the base form of an acid to an acid. Also connects the different charge states of the base. Example: the different charge states of lactate (CHEBI:24996) conjugate base of lactic acid (CHEBI:28358)
--     * Slot: conjugate_acid_of Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AcidBaseConflationClass" Description: "A molecule grouping class that can groups an acid together with all its conjugate bases. physiological"
--     * Slot: conjugate_base_of Description: connects the base form of an acid to an acid. Also connects the different charge states of the base. Example: the different charge states of lactate (CHEBI:24996) conjugate base of lactic acid (CHEBI:28358)
--     * Slot: conjugate_acid_of Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AtomGroupingClass" Description: "A grouping class that classifies atoms. For example, metal atom"
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "AtomGroupingByPeriodicTablePlacement" Description: ""
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AtomGroupingByPeriodicTableGroup" Description: "Example: p-block atom"
--     * Slot: in_periodic_table_group Description: 
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AtomGroupingByPeriodicTableBlock" Description: "Example: group 13 atom"
--     * Slot: in_periodic_table_block Description: A block of the periodic table is a set of elements unified by the orbitals their valence electrons or vacancies lie in
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AtomGroupingByProperty" Description: "Example: metal atom"
--     * Slot: id Description: 
--     * Slot: smarts_string Description: a molecular pattern matching language, related to the popular SMILES molecular language, that can be used to specify sub-structural patterns in molecules.
--     * Slot: markush_string Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Material" Description: "A substance composed of repeated chemical units that has a specific arrangement of atoms or molecules."
--     * Slot: has_repeat_unit Description: 
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
-- # Class: "Nanomaterial" Description: "A material of which a single unit is sized (in at least one dimension) between 1 and 100 nm"
--     * Slot: has_repeat_unit Description: 
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
-- # Class: "Mineral" Description: ""
--     * Slot: has_repeat_unit Description: 
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
-- # Class: "ChemicalEntityOrGrouping" Description: ""
--     * Slot: id Description: 
-- # Abstract Class: "Connectivity" Description: "Abstract grouping for slots that related chemical entities via a connectivity relationships"
--     * Slot: id Description: 
-- # Class: "FullyCovalentlyBonded" Description: "All pairs of atoms in this entity are transitively connected via covalent bonds"
--     * Slot: id Description: 
-- # Class: "WeaklyBonded" Description: "Not covalently bonded"
--     * Slot: id Description: 
-- # Abstract Class: "State" Description: ""
--     * Slot: id Description: 
-- # Class: "ChargeState" Description: "Applies to entities that have a charge state, which may be positive, negative, or neutral"
--     * Slot: id Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
-- # Class: "AnionState" Description: "This mixin is applied on an entity (atom or molecule) that is negatively charged"
--     * Slot: id Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
-- # Class: "CationState" Description: "This mixin is applied on an entity (atom or molecule) that is positively charged"
--     * Slot: id Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
-- # Class: "Uncharged" Description: "Applies to entities that are uncharged, i.e. have an elemental charge of zero"
--     * Slot: id Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
-- # Class: "Charged" Description: "Applies to entities that are charged, either positive or negative"
--     * Slot: id Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
-- # Abstract Class: "PolyatomicEntity" Description: "Any chemical entity consisting of more than one atom."
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "SmallMolecule" Description: "A molecule characterized by availability in small-molecule databases"
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Macromolecule" Description: "A large molecule, such as a polymer, lipid, or macrocycle"
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MolecularComplex" Description: "A molecular complex is a chemical complex composed of at least one weakly interacting molecule.[SIO] Examples: chromosome, double-standed DNA, protein-containing macromolecular complex"
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Peptide" Description: ""
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Protein" Description: "A macromolecule composed of one or more polypeptide chains of amino acids that fold into a specific three-dimensional structure and perform biological functions"
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Glycan" Description: "A macromolecule consisting of a large number of monosaccharides linked glycosidically"
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MonomolecularPolymer" Description: "A macromolecule composed of repeating subunits. Examples: cellulose"
--     * Slot: polymer_of Description: 
--     * Slot: has_repeat_unit Description: 
--     * Slot: is_branched Description: 
--     * Slot: polymer_architecture_type Description: morphological structure of a polymer
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "SupramolecularPolymer" Description: "polymeric arrays of monomeric units that are connected by reversible and highly directional secondary interactions–that is, non-covalent bonds"
--     * Slot: polymer_of Description: 
--     * Slot: has_repeat_unit Description: 
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Copolymer" Description: "a polymer with a more than one type of repeating unit"
--     * Slot: has_repeat_unit Description: 
--     * Slot: is_branched Description: 
--     * Slot: polymer_architecture_type Description: morphological structure of a polymer
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Homopolymer" Description: "a polymer with a single type of repeating unit"
--     * Slot: polymer_of Description: 
--     * Slot: has_repeat_unit Description: 
--     * Slot: is_branched Description: 
--     * Slot: polymer_architecture_type Description: morphological structure of a polymer
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MolecularComponent" Description: "A proper part of a molecule that is larger than an atom"
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "PolymerPart" Description: ""
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Monomer" Description: ""
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MolecularSubsequence" Description: ""
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ChemicalGroup" Description: ""
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "ChemicalMixture" Description: "A polyatomic entity that consists of two or more parts that are weakly bound, may be of known or unknown stoichiometry"
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "PreciseChemicalMixture" Description: "A polyatomic entity that consists of two or more parts that are weakly bound, and of known stoichiometry"
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ImpreciseChemicalMixture" Description: "A macroscopic polyatomic entity that consists of multiple chemical entities where the stoichiometry is not specified and the spatial arrangement of the ingredients is not defined. Examples include coal, tea tree oil, toothpaste, organometallic compounds, heterogeneous metals"
--     * Slot: has_mixfile_location Description: Location of a MixFile representing a chemical mixture
--     * Slot: has_minchi_representation Description: Proposed new Mixtures InChI
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Molecule" Description: "A chemical entity that consists of two or more atoms where all atoms are connected via covalent bonds."
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "NaturalProduct" Description: ""
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Moiety" Description: "a named part of a molecule. In some instances moieties may be composed of yet smaller moieties and functional groups"
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "SequenceInterval" Description: "a chain of connected monomers in a linear polymer - for example, a sub-region of an amino acid or nucleotide sequence."
--     * Slot: has_sequence_representation Description: 
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AminoAcidSequenceInterval" Description: ""
--     * Slot: has_sequence_representation Description: 
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "NucleotideSequenceInterval" Description: ""
--     * Slot: has_sequence_representation Description: By convention the sequence string is always the DNA sequence. For RNA intervals, this is the cDNA sequence
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "DNASequenceInterval" Description: ""
--     * Slot: has_sequence_representation Description: By convention the sequence string is always the DNA sequence. For RNA intervals, this is the cDNA sequence
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "RNASequenceInterval" Description: ""
--     * Slot: has_sequence_representation Description: By convention the sequence string is always the DNA sequence. For RNA intervals, this is the cDNA sequence
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "FunctionalGroup" Description: ""
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MolecularSpecies" Description: "A molecule in which the units are identical. Example: methyl"
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "NonSpeciesMolecule" Description: "A molecule in which the units are not identical. TODO: move this higher"
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "MoleculeByChargeState" Description: "A molecule that has a charge state specified"
--     * Slot: bronsted_acid_base_role Description: 
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "PolyatomicIon" Description: "A molecule that has a net charge. For example, nitrate is a molecular and ionic species; its formula is (NO3-)."
--     * Slot: conjugate_base_of Description: connects the base form of an acid to an acid. Also connects the different charge states of the base. Example: the different charge states of lactate (CHEBI:24996) conjugate base of lactic acid (CHEBI:28358)
--     * Slot: conjugate_acid_of Description: 
--     * Slot: bronsted_acid_base_role Description: 
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MolecularCation" Description: "A polyatomic ion that is positive"
--     * Slot: conjugate_base_of Description: connects the base form of an acid to an acid. Also connects the different charge states of the base. Example: the different charge states of lactate (CHEBI:24996) conjugate base of lactic acid (CHEBI:28358)
--     * Slot: conjugate_acid_of Description: 
--     * Slot: bronsted_acid_base_role Description: 
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MolecularAnion" Description: "A polyatomic ion that is negative"
--     * Slot: conjugate_base_of Description: connects the base form of an acid to an acid. Also connects the different charge states of the base. Example: the different charge states of lactate (CHEBI:24996) conjugate base of lactic acid (CHEBI:28358)
--     * Slot: conjugate_acid_of Description: 
--     * Slot: bronsted_acid_base_role Description: 
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "NetUnchargedMolecule" Description: "A molecule that has no net charge"
--     * Slot: bronsted_acid_base_role Description: 
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Zwitterion" Description: "A molecule that has both a positive and negative charges but is net neutral"
--     * Slot: bronsted_acid_base_role Description: 
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "NeutralMolecule" Description: "A molecule that has no net charge and is not a zwitterion"
--     * Slot: bronsted_acid_base_role Description: 
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "Atom" Description: "A chemical entity consisting of exactly one atomic nucleus and the electron(s) orbiting it."
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ChemicalElement" Description: "generic form of an atom, with unspecified neutron or charge"
--     * Slot: in_periodic_table_group Description: which number in periodic table column
--     * Slot: in_periodic_table_block Description: block of periodic table unified by the orbitals their valence electrons or vacancies lie in
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: E.g. O, K, Ge
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "UnchargedAtom" Description: "An atom type that has no charge"
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Nuclide" Description: "an atomic species characterized by the specific constitution of its nucleus"
--     * Slot: energy_level Description: e.g. ground, stable
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Radionuclide" Description: "an atom that has excess nuclear energy, making it unstable"
--     * Slot: energy_level Description: e.g. ground, stable
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Isotope" Description: "A specific subtype of an atom with a specified neutron number"
--     * Slot: has_element Description: 
--     * Slot: neutron_number Description: number of neutrons in an atom
--     * Slot: isotope_of Description: relationship that holds between two isotopes, always holds if the isotopes have the same atomic number and a different neutron number.
--     * Slot: half_life Description: 
--     * Slot: decay_product Description: 
--     * Slot: decay_mode Description: 
--     * Slot: decay_energy Description: 
--     * Slot: mode_of_formation Description: 
--     * Slot: energy_level Description: e.g. ground, stable
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Isobar" Description: "Isobars are atoms (nuclides) of different chemical elements that have the same number of nucleons."
--     * Slot: has_element Description: 
--     * Slot: nucleon_number Description: number of nucleons in an atom. proton number plus neutron number.
--     * Slot: isobar_of Description: equal mass number (Z1 + N1 = Z2 + N2)
--     * Slot: half_life Description: 
--     * Slot: decay_product Description: 
--     * Slot: decay_mode Description: 
--     * Slot: decay_energy Description: 
--     * Slot: mode_of_formation Description: 
--     * Slot: energy_level Description: e.g. ground, stable
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "AtomIonicForm" Description: "an atom type in which only charge state is specified, designated by the element followed by charge"
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MonoatomicIon" Description: "An atom type that has a charge"
--     * Slot: has_element Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AtomAnion" Description: "A monoatomic ion that is negative"
--     * Slot: has_element Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AtomCation" Description: "A monoatomic ion that is positive, e.g Cu(2+)"
--     * Slot: has_element Description: 
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "PartiallySpecifiedAtom" Description: "An atom type that only has a subset of properties (has atomic number, charge, and neutron number) stated"
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "FullySpecifiedAtom" Description: "An atom type that has atomic number, charge, and neutron number stated (equivalently: protons + mass + charge)"
--     * Slot: elemental_charge Description: number of protons minus number of electrons
--     * Slot: neutron_number Description: number of neutrons in an atom
--     * Slot: atomic_number Description: number of protons in an atom
--     * Slot: symbol Description: short symbol for chemical entity, e.g. K, C-16
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: has_nuclear_parts_id Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "ChemicalInformation" Description: ""
--     * Slot: id Description: 
-- # Abstract Class: "PeriodicTablePlacement" Description: ""
--     * Slot: id Description: 
-- # Abstract Class: "InchiObject" Description: "A representation of an InChI string as an object, composed of distinct sublayers"
--     * Slot: id Description: 
-- # Class: "StandardInchiObject" Description: ""
--     * Slot: id Description: 
--     * Slot: inchi_version_string Description: The first part of the inchi_string, after 'InChI='
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: inchi_hydrogen_connections_sublayer Description: Describes how many hydrogen atoms are connected to each of the other atoms.
--     * Slot: inchi_charge_sublayer Description: 
--     * Slot: inchi_proton_sublayer Description: 
--     * Slot: inchi_stereochemical_double_bond_sublayer Description: 
--     * Slot: inchi_tetrahedral_stereochemical_sublayer Description: 
--     * Slot: inchi_stereochemical_type_sublayer Description: 
--     * Slot: inchi_isotopic_layer Description: 
-- # Abstract Class: "ChemicalRelationship" Description: "A reified relationship"
--     * Slot: id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ChemicalRole" Description: "A characteristic of a chemical entity that is realized under particular conditions"
--     * Slot: id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "Location" Description: "Abstract grouping for entities that represent abstract or concrete locations of chemical entities or their parts."
--     * Slot: id Description: 
-- # Class: "Stereocenter" Description: "a geometric point in a molecule in which the interchanging of two substituents creates a stereoisomer."
--     * Slot: id Description: 
-- # Class: "ChiralityCenter" Description: "a stereocenter consisting of an atom holding a set of ligands (atoms or groups of atoms) in a spatial arrangement which is not superimposable on its mirror image. "
--     * Slot: id Description: 
-- # Class: "AtomicBond" Description: "A connection between two atoms. Note this is the reified form of 'atomically connected to'. "
--     * Slot: id Description: 
--     * Slot: subject Description: 
--     * Slot: object Description: 
--     * Slot: bond_type Description: 
--     * Slot: bond_order Description: the number of electron pairs (bonds) between a pair of atoms
--     * Slot: bond_length Description: the average distance between nuclei of two bonded atoms in a molecule
--     * Slot: bond_energy Description: the measure of bond strength in a chemical bond.
--     * Slot: bond_length_in_angstroms Description: the average distance between nuclei of two bonded atoms in a molecule. It is a transferable property of a bond between atoms of fixed types, relatively independent of the rest of the molecule.
--     * Slot: bond_angle Description: 
--     * Slot: torsional_angle Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "SubatomicParticleOccurrence" Description: ""
--     * Slot: id Description: 
--     * Slot: occurrence_of Description: 
--     * Slot: Count Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "AtomOccurrence" Description: "An occurrence of an atom in the context of a particular molecule. For example, one of two occurrences of oxygen in nitrate"
--     * Slot: name Description: 
--     * Slot: occurrence_of Description: 
--     * Slot: valence Description: the number of electrons that an atom uses in bonding [https://doi.org/10.1021%2Fed083p791]
--     * Slot: oxidation_number Description: The charge remaining on an atom when all ligands are removed heterolytically in their closed form, with the electrons being transferred to the more electronegative partner; homonuclear bonds do not contribute to the oxidation number. [https://doi.org/10.1021%2Fed083p791]
--     * Slot: formal_charge Description: The charge remaining on an atom when all ligands are removed homolytically. [https://doi.org/10.1021%2Fed083p791]
--     * Slot: coordination_number Description: The number of atoms bonded to the atom of interest. [https://doi.org/10.1021%2Fed083p791]
--     * Slot: SmallMolecule_id Description: Autocreated FK slot
--     * Slot: Macromolecule_id Description: Autocreated FK slot
--     * Slot: Peptide_id Description: Autocreated FK slot
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: Glycan_id Description: Autocreated FK slot
--     * Slot: MonomolecularPolymer_id Description: Autocreated FK slot
--     * Slot: Copolymer_id Description: Autocreated FK slot
--     * Slot: Homopolymer_id Description: Autocreated FK slot
--     * Slot: Molecule_id Description: Autocreated FK slot
--     * Slot: NaturalProduct_id Description: Autocreated FK slot
--     * Slot: MolecularSpecies_id Description: Autocreated FK slot
--     * Slot: NonSpeciesMolecule_id Description: Autocreated FK slot
--     * Slot: MoleculeByChargeState_id Description: Autocreated FK slot
--     * Slot: PolyatomicIon_id Description: Autocreated FK slot
--     * Slot: MolecularCation_id Description: Autocreated FK slot
--     * Slot: MolecularAnion_id Description: Autocreated FK slot
--     * Slot: NetUnchargedMolecule_id Description: Autocreated FK slot
--     * Slot: Zwitterion_id Description: Autocreated FK slot
--     * Slot: NeutralMolecule_id Description: Autocreated FK slot
--     * Slot: Ester_id Description: Autocreated FK slot
--     * Slot: Stereoisomer_id Description: Autocreated FK slot
--     * Slot: Enantiomer_id Description: Autocreated FK slot
--     * Slot: Allotrope_id Description: Autocreated FK slot
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ChemicalSalt" Description: "a chemical compound consisting of an ionic assembly of cations and anions."
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Ester" Description: "An ester is a chemical compound derived from an acid (organic or inorganic) in which at least one –OH hydroxyl group is replaced by an –O– alkyl (alkoxy) group"
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Stereoisomer" Description: ""
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Enantiomer" Description: "one of two stereoisomers of a chiral molecule that are mirror images. Example: R-thalidomide"
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "RacemicMixture" Description: "a chemical compound that has equal amounts of left- and right-handed enantiomers of a chiral molecule. An example is Thalidomide"
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Allotrope" Description: "A molecule consisting of atoms of the same element"
--     * Slot: is_organic Description: An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen, phosphorus, nitrogen, sulfur) [SIO]
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: IUPAC_name Description: 
--     * Slot: is_radical Description: 
--     * Slot: inchi_string Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
--     * Slot: smiles_string Description: A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol.
--     * Slot: empirical_formula Description: A chemical formula where numbers denote relative proportion of atoms. E.g. CH2O for glucose
--     * Slot: molecular_mass Description: The sum of the relative atomic masses of the constituent atoms of a molecule.
--     * Slot: water_solubility Description: The maximum amount of a substance that can dissolve in water at 25°C, expressed in grams per liter (g/L).
--     * Slot: pka_temperature Description: Temperature in Celsius at which pKa was measured. Default is 25°C if not specified.
--     * Slot: pka_ionic_strength Description: Ionic strength of solution in mol/L at which pKa was measured. Default is 0.0 M if not specified.
--     * Slot: pka_solvent Description: Solvent system for pKa measurement. Default is water (H₂O) if not specified.
--     * Slot: pka_pressure Description: Pressure in atmospheres at which pKa was measured. Default is 1 atm if not specified.
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
--     * Slot: has_chemical_role_id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "PolymerRepeatUnit" Description: "An abstract part of a polymer that is all instances of a repeated monomer of a single type"
--     * Slot: id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "Reaction" Description: "Reaction"
--     * Slot: has_rinchi_representation Description: Proposed Reactions InChI
--     * Slot: has_reaction_smiles_representation Description: 
--     * Slot: reaction_rate_coefficient Description: a proportionality constant that relates the reaction rate to reactant concentrations.
--     * Slot: reaction_rate Description: the overall speed of a reaction, typically measured in concentration change per unit time
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
-- # Class: "IsomeraseReaction" Description: "A reaction that converts a molecule from one isomer to another."
--     * Slot: has_rinchi_representation Description: Proposed Reactions InChI
--     * Slot: has_reaction_smiles_representation Description: 
--     * Slot: reaction_rate_coefficient Description: a proportionality constant that relates the reaction rate to reactant concentrations.
--     * Slot: reaction_rate Description: the overall speed of a reaction, typically measured in concentration change per unit time
--     * Slot: id Description: 
--     * Slot: name Description: name of chemical entity. E.g. nickel, carbon-16
--     * Slot: type Description: 
-- # Class: "ReactionParticipant" Description: "Instances of this link a reaction to a chemical entity participant"
--     * Slot: id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ProportionalPart" Description: "A part of a complex mixture that is of uniform composition"
--     * Slot: id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "ChemicalSimilarity" Description: "A relationship between two or more chemical entities where there is some degree of similarity between these entities on their similarity"
--     * Slot: id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "MoleculePairwiseSimilarity" Description: ""
--     * Slot: id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Class: "TanimotoSimilarity" Description: ""
--     * Slot: id Description: 
--     * Slot: owl_subclass_of_id Description: Holds between C and P if C owl:subClassOf P. Note that in this model, most classes are metaclasses (see 'owl class'), where these metaclasses may represent *groupings* or specific countable elements or species. We provide two different sub-properties of subclass of for two cases: (1) subtype_of, which connects grouping classes (e.g. alkane is_a hydrocarbon; alpha-amino-acid is_a amino-acid), (2) classified_by, which connects a specific element to a grouping class (e.g. methane is_a hydrocarbon; iron is_a metal; serine is_a amino-acid)
-- # Abstract Class: "SpecificityMixin" Description: ""
--     * Slot: id Description: 
-- # Class: "EntityWithAtomsEnumerated" Description: "A mixin for an entity that consists of one or more atoms where the atoms and the number of occurrences is counted (corresponding to the chemical layer in InChI)"
--     * Slot: id Description: 
--     * Slot: inchi_chemical_sublayer Description: The part of an InChI string that represents the chemical formula, occurring after the version string. E.g. C6H12O6 for glucose
-- # Class: "EntityWithConnectivitySpecificied" Description: "A mixin for an entity that consists of two or more atom occurrences where the connectivity is specified (corresponding to the /c layer in InChI)"
--     * Slot: id Description: 
--     * Slot: inchi_atom_connections_sublayer Description: The atoms in the chemical formula (except for hydrogens) are numbered in sequence; this sublayer describes which atoms are connected by bonds to which other ones.
--     * Slot: inchi_hydrogen_connections_sublayer Description: Describes how many hydrogen atoms are connected to each of the other atoms.
-- # Class: "EntityWithChargeSpecified" Description: "A mixin for an entity where the charge is explicitly specified (corresponding to the /q layer in InChI)"
--     * Slot: id Description: 
--     * Slot: inchi_charge_sublayer Description: 
-- # Class: "EntityWithStereochemistrySpecified" Description: "A mixin for an entity where the stereochemistry is explicitly specified (corresponding to the /t, m/, and /s layers in InChI)"
--     * Slot: id Description: 
--     * Slot: inchi_stereochemical_double_bond_sublayer Description: 
--     * Slot: inchi_tetrahedral_stereochemical_sublayer Description: 
--     * Slot: inchi_stereochemical_type_sublayer Description: 
-- # Class: "EntityWithIsotopeSpecified" Description: "A mixin for an entity where the charge is explicitly specified (corresponding to the /q layer in InChI)"
--     * Slot: id Description: 
--     * Slot: inchi_isotopic_layer Description: 
-- # Class: "ChemicalEntity_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "ChemicalEntity_pka_ionization_constant" Description: ""
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "GroupingClass_subtype_of" Description: ""
--     * Slot: GroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "PhysicochemicalEntityGroupingClass_subtype_of" Description: ""
--     * Slot: PhysicochemicalEntityGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "ChemicalGroupingClass_subtype_of" Description: ""
--     * Slot: ChemicalGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "ReactionGroupingClass_subtype_of" Description: ""
--     * Slot: ReactionGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "MaterialGroupingClass_subtype_of" Description: ""
--     * Slot: MaterialGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "ChemicalGroupingByCharge_subtype_of" Description: ""
--     * Slot: ChemicalGroupingByCharge_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "MoleculeGroupingClass_subtype_of" Description: ""
--     * Slot: MoleculeGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "MolecularComponentGroupingClass_subtype_of" Description: ""
--     * Slot: MolecularComponentGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "MolecularDerivativeGroupingClass_subtype_of" Description: ""
--     * Slot: MolecularDerivativeGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "MoleculeGroupingClassDefinedByComponents_subtype_of" Description: ""
--     * Slot: MoleculeGroupingClassDefinedByComponents_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "MoleculeGroupingClassDefinedByAdditionOfAGroup_subtype_of" Description: ""
--     * Slot: MoleculeGroupingClassDefinedByAdditionOfAGroup_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "ChemicalSaltGroupingClass_subtype_of" Description: ""
--     * Slot: ChemicalSaltGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "ChemicalSaltByCation_subtype_of" Description: ""
--     * Slot: ChemicalSaltByCation_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "ChemicalSaltByAnion_subtype_of" Description: ""
--     * Slot: ChemicalSaltByAnion_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "GeneralizedMolecularStructureClass_subtype_of" Description: ""
--     * Slot: GeneralizedMolecularStructureClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "MonomericPolymericGroupingClass_subtype_of" Description: ""
--     * Slot: MonomericPolymericGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "GroupingClassForAcidsOrBases_subtype_of" Description: ""
--     * Slot: GroupingClassForAcidsOrBases_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "AcidAnionGroupingClass_subtype_of" Description: ""
--     * Slot: AcidAnionGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "GeneralAcidBaseGroupingClass_subtype_of" Description: ""
--     * Slot: GeneralAcidBaseGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "AcidBaseConflationClass_subtype_of" Description: ""
--     * Slot: AcidBaseConflationClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: grouping classes can be arranged in hierarchies arbitrarily deep. Note that subtype_of should only connect two grouping classes
-- # Class: "AtomGroupingClass_subtype_of" Description: ""
--     * Slot: AtomGroupingClass_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "AtomGroupingByPeriodicTablePlacement_subtype_of" Description: ""
--     * Slot: AtomGroupingByPeriodicTablePlacement_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "AtomGroupingByPeriodicTableGroup_subtype_of" Description: ""
--     * Slot: AtomGroupingByPeriodicTableGroup_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "AtomGroupingByPeriodicTableBlock_subtype_of" Description: ""
--     * Slot: AtomGroupingByPeriodicTableBlock_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "AtomGroupingByProperty_subtype_of" Description: ""
--     * Slot: AtomGroupingByProperty_id Description: Autocreated FK slot
--     * Slot: subtype_of_id Description: A subtype_of relationship holds between C and P if C is a more specialized form of P. Here C and P denotes instances of OWL classes, where C and P both function as grouping class
-- # Class: "PolyatomicEntity_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: PolyatomicEntity_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "PolyatomicEntity_pka_ionization_constant" Description: ""
--     * Slot: PolyatomicEntity_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "SmallMolecule_has_bonds" Description: ""
--     * Slot: SmallMolecule_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "SmallMolecule_has_submolecules" Description: ""
--     * Slot: SmallMolecule_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "SmallMolecule_has_atoms" Description: ""
--     * Slot: SmallMolecule_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "SmallMolecule_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: SmallMolecule_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "SmallMolecule_pka_ionization_constant" Description: ""
--     * Slot: SmallMolecule_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Macromolecule_has_bonds" Description: ""
--     * Slot: Macromolecule_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Macromolecule_has_submolecules" Description: ""
--     * Slot: Macromolecule_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Macromolecule_has_atoms" Description: ""
--     * Slot: Macromolecule_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Macromolecule_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Macromolecule_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Macromolecule_pka_ionization_constant" Description: ""
--     * Slot: Macromolecule_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "MolecularComplex_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: MolecularComplex_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "MolecularComplex_pka_ionization_constant" Description: ""
--     * Slot: MolecularComplex_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Peptide_has_bonds" Description: ""
--     * Slot: Peptide_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Peptide_has_submolecules" Description: ""
--     * Slot: Peptide_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Peptide_has_atoms" Description: ""
--     * Slot: Peptide_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Peptide_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Peptide_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Peptide_pka_ionization_constant" Description: ""
--     * Slot: Peptide_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Protein_has_bonds" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Protein_has_submolecules" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Protein_has_atoms" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Protein_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Protein_pka_ionization_constant" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Glycan_has_bonds" Description: ""
--     * Slot: Glycan_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Glycan_has_submolecules" Description: ""
--     * Slot: Glycan_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Glycan_has_atoms" Description: ""
--     * Slot: Glycan_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Glycan_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Glycan_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Glycan_pka_ionization_constant" Description: ""
--     * Slot: Glycan_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "MonomolecularPolymer_has_bonds" Description: ""
--     * Slot: MonomolecularPolymer_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "MonomolecularPolymer_has_submolecules" Description: ""
--     * Slot: MonomolecularPolymer_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "MonomolecularPolymer_has_atoms" Description: ""
--     * Slot: MonomolecularPolymer_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "MonomolecularPolymer_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: MonomolecularPolymer_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "MonomolecularPolymer_pka_ionization_constant" Description: ""
--     * Slot: MonomolecularPolymer_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "SupramolecularPolymer_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: SupramolecularPolymer_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "SupramolecularPolymer_pka_ionization_constant" Description: ""
--     * Slot: SupramolecularPolymer_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Copolymer_polymer_of" Description: ""
--     * Slot: Copolymer_id Description: Autocreated FK slot
--     * Slot: polymer_of_id Description: 
-- # Class: "Copolymer_has_bonds" Description: ""
--     * Slot: Copolymer_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Copolymer_has_submolecules" Description: ""
--     * Slot: Copolymer_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Copolymer_has_atoms" Description: ""
--     * Slot: Copolymer_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Copolymer_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Copolymer_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Copolymer_pka_ionization_constant" Description: ""
--     * Slot: Copolymer_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Homopolymer_has_bonds" Description: ""
--     * Slot: Homopolymer_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Homopolymer_has_submolecules" Description: ""
--     * Slot: Homopolymer_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Homopolymer_has_atoms" Description: ""
--     * Slot: Homopolymer_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Homopolymer_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Homopolymer_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Homopolymer_pka_ionization_constant" Description: ""
--     * Slot: Homopolymer_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "MolecularComponent_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: MolecularComponent_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "MolecularComponent_pka_ionization_constant" Description: ""
--     * Slot: MolecularComponent_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "PolymerPart_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: PolymerPart_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "PolymerPart_pka_ionization_constant" Description: ""
--     * Slot: PolymerPart_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Monomer_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Monomer_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Monomer_pka_ionization_constant" Description: ""
--     * Slot: Monomer_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "MolecularSubsequence_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: MolecularSubsequence_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "MolecularSubsequence_pka_ionization_constant" Description: ""
--     * Slot: MolecularSubsequence_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "ChemicalGroup_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: ChemicalGroup_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "ChemicalGroup_pka_ionization_constant" Description: ""
--     * Slot: ChemicalGroup_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "ChemicalMixture_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: ChemicalMixture_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "ChemicalMixture_pka_ionization_constant" Description: ""
--     * Slot: ChemicalMixture_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "PreciseChemicalMixture_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: PreciseChemicalMixture_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "PreciseChemicalMixture_pka_ionization_constant" Description: ""
--     * Slot: PreciseChemicalMixture_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "ImpreciseChemicalMixture_has_proportional_parts" Description: ""
--     * Slot: ImpreciseChemicalMixture_id Description: Autocreated FK slot
--     * Slot: has_proportional_parts_id Description: Relationship between a complex mixture and its parts
-- # Class: "ImpreciseChemicalMixture_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: ImpreciseChemicalMixture_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "ImpreciseChemicalMixture_pka_ionization_constant" Description: ""
--     * Slot: ImpreciseChemicalMixture_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Molecule_has_bonds" Description: ""
--     * Slot: Molecule_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Molecule_has_submolecules" Description: ""
--     * Slot: Molecule_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Molecule_has_atoms" Description: ""
--     * Slot: Molecule_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Molecule_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Molecule_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Molecule_pka_ionization_constant" Description: ""
--     * Slot: Molecule_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "NaturalProduct_derived_from_organisms" Description: ""
--     * Slot: NaturalProduct_id Description: Autocreated FK slot
--     * Slot: derived_from_organisms Description: 
-- # Class: "NaturalProduct_has_bonds" Description: ""
--     * Slot: NaturalProduct_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "NaturalProduct_has_submolecules" Description: ""
--     * Slot: NaturalProduct_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "NaturalProduct_has_atoms" Description: ""
--     * Slot: NaturalProduct_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "NaturalProduct_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: NaturalProduct_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "NaturalProduct_pka_ionization_constant" Description: ""
--     * Slot: NaturalProduct_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Moiety_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Moiety_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Moiety_pka_ionization_constant" Description: ""
--     * Slot: Moiety_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "SequenceInterval_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: SequenceInterval_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "SequenceInterval_pka_ionization_constant" Description: ""
--     * Slot: SequenceInterval_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "AminoAcidSequenceInterval_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: AminoAcidSequenceInterval_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "AminoAcidSequenceInterval_pka_ionization_constant" Description: ""
--     * Slot: AminoAcidSequenceInterval_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "NucleotideSequenceInterval_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: NucleotideSequenceInterval_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "NucleotideSequenceInterval_pka_ionization_constant" Description: ""
--     * Slot: NucleotideSequenceInterval_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "DNASequenceInterval_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: DNASequenceInterval_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "DNASequenceInterval_pka_ionization_constant" Description: ""
--     * Slot: DNASequenceInterval_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "RNASequenceInterval_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: RNASequenceInterval_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "RNASequenceInterval_pka_ionization_constant" Description: ""
--     * Slot: RNASequenceInterval_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "FunctionalGroup_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: FunctionalGroup_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "FunctionalGroup_pka_ionization_constant" Description: ""
--     * Slot: FunctionalGroup_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "MolecularSpecies_has_bonds" Description: ""
--     * Slot: MolecularSpecies_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "MolecularSpecies_has_submolecules" Description: ""
--     * Slot: MolecularSpecies_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "MolecularSpecies_has_atoms" Description: ""
--     * Slot: MolecularSpecies_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "MolecularSpecies_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: MolecularSpecies_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "MolecularSpecies_pka_ionization_constant" Description: ""
--     * Slot: MolecularSpecies_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "NonSpeciesMolecule_has_bonds" Description: ""
--     * Slot: NonSpeciesMolecule_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "NonSpeciesMolecule_has_submolecules" Description: ""
--     * Slot: NonSpeciesMolecule_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "NonSpeciesMolecule_has_atoms" Description: ""
--     * Slot: NonSpeciesMolecule_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "NonSpeciesMolecule_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: NonSpeciesMolecule_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "NonSpeciesMolecule_pka_ionization_constant" Description: ""
--     * Slot: NonSpeciesMolecule_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "MoleculeByChargeState_has_bonds" Description: ""
--     * Slot: MoleculeByChargeState_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "MoleculeByChargeState_has_submolecules" Description: ""
--     * Slot: MoleculeByChargeState_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "MoleculeByChargeState_has_atoms" Description: ""
--     * Slot: MoleculeByChargeState_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "MoleculeByChargeState_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: MoleculeByChargeState_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "MoleculeByChargeState_pka_ionization_constant" Description: ""
--     * Slot: MoleculeByChargeState_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "PolyatomicIon_has_bonds" Description: ""
--     * Slot: PolyatomicIon_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "PolyatomicIon_has_submolecules" Description: ""
--     * Slot: PolyatomicIon_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "PolyatomicIon_has_atoms" Description: ""
--     * Slot: PolyatomicIon_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "PolyatomicIon_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: PolyatomicIon_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "PolyatomicIon_pka_ionization_constant" Description: ""
--     * Slot: PolyatomicIon_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "MolecularCation_has_bonds" Description: ""
--     * Slot: MolecularCation_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "MolecularCation_has_submolecules" Description: ""
--     * Slot: MolecularCation_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "MolecularCation_has_atoms" Description: ""
--     * Slot: MolecularCation_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "MolecularCation_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: MolecularCation_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "MolecularCation_pka_ionization_constant" Description: ""
--     * Slot: MolecularCation_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "MolecularAnion_has_bonds" Description: ""
--     * Slot: MolecularAnion_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "MolecularAnion_has_submolecules" Description: ""
--     * Slot: MolecularAnion_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "MolecularAnion_has_atoms" Description: ""
--     * Slot: MolecularAnion_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "MolecularAnion_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: MolecularAnion_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "MolecularAnion_pka_ionization_constant" Description: ""
--     * Slot: MolecularAnion_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "NetUnchargedMolecule_has_bonds" Description: ""
--     * Slot: NetUnchargedMolecule_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "NetUnchargedMolecule_has_submolecules" Description: ""
--     * Slot: NetUnchargedMolecule_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "NetUnchargedMolecule_has_atoms" Description: ""
--     * Slot: NetUnchargedMolecule_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "NetUnchargedMolecule_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: NetUnchargedMolecule_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "NetUnchargedMolecule_pka_ionization_constant" Description: ""
--     * Slot: NetUnchargedMolecule_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Zwitterion_has_bonds" Description: ""
--     * Slot: Zwitterion_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Zwitterion_has_submolecules" Description: ""
--     * Slot: Zwitterion_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Zwitterion_has_atoms" Description: ""
--     * Slot: Zwitterion_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Zwitterion_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Zwitterion_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Zwitterion_pka_ionization_constant" Description: ""
--     * Slot: Zwitterion_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "NeutralMolecule_has_bonds" Description: ""
--     * Slot: NeutralMolecule_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "NeutralMolecule_has_submolecules" Description: ""
--     * Slot: NeutralMolecule_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "NeutralMolecule_has_atoms" Description: ""
--     * Slot: NeutralMolecule_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "NeutralMolecule_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: NeutralMolecule_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "NeutralMolecule_pka_ionization_constant" Description: ""
--     * Slot: NeutralMolecule_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Atom_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Atom_pka_ionization_constant" Description: ""
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "ChemicalElement_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: ChemicalElement_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "ChemicalElement_pka_ionization_constant" Description: ""
--     * Slot: ChemicalElement_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "UnchargedAtom_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: UnchargedAtom_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "UnchargedAtom_pka_ionization_constant" Description: ""
--     * Slot: UnchargedAtom_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Nuclide_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Nuclide_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Nuclide_pka_ionization_constant" Description: ""
--     * Slot: Nuclide_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Radionuclide_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Radionuclide_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Radionuclide_pka_ionization_constant" Description: ""
--     * Slot: Radionuclide_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Isotope_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Isotope_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Isotope_pka_ionization_constant" Description: ""
--     * Slot: Isotope_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Isobar_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Isobar_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Isobar_pka_ionization_constant" Description: ""
--     * Slot: Isobar_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "AtomIonicForm_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: AtomIonicForm_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "AtomIonicForm_pka_ionization_constant" Description: ""
--     * Slot: AtomIonicForm_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "MonoatomicIon_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: MonoatomicIon_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "MonoatomicIon_pka_ionization_constant" Description: ""
--     * Slot: MonoatomicIon_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "AtomAnion_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: AtomAnion_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "AtomAnion_pka_ionization_constant" Description: ""
--     * Slot: AtomAnion_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "AtomCation_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: AtomCation_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "AtomCation_pka_ionization_constant" Description: ""
--     * Slot: AtomCation_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "PartiallySpecifiedAtom_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: PartiallySpecifiedAtom_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "PartiallySpecifiedAtom_pka_ionization_constant" Description: ""
--     * Slot: PartiallySpecifiedAtom_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "FullySpecifiedAtom_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: FullySpecifiedAtom_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "FullySpecifiedAtom_pka_ionization_constant" Description: ""
--     * Slot: FullySpecifiedAtom_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "ChemicalSalt_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: ChemicalSalt_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "ChemicalSalt_pka_ionization_constant" Description: ""
--     * Slot: ChemicalSalt_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Ester_has_bonds" Description: ""
--     * Slot: Ester_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Ester_has_submolecules" Description: ""
--     * Slot: Ester_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Ester_has_atoms" Description: ""
--     * Slot: Ester_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Ester_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Ester_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Ester_pka_ionization_constant" Description: ""
--     * Slot: Ester_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Stereoisomer_has_bonds" Description: ""
--     * Slot: Stereoisomer_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Stereoisomer_has_submolecules" Description: ""
--     * Slot: Stereoisomer_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Stereoisomer_has_atoms" Description: ""
--     * Slot: Stereoisomer_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Stereoisomer_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Stereoisomer_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Stereoisomer_pka_ionization_constant" Description: ""
--     * Slot: Stereoisomer_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Enantiomer_has_bonds" Description: ""
--     * Slot: Enantiomer_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Enantiomer_has_submolecules" Description: ""
--     * Slot: Enantiomer_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Enantiomer_has_atoms" Description: ""
--     * Slot: Enantiomer_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Enantiomer_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Enantiomer_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Enantiomer_pka_ionization_constant" Description: ""
--     * Slot: Enantiomer_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "RacemicMixture_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: RacemicMixture_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "RacemicMixture_pka_ionization_constant" Description: ""
--     * Slot: RacemicMixture_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.
-- # Class: "Allotrope_has_bonds" Description: ""
--     * Slot: Allotrope_id Description: Autocreated FK slot
--     * Slot: has_bonds_id Description: The set of all bonds connecting atoms in a molecule
-- # Class: "Allotrope_has_submolecules" Description: ""
--     * Slot: Allotrope_id Description: Autocreated FK slot
--     * Slot: has_submolecules_id Description: Relation between a molecule and the molecules it is made from.
-- # Class: "Allotrope_has_atoms" Description: ""
--     * Slot: Allotrope_id Description: Autocreated FK slot
--     * Slot: has_atoms_id Description: Relation between a molecule and the atoms it contains. Note that this is a shortcut relation: for granular representations go via atom occurrences
-- # Class: "Allotrope_has_major_microspecies_at_pH7_3" Description: ""
--     * Slot: Allotrope_id Description: Autocreated FK slot
--     * Slot: has_major_microspecies_at_pH7_3_id Description: Links different variants of the same chemical in different protonation states, where the target of this link is the (predicited) to be most common protonation state for this chemical at a pH of 7.3. This link may point to it's source. Connects an acid to the form that is stable at physiological pH (7.3). E.g. citric acid has physiological base citrate(3-)
-- # Class: "Allotrope_pka_ionization_constant" Description: ""
--     * Slot: Allotrope_id Description: Autocreated FK slot
--     * Slot: pka_ionization_constant Description: The negative logarithm of the acid dissociation constant (Ka) for ionizable groups in a molecule. Multiple pKa values may exist for molecules with multiple ionizable groups.

CREATE TABLE "Collection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PhysicochemicalEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SubatomicParticle" (
	subatomic_particle_type VARCHAR(20), 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "OwlClass" (
	id INTEGER NOT NULL, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalEntityOrGrouping" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Connectivity" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "FullyCovalentlyBonded" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "WeaklyBonded" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "State" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChargeState" (
	id INTEGER NOT NULL, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "AnionState" (
	id INTEGER NOT NULL, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "CationState" (
	id INTEGER NOT NULL, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "Uncharged" (
	id INTEGER NOT NULL, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "Charged" (
	id INTEGER NOT NULL, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalInformation" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PeriodicTablePlacement" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "InchiObject" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "StandardInchiObject" (
	id INTEGER NOT NULL, 
	inchi_version_string TEXT NOT NULL, 
	inchi_chemical_sublayer TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	inchi_hydrogen_connections_sublayer TEXT, 
	inchi_charge_sublayer TEXT, 
	inchi_proton_sublayer TEXT, 
	inchi_stereochemical_double_bond_sublayer TEXT, 
	inchi_tetrahedral_stereochemical_sublayer TEXT, 
	inchi_stereochemical_type_sublayer TEXT, 
	inchi_isotopic_layer TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Location" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Stereocenter" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChiralityCenter" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Reaction" (
	has_rinchi_representation TEXT, 
	has_reaction_smiles_representation TEXT, 
	reaction_rate_coefficient FLOAT, 
	reaction_rate FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "IsomeraseReaction" (
	has_rinchi_representation TEXT, 
	has_reaction_smiles_representation TEXT, 
	reaction_rate_coefficient FLOAT, 
	reaction_rate FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SpecificityMixin" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "EntityWithAtomsEnumerated" (
	id INTEGER NOT NULL, 
	inchi_chemical_sublayer TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EntityWithConnectivitySpecificied" (
	id INTEGER NOT NULL, 
	inchi_atom_connections_sublayer TEXT, 
	inchi_hydrogen_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EntityWithChargeSpecified" (
	id INTEGER NOT NULL, 
	inchi_charge_sublayer TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EntityWithStereochemistrySpecified" (
	id INTEGER NOT NULL, 
	inchi_stereochemical_double_bond_sublayer TEXT, 
	inchi_tetrahedral_stereochemical_sublayer TEXT, 
	inchi_stereochemical_type_sublayer TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EntityWithIsotopeSpecified" (
	id INTEGER NOT NULL, 
	inchi_isotopic_layer TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DomainEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"Collection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Collection_id") REFERENCES "Collection" (id)
);
CREATE TABLE "GroupingClass" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "PhysicochemicalEntityGroupingClass" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalGroupingClass" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ReactionGroupingClass" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MaterialGroupingClass" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalGroupingByCharge" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MoleculeGroupingClass" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MolecularComponentGroupingClass" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MoleculeGroupingClassDefinedByComponents" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	has_part_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ChemicalEntityOrGrouping" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MoleculeGroupingClassDefinedByAdditionOfAGroup" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalSaltGroupingClass" (
	has_anionic_component TEXT, 
	has_cationic_component TEXT, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalSaltByCation" (
	has_cationic_component TEXT, 
	has_anionic_component TEXT, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalSaltByAnion" (
	has_anionic_component TEXT, 
	has_cationic_component TEXT, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "GeneralizedMolecularStructureClass" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AtomGroupingClass" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AtomGroupingByPeriodicTablePlacement" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AtomGroupingByPeriodicTableGroup" (
	in_periodic_table_group INTEGER, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AtomGroupingByPeriodicTableBlock" (
	in_periodic_table_block VARCHAR(7), 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AtomGroupingByProperty" (
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalRelationship" (
	id INTEGER NOT NULL, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalRole" (
	id INTEGER NOT NULL, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "SubatomicParticleOccurrence" (
	id INTEGER NOT NULL, 
	occurrence_of TEXT NOT NULL, 
	"Count" INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(occurrence_of) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "PolymerRepeatUnit" (
	id INTEGER NOT NULL, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ReactionParticipant" (
	id INTEGER NOT NULL, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ProportionalPart" (
	id INTEGER NOT NULL, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalSimilarity" (
	id INTEGER NOT NULL, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MoleculePairwiseSimilarity" (
	id INTEGER NOT NULL, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "TanimotoSimilarity" (
	id INTEGER NOT NULL, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalEntity" (
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (smiles_string), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MolecularDerivativeGroupingClass" (
	derivative_of TEXT, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(derivative_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "GroupingClassForAcidsOrBases" (
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AcidAnionGroupingClass" (
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "GeneralAcidBaseGroupingClass" (
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AcidBaseConflationClass" (
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "PolyatomicEntity" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "SmallMolecule" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Macromolecule" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MolecularComplex" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Peptide" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Protein" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Glycan" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MolecularComponent" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "PolymerPart" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Monomer" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MolecularSubsequence" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalGroup" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalMixture" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "PreciseChemicalMixture" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ImpreciseChemicalMixture" (
	has_mixfile_location TEXT, 
	has_minchi_representation TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Molecule" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "NaturalProduct" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Moiety" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "SequenceInterval" (
	has_sequence_representation TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AminoAcidSequenceInterval" (
	has_sequence_representation TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "NucleotideSequenceInterval" (
	has_sequence_representation TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "DNASequenceInterval" (
	has_sequence_representation TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "RNASequenceInterval" (
	has_sequence_representation TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "FunctionalGroup" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MolecularSpecies" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "NonSpeciesMolecule" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MoleculeByChargeState" (
	bronsted_acid_base_role VARCHAR(4), 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "PolyatomicIon" (
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	bronsted_acid_base_role VARCHAR(4), 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	elemental_charge INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MolecularCation" (
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	bronsted_acid_base_role VARCHAR(4), 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	elemental_charge INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MolecularAnion" (
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	bronsted_acid_base_role VARCHAR(4), 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	elemental_charge INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "NetUnchargedMolecule" (
	bronsted_acid_base_role VARCHAR(4), 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	elemental_charge INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Zwitterion" (
	bronsted_acid_base_role VARCHAR(4), 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	elemental_charge INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "NeutralMolecule" (
	bronsted_acid_base_role VARCHAR(4), 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	elemental_charge INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Atom" (
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalElement" (
	in_periodic_table_group INTEGER, 
	in_periodic_table_block VARCHAR(7), 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (atomic_number), 
	UNIQUE (atomic_number), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "UnchargedAtom" (
	elemental_charge INTEGER, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Nuclide" (
	energy_level TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Radionuclide" (
	energy_level TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AtomIonicForm" (
	elemental_charge INTEGER, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "PartiallySpecifiedAtom" (
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "FullySpecifiedAtom" (
	elemental_charge INTEGER, 
	neutron_number INTEGER, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalSalt" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Ester" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Stereoisomer" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Enantiomer" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "RacemicMixture" (
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Allotrope" (
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "GroupingClass_subtype_of" (
	"GroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("GroupingClass_id", subtype_of_id), 
	FOREIGN KEY("GroupingClass_id") REFERENCES "GroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "GroupingClass" (id)
);
CREATE TABLE "PhysicochemicalEntityGroupingClass_subtype_of" (
	"PhysicochemicalEntityGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("PhysicochemicalEntityGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("PhysicochemicalEntityGroupingClass_id") REFERENCES "PhysicochemicalEntityGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "PhysicochemicalEntityGroupingClass" (id)
);
CREATE TABLE "ChemicalGroupingClass_subtype_of" (
	"ChemicalGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("ChemicalGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("ChemicalGroupingClass_id") REFERENCES "ChemicalGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "ChemicalGroupingClass" (id)
);
CREATE TABLE "ReactionGroupingClass_subtype_of" (
	"ReactionGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("ReactionGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("ReactionGroupingClass_id") REFERENCES "ReactionGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "ReactionGroupingClass" (id)
);
CREATE TABLE "MaterialGroupingClass_subtype_of" (
	"MaterialGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("MaterialGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("MaterialGroupingClass_id") REFERENCES "MaterialGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MaterialGroupingClass" (id)
);
CREATE TABLE "ChemicalGroupingByCharge_subtype_of" (
	"ChemicalGroupingByCharge_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("ChemicalGroupingByCharge_id", subtype_of_id), 
	FOREIGN KEY("ChemicalGroupingByCharge_id") REFERENCES "ChemicalGroupingByCharge" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "MoleculeGroupingClass_subtype_of" (
	"MoleculeGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("MoleculeGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("MoleculeGroupingClass_id") REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "MolecularComponentGroupingClass_subtype_of" (
	"MolecularComponentGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("MolecularComponentGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("MolecularComponentGroupingClass_id") REFERENCES "MolecularComponentGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MolecularComponentGroupingClass" (id)
);
CREATE TABLE "MoleculeGroupingClassDefinedByComponents_subtype_of" (
	"MoleculeGroupingClassDefinedByComponents_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("MoleculeGroupingClassDefinedByComponents_id", subtype_of_id), 
	FOREIGN KEY("MoleculeGroupingClassDefinedByComponents_id") REFERENCES "MoleculeGroupingClassDefinedByComponents" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "MoleculeGroupingClassDefinedByAdditionOfAGroup_subtype_of" (
	"MoleculeGroupingClassDefinedByAdditionOfAGroup_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("MoleculeGroupingClassDefinedByAdditionOfAGroup_id", subtype_of_id), 
	FOREIGN KEY("MoleculeGroupingClassDefinedByAdditionOfAGroup_id") REFERENCES "MoleculeGroupingClassDefinedByAdditionOfAGroup" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "ChemicalSaltGroupingClass_subtype_of" (
	"ChemicalSaltGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("ChemicalSaltGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("ChemicalSaltGroupingClass_id") REFERENCES "ChemicalSaltGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "ChemicalSaltByCation_subtype_of" (
	"ChemicalSaltByCation_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("ChemicalSaltByCation_id", subtype_of_id), 
	FOREIGN KEY("ChemicalSaltByCation_id") REFERENCES "ChemicalSaltByCation" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "ChemicalSaltByAnion_subtype_of" (
	"ChemicalSaltByAnion_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("ChemicalSaltByAnion_id", subtype_of_id), 
	FOREIGN KEY("ChemicalSaltByAnion_id") REFERENCES "ChemicalSaltByAnion" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "GeneralizedMolecularStructureClass_subtype_of" (
	"GeneralizedMolecularStructureClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("GeneralizedMolecularStructureClass_id", subtype_of_id), 
	FOREIGN KEY("GeneralizedMolecularStructureClass_id") REFERENCES "GeneralizedMolecularStructureClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "AtomGroupingClass_subtype_of" (
	"AtomGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("AtomGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("AtomGroupingClass_id") REFERENCES "AtomGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "AtomGroupingByPeriodicTablePlacement_subtype_of" (
	"AtomGroupingByPeriodicTablePlacement_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("AtomGroupingByPeriodicTablePlacement_id", subtype_of_id), 
	FOREIGN KEY("AtomGroupingByPeriodicTablePlacement_id") REFERENCES "AtomGroupingByPeriodicTablePlacement" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "AtomGroupingByPeriodicTableGroup_subtype_of" (
	"AtomGroupingByPeriodicTableGroup_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("AtomGroupingByPeriodicTableGroup_id", subtype_of_id), 
	FOREIGN KEY("AtomGroupingByPeriodicTableGroup_id") REFERENCES "AtomGroupingByPeriodicTableGroup" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "AtomGroupingByPeriodicTableBlock_subtype_of" (
	"AtomGroupingByPeriodicTableBlock_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("AtomGroupingByPeriodicTableBlock_id", subtype_of_id), 
	FOREIGN KEY("AtomGroupingByPeriodicTableBlock_id") REFERENCES "AtomGroupingByPeriodicTableBlock" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "AtomGroupingByProperty_subtype_of" (
	"AtomGroupingByProperty_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("AtomGroupingByProperty_id", subtype_of_id), 
	FOREIGN KEY("AtomGroupingByProperty_id") REFERENCES "AtomGroupingByProperty" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "MonomericPolymericGroupingClass" (
	has_repeat_unit TEXT, 
	id TEXT NOT NULL, 
	smarts_string TEXT, 
	markush_string TEXT, 
	name TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_repeat_unit) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Material" (
	has_repeat_unit TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_repeat_unit) REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Nanomaterial" (
	has_repeat_unit TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_repeat_unit) REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Mineral" (
	has_repeat_unit TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_repeat_unit) REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MonomolecularPolymer" (
	polymer_of TEXT, 
	has_repeat_unit TEXT, 
	is_branched BOOLEAN, 
	polymer_architecture_type TEXT, 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polymer_of) REFERENCES "Macromolecule" (id), 
	FOREIGN KEY(has_repeat_unit) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "SupramolecularPolymer" (
	polymer_of TEXT, 
	has_repeat_unit TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polymer_of) REFERENCES "Macromolecule" (id), 
	FOREIGN KEY(has_repeat_unit) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Copolymer" (
	has_repeat_unit TEXT, 
	is_branched BOOLEAN, 
	polymer_architecture_type TEXT, 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_repeat_unit) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Homopolymer" (
	polymer_of TEXT, 
	has_repeat_unit TEXT, 
	is_branched BOOLEAN, 
	polymer_architecture_type TEXT, 
	is_organic BOOLEAN, 
	inchi_atom_connections_sublayer TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polymer_of) REFERENCES "Macromolecule" (id), 
	FOREIGN KEY(has_repeat_unit) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Isotope" (
	has_element TEXT, 
	neutron_number INTEGER, 
	isotope_of TEXT, 
	half_life INTEGER, 
	decay_product TEXT, 
	decay_mode TEXT, 
	decay_energy TEXT, 
	mode_of_formation TEXT, 
	energy_level TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY(isotope_of) REFERENCES "Isotope" (id), 
	FOREIGN KEY(decay_product) REFERENCES "Isotope" (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MonoatomicIon" (
	has_element TEXT, 
	elemental_charge INTEGER, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AtomAnion" (
	has_element TEXT, 
	elemental_charge INTEGER, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AtomCation" (
	has_element TEXT, 
	elemental_charge INTEGER, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "ChemicalEntity_has_major_microspecies_at_pH7_3" (
	"ChemicalEntity_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("ChemicalEntity_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "ChemicalEntity_pka_ionization_constant" (
	"ChemicalEntity_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("ChemicalEntity_id", pka_ionization_constant), 
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MolecularDerivativeGroupingClass_subtype_of" (
	"MolecularDerivativeGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("MolecularDerivativeGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("MolecularDerivativeGroupingClass_id") REFERENCES "MolecularDerivativeGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "GroupingClassForAcidsOrBases_subtype_of" (
	"GroupingClassForAcidsOrBases_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("GroupingClassForAcidsOrBases_id", subtype_of_id), 
	FOREIGN KEY("GroupingClassForAcidsOrBases_id") REFERENCES "GroupingClassForAcidsOrBases" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "AcidAnionGroupingClass_subtype_of" (
	"AcidAnionGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("AcidAnionGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("AcidAnionGroupingClass_id") REFERENCES "AcidAnionGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "GeneralAcidBaseGroupingClass_subtype_of" (
	"GeneralAcidBaseGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("GeneralAcidBaseGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("GeneralAcidBaseGroupingClass_id") REFERENCES "GeneralAcidBaseGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "AcidBaseConflationClass_subtype_of" (
	"AcidBaseConflationClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("AcidBaseConflationClass_id", subtype_of_id), 
	FOREIGN KEY("AcidBaseConflationClass_id") REFERENCES "AcidBaseConflationClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "PolyatomicEntity_has_major_microspecies_at_pH7_3" (
	"PolyatomicEntity_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("PolyatomicEntity_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("PolyatomicEntity_id") REFERENCES "PolyatomicEntity" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "PolyatomicEntity_pka_ionization_constant" (
	"PolyatomicEntity_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("PolyatomicEntity_id", pka_ionization_constant), 
	FOREIGN KEY("PolyatomicEntity_id") REFERENCES "PolyatomicEntity" (id)
);
CREATE TABLE "SmallMolecule_has_submolecules" (
	"SmallMolecule_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("SmallMolecule_id", has_submolecules_id), 
	FOREIGN KEY("SmallMolecule_id") REFERENCES "SmallMolecule" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "SmallMolecule_has_atoms" (
	"SmallMolecule_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("SmallMolecule_id", has_atoms_id), 
	FOREIGN KEY("SmallMolecule_id") REFERENCES "SmallMolecule" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "SmallMolecule_has_major_microspecies_at_pH7_3" (
	"SmallMolecule_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("SmallMolecule_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("SmallMolecule_id") REFERENCES "SmallMolecule" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "SmallMolecule_pka_ionization_constant" (
	"SmallMolecule_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("SmallMolecule_id", pka_ionization_constant), 
	FOREIGN KEY("SmallMolecule_id") REFERENCES "SmallMolecule" (id)
);
CREATE TABLE "Macromolecule_has_submolecules" (
	"Macromolecule_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Macromolecule_id", has_submolecules_id), 
	FOREIGN KEY("Macromolecule_id") REFERENCES "Macromolecule" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Macromolecule_has_atoms" (
	"Macromolecule_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Macromolecule_id", has_atoms_id), 
	FOREIGN KEY("Macromolecule_id") REFERENCES "Macromolecule" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Macromolecule_has_major_microspecies_at_pH7_3" (
	"Macromolecule_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Macromolecule_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Macromolecule_id") REFERENCES "Macromolecule" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Macromolecule_pka_ionization_constant" (
	"Macromolecule_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Macromolecule_id", pka_ionization_constant), 
	FOREIGN KEY("Macromolecule_id") REFERENCES "Macromolecule" (id)
);
CREATE TABLE "MolecularComplex_has_major_microspecies_at_pH7_3" (
	"MolecularComplex_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("MolecularComplex_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("MolecularComplex_id") REFERENCES "MolecularComplex" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MolecularComplex_pka_ionization_constant" (
	"MolecularComplex_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("MolecularComplex_id", pka_ionization_constant), 
	FOREIGN KEY("MolecularComplex_id") REFERENCES "MolecularComplex" (id)
);
CREATE TABLE "Peptide_has_submolecules" (
	"Peptide_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Peptide_id", has_submolecules_id), 
	FOREIGN KEY("Peptide_id") REFERENCES "Peptide" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Peptide_has_atoms" (
	"Peptide_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Peptide_id", has_atoms_id), 
	FOREIGN KEY("Peptide_id") REFERENCES "Peptide" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Peptide_has_major_microspecies_at_pH7_3" (
	"Peptide_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Peptide_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Peptide_id") REFERENCES "Peptide" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Peptide_pka_ionization_constant" (
	"Peptide_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Peptide_id", pka_ionization_constant), 
	FOREIGN KEY("Peptide_id") REFERENCES "Peptide" (id)
);
CREATE TABLE "Protein_has_submolecules" (
	"Protein_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Protein_id", has_submolecules_id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Protein_has_atoms" (
	"Protein_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Protein_id", has_atoms_id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Protein_has_major_microspecies_at_pH7_3" (
	"Protein_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Protein_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Protein_pka_ionization_constant" (
	"Protein_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Protein_id", pka_ionization_constant), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Glycan_has_submolecules" (
	"Glycan_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Glycan_id", has_submolecules_id), 
	FOREIGN KEY("Glycan_id") REFERENCES "Glycan" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Glycan_has_atoms" (
	"Glycan_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Glycan_id", has_atoms_id), 
	FOREIGN KEY("Glycan_id") REFERENCES "Glycan" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Glycan_has_major_microspecies_at_pH7_3" (
	"Glycan_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Glycan_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Glycan_id") REFERENCES "Glycan" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Glycan_pka_ionization_constant" (
	"Glycan_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Glycan_id", pka_ionization_constant), 
	FOREIGN KEY("Glycan_id") REFERENCES "Glycan" (id)
);
CREATE TABLE "MolecularComponent_has_major_microspecies_at_pH7_3" (
	"MolecularComponent_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("MolecularComponent_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("MolecularComponent_id") REFERENCES "MolecularComponent" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MolecularComponent_pka_ionization_constant" (
	"MolecularComponent_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("MolecularComponent_id", pka_ionization_constant), 
	FOREIGN KEY("MolecularComponent_id") REFERENCES "MolecularComponent" (id)
);
CREATE TABLE "PolymerPart_has_major_microspecies_at_pH7_3" (
	"PolymerPart_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("PolymerPart_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("PolymerPart_id") REFERENCES "PolymerPart" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "PolymerPart_pka_ionization_constant" (
	"PolymerPart_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("PolymerPart_id", pka_ionization_constant), 
	FOREIGN KEY("PolymerPart_id") REFERENCES "PolymerPart" (id)
);
CREATE TABLE "Monomer_has_major_microspecies_at_pH7_3" (
	"Monomer_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Monomer_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Monomer_id") REFERENCES "Monomer" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Monomer_pka_ionization_constant" (
	"Monomer_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Monomer_id", pka_ionization_constant), 
	FOREIGN KEY("Monomer_id") REFERENCES "Monomer" (id)
);
CREATE TABLE "MolecularSubsequence_has_major_microspecies_at_pH7_3" (
	"MolecularSubsequence_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("MolecularSubsequence_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("MolecularSubsequence_id") REFERENCES "MolecularSubsequence" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MolecularSubsequence_pka_ionization_constant" (
	"MolecularSubsequence_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("MolecularSubsequence_id", pka_ionization_constant), 
	FOREIGN KEY("MolecularSubsequence_id") REFERENCES "MolecularSubsequence" (id)
);
CREATE TABLE "ChemicalGroup_has_major_microspecies_at_pH7_3" (
	"ChemicalGroup_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("ChemicalGroup_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("ChemicalGroup_id") REFERENCES "ChemicalGroup" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "ChemicalGroup_pka_ionization_constant" (
	"ChemicalGroup_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("ChemicalGroup_id", pka_ionization_constant), 
	FOREIGN KEY("ChemicalGroup_id") REFERENCES "ChemicalGroup" (id)
);
CREATE TABLE "ChemicalMixture_has_major_microspecies_at_pH7_3" (
	"ChemicalMixture_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("ChemicalMixture_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("ChemicalMixture_id") REFERENCES "ChemicalMixture" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "ChemicalMixture_pka_ionization_constant" (
	"ChemicalMixture_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("ChemicalMixture_id", pka_ionization_constant), 
	FOREIGN KEY("ChemicalMixture_id") REFERENCES "ChemicalMixture" (id)
);
CREATE TABLE "PreciseChemicalMixture_has_major_microspecies_at_pH7_3" (
	"PreciseChemicalMixture_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("PreciseChemicalMixture_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("PreciseChemicalMixture_id") REFERENCES "PreciseChemicalMixture" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "PreciseChemicalMixture_pka_ionization_constant" (
	"PreciseChemicalMixture_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("PreciseChemicalMixture_id", pka_ionization_constant), 
	FOREIGN KEY("PreciseChemicalMixture_id") REFERENCES "PreciseChemicalMixture" (id)
);
CREATE TABLE "ImpreciseChemicalMixture_has_proportional_parts" (
	"ImpreciseChemicalMixture_id" TEXT, 
	has_proportional_parts_id INTEGER, 
	PRIMARY KEY ("ImpreciseChemicalMixture_id", has_proportional_parts_id), 
	FOREIGN KEY("ImpreciseChemicalMixture_id") REFERENCES "ImpreciseChemicalMixture" (id), 
	FOREIGN KEY(has_proportional_parts_id) REFERENCES "ProportionalPart" (id)
);
CREATE TABLE "ImpreciseChemicalMixture_has_major_microspecies_at_pH7_3" (
	"ImpreciseChemicalMixture_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("ImpreciseChemicalMixture_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("ImpreciseChemicalMixture_id") REFERENCES "ImpreciseChemicalMixture" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "ImpreciseChemicalMixture_pka_ionization_constant" (
	"ImpreciseChemicalMixture_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("ImpreciseChemicalMixture_id", pka_ionization_constant), 
	FOREIGN KEY("ImpreciseChemicalMixture_id") REFERENCES "ImpreciseChemicalMixture" (id)
);
CREATE TABLE "Molecule_has_submolecules" (
	"Molecule_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Molecule_id", has_submolecules_id), 
	FOREIGN KEY("Molecule_id") REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Molecule_has_atoms" (
	"Molecule_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Molecule_id", has_atoms_id), 
	FOREIGN KEY("Molecule_id") REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Molecule_has_major_microspecies_at_pH7_3" (
	"Molecule_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Molecule_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Molecule_id") REFERENCES "Molecule" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Molecule_pka_ionization_constant" (
	"Molecule_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Molecule_id", pka_ionization_constant), 
	FOREIGN KEY("Molecule_id") REFERENCES "Molecule" (id)
);
CREATE TABLE "NaturalProduct_derived_from_organisms" (
	"NaturalProduct_id" TEXT, 
	derived_from_organisms TEXT, 
	PRIMARY KEY ("NaturalProduct_id", derived_from_organisms), 
	FOREIGN KEY("NaturalProduct_id") REFERENCES "NaturalProduct" (id)
);
CREATE TABLE "NaturalProduct_has_submolecules" (
	"NaturalProduct_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("NaturalProduct_id", has_submolecules_id), 
	FOREIGN KEY("NaturalProduct_id") REFERENCES "NaturalProduct" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "NaturalProduct_has_atoms" (
	"NaturalProduct_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("NaturalProduct_id", has_atoms_id), 
	FOREIGN KEY("NaturalProduct_id") REFERENCES "NaturalProduct" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "NaturalProduct_has_major_microspecies_at_pH7_3" (
	"NaturalProduct_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("NaturalProduct_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("NaturalProduct_id") REFERENCES "NaturalProduct" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "NaturalProduct_pka_ionization_constant" (
	"NaturalProduct_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("NaturalProduct_id", pka_ionization_constant), 
	FOREIGN KEY("NaturalProduct_id") REFERENCES "NaturalProduct" (id)
);
CREATE TABLE "Moiety_has_major_microspecies_at_pH7_3" (
	"Moiety_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Moiety_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Moiety_id") REFERENCES "Moiety" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Moiety_pka_ionization_constant" (
	"Moiety_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Moiety_id", pka_ionization_constant), 
	FOREIGN KEY("Moiety_id") REFERENCES "Moiety" (id)
);
CREATE TABLE "SequenceInterval_has_major_microspecies_at_pH7_3" (
	"SequenceInterval_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("SequenceInterval_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("SequenceInterval_id") REFERENCES "SequenceInterval" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "SequenceInterval_pka_ionization_constant" (
	"SequenceInterval_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("SequenceInterval_id", pka_ionization_constant), 
	FOREIGN KEY("SequenceInterval_id") REFERENCES "SequenceInterval" (id)
);
CREATE TABLE "AminoAcidSequenceInterval_has_major_microspecies_at_pH7_3" (
	"AminoAcidSequenceInterval_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("AminoAcidSequenceInterval_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("AminoAcidSequenceInterval_id") REFERENCES "AminoAcidSequenceInterval" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "AminoAcidSequenceInterval_pka_ionization_constant" (
	"AminoAcidSequenceInterval_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("AminoAcidSequenceInterval_id", pka_ionization_constant), 
	FOREIGN KEY("AminoAcidSequenceInterval_id") REFERENCES "AminoAcidSequenceInterval" (id)
);
CREATE TABLE "NucleotideSequenceInterval_has_major_microspecies_at_pH7_3" (
	"NucleotideSequenceInterval_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("NucleotideSequenceInterval_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("NucleotideSequenceInterval_id") REFERENCES "NucleotideSequenceInterval" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "NucleotideSequenceInterval_pka_ionization_constant" (
	"NucleotideSequenceInterval_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("NucleotideSequenceInterval_id", pka_ionization_constant), 
	FOREIGN KEY("NucleotideSequenceInterval_id") REFERENCES "NucleotideSequenceInterval" (id)
);
CREATE TABLE "DNASequenceInterval_has_major_microspecies_at_pH7_3" (
	"DNASequenceInterval_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("DNASequenceInterval_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("DNASequenceInterval_id") REFERENCES "DNASequenceInterval" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "DNASequenceInterval_pka_ionization_constant" (
	"DNASequenceInterval_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("DNASequenceInterval_id", pka_ionization_constant), 
	FOREIGN KEY("DNASequenceInterval_id") REFERENCES "DNASequenceInterval" (id)
);
CREATE TABLE "RNASequenceInterval_has_major_microspecies_at_pH7_3" (
	"RNASequenceInterval_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("RNASequenceInterval_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("RNASequenceInterval_id") REFERENCES "RNASequenceInterval" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "RNASequenceInterval_pka_ionization_constant" (
	"RNASequenceInterval_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("RNASequenceInterval_id", pka_ionization_constant), 
	FOREIGN KEY("RNASequenceInterval_id") REFERENCES "RNASequenceInterval" (id)
);
CREATE TABLE "FunctionalGroup_has_major_microspecies_at_pH7_3" (
	"FunctionalGroup_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("FunctionalGroup_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("FunctionalGroup_id") REFERENCES "FunctionalGroup" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "FunctionalGroup_pka_ionization_constant" (
	"FunctionalGroup_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("FunctionalGroup_id", pka_ionization_constant), 
	FOREIGN KEY("FunctionalGroup_id") REFERENCES "FunctionalGroup" (id)
);
CREATE TABLE "MolecularSpecies_has_submolecules" (
	"MolecularSpecies_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("MolecularSpecies_id", has_submolecules_id), 
	FOREIGN KEY("MolecularSpecies_id") REFERENCES "MolecularSpecies" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "MolecularSpecies_has_atoms" (
	"MolecularSpecies_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("MolecularSpecies_id", has_atoms_id), 
	FOREIGN KEY("MolecularSpecies_id") REFERENCES "MolecularSpecies" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "MolecularSpecies_has_major_microspecies_at_pH7_3" (
	"MolecularSpecies_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("MolecularSpecies_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("MolecularSpecies_id") REFERENCES "MolecularSpecies" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MolecularSpecies_pka_ionization_constant" (
	"MolecularSpecies_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("MolecularSpecies_id", pka_ionization_constant), 
	FOREIGN KEY("MolecularSpecies_id") REFERENCES "MolecularSpecies" (id)
);
CREATE TABLE "NonSpeciesMolecule_has_submolecules" (
	"NonSpeciesMolecule_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("NonSpeciesMolecule_id", has_submolecules_id), 
	FOREIGN KEY("NonSpeciesMolecule_id") REFERENCES "NonSpeciesMolecule" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "NonSpeciesMolecule_has_atoms" (
	"NonSpeciesMolecule_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("NonSpeciesMolecule_id", has_atoms_id), 
	FOREIGN KEY("NonSpeciesMolecule_id") REFERENCES "NonSpeciesMolecule" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "NonSpeciesMolecule_has_major_microspecies_at_pH7_3" (
	"NonSpeciesMolecule_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("NonSpeciesMolecule_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("NonSpeciesMolecule_id") REFERENCES "NonSpeciesMolecule" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "NonSpeciesMolecule_pka_ionization_constant" (
	"NonSpeciesMolecule_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("NonSpeciesMolecule_id", pka_ionization_constant), 
	FOREIGN KEY("NonSpeciesMolecule_id") REFERENCES "NonSpeciesMolecule" (id)
);
CREATE TABLE "MoleculeByChargeState_has_submolecules" (
	"MoleculeByChargeState_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("MoleculeByChargeState_id", has_submolecules_id), 
	FOREIGN KEY("MoleculeByChargeState_id") REFERENCES "MoleculeByChargeState" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "MoleculeByChargeState_has_atoms" (
	"MoleculeByChargeState_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("MoleculeByChargeState_id", has_atoms_id), 
	FOREIGN KEY("MoleculeByChargeState_id") REFERENCES "MoleculeByChargeState" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "MoleculeByChargeState_has_major_microspecies_at_pH7_3" (
	"MoleculeByChargeState_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("MoleculeByChargeState_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("MoleculeByChargeState_id") REFERENCES "MoleculeByChargeState" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MoleculeByChargeState_pka_ionization_constant" (
	"MoleculeByChargeState_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("MoleculeByChargeState_id", pka_ionization_constant), 
	FOREIGN KEY("MoleculeByChargeState_id") REFERENCES "MoleculeByChargeState" (id)
);
CREATE TABLE "PolyatomicIon_has_submolecules" (
	"PolyatomicIon_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("PolyatomicIon_id", has_submolecules_id), 
	FOREIGN KEY("PolyatomicIon_id") REFERENCES "PolyatomicIon" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "PolyatomicIon_has_atoms" (
	"PolyatomicIon_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("PolyatomicIon_id", has_atoms_id), 
	FOREIGN KEY("PolyatomicIon_id") REFERENCES "PolyatomicIon" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "PolyatomicIon_has_major_microspecies_at_pH7_3" (
	"PolyatomicIon_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("PolyatomicIon_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("PolyatomicIon_id") REFERENCES "PolyatomicIon" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "PolyatomicIon_pka_ionization_constant" (
	"PolyatomicIon_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("PolyatomicIon_id", pka_ionization_constant), 
	FOREIGN KEY("PolyatomicIon_id") REFERENCES "PolyatomicIon" (id)
);
CREATE TABLE "MolecularCation_has_submolecules" (
	"MolecularCation_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("MolecularCation_id", has_submolecules_id), 
	FOREIGN KEY("MolecularCation_id") REFERENCES "MolecularCation" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "MolecularCation_has_atoms" (
	"MolecularCation_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("MolecularCation_id", has_atoms_id), 
	FOREIGN KEY("MolecularCation_id") REFERENCES "MolecularCation" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "MolecularCation_has_major_microspecies_at_pH7_3" (
	"MolecularCation_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("MolecularCation_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("MolecularCation_id") REFERENCES "MolecularCation" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MolecularCation_pka_ionization_constant" (
	"MolecularCation_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("MolecularCation_id", pka_ionization_constant), 
	FOREIGN KEY("MolecularCation_id") REFERENCES "MolecularCation" (id)
);
CREATE TABLE "MolecularAnion_has_submolecules" (
	"MolecularAnion_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("MolecularAnion_id", has_submolecules_id), 
	FOREIGN KEY("MolecularAnion_id") REFERENCES "MolecularAnion" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "MolecularAnion_has_atoms" (
	"MolecularAnion_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("MolecularAnion_id", has_atoms_id), 
	FOREIGN KEY("MolecularAnion_id") REFERENCES "MolecularAnion" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "MolecularAnion_has_major_microspecies_at_pH7_3" (
	"MolecularAnion_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("MolecularAnion_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("MolecularAnion_id") REFERENCES "MolecularAnion" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MolecularAnion_pka_ionization_constant" (
	"MolecularAnion_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("MolecularAnion_id", pka_ionization_constant), 
	FOREIGN KEY("MolecularAnion_id") REFERENCES "MolecularAnion" (id)
);
CREATE TABLE "NetUnchargedMolecule_has_submolecules" (
	"NetUnchargedMolecule_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("NetUnchargedMolecule_id", has_submolecules_id), 
	FOREIGN KEY("NetUnchargedMolecule_id") REFERENCES "NetUnchargedMolecule" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "NetUnchargedMolecule_has_atoms" (
	"NetUnchargedMolecule_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("NetUnchargedMolecule_id", has_atoms_id), 
	FOREIGN KEY("NetUnchargedMolecule_id") REFERENCES "NetUnchargedMolecule" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "NetUnchargedMolecule_has_major_microspecies_at_pH7_3" (
	"NetUnchargedMolecule_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("NetUnchargedMolecule_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("NetUnchargedMolecule_id") REFERENCES "NetUnchargedMolecule" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "NetUnchargedMolecule_pka_ionization_constant" (
	"NetUnchargedMolecule_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("NetUnchargedMolecule_id", pka_ionization_constant), 
	FOREIGN KEY("NetUnchargedMolecule_id") REFERENCES "NetUnchargedMolecule" (id)
);
CREATE TABLE "Zwitterion_has_submolecules" (
	"Zwitterion_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Zwitterion_id", has_submolecules_id), 
	FOREIGN KEY("Zwitterion_id") REFERENCES "Zwitterion" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Zwitterion_has_atoms" (
	"Zwitterion_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Zwitterion_id", has_atoms_id), 
	FOREIGN KEY("Zwitterion_id") REFERENCES "Zwitterion" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Zwitterion_has_major_microspecies_at_pH7_3" (
	"Zwitterion_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Zwitterion_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Zwitterion_id") REFERENCES "Zwitterion" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Zwitterion_pka_ionization_constant" (
	"Zwitterion_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Zwitterion_id", pka_ionization_constant), 
	FOREIGN KEY("Zwitterion_id") REFERENCES "Zwitterion" (id)
);
CREATE TABLE "NeutralMolecule_has_submolecules" (
	"NeutralMolecule_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("NeutralMolecule_id", has_submolecules_id), 
	FOREIGN KEY("NeutralMolecule_id") REFERENCES "NeutralMolecule" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "NeutralMolecule_has_atoms" (
	"NeutralMolecule_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("NeutralMolecule_id", has_atoms_id), 
	FOREIGN KEY("NeutralMolecule_id") REFERENCES "NeutralMolecule" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "NeutralMolecule_has_major_microspecies_at_pH7_3" (
	"NeutralMolecule_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("NeutralMolecule_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("NeutralMolecule_id") REFERENCES "NeutralMolecule" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "NeutralMolecule_pka_ionization_constant" (
	"NeutralMolecule_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("NeutralMolecule_id", pka_ionization_constant), 
	FOREIGN KEY("NeutralMolecule_id") REFERENCES "NeutralMolecule" (id)
);
CREATE TABLE "Atom_has_major_microspecies_at_pH7_3" (
	"Atom_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Atom_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Atom_pka_ionization_constant" (
	"Atom_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Atom_id", pka_ionization_constant), 
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id)
);
CREATE TABLE "ChemicalElement_has_major_microspecies_at_pH7_3" (
	"ChemicalElement_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("ChemicalElement_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("ChemicalElement_id") REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalElement" (id)
);
CREATE TABLE "ChemicalElement_pka_ionization_constant" (
	"ChemicalElement_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("ChemicalElement_id", pka_ionization_constant), 
	FOREIGN KEY("ChemicalElement_id") REFERENCES "ChemicalElement" (id)
);
CREATE TABLE "UnchargedAtom_has_major_microspecies_at_pH7_3" (
	"UnchargedAtom_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("UnchargedAtom_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("UnchargedAtom_id") REFERENCES "UnchargedAtom" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "UnchargedAtom_pka_ionization_constant" (
	"UnchargedAtom_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("UnchargedAtom_id", pka_ionization_constant), 
	FOREIGN KEY("UnchargedAtom_id") REFERENCES "UnchargedAtom" (id)
);
CREATE TABLE "Nuclide_has_major_microspecies_at_pH7_3" (
	"Nuclide_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Nuclide_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Nuclide_id") REFERENCES "Nuclide" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Nuclide_pka_ionization_constant" (
	"Nuclide_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Nuclide_id", pka_ionization_constant), 
	FOREIGN KEY("Nuclide_id") REFERENCES "Nuclide" (id)
);
CREATE TABLE "Radionuclide_has_major_microspecies_at_pH7_3" (
	"Radionuclide_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Radionuclide_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Radionuclide_id") REFERENCES "Radionuclide" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Radionuclide_pka_ionization_constant" (
	"Radionuclide_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Radionuclide_id", pka_ionization_constant), 
	FOREIGN KEY("Radionuclide_id") REFERENCES "Radionuclide" (id)
);
CREATE TABLE "AtomIonicForm_has_major_microspecies_at_pH7_3" (
	"AtomIonicForm_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("AtomIonicForm_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("AtomIonicForm_id") REFERENCES "AtomIonicForm" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "AtomIonicForm_pka_ionization_constant" (
	"AtomIonicForm_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("AtomIonicForm_id", pka_ionization_constant), 
	FOREIGN KEY("AtomIonicForm_id") REFERENCES "AtomIonicForm" (id)
);
CREATE TABLE "PartiallySpecifiedAtom_has_major_microspecies_at_pH7_3" (
	"PartiallySpecifiedAtom_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("PartiallySpecifiedAtom_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("PartiallySpecifiedAtom_id") REFERENCES "PartiallySpecifiedAtom" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "PartiallySpecifiedAtom_pka_ionization_constant" (
	"PartiallySpecifiedAtom_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("PartiallySpecifiedAtom_id", pka_ionization_constant), 
	FOREIGN KEY("PartiallySpecifiedAtom_id") REFERENCES "PartiallySpecifiedAtom" (id)
);
CREATE TABLE "FullySpecifiedAtom_has_major_microspecies_at_pH7_3" (
	"FullySpecifiedAtom_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("FullySpecifiedAtom_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("FullySpecifiedAtom_id") REFERENCES "FullySpecifiedAtom" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "FullySpecifiedAtom_pka_ionization_constant" (
	"FullySpecifiedAtom_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("FullySpecifiedAtom_id", pka_ionization_constant), 
	FOREIGN KEY("FullySpecifiedAtom_id") REFERENCES "FullySpecifiedAtom" (id)
);
CREATE TABLE "ChemicalSalt_has_major_microspecies_at_pH7_3" (
	"ChemicalSalt_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("ChemicalSalt_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("ChemicalSalt_id") REFERENCES "ChemicalSalt" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "ChemicalSalt_pka_ionization_constant" (
	"ChemicalSalt_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("ChemicalSalt_id", pka_ionization_constant), 
	FOREIGN KEY("ChemicalSalt_id") REFERENCES "ChemicalSalt" (id)
);
CREATE TABLE "Ester_has_submolecules" (
	"Ester_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Ester_id", has_submolecules_id), 
	FOREIGN KEY("Ester_id") REFERENCES "Ester" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Ester_has_atoms" (
	"Ester_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Ester_id", has_atoms_id), 
	FOREIGN KEY("Ester_id") REFERENCES "Ester" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Ester_has_major_microspecies_at_pH7_3" (
	"Ester_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Ester_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Ester_id") REFERENCES "Ester" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Ester_pka_ionization_constant" (
	"Ester_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Ester_id", pka_ionization_constant), 
	FOREIGN KEY("Ester_id") REFERENCES "Ester" (id)
);
CREATE TABLE "Stereoisomer_has_submolecules" (
	"Stereoisomer_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Stereoisomer_id", has_submolecules_id), 
	FOREIGN KEY("Stereoisomer_id") REFERENCES "Stereoisomer" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Stereoisomer_has_atoms" (
	"Stereoisomer_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Stereoisomer_id", has_atoms_id), 
	FOREIGN KEY("Stereoisomer_id") REFERENCES "Stereoisomer" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Stereoisomer_has_major_microspecies_at_pH7_3" (
	"Stereoisomer_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Stereoisomer_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Stereoisomer_id") REFERENCES "Stereoisomer" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Stereoisomer_pka_ionization_constant" (
	"Stereoisomer_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Stereoisomer_id", pka_ionization_constant), 
	FOREIGN KEY("Stereoisomer_id") REFERENCES "Stereoisomer" (id)
);
CREATE TABLE "Enantiomer_has_submolecules" (
	"Enantiomer_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Enantiomer_id", has_submolecules_id), 
	FOREIGN KEY("Enantiomer_id") REFERENCES "Enantiomer" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Enantiomer_has_atoms" (
	"Enantiomer_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Enantiomer_id", has_atoms_id), 
	FOREIGN KEY("Enantiomer_id") REFERENCES "Enantiomer" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Enantiomer_has_major_microspecies_at_pH7_3" (
	"Enantiomer_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Enantiomer_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Enantiomer_id") REFERENCES "Enantiomer" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Enantiomer_pka_ionization_constant" (
	"Enantiomer_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Enantiomer_id", pka_ionization_constant), 
	FOREIGN KEY("Enantiomer_id") REFERENCES "Enantiomer" (id)
);
CREATE TABLE "RacemicMixture_has_major_microspecies_at_pH7_3" (
	"RacemicMixture_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("RacemicMixture_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("RacemicMixture_id") REFERENCES "RacemicMixture" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "RacemicMixture_pka_ionization_constant" (
	"RacemicMixture_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("RacemicMixture_id", pka_ionization_constant), 
	FOREIGN KEY("RacemicMixture_id") REFERENCES "RacemicMixture" (id)
);
CREATE TABLE "Allotrope_has_submolecules" (
	"Allotrope_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Allotrope_id", has_submolecules_id), 
	FOREIGN KEY("Allotrope_id") REFERENCES "Allotrope" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Allotrope_has_atoms" (
	"Allotrope_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Allotrope_id", has_atoms_id), 
	FOREIGN KEY("Allotrope_id") REFERENCES "Allotrope" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Allotrope_has_major_microspecies_at_pH7_3" (
	"Allotrope_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Allotrope_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Allotrope_id") REFERENCES "Allotrope" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Allotrope_pka_ionization_constant" (
	"Allotrope_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Allotrope_id", pka_ionization_constant), 
	FOREIGN KEY("Allotrope_id") REFERENCES "Allotrope" (id)
);
CREATE TABLE "Isobar" (
	has_element TEXT, 
	nucleon_number INTEGER, 
	isobar_of TEXT, 
	half_life INTEGER, 
	decay_product TEXT, 
	decay_mode TEXT, 
	decay_energy TEXT, 
	mode_of_formation TEXT, 
	energy_level TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	smiles_string TEXT, 
	empirical_formula TEXT, 
	molecular_mass FLOAT, 
	water_solubility FLOAT, 
	pka_temperature FLOAT, 
	pka_ionic_strength FLOAT, 
	pka_solvent TEXT, 
	pka_pressure FLOAT, 
	id TEXT NOT NULL, 
	type TEXT, 
	has_nuclear_parts_id INTEGER, 
	has_chemical_role_id INTEGER, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY(isobar_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(decay_product) REFERENCES "Isotope" (id), 
	FOREIGN KEY(has_nuclear_parts_id) REFERENCES "SubatomicParticleOccurrence" (id), 
	FOREIGN KEY(has_chemical_role_id) REFERENCES "ChemicalRole" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "AtomOccurrence" (
	name TEXT NOT NULL, 
	occurrence_of TEXT NOT NULL, 
	valence INTEGER, 
	oxidation_number INTEGER, 
	formal_charge INTEGER, 
	coordination_number INTEGER, 
	"SmallMolecule_id" TEXT, 
	"Macromolecule_id" TEXT, 
	"Peptide_id" TEXT, 
	"Protein_id" TEXT, 
	"Glycan_id" TEXT, 
	"MonomolecularPolymer_id" TEXT, 
	"Copolymer_id" TEXT, 
	"Homopolymer_id" TEXT, 
	"Molecule_id" TEXT, 
	"NaturalProduct_id" TEXT, 
	"MolecularSpecies_id" TEXT, 
	"NonSpeciesMolecule_id" TEXT, 
	"MoleculeByChargeState_id" TEXT, 
	"PolyatomicIon_id" TEXT, 
	"MolecularCation_id" TEXT, 
	"MolecularAnion_id" TEXT, 
	"NetUnchargedMolecule_id" TEXT, 
	"Zwitterion_id" TEXT, 
	"NeutralMolecule_id" TEXT, 
	"Ester_id" TEXT, 
	"Stereoisomer_id" TEXT, 
	"Enantiomer_id" TEXT, 
	"Allotrope_id" TEXT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY(occurrence_of) REFERENCES "Atom" (id), 
	FOREIGN KEY("SmallMolecule_id") REFERENCES "SmallMolecule" (id), 
	FOREIGN KEY("Macromolecule_id") REFERENCES "Macromolecule" (id), 
	FOREIGN KEY("Peptide_id") REFERENCES "Peptide" (id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("Glycan_id") REFERENCES "Glycan" (id), 
	FOREIGN KEY("MonomolecularPolymer_id") REFERENCES "MonomolecularPolymer" (id), 
	FOREIGN KEY("Copolymer_id") REFERENCES "Copolymer" (id), 
	FOREIGN KEY("Homopolymer_id") REFERENCES "Homopolymer" (id), 
	FOREIGN KEY("Molecule_id") REFERENCES "Molecule" (id), 
	FOREIGN KEY("NaturalProduct_id") REFERENCES "NaturalProduct" (id), 
	FOREIGN KEY("MolecularSpecies_id") REFERENCES "MolecularSpecies" (id), 
	FOREIGN KEY("NonSpeciesMolecule_id") REFERENCES "NonSpeciesMolecule" (id), 
	FOREIGN KEY("MoleculeByChargeState_id") REFERENCES "MoleculeByChargeState" (id), 
	FOREIGN KEY("PolyatomicIon_id") REFERENCES "PolyatomicIon" (id), 
	FOREIGN KEY("MolecularCation_id") REFERENCES "MolecularCation" (id), 
	FOREIGN KEY("MolecularAnion_id") REFERENCES "MolecularAnion" (id), 
	FOREIGN KEY("NetUnchargedMolecule_id") REFERENCES "NetUnchargedMolecule" (id), 
	FOREIGN KEY("Zwitterion_id") REFERENCES "Zwitterion" (id), 
	FOREIGN KEY("NeutralMolecule_id") REFERENCES "NeutralMolecule" (id), 
	FOREIGN KEY("Ester_id") REFERENCES "Ester" (id), 
	FOREIGN KEY("Stereoisomer_id") REFERENCES "Stereoisomer" (id), 
	FOREIGN KEY("Enantiomer_id") REFERENCES "Enantiomer" (id), 
	FOREIGN KEY("Allotrope_id") REFERENCES "Allotrope" (id), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "MonomericPolymericGroupingClass_subtype_of" (
	"MonomericPolymericGroupingClass_id" TEXT, 
	subtype_of_id TEXT, 
	PRIMARY KEY ("MonomericPolymericGroupingClass_id", subtype_of_id), 
	FOREIGN KEY("MonomericPolymericGroupingClass_id") REFERENCES "MonomericPolymericGroupingClass" (id), 
	FOREIGN KEY(subtype_of_id) REFERENCES "MoleculeGroupingClass" (id)
);
CREATE TABLE "MonomolecularPolymer_has_submolecules" (
	"MonomolecularPolymer_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("MonomolecularPolymer_id", has_submolecules_id), 
	FOREIGN KEY("MonomolecularPolymer_id") REFERENCES "MonomolecularPolymer" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "MonomolecularPolymer_has_atoms" (
	"MonomolecularPolymer_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("MonomolecularPolymer_id", has_atoms_id), 
	FOREIGN KEY("MonomolecularPolymer_id") REFERENCES "MonomolecularPolymer" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "MonomolecularPolymer_has_major_microspecies_at_pH7_3" (
	"MonomolecularPolymer_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("MonomolecularPolymer_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("MonomolecularPolymer_id") REFERENCES "MonomolecularPolymer" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MonomolecularPolymer_pka_ionization_constant" (
	"MonomolecularPolymer_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("MonomolecularPolymer_id", pka_ionization_constant), 
	FOREIGN KEY("MonomolecularPolymer_id") REFERENCES "MonomolecularPolymer" (id)
);
CREATE TABLE "SupramolecularPolymer_has_major_microspecies_at_pH7_3" (
	"SupramolecularPolymer_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("SupramolecularPolymer_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("SupramolecularPolymer_id") REFERENCES "SupramolecularPolymer" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "SupramolecularPolymer_pka_ionization_constant" (
	"SupramolecularPolymer_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("SupramolecularPolymer_id", pka_ionization_constant), 
	FOREIGN KEY("SupramolecularPolymer_id") REFERENCES "SupramolecularPolymer" (id)
);
CREATE TABLE "Copolymer_polymer_of" (
	"Copolymer_id" TEXT, 
	polymer_of_id TEXT, 
	PRIMARY KEY ("Copolymer_id", polymer_of_id), 
	FOREIGN KEY("Copolymer_id") REFERENCES "Copolymer" (id), 
	FOREIGN KEY(polymer_of_id) REFERENCES "Macromolecule" (id)
);
CREATE TABLE "Copolymer_has_submolecules" (
	"Copolymer_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Copolymer_id", has_submolecules_id), 
	FOREIGN KEY("Copolymer_id") REFERENCES "Copolymer" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Copolymer_has_atoms" (
	"Copolymer_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Copolymer_id", has_atoms_id), 
	FOREIGN KEY("Copolymer_id") REFERENCES "Copolymer" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Copolymer_has_major_microspecies_at_pH7_3" (
	"Copolymer_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Copolymer_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Copolymer_id") REFERENCES "Copolymer" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Copolymer_pka_ionization_constant" (
	"Copolymer_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Copolymer_id", pka_ionization_constant), 
	FOREIGN KEY("Copolymer_id") REFERENCES "Copolymer" (id)
);
CREATE TABLE "Homopolymer_has_submolecules" (
	"Homopolymer_id" TEXT, 
	has_submolecules_id TEXT, 
	PRIMARY KEY ("Homopolymer_id", has_submolecules_id), 
	FOREIGN KEY("Homopolymer_id") REFERENCES "Homopolymer" (id), 
	FOREIGN KEY(has_submolecules_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Homopolymer_has_atoms" (
	"Homopolymer_id" TEXT, 
	has_atoms_id TEXT, 
	PRIMARY KEY ("Homopolymer_id", has_atoms_id), 
	FOREIGN KEY("Homopolymer_id") REFERENCES "Homopolymer" (id), 
	FOREIGN KEY(has_atoms_id) REFERENCES "Atom" (id)
);
CREATE TABLE "Homopolymer_has_major_microspecies_at_pH7_3" (
	"Homopolymer_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Homopolymer_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Homopolymer_id") REFERENCES "Homopolymer" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Homopolymer_pka_ionization_constant" (
	"Homopolymer_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Homopolymer_id", pka_ionization_constant), 
	FOREIGN KEY("Homopolymer_id") REFERENCES "Homopolymer" (id)
);
CREATE TABLE "Isotope_has_major_microspecies_at_pH7_3" (
	"Isotope_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Isotope_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Isotope_id") REFERENCES "Isotope" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Isotope_pka_ionization_constant" (
	"Isotope_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Isotope_id", pka_ionization_constant), 
	FOREIGN KEY("Isotope_id") REFERENCES "Isotope" (id)
);
CREATE TABLE "MonoatomicIon_has_major_microspecies_at_pH7_3" (
	"MonoatomicIon_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("MonoatomicIon_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("MonoatomicIon_id") REFERENCES "MonoatomicIon" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "MonoatomicIon_pka_ionization_constant" (
	"MonoatomicIon_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("MonoatomicIon_id", pka_ionization_constant), 
	FOREIGN KEY("MonoatomicIon_id") REFERENCES "MonoatomicIon" (id)
);
CREATE TABLE "AtomAnion_has_major_microspecies_at_pH7_3" (
	"AtomAnion_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("AtomAnion_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("AtomAnion_id") REFERENCES "AtomAnion" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "AtomAnion_pka_ionization_constant" (
	"AtomAnion_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("AtomAnion_id", pka_ionization_constant), 
	FOREIGN KEY("AtomAnion_id") REFERENCES "AtomAnion" (id)
);
CREATE TABLE "AtomCation_has_major_microspecies_at_pH7_3" (
	"AtomCation_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("AtomCation_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("AtomCation_id") REFERENCES "AtomCation" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "AtomCation_pka_ionization_constant" (
	"AtomCation_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("AtomCation_id", pka_ionization_constant), 
	FOREIGN KEY("AtomCation_id") REFERENCES "AtomCation" (id)
);
CREATE TABLE "AtomicBond" (
	id INTEGER NOT NULL, 
	subject TEXT, 
	object TEXT, 
	bond_type VARCHAR(14), 
	bond_order INTEGER, 
	bond_length FLOAT, 
	bond_energy FLOAT, 
	bond_length_in_angstroms FLOAT, 
	bond_angle FLOAT, 
	torsional_angle FLOAT, 
	owl_subclass_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "AtomOccurrence" (name), 
	FOREIGN KEY(object) REFERENCES "AtomOccurrence" (name), 
	FOREIGN KEY(owl_subclass_of_id) REFERENCES "OwlClass" (id)
);
CREATE TABLE "Isobar_has_major_microspecies_at_pH7_3" (
	"Isobar_id" TEXT, 
	"has_major_microspecies_at_pH7_3_id" TEXT, 
	PRIMARY KEY ("Isobar_id", "has_major_microspecies_at_pH7_3_id"), 
	FOREIGN KEY("Isobar_id") REFERENCES "Isobar" (id), 
	FOREIGN KEY("has_major_microspecies_at_pH7_3_id") REFERENCES "ChemicalEntity" (id)
);
CREATE TABLE "Isobar_pka_ionization_constant" (
	"Isobar_id" TEXT, 
	pka_ionization_constant FLOAT, 
	PRIMARY KEY ("Isobar_id", pka_ionization_constant), 
	FOREIGN KEY("Isobar_id") REFERENCES "Isobar" (id)
);
CREATE TABLE "SmallMolecule_has_bonds" (
	"SmallMolecule_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("SmallMolecule_id", has_bonds_id), 
	FOREIGN KEY("SmallMolecule_id") REFERENCES "SmallMolecule" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Macromolecule_has_bonds" (
	"Macromolecule_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Macromolecule_id", has_bonds_id), 
	FOREIGN KEY("Macromolecule_id") REFERENCES "Macromolecule" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Peptide_has_bonds" (
	"Peptide_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Peptide_id", has_bonds_id), 
	FOREIGN KEY("Peptide_id") REFERENCES "Peptide" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Protein_has_bonds" (
	"Protein_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Protein_id", has_bonds_id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Glycan_has_bonds" (
	"Glycan_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Glycan_id", has_bonds_id), 
	FOREIGN KEY("Glycan_id") REFERENCES "Glycan" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "MonomolecularPolymer_has_bonds" (
	"MonomolecularPolymer_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("MonomolecularPolymer_id", has_bonds_id), 
	FOREIGN KEY("MonomolecularPolymer_id") REFERENCES "MonomolecularPolymer" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Copolymer_has_bonds" (
	"Copolymer_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Copolymer_id", has_bonds_id), 
	FOREIGN KEY("Copolymer_id") REFERENCES "Copolymer" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Homopolymer_has_bonds" (
	"Homopolymer_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Homopolymer_id", has_bonds_id), 
	FOREIGN KEY("Homopolymer_id") REFERENCES "Homopolymer" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Molecule_has_bonds" (
	"Molecule_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Molecule_id", has_bonds_id), 
	FOREIGN KEY("Molecule_id") REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "NaturalProduct_has_bonds" (
	"NaturalProduct_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("NaturalProduct_id", has_bonds_id), 
	FOREIGN KEY("NaturalProduct_id") REFERENCES "NaturalProduct" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "MolecularSpecies_has_bonds" (
	"MolecularSpecies_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("MolecularSpecies_id", has_bonds_id), 
	FOREIGN KEY("MolecularSpecies_id") REFERENCES "MolecularSpecies" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "NonSpeciesMolecule_has_bonds" (
	"NonSpeciesMolecule_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("NonSpeciesMolecule_id", has_bonds_id), 
	FOREIGN KEY("NonSpeciesMolecule_id") REFERENCES "NonSpeciesMolecule" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "MoleculeByChargeState_has_bonds" (
	"MoleculeByChargeState_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("MoleculeByChargeState_id", has_bonds_id), 
	FOREIGN KEY("MoleculeByChargeState_id") REFERENCES "MoleculeByChargeState" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "PolyatomicIon_has_bonds" (
	"PolyatomicIon_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("PolyatomicIon_id", has_bonds_id), 
	FOREIGN KEY("PolyatomicIon_id") REFERENCES "PolyatomicIon" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "MolecularCation_has_bonds" (
	"MolecularCation_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("MolecularCation_id", has_bonds_id), 
	FOREIGN KEY("MolecularCation_id") REFERENCES "MolecularCation" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "MolecularAnion_has_bonds" (
	"MolecularAnion_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("MolecularAnion_id", has_bonds_id), 
	FOREIGN KEY("MolecularAnion_id") REFERENCES "MolecularAnion" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "NetUnchargedMolecule_has_bonds" (
	"NetUnchargedMolecule_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("NetUnchargedMolecule_id", has_bonds_id), 
	FOREIGN KEY("NetUnchargedMolecule_id") REFERENCES "NetUnchargedMolecule" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Zwitterion_has_bonds" (
	"Zwitterion_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Zwitterion_id", has_bonds_id), 
	FOREIGN KEY("Zwitterion_id") REFERENCES "Zwitterion" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "NeutralMolecule_has_bonds" (
	"NeutralMolecule_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("NeutralMolecule_id", has_bonds_id), 
	FOREIGN KEY("NeutralMolecule_id") REFERENCES "NeutralMolecule" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Ester_has_bonds" (
	"Ester_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Ester_id", has_bonds_id), 
	FOREIGN KEY("Ester_id") REFERENCES "Ester" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Stereoisomer_has_bonds" (
	"Stereoisomer_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Stereoisomer_id", has_bonds_id), 
	FOREIGN KEY("Stereoisomer_id") REFERENCES "Stereoisomer" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Enantiomer_has_bonds" (
	"Enantiomer_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Enantiomer_id", has_bonds_id), 
	FOREIGN KEY("Enantiomer_id") REFERENCES "Enantiomer" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);
CREATE TABLE "Allotrope_has_bonds" (
	"Allotrope_id" TEXT, 
	has_bonds_id INTEGER, 
	PRIMARY KEY ("Allotrope_id", has_bonds_id), 
	FOREIGN KEY("Allotrope_id") REFERENCES "Allotrope" (id), 
	FOREIGN KEY(has_bonds_id) REFERENCES "AtomicBond" (id)
);