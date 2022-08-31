

CREATE TABLE acid_anion_grouping_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE amino_acid_sequence_interval (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE atom_grouping_by_periodic_table_block (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	in_periodic_table_block TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE atom_grouping_by_periodic_table_group (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	in_periodic_table_group INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE atom_grouping_by_property (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE atom_grouping_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE atom_occurrence (
	owl_subclass_of TEXT, 
	occurrence_of TEXT NOT NULL, 
	valence INTEGER, 
	oxidation_number INTEGER, 
	formal_charge INTEGER, 
	coordination_number INTEGER, 
	PRIMARY KEY (owl_subclass_of, occurrence_of, valence, oxidation_number, formal_charge, coordination_number)
);

CREATE TABLE atomic_bond (
	owl_subclass_of TEXT, 
	has_atom_occurrences TEXT, 
	bond_order INTEGER, 
	bond_type VARCHAR(11), 
	bond_length_in_angstroms FLOAT, 
	bond_angle FLOAT, 
	torsional_angle FLOAT, 
	PRIMARY KEY (owl_subclass_of, has_atom_occurrences, bond_order, bond_type, bond_length_in_angstroms, bond_angle, torsional_angle)
);

CREATE TABLE "Bronsted_acid" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	acidity FLOAT, 
	hard_or_soft VARCHAR(10), 
	acid_form_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE chemical_grouping_by_charge (
	id TEXT NOT NULL, 
	classifies TEXT, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	has_charge_state TEXT, 
	charge_agnostic_entity TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE chemical_role (
	owl_subclass_of TEXT, 
	PRIMARY KEY (owl_subclass_of)
);

CREATE TABLE chemical_salt (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	elemental_charge INTEGER, 
	has_cationic_component TEXT, 
	has_anionic_component TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE chirality_center (
	owl_subclass_of TEXT, 
	PRIMARY KEY (owl_subclass_of)
);

CREATE TABLE copolymer (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_repeat_unit TEXT, 
	is_branched BOOLEAN, 
	polymer_architecture_type TEXT, 
	polymer_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DNA_sequence_interval" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE enantiomer (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	relative_configuration TEXT, 
	optical_configuration TEXT, 
	absolute_configuration TEXT, 
	enantiomer_form_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE functional_group (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	is_substitutent_group_from TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE general_acid_base_grouping_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE generalized_molecular_structure_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE glycan (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE imprecise_chemical_mixture (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_mixfile_location TEXT, 
	has_minchi_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE isomerase_reaction (
	has_rinchi_representation TEXT NOT NULL, 
	has_reaction_smiles_representation TEXT, 
	left_participants TEXT, 
	right_participants TEXT, 
	direction TEXT, 
	smarts_string TEXT, 
	is_diastereoselective BOOLEAN, 
	is_stereo BOOLEAN, 
	is_balanced BOOLEAN, 
	is_transport BOOLEAN, 
	is_fully_characterized BOOLEAN, 
	reaction_center TEXT, 
	description TEXT, 
	PRIMARY KEY (has_rinchi_representation, has_reaction_smiles_representation, left_participants, right_participants, direction, smarts_string, is_diastereoselective, is_stereo, is_balanced, is_transport, is_fully_characterized, reaction_center, description)
);

CREATE TABLE lipid (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE location (
	owl_subclass_of TEXT, 
	PRIMARY KEY (owl_subclass_of)
);

CREATE TABLE macromolecule (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE material (
	has_part TEXT, 
	PRIMARY KEY (has_part)
);

CREATE TABLE material_grouping_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE mineral (
	has_part TEXT, 
	PRIMARY KEY (has_part)
);

CREATE TABLE moiety (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecular_anion (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE molecular_cation (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE molecular_complex (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecular_component (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecular_derivative_grouping_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	derivative_of TEXT, 
	name TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecular_species (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecular_subsequence (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecule_grouping_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecule_grouping_class_defined_by_addition_of_a_group (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	derivative_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecule_grouping_class_defined_by_components (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecule_pairwise_similarity (
	owl_subclass_of TEXT, 
	left_molecule TEXT, 
	right_molecule TEXT, 
	score TEXT, 
	PRIMARY KEY (owl_subclass_of, left_molecule, right_molecule, score)
);

CREATE TABLE monomer (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE monomeric_polymeric_grouping_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	has_repeat_unit TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE nanostructure (
	has_part TEXT, 
	has_morphological_category VARCHAR(12), 
	PRIMARY KEY (has_part, has_morphological_category)
);

CREATE TABLE natural_product (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE non_species_molecule (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE nucleotide_sequence_interval (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE peptide (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE periodic_table_block (
	type VARCHAR(7), 
	PRIMARY KEY (type)
);

CREATE TABLE polyatomic_ion (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE polymer_part (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE polymer_repeat_unit (
	owl_subclass_of TEXT, 
	repetition_of TEXT, 
	degree_of_polymerization INTEGER, 
	mass FLOAT, 
	PRIMARY KEY (owl_subclass_of, repetition_of, degree_of_polymerization, mass)
);

CREATE TABLE protein (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE reaction (
	has_rinchi_representation TEXT NOT NULL, 
	has_reaction_smiles_representation TEXT, 
	left_participants TEXT, 
	right_participants TEXT, 
	direction TEXT, 
	smarts_string TEXT, 
	is_diastereoselective BOOLEAN, 
	is_stereo BOOLEAN, 
	is_balanced BOOLEAN, 
	is_transport BOOLEAN, 
	is_fully_characterized BOOLEAN, 
	reaction_center TEXT, 
	description TEXT, 
	PRIMARY KEY (has_rinchi_representation, has_reaction_smiles_representation, left_participants, right_participants, direction, smarts_string, is_diastereoselective, is_stereo, is_balanced, is_transport, is_fully_characterized, reaction_center, description)
);

CREATE TABLE reaction_grouping_class (
	classifies TEXT, 
	PRIMARY KEY (classifies)
);

CREATE TABLE reaction_participant (
	owl_subclass_of TEXT, 
	participant TEXT, 
	stoichiometry INTEGER, 
	PRIMARY KEY (owl_subclass_of, participant, stoichiometry)
);

CREATE TABLE "RNA_sequence_interval" (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE similarity (
	owl_subclass_of TEXT, 
	PRIMARY KEY (owl_subclass_of)
);

CREATE TABLE small_molecule (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE standard_inchi_object (
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
	PRIMARY KEY (inchi_version_string, inchi_chemical_sublayer, inchi_atom_connections_sublayer, inchi_hydrogen_connections_sublayer, inchi_charge_sublayer, inchi_proton_sublayer, inchi_stereochemical_double_bond_sublayer, inchi_tetrahedral_stereochemical_sublayer, inchi_stereochemical_type_sublayer, inchi_isotopic_layer)
);

CREATE TABLE stereoisomer (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE subatomic_particle (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE tanimoto_similarity (
	owl_subclass_of TEXT, 
	left_molecule TEXT, 
	right_molecule TEXT, 
	score FLOAT, 
	PRIMARY KEY (owl_subclass_of, left_molecule, right_molecule, score)
);

CREATE TABLE uncharged_molecule (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE acid_base (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge INTEGER, 
	has_acid_form TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_acid_form) REFERENCES "Bronsted_acid" (id)
);

CREATE TABLE chemical_element (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	name TEXT, 
	has_part TEXT, 
	symbol TEXT, 
	in_periodic_table_group INTEGER, 
	in_periodic_table_block TEXT, 
	boiling_point_in_celcius FLOAT, 
	melting_point_in_celcius FLOAT, 
	standard_atomic_weight FLOAT, 
	mass FLOAT, 
	monoisotopic_mass FLOAT, 
	electron_configuration TEXT, 
	has_physiologically_stable_form TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id)
);

CREATE TABLE chemical_group (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	molecule_grouping_class_defined_by_addition_of_a_group_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(molecule_grouping_class_defined_by_addition_of_a_group_id) REFERENCES molecule_grouping_class_defined_by_addition_of_a_group (id)
);

CREATE TABLE chemical_salt_by_anion (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	has_cationic_component TEXT, 
	classifies TEXT, 
	has_anionic_component TEXT, 
	name TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES chemical_salt (id)
);

CREATE TABLE chemical_salt_by_cation (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	has_anionic_component TEXT, 
	classifies TEXT, 
	has_cationic_component TEXT, 
	name TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES chemical_salt (id)
);

CREATE TABLE chemical_salt_grouping_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	has_anionic_component TEXT, 
	has_cationic_component TEXT, 
	name TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES chemical_salt (id)
);

CREATE TABLE ester (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_parent_alcohol TEXT, 
	has_parent_acid TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_parent_acid) REFERENCES "Bronsted_acid" (id)
);

CREATE TABLE fully_specified_atom (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	elemental_charge INTEGER, 
	neutron_number INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id)
);

CREATE TABLE homopolymer (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_repeat_unit TEXT, 
	is_branched BOOLEAN, 
	polymer_architecture_type TEXT, 
	polymer_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polymer_of) REFERENCES macromolecule (id)
);

CREATE TABLE molecular_component_grouping_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	classifies TEXT, 
	molecular_component_grouping_class_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES molecular_component (id), 
	FOREIGN KEY(molecular_component_grouping_class_id) REFERENCES molecular_component_grouping_class (id)
);

CREATE TABLE monomolecular_polymer (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	polymer_of TEXT, 
	has_repeat_unit TEXT, 
	is_branched BOOLEAN, 
	polymer_architecture_type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polymer_of) REFERENCES macromolecule (id)
);

CREATE TABLE nuclide (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id)
);

CREATE TABLE proportional_part (
	owl_subclass_of TEXT, 
	has_role VARCHAR(19), 
	composed_of TEXT, 
	minimal_percentage FLOAT, 
	maximum_percentage FLOAT, 
	imprecise_chemical_mixture_id TEXT, 
	PRIMARY KEY (owl_subclass_of, has_role, composed_of, minimal_percentage, maximum_percentage, imprecise_chemical_mixture_id), 
	FOREIGN KEY(imprecise_chemical_mixture_id) REFERENCES imprecise_chemical_mixture (id)
);

CREATE TABLE racemic_mixture (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_left_enantiomer TEXT NOT NULL, 
	has_right_enantiomer TEXT NOT NULL, 
	chirality_agnostic_form TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_left_enantiomer) REFERENCES enantiomer (id), 
	FOREIGN KEY(has_right_enantiomer) REFERENCES enantiomer (id)
);

CREATE TABLE radionuclide (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id)
);

CREATE TABLE supramolecular_polymer (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	polymer_of TEXT, 
	has_repeat_unit TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polymer_of) REFERENCES macromolecule (id)
);

CREATE TABLE uncharged_atom (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id)
);

CREATE TABLE "Bronsted_acid_has_submolecules" (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES "Bronsted_acid" (id)
);

CREATE TABLE "Bronsted_acid_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Bronsted_acid" (id)
);

CREATE TABLE copolymer_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES copolymer (id)
);

CREATE TABLE copolymer_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES copolymer (id)
);

CREATE TABLE enantiomer_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES enantiomer (id)
);

CREATE TABLE enantiomer_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES enantiomer (id)
);

CREATE TABLE glycan_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES glycan (id)
);

CREATE TABLE glycan_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES glycan (id)
);

CREATE TABLE lipid_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES lipid (id)
);

CREATE TABLE lipid_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES lipid (id)
);

CREATE TABLE macromolecule_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES macromolecule (id)
);

CREATE TABLE macromolecule_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES macromolecule (id)
);

CREATE TABLE material_grouping_class_subtype_of (
	backref_id TEXT, 
	subtype_of TEXT, 
	PRIMARY KEY (backref_id, subtype_of), 
	FOREIGN KEY(backref_id) REFERENCES material_grouping_class (id)
);

CREATE TABLE molecular_anion_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES molecular_anion (id)
);

CREATE TABLE molecular_anion_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES molecular_anion (id)
);

CREATE TABLE molecular_cation_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES molecular_cation (id)
);

CREATE TABLE molecular_cation_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES molecular_cation (id)
);

CREATE TABLE molecular_species_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES molecular_species (id)
);

CREATE TABLE molecular_species_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES molecular_species (id)
);

CREATE TABLE natural_product_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES natural_product (id)
);

CREATE TABLE natural_product_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES natural_product (id)
);

CREATE TABLE non_species_molecule_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES non_species_molecule (id)
);

CREATE TABLE non_species_molecule_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES non_species_molecule (id)
);

