

CREATE TABLE "AminoAcidSequenceInterval" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AtomGroupingByPeriodicTableBlock" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	in_periodic_table_block VARCHAR(7), 
	PRIMARY KEY (id)
);

CREATE TABLE "AtomGroupingByPeriodicTableGroup" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	in_periodic_table_group INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE "AtomGroupingByProperty" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AtomGroupingClass" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AtomOccurrence" (
	owl_subclass_of TEXT, 
	name TEXT NOT NULL, 
	occurrence_of TEXT NOT NULL, 
	valence INTEGER, 
	oxidation_number INTEGER, 
	formal_charge INTEGER, 
	coordination_number INTEGER, 
	PRIMARY KEY (name)
);

CREATE TABLE "BronstedAcid" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	acidity FLOAT, 
	hard_or_soft VARCHAR(10), 
	acid_form_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChemicalGroupingByCharge" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	classifies TEXT, 
	subtype_of TEXT, 
	has_charge_state TEXT, 
	charge_agnostic_entity TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChemicalRole" (
	owl_subclass_of TEXT, 
	PRIMARY KEY (owl_subclass_of)
);

CREATE TABLE "ChemicalSalt" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	elemental_charge INTEGER, 
	has_cationic_component TEXT, 
	has_anionic_component TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChemicalSimilarity" (
	owl_subclass_of TEXT, 
	PRIMARY KEY (owl_subclass_of)
);

CREATE TABLE "Collection" (
	entities TEXT, 
	PRIMARY KEY (entities)
);

CREATE TABLE "Copolymer" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_submolecules TEXT, 
	has_repeat_unit TEXT, 
	is_branched BOOLEAN, 
	polymer_architecture_type TEXT, 
	polymer_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DNASequenceInterval" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Glycan" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ImpreciseChemicalMixture" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_mixfile_location TEXT, 
	has_minchi_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "IsomeraseReaction" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_rinchi_representation TEXT, 
	has_reaction_smiles_representation TEXT, 
	reaction_rate_coefficient FLOAT, 
	reaction_rate FLOAT, 
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
	PRIMARY KEY (id)
);

CREATE TABLE "Lipid" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Macromolecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Material" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_repeat_unit TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Mineral" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_repeat_unit TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Moiety" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularAnion" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularCation" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularComplex" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularComponent" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularSpecies" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularSubsequence" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Molecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Monomer" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Nanomaterial" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_repeat_unit TEXT, 
	has_part TEXT, 
	has_morphological_category VARCHAR(12), 
	PRIMARY KEY (id)
);

CREATE TABLE "NaturalProduct" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NonSpeciesMolecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NucleotideSequenceInterval" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Peptide" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PolyatomicIon" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE "PolymerPart" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Protein" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_submolecules TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Reaction" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	has_rinchi_representation TEXT, 
	has_reaction_smiles_representation TEXT, 
	reaction_rate_coefficient FLOAT, 
	reaction_rate FLOAT, 
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
	PRIMARY KEY (id)
);

CREATE TABLE "ReactionParticipant" (
	owl_subclass_of TEXT, 
	participant TEXT, 
	stoichiometry INTEGER, 
	PRIMARY KEY (owl_subclass_of, participant, stoichiometry)
);

CREATE TABLE "RNASequenceInterval" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_sequence_representation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SmallMolecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "StandardInchiObject" (
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

CREATE TABLE "Stereoisomer" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SubatomicParticle" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subatomic_particle_type VARCHAR(20), 
	PRIMARY KEY (id)
);

CREATE TABLE "UnchargedMolecule" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE "AcidAnionGroupingClass" (
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	name TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "AcidBase" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	elemental_charge INTEGER, 
	has_acid_form TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_acid_form) REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "AtomicBond" (
	owl_subclass_of TEXT, 
	subject TEXT, 
	object TEXT, 
	bond_type VARCHAR(14), 
	bond_order INTEGER, 
	bond_length FLOAT, 
	bond_energy FLOAT, 
	bond_length_in_angstroms FLOAT, 
	bond_angle FLOAT, 
	torsional_angle FLOAT, 
	PRIMARY KEY (owl_subclass_of, subject, object, bond_type, bond_order, bond_length, bond_energy, bond_length_in_angstroms, bond_angle, torsional_angle), 
	FOREIGN KEY(subject) REFERENCES "AtomOccurrence" (name), 
	FOREIGN KEY(object) REFERENCES "AtomOccurrence" (name)
);

