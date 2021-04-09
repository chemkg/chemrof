
CREATE TABLE "AcidBase" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge TEXT, 
	has_acid_form TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(has_acid_form) REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "AminoAcidSequenceInterval" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnionState" (
	elemental_charge TEXT
);

CREATE TABLE "AtomicBond" (
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	bond_order TEXT, 
	bond_type VARCHAR(11), 
	bond_length_in_angstroms FLOAT, 
	bond_angle FLOAT, 
	torsional_angle FLOAT, 
	PRIMARY KEY (id)
);

CREATE TABLE "BronstedAcid" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	acidity FLOAT, 
	hard_or_soft VARCHAR(10), 
	acid_form_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(acid_form_of) REFERENCES "AcidBase" (id)
);

CREATE TABLE "CationState" (
	elemental_charge TEXT
);

CREATE TABLE "ChargeState" (
	elemental_charge TEXT
);

CREATE TABLE "Charged" (
	elemental_charge TEXT
);

CREATE TABLE "ChemicalEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChemicalGroup" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChemicalMixture" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChemicalSalt" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	elemental_charge TEXT, 
	has_cationic_component TEXT, 
	has_anionic_component TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChiralityCenter" (
	owl_subclass_of TEXT
);

CREATE TABLE "DNASequenceInterval" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Electron" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "EntityWithAtomsEnumerated" (
	inchi_chemical_sublayer TEXT NOT NULL
);

CREATE TABLE "EntityWithChargeSpecified" (
	inchi_charge_sublayer TEXT
);

CREATE TABLE "EntityWithConnectivitySpecificied" (
	inchi_atom_connections_sublayer TEXT, 
	inchi_hydrogen_connections_sublayer TEXT
);

CREATE TABLE "EntityWithIsotopeSpecified" (
	inchi_isotopic_layer TEXT
);

CREATE TABLE "EntityWithStereochemistrySpecified" (
	inchi_stereochemical_double_bond_sublayer TEXT, 
	inchi_tetrahedral_stereochemical_sublayer TEXT, 
	inchi_stereochemical_type_sublayer TEXT
);

CREATE TABLE "ImpreciseChemicalMixture" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_proportional_parts TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "IsomeraseReaction" (
	id TEXT NOT NULL, 
	left_participants TEXT, 
	right_participants TEXT, 
	direction TEXT, 
	smarts_string TEXT, 
	is_diastereoselective TEXT, 
	is_stereo TEXT, 
	is_balanced TEXT, 
	is_transport TEXT, 
	is_fully_characterized TEXT, 
	reaction_center TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Location" (
	owl_subclass_of TEXT
);

CREATE TABLE "Measure" (
	owl_subclass_of TEXT
);

CREATE TABLE "Moiety" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularComplex" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularComponent" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularSubsequence" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Monomer" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Neutron" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Nucleon" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NucleotideSequenceInterval" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OwlClass" (
	owl_subclass_of TEXT
);

CREATE TABLE "PeriodicTableBlock" (
	type VARCHAR(7)
);

CREATE TABLE "PolyatomicEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "PolymerPart" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "PreciseChemicalMixture" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Proton" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Reaction" (
	id TEXT NOT NULL, 
	left_participants TEXT, 
	right_participants TEXT, 
	direction TEXT, 
	smarts_string TEXT, 
	is_diastereoselective TEXT, 
	is_stereo TEXT, 
	is_balanced TEXT, 
	is_transport TEXT, 
	is_fully_characterized TEXT, 
	reaction_center TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "RelationalChemicalEntity" (
	owl_subclass_of TEXT
);

CREATE TABLE "RNASequenceInterval" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SequenceInterval" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "StandardInchiObject" (
	inchi_version_string TEXT NOT NULL, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	inchi_atom_connections_sublayer TEXT, 
	inchi_hydrogen_connections_sublayer TEXT, 
	inchi_charge_sublayer TEXT, 
	inchi_proton_sublayer TEXT, 
	inchi_stereochemical_double_bond_sublayer TEXT, 
	inchi_tetrahedral_stereochemical_sublayer TEXT, 
	inchi_stereochemical_type_sublayer TEXT, 
	inchi_isotopic_layer TEXT
);

CREATE TABLE "Stereocenter" (
	owl_subclass_of TEXT
);

