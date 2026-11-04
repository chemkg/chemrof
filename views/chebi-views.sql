-- Analysis views over a semsql ChEBI database, for DuckDB only
-- (uses list(), str_split(), list slicing and `FROM 'file.tsv'`).
--
-- Build with `make database/chebi.ddb`, which copies the semsql base tables
-- from db/chebi.db into a duckdb file, recreates the semsql views this file
-- relies on (edge, rdfs_label_statement, has_dbxref_statement,
-- rdf_type_statement, axiom_dbxref_annotation) and then runs this file.
--
-- Inputs, both produced by make targets:
--   database/chebi_pH7_3_mapping.tsv   Rhea pH 7.3 mapping (id, has_physiological_stable_form, source)
--   database/go-chebi-used.csv         CHEBI ids used in GO, from views/go-views.sql
CREATE VIEW IF NOT EXISTS entailed_subclass_of_edge AS SELECT * FROM entailed_edge WHERE predicate='rdfs:subClassOf';
CREATE VIEW IF NOT EXISTS has_part_edge AS SELECT * FROM edge WHERE predicate='BFO:0000051';
CREATE VIEW IF NOT EXISTS entailed_has_part_edge AS SELECT * FROM entailed_edge WHERE predicate='BFO:0000051';

CREATE TABLE has_physiological_stable_form AS FROM 'database/chebi_pH7_3_mapping.tsv';
CREATE TABLE has_physiological_stable_form_non_trivial AS
 SELECT s.* FROM has_physiological_stable_form AS s
  WHERE s.has_physiological_stable_form IN (SELECT s2.has_physiological_stable_form FROM has_physiological_stable_form AS s2 WHERE s2.has_physiological_stable_form != s2.id);
  
CREATE TABLE node_is_physiologically_stable AS
 SELECT
   id,
   CASE
     WHEN has_physiological_stable_form=id
     THEN true
     ELSE false
   END as is_stable
  FROM has_physiological_stable_form_non_trivial;
 

CREATE TABLE go_chebi_used AS FROM 'database/go-chebi-used.csv';

CREATE OR REPLACE VIEW node_data_property AS SELECT subject AS id, predicate, value FROM statements WHERE value IS NOT NULL;
CREATE OR REPLACE VIEW node_relationship AS SELECT subject AS id, predicate, object FROM edge WHERE object IS NOT NULL;
CREATE OR REPLACE VIEW node_classification AS SELECT subject AS id, predicate, object FROM entailed_subclass_of_edge;

-- CREATE TABLE node_xrefs (id varchar, xrefs varchar[]);
CREATE TABLE node_xrefs AS
 SELECT subject AS id, list(value) AS xrefs, length(list(value)) AS n_xrefs
 FROM has_dbxref_statement
 WHERE subject LIKE 'CHEBI:%'
 GROUP BY subject;

CREATE TABLE node_is_stable_xrefs AS
 SELECT s.id, s.is_stable, nx.xrefs, COALESCE(nx.n_xrefs, 0) AS n_xrefs
 FROM
  node_is_physiologically_stable AS s
  LEFT OUTER JOIN node_xrefs AS nx ON (s.id=nx.id);
 

COPY (SELECT * FROM node_is_stable_xrefs) TO 'tmp/stable_xrefs.csv' (HEADER, DELIMITER ',');



CREATE VIEW name AS SELECT id, value AS name FROM node_data_property WHERE predicate='rdfs:label';

-- ChEBI's data properties, as semsql stores them (obo:chebi/*), exposed under
-- the chemrof slot names used by the views below.
CREATE OR REPLACE TABLE charge AS SELECT id, cast(value AS int) AS charge  FROM node_data_property where predicate='obo:chebi/charge';
CREATE INDEX charge_ix ON charge(id, charge);