CREATE TABLE "ChemicalElement" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	name TEXT, 
	has_nuclear_parts TEXT, 
	has_part TEXT, 
	symbol TEXT, 
	in_periodic_table_group INTEGER, 
	in_periodic_table_block VARCHAR(7), 
	boiling_point_in_celcius FLOAT, 
	melting_point_in_celcius FLOAT, 
	standard_atomic_weight FLOAT, 
	mass FLOAT, 
	monoisotopic_mass FLOAT, 
	electron_configuration TEXT, 
	has_physiologically_stable_form TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "ChemicalSaltByAnion" (
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	has_cationic_component TEXT, 
	classifies TEXT, 
	has_anionic_component TEXT, 
	name TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "ChemicalSalt" (id)
);

CREATE TABLE "ChemicalSaltByCation" (
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	has_anionic_component TEXT, 
	classifies TEXT, 
	has_cationic_component TEXT, 
	name TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "ChemicalSalt" (id)
);

CREATE TABLE "ChemicalSaltGroupingClass" (
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	has_anionic_component TEXT, 
	has_cationic_component TEXT, 
	name TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "ChemicalSalt" (id)
);

CREATE TABLE "Enantiomer" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	relative_configuration TEXT, 
	optical_configuration TEXT, 
	absolute_configuration TEXT, 
	enantiomer_form_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(enantiomer_form_of) REFERENCES "Molecule" (id)
);

CREATE TABLE "Ester" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_parent_alcohol TEXT, 
	has_parent_acid TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_parent_acid) REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "FullySpecifiedAtom" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_nuclear_parts TEXT, 
	has_part TEXT, 
	elemental_charge INTEGER, 
	neutron_number INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "FunctionalGroup" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	is_substitutent_group_from TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(is_substitutent_group_from) REFERENCES "Molecule" (id)
);

CREATE TABLE "GeneralAcidBaseGroupingClass" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "GeneralizedMolecularStructureClass" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "Homopolymer" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_submolecules TEXT, 
	has_repeat_unit TEXT, 
	is_branched BOOLEAN, 
	polymer_architecture_type TEXT, 
	polymer_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polymer_of) REFERENCES "Macromolecule" (id)
);

CREATE TABLE "MaterialGroupingClass" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_subclass_of TEXT, 
	classifies TEXT, 
	"MaterialGroupingClass_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Material" (id), 
	FOREIGN KEY("MaterialGroupingClass_id") REFERENCES "MaterialGroupingClass" (id)
);

CREATE TABLE "MolecularComponentGroupingClass" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	classifies TEXT, 
	"MolecularComponentGroupingClass_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "MolecularComponent" (id), 
	FOREIGN KEY("MolecularComponentGroupingClass_id") REFERENCES "MolecularComponentGroupingClass" (id)
);

CREATE TABLE "MolecularDerivativeGroupingClass" (
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	derivative_of TEXT, 
	name TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "MoleculeGroupingClass" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "MoleculeGroupingClassDefinedByAdditionOfAGroup" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	derivative_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "MoleculeGroupingClassDefinedByComponents" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	has_part TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "MoleculePairwiseSimilarity" (
	owl_subclass_of TEXT, 
	left_molecule TEXT, 
	right_molecule TEXT, 
	score FLOAT, 
	PRIMARY KEY (owl_subclass_of, left_molecule, right_molecule, score), 
	FOREIGN KEY(left_molecule) REFERENCES "Molecule" (id), 
	FOREIGN KEY(right_molecule) REFERENCES "Molecule" (id)
);

CREATE TABLE "MonomericPolymericGroupingClass" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	has_repeat_unit TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id)
);

