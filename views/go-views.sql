CREATE OR REPLACE VIEW annotatable AS
  SELECT * FROM rdfs_label_statement WHERE subject LIKE 'GO:%' AND subject NOT IN (select subject from statements where object='obo:go#gocheck_do_not_manually_annotate' union select subject from statements where object='obo:go#gocheck_do_not_annotate');

CREATE OR REPLACE VIEW Response_t AS SELECT subject AS id from entailed_edge WHERE predicate='rdfs:subClassOf' and object='GO:0050896';


CREATE OR REPLACE VIEW chebi_used AS
  SELECT DISTINCT e.object AS id
   FROM edge AS e
   INNER JOIN annotatable AS a ON (e.subject=a.subject)
  WHERE e.object like 'CHEBI:%'
   AND e.subject NOT IN (select id FROM Response_t);

COPY (SELECT * FROM chebi_used) TO 'database/go-chebi-used.csv' (HEADER, DELIMITER ',');