CREATE OR REPLACE VIEW mass AS SELECT id, cast(value AS float) AS mass  FROM node_data_property where predicate='obo:chebi/mass';
CREATE OR REPLACE VIEW monoisotopic_mass AS SELECT id, cast(value AS float) AS monoisotopic_mass  FROM node_data_property where predicate='obo:chebi/monoisotopicmass';
CREATE OR REPLACE VIEW generalized_empirical_formula AS SELECT id, value AS chebi_formula FROM node_data_property where predicate='obo:chebi/formula';
CREATE OR REPLACE VIEW smiles_string AS SELECT id, value AS smiles_string FROM node_data_property where predicate='obo:chebi/smiles';
CREATE OR REPLACE VIEW inchi_key_string AS SELECT id, value AS inchi_key_string FROM node_data_property where predicate='obo:chebi/inchikey';
CREATE OR REPLACE VIEW inchi_string AS SELECT id, value AS inchi_string FROM node_data_property where predicate='obo:chebi/inchi';

-- not in schema
CREATE OR REPLACE VIEW inchi_components AS SELECT id, inchi_string, str_split(inchi_string, '/') AS inchi_components, len(str_split(inchi_string, '/')) as inchi_components_length  from inchi_string;

-- older ChEBI releases use the obo:chebi# predicates, newer ones the RO ids
CREATE OR REPLACE TABLE is_conjugate_acid_of AS SELECT * FROM node_relationship WHERE predicate IN ('RO:0018034', 'obo:chebi#is_conjugate_acid_of');
CREATE OR REPLACE TABLE is_conjugate_base_of AS SELECT * FROM node_relationship WHERE predicate IN ('RO:0018033', 'obo:chebi#is_conjugate_base_of');
CREATE VIEW is_conjugate_of AS SELECT * FROM is_conjugate_acid_of UNION SELECT * FROM is_conjugate_base_of;
CREATE VIEW has_part AS SELECT * FROM node_relationship WHERE predicate='BFO:0000051';

CREATE VIEW is_conjugate_base_of_with_charges AS
 SELECT
  cbo.id AS subject,
  cbo.object,
  cs.charge AS subject_charge,
  co.charge AS object_charge,
  cs.charge-co.charge AS diff,
  sign(cs.charge-co.charge) AS diff_sign
 FROM
  is_conjugate_base_of AS cbo
  INNER JOIN charge AS cs ON (cs.id=cbo.id)
  INNER JOIN charge AS co ON (co.id=cbo.object);

CREATE VIEW missing_has_physiological_stable_form AS SELECT DISTINCT(id) from is_conjugate_of WHERE id NOT IN (SELECT id FROM has_physiological_stable_form);

CREATE VIEW alias AS SELECT id, predicate, value AS alias FROM node_data_property WHERE predicate IN ('rdfs:label', 'oio:hasExactSynonym', 'oio:hasRelatedSynonym', 'oio:hasBroadSynonym', 'oio:hasNarrowSynonym');

CREATE VIEW _uniprot_synonym AS SELECT * FROM axiom_dbxref_annotation where annotation_value='UniProt';
CREATE VIEW _ph73_name AS
 SELECT
   p.id, p.has_physiological_stable_form, p.source, s.value AS name, s.predicate
 FROM
   _uniprot_synonym AS s
   INNER JOIN has_physiological_stable_form AS p ON (s.subject=p.has_physiological_stable_form);




CREATE VIEW OwlClass AS
  SELECT distinct subject AS id from rdf_type_statement WHERE object = 'owl:Class';
  
CREATE VIEW Entity AS
 SELECT
   n.*,
   f.chebi_formula,
   s.smiles_string,
   ic.inchi_string,
   ic.inchi_components,
   ic.inchi_components_length,
   c.charge,
   m.mass,
   mi.monoisotopic_mass
 FROM
  name AS n
  LEFT OUTER JOIN generalized_empirical_formula AS f  ON (n.id=f.id)
  LEFT OUTER JOIN inchi_components AS ic ON (n.id=ic.id)
  LEFT OUTER JOIN smiles_string AS s ON (s.id=n.id)
  LEFT OUTER JOIN charge AS c ON (c.id=n.id)
  LEFT OUTER JOIN mass AS m ON (m.id=n.id)
  LEFT OUTER JOIN monoisotopic_mass AS mi ON (mi.id=n.id);