CREATE TABLE "MonomolecularPolymer" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	has_submolecules TEXT, 
	polymer_of TEXT, 
	has_repeat_unit TEXT, 
	is_branched BOOLEAN, 
	polymer_architecture_type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polymer_of) REFERENCES "Macromolecule" (id)
);

CREATE TABLE "Nuclide" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_nuclear_parts TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "PolymerRepeatUnit" (
	owl_subclass_of TEXT, 
	repetition_of TEXT, 
	degree_of_polymerization INTEGER, 
	mass FLOAT, 
	PRIMARY KEY (owl_subclass_of, repetition_of, degree_of_polymerization, mass), 
	FOREIGN KEY(repetition_of) REFERENCES "Molecule" (id)
);

CREATE TABLE "ProportionalPart" (
	owl_subclass_of TEXT, 
	has_role VARCHAR(19), 
	composed_of TEXT, 
	minimal_percentage FLOAT, 
	maximum_percentage FLOAT, 
	"ImpreciseChemicalMixture_id" TEXT, 
	PRIMARY KEY (owl_subclass_of, has_role, composed_of, minimal_percentage, maximum_percentage, "ImpreciseChemicalMixture_id"), 
	FOREIGN KEY("ImpreciseChemicalMixture_id") REFERENCES "ImpreciseChemicalMixture" (id)
);

CREATE TABLE "Radionuclide" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_nuclear_parts TEXT, 
	has_part TEXT, 
	energy_level TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "ReactionGroupingClass" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_subclass_of TEXT, 
	classifies TEXT, 
	"ReactionGroupingClass_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Reaction" (id), 
	FOREIGN KEY("ReactionGroupingClass_id") REFERENCES "ReactionGroupingClass" (id)
);

CREATE TABLE "SubatomicParticleOccurrence" (
	owl_subclass_of TEXT, 
	occurrence_of TEXT NOT NULL, 
	"Count" INTEGER, 
	PRIMARY KEY (owl_subclass_of, occurrence_of, "Count"), 
	FOREIGN KEY(occurrence_of) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "SupramolecularPolymer" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	polymer_of TEXT, 
	has_repeat_unit TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polymer_of) REFERENCES "Macromolecule" (id)
);

CREATE TABLE "TanimotoSimilarity" (
	owl_subclass_of TEXT, 
	left_molecule TEXT, 
	right_molecule TEXT, 
	score FLOAT, 
	PRIMARY KEY (owl_subclass_of, left_molecule, right_molecule, score), 
	FOREIGN KEY(left_molecule) REFERENCES "Molecule" (id), 
	FOREIGN KEY(right_molecule) REFERENCES "Molecule" (id)
);

CREATE TABLE "UnchargedAtom" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_nuclear_parts TEXT, 
	has_part TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id)
);

CREATE TABLE "AminoAcidSequenceInterval_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "AminoAcidSequenceInterval" (id)
);

CREATE TABLE "BronstedAcid_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "BronstedAcid_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "BronstedAcid" (id)
);

CREATE TABLE "ChemicalSalt_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "ChemicalSalt" (id)
);

CREATE TABLE "Copolymer_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Copolymer" (id)
);

CREATE TABLE "Copolymer_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Copolymer" (id)
);

CREATE TABLE "DNASequenceInterval_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "DNASequenceInterval" (id)
);

CREATE TABLE "Glycan_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Glycan" (id)
);

CREATE TABLE "Glycan_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Glycan" (id)
);

CREATE TABLE "ImpreciseChemicalMixture_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "ImpreciseChemicalMixture" (id)
);

CREATE TABLE "Lipid_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Lipid" (id)
);

CREATE TABLE "Lipid_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Lipid" (id)
);

CREATE TABLE "Macromolecule_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Macromolecule" (id)
);

CREATE TABLE "Macromolecule_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Macromolecule" (id)
);

CREATE TABLE "Moiety_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Moiety" (id)
);

CREATE TABLE "MolecularAnion_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "MolecularAnion" (id)
);

CREATE TABLE "MolecularAnion_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "MolecularAnion" (id)
);