CREATE TABLE "SubatomicParticle" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SupramolecularPolymer" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Uncharged" (
	elemental_charge TEXT
);

CREATE TABLE "AcidBase_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_AcidBase" TEXT NOT NULL, 
	FOREIGN KEY("ref_AcidBase") REFERENCES "AcidBase" (id)
);

CREATE TABLE "AcidBase_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_AcidBase" TEXT NOT NULL, 
	FOREIGN KEY("ref_AcidBase") REFERENCES "AcidBase" (id)
);

CREATE TABLE "AcidBase_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_AcidBase" TEXT NOT NULL, 
	FOREIGN KEY("ref_AcidBase") REFERENCES "AcidBase" (id)
);

CREATE TABLE "AcidBase_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_AcidBase" TEXT NOT NULL, 
	FOREIGN KEY("ref_AcidBase") REFERENCES "AcidBase" (id)
);

CREATE TABLE "Atom" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "AtomIonicForm" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	elemental_charge TEXT, 
	elemental_change TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "AtomicBond_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_AtomicBond" TEXT NOT NULL, 
	FOREIGN KEY("ref_AtomicBond") REFERENCES "AtomicBond" (id)
);

CREATE TABLE "BronstedAcid_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_BronstedAcid" TEXT NOT NULL, 
	FOREIGN KEY("ref_BronstedAcid") REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "BronstedAcid_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_BronstedAcid" TEXT NOT NULL, 
	FOREIGN KEY("ref_BronstedAcid") REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "BronstedAcid_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_BronstedAcid" TEXT NOT NULL, 
	FOREIGN KEY("ref_BronstedAcid") REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "BronstedAcid_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_BronstedAcid" TEXT NOT NULL, 
	FOREIGN KEY("ref_BronstedAcid") REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "BronstedAcid_to_acid_form_of" (
	acid_form_of TEXT NOT NULL, 
	"ref_BronstedAcid" TEXT NOT NULL, 
	FOREIGN KEY("ref_BronstedAcid") REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "ChemicalElement" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	name TEXT, 
	has_part TEXT, 
	symbol TEXT, 
	in_periodic_table_group TEXT, 
	in_periodic_table_block TEXT, 
	boiling_point_in_celcius FLOAT, 
	melting_point_in_celcius FLOAT, 
	standard_atomic_weight FLOAT, 
	electron_configuration TEXT, 
	has_stereocenter TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "FullySpecifiedAtom" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	elemental_charge TEXT, 
	neutron_number TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "GroupingClass" (
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	owl_subclass_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "GroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "ImpreciseChemicalMixture_to_has_proportional_parts" (
	has_proportional_parts TEXT NOT NULL, 
	"ref_ImpreciseChemicalMixture" TEXT NOT NULL, 
	FOREIGN KEY("ref_ImpreciseChemicalMixture") REFERENCES "ImpreciseChemicalMixture" (id)
);

CREATE TABLE "IsomeraseReaction_to_left_participants" (
	left_participants TEXT NOT NULL, 
	"ref_IsomeraseReaction" TEXT NOT NULL, 
	FOREIGN KEY("ref_IsomeraseReaction") REFERENCES "IsomeraseReaction" (id)
);

CREATE TABLE "IsomeraseReaction_to_right_participants" (
	right_participants TEXT NOT NULL, 
	"ref_IsomeraseReaction" TEXT NOT NULL, 
	FOREIGN KEY("ref_IsomeraseReaction") REFERENCES "IsomeraseReaction" (id)
);

CREATE TABLE "Material" (
	has_part TEXT, 
	FOREIGN KEY(has_part) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "MolecularComponentGroupingClass" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MolecularComponentGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "MolecularComponent" (id)
);

CREATE TABLE "Nanostructure" (
	has_part TEXT, 
	has_morphological_category VARCHAR(12), 
	FOREIGN KEY(has_part) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "Nuclide" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "ProportionalPart" (
	owl_subclass_of TEXT, 
	has_role VARCHAR(19), 
	composed_of TEXT, 
	minimal_percentage FLOAT, 
	maximum_percentage FLOAT, 
	FOREIGN KEY(composed_of) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "Radionuclide" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "Reaction_to_left_participants" (
	left_participants TEXT NOT NULL, 
	"ref_Reaction" TEXT NOT NULL, 
	FOREIGN KEY("ref_Reaction") REFERENCES "Reaction" (id)
);

CREATE TABLE "Reaction_to_right_participants" (
	right_participants TEXT NOT NULL, 
	"ref_Reaction" TEXT NOT NULL, 
	FOREIGN KEY("ref_Reaction") REFERENCES "Reaction" (id)
);

CREATE TABLE "ReactionParticipant" (
	owl_subclass_of TEXT, 
	participant TEXT, 
	stoichiometry TEXT, 
	FOREIGN KEY(participant) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "UnchargedAtom" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	elemental_charge TEXT, 
	elemental_change TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "AtomAnion" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	elemental_change TEXT, 
	has_element TEXT, 
	elemental_charge TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "AtomCation" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	elemental_change TEXT, 
	has_element TEXT, 
	elemental_charge TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "AtomOccurrence" (
	owl_subclass_of TEXT, 
	occurrence_of TEXT NOT NULL, 
	valence TEXT, 
	oxidation_number TEXT, 
	formal_charge TEXT, 
	coordination_number TEXT, 
	FOREIGN KEY(occurrence_of) REFERENCES "Atom" (id)
);

CREATE TABLE "ChemicalElement_to_has_stereocenter" (
	has_stereocenter TEXT NOT NULL, 
	"ref_ChemicalElement" TEXT NOT NULL, 
	FOREIGN KEY("ref_ChemicalElement") REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "GroupingClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_GroupingClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_GroupingClass") REFERENCES "GroupingClass" (id)
);

CREATE TABLE "Isotope" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	has_element TEXT, 
	neutron_number TEXT, 
	isotope_of TEXT, 
	half_life TEXT, 
	decay_product TEXT, 
	decay_mode TEXT, 
	decay_energy TEXT, 
	mode_of_formation TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY(isotope_of) REFERENCES "Isotope" (id), 
	FOREIGN KEY(decay_product) REFERENCES "Isotope" (id)
);

CREATE TABLE "MolecularComponentGroupingClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_MolecularComponentGroupingClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularComponentGroupingClass") REFERENCES "MolecularComponentGroupingClass" (id)
);