CREATE VIEW Atom_t AS
 SELECT id FROM node_classification WHERE object='CHEBI:33250';

-- https://github.com/ebi-chebi/ChEBI/issues/4490
CREATE VIEW ChemicalElement AS
  SELECT
     id,
     name,
     chebi_formula AS symbol,
     mass
   FROM Entity AS e
   WHERE
    name LIKE '% atom'
    AND inchi_components_length=2;

-- https://github.com/ebi-chebi/ChEBI/issues/4491
CREATE TABLE Isotope AS
  SELECT
     id,
     name,
     chebi_formula AS symbol,
     inchi_string,
     mass,
     CAST(inchi_components[3][3:] AS int) AS nucleon_number_difference
   FROM Entity AS e
   WHERE
    e.id IN (SELECT id FROM Atom_t)
    AND e.inchi_components_length=3;

CREATE VIEW Zwitterion_t AS
 SELECT id FROM node_classification WHERE object='CHEBI:27369';


CREATE VIEW MonoatomicCation_t AS
 SELECT id FROM node_classification WHERE object='CHEBI:23906';

CREATE VIEW MonoatomicCation AS
  SELECT
      e.*,
      ps.has_physiological_stable_form
    FROM Entity AS e
    INNER JOIN MonoatomicCation_t AS i ON (i.id=e.id)
    LEFT OUTER JOIN has_physiological_stable_form AS ps ON (e.id=ps.id)
  WHERE
    e.inchi_string IS NOT NULL
    AND inchi_components_length=3;

CREATE VIEW MonoatomicAnion_t AS
 SELECT id FROM node_classification WHERE object='CHEBI:23905';

 


CREATE VIEW group_by_inchi_components_length AS
  SELECT inchi_components_length,count(*) FROM Entity GROUP BY inchi_components_length;

CREATE VIEW chemical_l2 AS SELECT * FROM Entity WHERE inchi_components_length = 2;

CREATE VIEW term_parts AS
 SELECT l.subject AS id, l.value AS name, list(e.object) AS ancestors
 FROM rdfs_label_statement AS l
  LEFT JOIN edge AS e ON (l.subject=e.subject)
 WHERE e.predicate='BFO:0000051'
 GROUP BY l.subject, l.value;

CREATE VIEW term_ancestors AS
 SELECT l.subject AS id, l.value AS name, list(e.object) AS ancestors
 FROM rdfs_label_statement AS l
  LEFT JOIN entailed_edge AS e ON (l.subject=e.subject)
 GROUP BY l.subject, l.value;


CREATE VIEW cation AS
 SELECT c.*
 FROM Entity AS c
  INNER JOIN entailed_subclass_of_edge AS s ON (c.id = s.subject)
 WHERE s.object='CHEBI:36916';

CREATE VIEW anion AS
 SELECT c.*
 FROM Entity AS c
  INNER JOIN entailed_subclass_of_edge AS s ON (c.id = s.subject)
 WHERE s.object='CHEBI:22563';

CREATE VIEW Ion_t AS
 SELECT id
  FROM node_classification WHERE object='CHEBI:24870';

CREATE VIEW acid AS
 SELECT c.*
 FROM Entity AS c
  INNER JOIN entailed_edge AS e ON (c.id = e.subject)
 WHERE e.object='CHEBI:37527' AND predicate='RO:0000087';

CREATE VIEW salt AS
 SELECT c.*
 FROM Entity AS c
  INNER JOIN entailed_subclass_of_edge AS s ON (c.id = s.subject)
 WHERE s.object='CHEBI:24866';

CREATE VIEW salt_cationic_component AS
 SELECT salt.*, e.object AS has_cationic_component
 FROM
  salt
  INNER JOIN has_part_edge AS e ON (salt.id=e.subject)
 WHERE
  e.object IN (SELECT id FROM cation);


