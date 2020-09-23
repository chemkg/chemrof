EXTS = _datamodel.py .graphql .schema.json .owl -docs .shex

all: $(patsubst %,src/schema/chemont%, $(EXTS))

test: all

src/schema/%_datamodel.py: src/schema/%.yaml
	gen-py-classes $< > $@
src/schema/%.graphql: src/schema/%.yaml
	gen-graphql $< > $@
src/schema/%.schema.json: src/schema/%.yaml
	gen-json-schema -t transaction $< > $@
src/schema/%.shex: src/schema/%.yaml
	gen-shex $< > $@
src/schema/%.csv: src/schema/%.yaml
	gen-csv $< > $@
src/schema/%.owl.ttl: src/schema/%.yaml
	gen-owl $< > $@
src/schema/%.ttl: src/schema/%.owl
	cp $< $@
src/schema/%-docs: src/schema/%.yaml
	pipenv run gen-markdown --dir $@ $<

deploy-docs:
	cp src/schema/chemont-docs/*md docs/


OWLSRC = src/schema/chemont.owl.ttl
# scans wikidata for potential matches; the result is a sub-ontology
matches/close-matches.ttl: $(OWLSRC)
	wd-ontomatch -d ontomatcher -i $< match_all && cp CACHE.ttl $@

matches/close-matches-enhanced.ttl: matches/close-matches.ttl
	robot query -i $< -u sparql/wd-add-category.ru -o $@

matches/matches.tsv: matches/close-matches.ttl  $(OWLSRC)
	rdfmatch -p chemont -w matches/weights.pro  -i prefixes.ttl -i $(OWLSRC) -G matches/matches.ttl -d index -i $< match > $@
nomatches.tsv: close-matches.ttl bosch.ttl
	rdfmatch --label_only -p bosch --match_prefix wd -w conf/bosch_weights.pro  -i prefixes.ttl -i bosch.ttl -G matches.ttl -d index -i $< nomatch > $@