CREATE TABLE "Molecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id)
);

CREATE TABLE "MonoatomicIon" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	elemental_charge TEXT, 
	elemental_change TEXT, 
	has_element TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "Allotrope" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	allotropic_analog_of TEXT NOT NULL, 
	has_bonding_structure TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(allotropic_analog_of) REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "Enantiomer" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	relative_configuration TEXT, 
	optical_configuration TEXT, 
	absolute_configuration TEXT, 
	enantiomer_form_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(enantiomer_form_of) REFERENCES "Molecule" (id)
);

CREATE TABLE "Ester" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	has_parent_alcohol TEXT, 
	has_parent_acid TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(has_parent_alcohol) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(has_parent_acid) REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "FunctionalGroup" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	is_substitutent_group_from TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(is_substitutent_group_from) REFERENCES "Molecule" (id)
);

CREATE TABLE "Glycan" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id)
);

CREATE TABLE "Isobar" (
	id TEXT NOT NULL, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	atomic_number TEXT, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	has_element TEXT, 
	nucleon_number TEXT, 
	isobar_of TEXT, 
	half_life TEXT, 
	decay_product TEXT, 
	decay_mode TEXT, 
	decay_energy TEXT, 
	mode_of_formation TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY(isobar_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(decay_product) REFERENCES "Isotope" (id)
);

CREATE TABLE "Macromolecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id)
);

CREATE TABLE "MolecularAnion" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "MolecularCation" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "MolecularSpecies" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id)
);

CREATE TABLE "Molecule_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Molecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_Molecule") REFERENCES "Molecule" (id)
);

CREATE TABLE "Molecule_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Molecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_Molecule") REFERENCES "Molecule" (id)
);

CREATE TABLE "Molecule_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Molecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_Molecule") REFERENCES "Molecule" (id)
);

CREATE TABLE "Molecule_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Molecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_Molecule") REFERENCES "Molecule" (id)
);

CREATE TABLE "MoleculeGroupingClass" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "MoleculePairwiseSimilarity" (
	owl_subclass_of TEXT, 
	left_molecule TEXT, 
	right_molecule TEXT, 
	score TEXT, 
	FOREIGN KEY(left_molecule) REFERENCES "Molecule" (id), 
	FOREIGN KEY(right_molecule) REFERENCES "Molecule" (id)
);