CREATE TABLE "MolecularCation_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "MolecularCation" (id)
);

CREATE TABLE "MolecularCation_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "MolecularCation" (id)
);

CREATE TABLE "MolecularComplex_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "MolecularComplex" (id)
);

CREATE TABLE "MolecularComponent_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "MolecularComponent" (id)
);

CREATE TABLE "MolecularSpecies_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "MolecularSpecies" (id)
);

CREATE TABLE "MolecularSpecies_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "MolecularSpecies" (id)
);

CREATE TABLE "MolecularSubsequence_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "MolecularSubsequence" (id)
);

CREATE TABLE "Molecule_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Molecule" (id)
);

CREATE TABLE "Molecule_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Molecule" (id)
);

CREATE TABLE "Monomer_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Monomer" (id)
);

CREATE TABLE "NaturalProduct_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "NaturalProduct" (id)
);

CREATE TABLE "NaturalProduct_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "NaturalProduct" (id)
);

CREATE TABLE "NonSpeciesMolecule_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "NonSpeciesMolecule" (id)
);

CREATE TABLE "NonSpeciesMolecule_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "NonSpeciesMolecule" (id)
);

CREATE TABLE "NucleotideSequenceInterval_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "NucleotideSequenceInterval" (id)
);

CREATE TABLE "Peptide_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Peptide" (id)
);

CREATE TABLE "Peptide_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Peptide" (id)
);

CREATE TABLE "PolyatomicIon_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "PolyatomicIon" (id)
);

CREATE TABLE "PolyatomicIon_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "PolyatomicIon" (id)
);

CREATE TABLE "PolymerPart_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "PolymerPart" (id)
);

CREATE TABLE "Protein_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Protein" (id)
);

CREATE TABLE "Protein_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Protein" (id)
);

CREATE TABLE "RNASequenceInterval_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "RNASequenceInterval" (id)
);

CREATE TABLE "SmallMolecule_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "SmallMolecule" (id)
);

CREATE TABLE "SmallMolecule_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "SmallMolecule" (id)
);

CREATE TABLE "Stereoisomer_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Stereoisomer" (id)
);

CREATE TABLE "Stereoisomer_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Stereoisomer" (id)
);

CREATE TABLE "UnchargedMolecule_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "UnchargedMolecule" (id)
);

CREATE TABLE "UnchargedMolecule_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "UnchargedMolecule" (id)
);

CREATE TABLE "AcidBaseConflationClass" (
	name TEXT, 
	owl_subclass_of TEXT, 
	id TEXT NOT NULL, 
	subtype_of TEXT, 
	classifies TEXT, 
	conjugate_base_of TEXT, 
	conjugate_acid_of TEXT, 
	has_physiological_base TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classifies) REFERENCES "Molecule" (id), 
	FOREIGN KEY(has_physiological_base) REFERENCES "AcidBase" (id)
);

CREATE TABLE "Allotrope" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_atom_occurrences TEXT, 
	has_bonds TEXT, 
	has_submolecules TEXT, 
	is_organic BOOLEAN, 
	has_part TEXT, 
	allotropic_analog_of TEXT NOT NULL, 
	has_bonding_structure TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(allotropic_analog_of) REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "AtomAnion" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_nuclear_parts TEXT, 
	has_part TEXT, 
	has_element TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "AtomCation" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_nuclear_parts TEXT, 
	has_part TEXT, 
	has_element TEXT, 
	elemental_charge INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "ChemicalGroup" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	"MoleculeGroupingClassDefinedByAdditionOfAGroup_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("MoleculeGroupingClassDefinedByAdditionOfAGroup_id") REFERENCES "MoleculeGroupingClassDefinedByAdditionOfAGroup" (id)
);

CREATE TABLE "Isotope" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_nuclear_parts TEXT, 
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
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY(isotope_of) REFERENCES "Isotope" (id), 
	FOREIGN KEY(decay_product) REFERENCES "Isotope" (id)
);