CREATE TABLE peptide_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES peptide (id)
);

CREATE TABLE peptide_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES peptide (id)
);

CREATE TABLE polyatomic_ion_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES polyatomic_ion (id)
);

CREATE TABLE polyatomic_ion_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES polyatomic_ion (id)
);

CREATE TABLE protein_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES protein (id)
);

CREATE TABLE protein_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES protein (id)
);

CREATE TABLE small_molecule_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES small_molecule (id)
);

CREATE TABLE small_molecule_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES small_molecule (id)
);

CREATE TABLE stereoisomer_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES stereoisomer (id)
);

CREATE TABLE stereoisomer_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES stereoisomer (id)
);

CREATE TABLE uncharged_molecule_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES uncharged_molecule (id)
);

CREATE TABLE uncharged_molecule_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES uncharged_molecule (id)
);

CREATE TABLE acid_base_conflation_class (
	id TEXT NOT NULL, 
	owl_subclass_of TEXT, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	has_physiological_base TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_physiological_base) REFERENCES acid_base (id)
);

CREATE TABLE allotrope (
	id TEXT NOT NULL, 
	name TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	allotropic_analog_of TEXT NOT NULL, 
	has_bonding_structure TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(allotropic_analog_of) REFERENCES chemical_element (id)
);