CREATE TABLE "NaturalProduct" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id)
);

CREATE TABLE "NonSpeciesMolecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id)
);

CREATE TABLE "Peptide" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id)
);

CREATE TABLE "PolyatomicIon" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "Protein" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id)
);

CREATE TABLE "SmallMolecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id)
);

CREATE TABLE "Stereoisomer" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id)
);

CREATE TABLE "TanimotoSimilarity" (
	owl_subclass_of TEXT, 
	left_molecule TEXT, 
	right_molecule TEXT, 
	score FLOAT, 
	FOREIGN KEY(left_molecule) REFERENCES "Molecule" (id), 
	FOREIGN KEY(right_molecule) REFERENCES "Molecule" (id)
);

CREATE TABLE "UnchargedMolecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	elemental_charge TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id)
);

CREATE TABLE "AcidAnionGroupingClass" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	name TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "AcidBaseConflationClass" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	has_physiological_base TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(has_physiological_base) REFERENCES "AcidBase" (id)
);

CREATE TABLE "Allotrope_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Allotrope" TEXT NOT NULL, 
	FOREIGN KEY("ref_Allotrope") REFERENCES "Allotrope" (id)
);

CREATE TABLE "Allotrope_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Allotrope" TEXT NOT NULL, 
	FOREIGN KEY("ref_Allotrope") REFERENCES "Allotrope" (id)
);

CREATE TABLE "Allotrope_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Allotrope" TEXT NOT NULL, 
	FOREIGN KEY("ref_Allotrope") REFERENCES "Allotrope" (id)
);

CREATE TABLE "Allotrope_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Allotrope" TEXT NOT NULL, 
	FOREIGN KEY("ref_Allotrope") REFERENCES "Allotrope" (id)
);

CREATE TABLE "AtomGroupingByPeriodicTableBlock" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	in_periodic_table_block TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Atom" (id)
);

CREATE TABLE "AtomGroupingByPeriodicTableGroup" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	in_periodic_table_group TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Atom" (id)
);

CREATE TABLE "AtomGroupingByPeriodicTablePlacement" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Atom" (id)
);

CREATE TABLE "AtomGroupingByProperty" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Atom" (id)
);

CREATE TABLE "AtomGroupingClass" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Atom" (id)
);

CREATE TABLE "ChemicalGroupingByCharge" (
	id TEXT NOT NULL, 
	classifies TEXT, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	has_charge_state TEXT, 
	charge_agnostic_entity TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(charge_agnostic_entity) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "ChemicalSaltByAnion" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	has_cationic_component TEXT, 
	classifies TEXT, 
	has_anionic_component TEXT, 
	name TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "ChemicalSalt" (id)
);

CREATE TABLE "ChemicalSaltByCation" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	has_anionic_component TEXT, 
	classifies TEXT, 
	has_cationic_component TEXT, 
	name TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "ChemicalSalt" (id)
);

CREATE TABLE "ChemicalSaltGroupingClass" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	has_anionic_component TEXT, 
	has_cationic_component TEXT, 
	name TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "ChemicalSalt" (id)
);

CREATE TABLE "Copolymer" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_submolecules TEXT, 
	polymer_of TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(polymer_of) REFERENCES "Macromolecule" (id), 
	FOREIGN KEY(has_part) REFERENCES "Macromolecule" (id)
);

CREATE TABLE "Enantiomer_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Enantiomer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Enantiomer") REFERENCES "Enantiomer" (id)
);

CREATE TABLE "Enantiomer_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Enantiomer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Enantiomer") REFERENCES "Enantiomer" (id)
);

CREATE TABLE "Enantiomer_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Enantiomer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Enantiomer") REFERENCES "Enantiomer" (id)
);

CREATE TABLE "Enantiomer_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Enantiomer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Enantiomer") REFERENCES "Enantiomer" (id)
);

CREATE TABLE "Ester_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Ester" TEXT NOT NULL, 
	FOREIGN KEY("ref_Ester") REFERENCES "Ester" (id)
);

CREATE TABLE "Ester_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Ester" TEXT NOT NULL, 
	FOREIGN KEY("ref_Ester") REFERENCES "Ester" (id)
);

CREATE TABLE "Ester_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Ester" TEXT NOT NULL, 
	FOREIGN KEY("ref_Ester") REFERENCES "Ester" (id)
);

