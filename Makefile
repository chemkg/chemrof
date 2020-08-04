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
src/schema/%.owl: src/schema/%.yaml
	gen-owl $< > $@
src/schema/%.ttl: src/schema/%.owl
	cp $< $@
src/schema/%-docs: src/schema/%.yaml
	pipenv run gen-markdown --dir $@ $<

deploy-docs:
	cp src/schema/chemont-docs/*md docs/