-- consider entailed
CREATE VIEW salt_anionic_component AS
 SELECT salt.*, e.object AS has_anionic_component
 FROM
  salt
  INNER JOIN has_part_edge AS e ON (salt.id=e.subject)
 WHERE
  e.object IN (SELECT id FROM anion);

CREATE VIEW salt_rels AS
SELECT * FROM
  salt_anionic_component AS a
  INNER JOIN salt_cationic_component AS c ON (a.id=c.id);
  
CREATE VIEW Racemate_t AS
 SELECT id
  FROM node_classification WHERE object='CHEBI:60911';

--CREATE VIEW stereo_component AS SELECT inchi_components[-2] AS stereo, * FROM inchi_components;
 
CREATE TABLE racemate_parts AS
 SELECT
  r.id,
  p.object AS part_id,
  i.inchi_components[-2] AS stereo,
  i.*
 FROM
  Racemate_t AS r
  INNER JOIN has_part AS p ON (r.id=p.id)
  INNER JOIN inchi_components AS i ON (p.object=i.id);

CREATE TABLE racemate_left AS
 SELECT DISTINCT
  r.id AS racemate_id,
  p.object AS part_id
 FROM
  Racemate_t AS r
  INNER JOIN has_part AS p ON (r.id=p.id)
  INNER JOIN alias AS a ON (p.object=a.id)
 WHERE
  a.alias LIKE '(S)%';

CREATE TABLE racemate_right AS
 SELECT DISTINCT
  r.id AS racemate_id,
  p.object AS part_id
 FROM
  Racemate_t AS r
  INNER JOIN has_part AS p ON (r.id=p.id)
  INNER JOIN alias AS a ON (p.object=a.id)
 WHERE
  a.alias LIKE '(R)%';



CREATE VIEW racemate AS
 SELECT
  c.id,
  lp.part_id AS left_id,
  rp.part_id AS right_id,
  c.*
 FROM
  Entity AS c
  INNER JOIN Racemate_t AS r ON (c.id=r.id)
  INNER JOIN racemate_left AS lp ON (lp.racemate_id=c.id)
  INNER JOIN racemate_right AS rp ON (rp.racemate_id=c.id);

CREATE TABLE racemate_no_left AS
 SELECT
  *
 FROM
  Entity AS c
  INNER JOIN Racemate_t AS r ON (c.id=r.id)
  WHERE c.id NOT IN (SELECT racemate_id FROM racemate_left);

CREATE TABLE racemate_no_right AS
 SELECT
  *
 FROM
  Entity AS c
  INNER JOIN Racemate_t AS r ON (c.id=r.id)
  WHERE c.id NOT IN (SELECT racemate_id FROM racemate_right);


CREATE VIEW Macromolecule_t AS
 SELECT id
  FROM node_classification WHERE object='CHEBI:33839';

CREATE VIEW Lipid_t AS
 SELECT id
  FROM node_classification WHERE object='CHEBI:18059';

CREATE VIEW Peptide_t AS
 SELECT id
  FROM node_classification WHERE object='CHEBI:16670';


CREATE VIEW Ester_t AS
 SELECT id
  FROM node_classification WHERE object='CHEBI:35701';



CREATE VIEW _Entity_no_ph73_mapping AS
 SELECT * FROM Entity
 WHERE id NOT IN (SELECT id FROM has_physiological_stable_form)
  AND id NOT IN (SELECT id FROM Macromolecule_t UNION SELECT id FROM Racemate_t  UNION SELECT id FROM Peptide_t)
  AND chebi_formula IS NOT NULL
  AND inchi_string is not NULL;

CREATE VIEW subset_3_star AS
 SELECT * FROM statements WHERE predicate='oio:inSubset' AND object = 'obo:chebi#3_STAR';
CREATE VIEW subset_2_star AS
 SELECT * FROM statements WHERE predicate='oio:inSubset' AND object = 'obo:chebi#2_STAR';
CREATE VIEW subset_1_star AS
 SELECT * FROM statements WHERE predicate='oio:inSubset' AND object = 'obo:chebi#1_STAR';
 