CREATE TABLE "Ester_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Ester" TEXT NOT NULL, 
	FOREIGN KEY("ref_Ester") REFERENCES "Ester" (id)
);

CREATE TABLE "GeneralAcidBaseGroupingClass" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "GeneralizedMolecularStructureClass" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "Glycan_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Glycan" TEXT NOT NULL, 
	FOREIGN KEY("ref_Glycan") REFERENCES "Glycan" (id)
);

CREATE TABLE "Glycan_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Glycan" TEXT NOT NULL, 
	FOREIGN KEY("ref_Glycan") REFERENCES "Glycan" (id)
);

CREATE TABLE "Glycan_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Glycan" TEXT NOT NULL, 
	FOREIGN KEY("ref_Glycan") REFERENCES "Glycan" (id)
);

CREATE TABLE "Glycan_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Glycan" TEXT NOT NULL, 
	FOREIGN KEY("ref_Glycan") REFERENCES "Glycan" (id)
);

CREATE TABLE "GroupingClassForAcidsOrBases" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id), 
	FOREIGN KEY(conjugate_base_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(conjugate_acid_of) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "Macromolecule_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Macromolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_Macromolecule") REFERENCES "Macromolecule" (id)
);

CREATE TABLE "Macromolecule_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Macromolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_Macromolecule") REFERENCES "Macromolecule" (id)
);

CREATE TABLE "Macromolecule_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Macromolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_Macromolecule") REFERENCES "Macromolecule" (id)
);

CREATE TABLE "Macromolecule_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Macromolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_Macromolecule") REFERENCES "Macromolecule" (id)
);

CREATE TABLE "MolecularAnion_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_MolecularAnion" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularAnion") REFERENCES "MolecularAnion" (id)
);

CREATE TABLE "MolecularAnion_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_MolecularAnion" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularAnion") REFERENCES "MolecularAnion" (id)
);

CREATE TABLE "MolecularAnion_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_MolecularAnion" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularAnion") REFERENCES "MolecularAnion" (id)
);

CREATE TABLE "MolecularAnion_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_MolecularAnion" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularAnion") REFERENCES "MolecularAnion" (id)
);

CREATE TABLE "MolecularCation_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_MolecularCation" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularCation") REFERENCES "MolecularCation" (id)
);

CREATE TABLE "MolecularCation_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_MolecularCation" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularCation") REFERENCES "MolecularCation" (id)
);

CREATE TABLE "MolecularCation_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_MolecularCation" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularCation") REFERENCES "MolecularCation" (id)
);

CREATE TABLE "MolecularCation_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_MolecularCation" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularCation") REFERENCES "MolecularCation" (id)
);

CREATE TABLE "MolecularDerivativeGroupingClass" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	derivative_of TEXT, 
	name TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(derivative_of) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "MolecularSpecies_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_MolecularSpecies" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularSpecies") REFERENCES "MolecularSpecies" (id)
);

CREATE TABLE "MolecularSpecies_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_MolecularSpecies" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularSpecies") REFERENCES "MolecularSpecies" (id)
);

CREATE TABLE "MolecularSpecies_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_MolecularSpecies" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularSpecies") REFERENCES "MolecularSpecies" (id)
);

CREATE TABLE "MolecularSpecies_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_MolecularSpecies" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularSpecies") REFERENCES "MolecularSpecies" (id)
);

CREATE TABLE "MoleculeGroupingClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_MoleculeGroupingClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_MoleculeGroupingClass") REFERENCES "MoleculeGroupingClass" (id)
);

CREATE TABLE "MoleculeGroupingClassDefinedByAdditionOfAGroup" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	has_group TEXT, 
	derivative_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_group) REFERENCES "ChemicalGroup" (id), 
	FOREIGN KEY(derivative_of) REFERENCES "PolyatomicEntity" (id)
);

CREATE TABLE "MoleculeGroupingClassDefinedByComponents" (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subtype_of) REFERENCES "MoleculeGroupingClass" (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "MonomolecularPolymer" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_atoms TEXT, 
	is_organic TEXT, 
	has_part TEXT, 
	has_submolecules TEXT, 
	polymer_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_atoms) REFERENCES "Atom" (id), 
	FOREIGN KEY(has_submolecules) REFERENCES "Molecule" (id), 
	FOREIGN KEY(polymer_of) REFERENCES "Macromolecule" (id)
);