CREATE TABLE atom_anion (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	has_element TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id), 
	FOREIGN KEY(has_element) REFERENCES chemical_element (id)
);

CREATE TABLE atom_cation (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	has_element TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id), 
	FOREIGN KEY(has_element) REFERENCES chemical_element (id)
);

CREATE TABLE isotope (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	has_element TEXT, 
	neutron_number INTEGER, 
	isotope_of TEXT, 
	half_life INTEGER, 
	decay_product TEXT, 
	decay_mode TEXT, 
	decay_energy TEXT, 
	mode_of_formation TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id), 
	FOREIGN KEY(has_element) REFERENCES chemical_element (id), 
	FOREIGN KEY(isotope_of) REFERENCES isotope (id), 
	FOREIGN KEY(decay_product) REFERENCES isotope (id)
);

CREATE TABLE monoatomic_ion (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	elemental_charge INTEGER, 
	has_element TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id), 
	FOREIGN KEY(has_element) REFERENCES chemical_element (id)
);

CREATE TABLE stereocenter (
	owl_subclass_of TEXT, 
	chemical_element_id TEXT, 
	PRIMARY KEY (owl_subclass_of, chemical_element_id), 
	FOREIGN KEY(chemical_element_id) REFERENCES chemical_element (id)
);

CREATE TABLE acid_base_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES acid_base (id)
);

CREATE TABLE acid_base_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES acid_base (id)
);

CREATE TABLE ester_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES ester (id)
);

CREATE TABLE ester_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES ester (id)
);

CREATE TABLE homopolymer_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES homopolymer (id)
);

CREATE TABLE homopolymer_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES homopolymer (id)
);

CREATE TABLE monomolecular_polymer_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES monomolecular_polymer (id)
);

CREATE TABLE monomolecular_polymer_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES monomolecular_polymer (id)
);

CREATE TABLE isobar (
	id TEXT NOT NULL, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	has_element TEXT, 
	nucleon_number INTEGER, 
	isobar_of TEXT, 
	half_life INTEGER, 
	decay_product TEXT, 
	decay_mode TEXT, 
	decay_energy TEXT, 
	mode_of_formation TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES subatomic_particle (id), 
	FOREIGN KEY(has_element) REFERENCES chemical_element (id), 
	FOREIGN KEY(decay_product) REFERENCES isotope (id)
);

CREATE TABLE allotrope_has_submolecules (
	backref_id TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (backref_id, has_submolecules), 
	FOREIGN KEY(backref_id) REFERENCES allotrope (id)
);

CREATE TABLE allotrope_has_atoms (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES allotrope (id)
);