CREATE TABLE "MonoatomicIon" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_nuclear_parts TEXT, 
	has_part TEXT, 
	elemental_charge INTEGER, 
	has_element TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "RacemicMixture" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	inchi_atom_connections_sublayer TEXT, 
	has_left_enantiomer TEXT NOT NULL, 
	has_right_enantiomer TEXT NOT NULL, 
	chirality_agnostic_form TEXT, 
	"IUPAC_name" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_left_enantiomer) REFERENCES "Enantiomer" (id), 
	FOREIGN KEY(has_right_enantiomer) REFERENCES "Enantiomer" (id), 
	FOREIGN KEY(chirality_agnostic_form) REFERENCES "Molecule" (id)
);

CREATE TABLE "Stereocenter" (
	"ChemicalElement_id" TEXT, 
	PRIMARY KEY ("ChemicalElement_id"), 
	FOREIGN KEY("ChemicalElement_id") REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "AcidBase_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "AcidBase" (id)
);

CREATE TABLE "AcidBase_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "AcidBase" (id)
);

CREATE TABLE "ChemicalElement_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "ChemicalElement" (id)
);

CREATE TABLE "Enantiomer_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Enantiomer" (id)
);

CREATE TABLE "Enantiomer_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Enantiomer" (id)
);

CREATE TABLE "Ester_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Ester" (id)
);

CREATE TABLE "Ester_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Ester" (id)
);

CREATE TABLE "FullySpecifiedAtom_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "FullySpecifiedAtom" (id)
);

CREATE TABLE "FunctionalGroup_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "FunctionalGroup" (id)
);

CREATE TABLE "Homopolymer_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Homopolymer" (id)
);

CREATE TABLE "Homopolymer_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Homopolymer" (id)
);

CREATE TABLE "MonomolecularPolymer_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "MonomolecularPolymer" (id)
);

CREATE TABLE "MonomolecularPolymer_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "MonomolecularPolymer" (id)
);

CREATE TABLE "Nuclide_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Nuclide" (id)
);

CREATE TABLE "Radionuclide_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Radionuclide" (id)
);

CREATE TABLE "SupramolecularPolymer_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "SupramolecularPolymer" (id)
);

CREATE TABLE "UnchargedAtom_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "UnchargedAtom" (id)
);

CREATE TABLE "Isobar" (
	id TEXT NOT NULL, 
	type TEXT, 
	"IUPAC_name" TEXT, 
	is_radical BOOLEAN, 
	has_chemical_role TEXT, 
	inchi_string TEXT, 
	inchi_chemical_sublayer TEXT, 
	empirical_formula TEXT, 
	owl_subclass_of TEXT, 
	atomic_number INTEGER, 
	symbol TEXT, 
	name TEXT, 
	has_nuclear_parts TEXT, 
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
	FOREIGN KEY(has_part) REFERENCES "SubatomicParticle" (id), 
	FOREIGN KEY(has_element) REFERENCES "ChemicalElement" (id), 
	FOREIGN KEY(decay_product) REFERENCES "Isotope" (id)
);

CREATE TABLE "Allotrope_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Allotrope" (id)
);

CREATE TABLE "Allotrope_has_atoms" (
	backref_id TEXT, 
	has_atoms TEXT, 
	PRIMARY KEY (backref_id, has_atoms), 
	FOREIGN KEY(backref_id) REFERENCES "Allotrope" (id)
);

CREATE TABLE "AtomAnion_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "AtomAnion" (id)
);

CREATE TABLE "AtomCation_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "AtomCation" (id)
);

CREATE TABLE "ChemicalGroup_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "ChemicalGroup" (id)
);

CREATE TABLE "Isotope_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Isotope" (id)
);

CREATE TABLE "MonoatomicIon_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "MonoatomicIon" (id)
);

CREATE TABLE "RacemicMixture_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "RacemicMixture" (id)
);

CREATE TABLE "Isobar_smiles_string" (
	backref_id TEXT, 
	smiles_string TEXT, 
	PRIMARY KEY (backref_id, smiles_string), 
	FOREIGN KEY(backref_id) REFERENCES "Isobar" (id)
);