CREATE TABLE "NaturalProduct_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_NaturalProduct" TEXT NOT NULL, 
	FOREIGN KEY("ref_NaturalProduct") REFERENCES "NaturalProduct" (id)
);

CREATE TABLE "NaturalProduct_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_NaturalProduct" TEXT NOT NULL, 
	FOREIGN KEY("ref_NaturalProduct") REFERENCES "NaturalProduct" (id)
);

CREATE TABLE "NaturalProduct_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_NaturalProduct" TEXT NOT NULL, 
	FOREIGN KEY("ref_NaturalProduct") REFERENCES "NaturalProduct" (id)
);

CREATE TABLE "NaturalProduct_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_NaturalProduct" TEXT NOT NULL, 
	FOREIGN KEY("ref_NaturalProduct") REFERENCES "NaturalProduct" (id)
);

CREATE TABLE "NonSpeciesMolecule_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_NonSpeciesMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_NonSpeciesMolecule") REFERENCES "NonSpeciesMolecule" (id)
);

CREATE TABLE "NonSpeciesMolecule_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_NonSpeciesMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_NonSpeciesMolecule") REFERENCES "NonSpeciesMolecule" (id)
);

CREATE TABLE "NonSpeciesMolecule_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_NonSpeciesMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_NonSpeciesMolecule") REFERENCES "NonSpeciesMolecule" (id)
);

CREATE TABLE "NonSpeciesMolecule_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_NonSpeciesMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_NonSpeciesMolecule") REFERENCES "NonSpeciesMolecule" (id)
);

CREATE TABLE "Peptide_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Peptide" TEXT NOT NULL, 
	FOREIGN KEY("ref_Peptide") REFERENCES "Peptide" (id)
);

CREATE TABLE "Peptide_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Peptide" TEXT NOT NULL, 
	FOREIGN KEY("ref_Peptide") REFERENCES "Peptide" (id)
);

CREATE TABLE "Peptide_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Peptide" TEXT NOT NULL, 
	FOREIGN KEY("ref_Peptide") REFERENCES "Peptide" (id)
);

CREATE TABLE "Peptide_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Peptide" TEXT NOT NULL, 
	FOREIGN KEY("ref_Peptide") REFERENCES "Peptide" (id)
);

CREATE TABLE "PolyatomicIon_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_PolyatomicIon" TEXT NOT NULL, 
	FOREIGN KEY("ref_PolyatomicIon") REFERENCES "PolyatomicIon" (id)
);

CREATE TABLE "PolyatomicIon_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_PolyatomicIon" TEXT NOT NULL, 
	FOREIGN KEY("ref_PolyatomicIon") REFERENCES "PolyatomicIon" (id)
);

CREATE TABLE "PolyatomicIon_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_PolyatomicIon" TEXT NOT NULL, 
	FOREIGN KEY("ref_PolyatomicIon") REFERENCES "PolyatomicIon" (id)
);

CREATE TABLE "PolyatomicIon_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_PolyatomicIon" TEXT NOT NULL, 
	FOREIGN KEY("ref_PolyatomicIon") REFERENCES "PolyatomicIon" (id)
);

CREATE TABLE "Protein_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Protein" TEXT NOT NULL, 
	FOREIGN KEY("ref_Protein") REFERENCES "Protein" (id)
);

CREATE TABLE "Protein_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Protein" TEXT NOT NULL, 
	FOREIGN KEY("ref_Protein") REFERENCES "Protein" (id)
);

CREATE TABLE "Protein_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Protein" TEXT NOT NULL, 
	FOREIGN KEY("ref_Protein") REFERENCES "Protein" (id)
);

CREATE TABLE "Protein_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Protein" TEXT NOT NULL, 
	FOREIGN KEY("ref_Protein") REFERENCES "Protein" (id)
);

CREATE TABLE "RacemicMixture" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical TEXT, 
	has_characteristic TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT NOT NULL, 
	has_left_enantiomer TEXT NOT NULL, 
	has_right_enantiomer TEXT NOT NULL, 
	chirality_agnostic_form TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_left_enantiomer) REFERENCES "Enantiomer" (id), 
	FOREIGN KEY(has_right_enantiomer) REFERENCES "Enantiomer" (id), 
	FOREIGN KEY(chirality_agnostic_form) REFERENCES "Molecule" (id)
);

CREATE TABLE "SmallMolecule_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_SmallMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_SmallMolecule") REFERENCES "SmallMolecule" (id)
);

CREATE TABLE "SmallMolecule_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_SmallMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_SmallMolecule") REFERENCES "SmallMolecule" (id)
);

CREATE TABLE "SmallMolecule_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_SmallMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_SmallMolecule") REFERENCES "SmallMolecule" (id)
);

CREATE TABLE "SmallMolecule_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_SmallMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_SmallMolecule") REFERENCES "SmallMolecule" (id)
);

CREATE TABLE "Stereoisomer_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Stereoisomer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Stereoisomer") REFERENCES "Stereoisomer" (id)
);

CREATE TABLE "Stereoisomer_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Stereoisomer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Stereoisomer") REFERENCES "Stereoisomer" (id)
);

CREATE TABLE "Stereoisomer_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Stereoisomer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Stereoisomer") REFERENCES "Stereoisomer" (id)
);

CREATE TABLE "Stereoisomer_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Stereoisomer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Stereoisomer") REFERENCES "Stereoisomer" (id)
);

CREATE TABLE "UnchargedMolecule_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_UnchargedMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_UnchargedMolecule") REFERENCES "UnchargedMolecule" (id)
);

CREATE TABLE "UnchargedMolecule_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_UnchargedMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_UnchargedMolecule") REFERENCES "UnchargedMolecule" (id)
);

CREATE TABLE "UnchargedMolecule_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_UnchargedMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_UnchargedMolecule") REFERENCES "UnchargedMolecule" (id)
);

CREATE TABLE "UnchargedMolecule_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_UnchargedMolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_UnchargedMolecule") REFERENCES "UnchargedMolecule" (id)
);

CREATE TABLE "AcidAnionGroupingClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_AcidAnionGroupingClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_AcidAnionGroupingClass") REFERENCES "AcidAnionGroupingClass" (id)
);

CREATE TABLE "AcidBaseConflationClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_AcidBaseConflationClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_AcidBaseConflationClass") REFERENCES "AcidBaseConflationClass" (id)
);

CREATE TABLE "AtomGroupingByPeriodicTableBlock_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_AtomGroupingByPeriodicTableBlock" TEXT NOT NULL, 
	FOREIGN KEY("ref_AtomGroupingByPeriodicTableBlock") REFERENCES "AtomGroupingByPeriodicTableBlock" (id)
);

CREATE TABLE "AtomGroupingByPeriodicTableGroup_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_AtomGroupingByPeriodicTableGroup" TEXT NOT NULL, 
	FOREIGN KEY("ref_AtomGroupingByPeriodicTableGroup") REFERENCES "AtomGroupingByPeriodicTableGroup" (id)
);

CREATE TABLE "AtomGroupingByPeriodicTablePlacement_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_AtomGroupingByPeriodicTablePlacement" TEXT NOT NULL, 
	FOREIGN KEY("ref_AtomGroupingByPeriodicTablePlacement") REFERENCES "AtomGroupingByPeriodicTablePlacement" (id)
);

CREATE TABLE "AtomGroupingByProperty_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_AtomGroupingByProperty" TEXT NOT NULL, 
	FOREIGN KEY("ref_AtomGroupingByProperty") REFERENCES "AtomGroupingByProperty" (id)
);

CREATE TABLE "AtomGroupingClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_AtomGroupingClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_AtomGroupingClass") REFERENCES "AtomGroupingClass" (id)
);

CREATE TABLE "ChemicalGroupingByCharge_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_ChemicalGroupingByCharge" TEXT NOT NULL, 
	FOREIGN KEY("ref_ChemicalGroupingByCharge") REFERENCES "ChemicalGroupingByCharge" (id)
);

CREATE TABLE "ChemicalSaltByAnion_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_ChemicalSaltByAnion" TEXT NOT NULL, 
	FOREIGN KEY("ref_ChemicalSaltByAnion") REFERENCES "ChemicalSaltByAnion" (id)
);

CREATE TABLE "ChemicalSaltByCation_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_ChemicalSaltByCation" TEXT NOT NULL, 
	FOREIGN KEY("ref_ChemicalSaltByCation") REFERENCES "ChemicalSaltByCation" (id)
);

CREATE TABLE "ChemicalSaltGroupingClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_ChemicalSaltGroupingClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_ChemicalSaltGroupingClass") REFERENCES "ChemicalSaltGroupingClass" (id)
);

CREATE TABLE "Copolymer_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_Copolymer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Copolymer") REFERENCES "Copolymer" (id)
);

CREATE TABLE "Copolymer_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_Copolymer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Copolymer") REFERENCES "Copolymer" (id)
);

CREATE TABLE "Copolymer_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_Copolymer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Copolymer") REFERENCES "Copolymer" (id)
);

CREATE TABLE "Copolymer_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_Copolymer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Copolymer") REFERENCES "Copolymer" (id)
);

CREATE TABLE "Copolymer_to_has_part" (
	has_part TEXT NOT NULL, 
	"ref_Copolymer" TEXT NOT NULL, 
	FOREIGN KEY("ref_Copolymer") REFERENCES "Copolymer" (id)
);

CREATE TABLE "GeneralAcidBaseGroupingClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_GeneralAcidBaseGroupingClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_GeneralAcidBaseGroupingClass") REFERENCES "GeneralAcidBaseGroupingClass" (id)
);

CREATE TABLE "GeneralizedMolecularStructureClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_GeneralizedMolecularStructureClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_GeneralizedMolecularStructureClass") REFERENCES "GeneralizedMolecularStructureClass" (id)
);

CREATE TABLE "GroupingClassForAcidsOrBases_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_GroupingClassForAcidsOrBases" TEXT NOT NULL, 
	FOREIGN KEY("ref_GroupingClassForAcidsOrBases") REFERENCES "GroupingClassForAcidsOrBases" (id)
);

CREATE TABLE "MolecularDerivativeGroupingClass_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_MolecularDerivativeGroupingClass" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularDerivativeGroupingClass") REFERENCES "MolecularDerivativeGroupingClass" (id)
);

CREATE TABLE "MoleculeGroupingClassDefinedByAdditionOfAGroup_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_MoleculeGroupingClassDefinedByAdditionOfAGroup" TEXT NOT NULL, 
	FOREIGN KEY("ref_MoleculeGroupingClassDefinedByAdditionOfAGroup") REFERENCES "MoleculeGroupingClassDefinedByAdditionOfAGroup" (id)
);

CREATE TABLE "MoleculeGroupingClassDefinedByAdditionOfAGroup_to_has_group" (
	has_group TEXT NOT NULL, 
	"ref_MoleculeGroupingClassDefinedByAdditionOfAGroup" TEXT NOT NULL, 
	FOREIGN KEY("ref_MoleculeGroupingClassDefinedByAdditionOfAGroup") REFERENCES "MoleculeGroupingClassDefinedByAdditionOfAGroup" (id)
);

CREATE TABLE "MoleculeGroupingClassDefinedByComponents_to_subtype_of" (
	subtype_of TEXT NOT NULL, 
	"ref_MoleculeGroupingClassDefinedByComponents" TEXT NOT NULL, 
	FOREIGN KEY("ref_MoleculeGroupingClassDefinedByComponents") REFERENCES "MoleculeGroupingClassDefinedByComponents" (id)
);

CREATE TABLE "MonomolecularPolymer_to_has_atom_occurrences" (
	has_atom_occurrences TEXT NOT NULL, 
	"ref_MonomolecularPolymer" TEXT NOT NULL, 
	FOREIGN KEY("ref_MonomolecularPolymer") REFERENCES "MonomolecularPolymer" (id)
);

CREATE TABLE "MonomolecularPolymer_to_has_bonds" (
	has_bonds TEXT NOT NULL, 
	"ref_MonomolecularPolymer" TEXT NOT NULL, 
	FOREIGN KEY("ref_MonomolecularPolymer") REFERENCES "MonomolecularPolymer" (id)
);

CREATE TABLE "MonomolecularPolymer_to_has_atoms" (
	has_atoms TEXT NOT NULL, 
	"ref_MonomolecularPolymer" TEXT NOT NULL, 
	FOREIGN KEY("ref_MonomolecularPolymer") REFERENCES "MonomolecularPolymer" (id)
);

CREATE TABLE "MonomolecularPolymer_to_has_submolecules" (
	has_submolecules TEXT NOT NULL, 
	"ref_MonomolecularPolymer" TEXT NOT NULL, 
	FOREIGN KEY("ref_MonomolecularPolymer") REFERENCES "MonomolecularPolymer" (id)
);

