MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run
SRC_DIR = src
SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = chemrof
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
TGTS = graphql jsonschema docs shex owl csv graphql python

#GEN_OPTS = --no-mergeimports
GEN_OPTS =

# environment variables
include config.env


GEN_PARGS =
ifdef LINKML_GENERATORS_PROJECT_ARGS
GEN_PARGS = ${LINKML_GENERATORS_PROJECT_ARGS}
endif

GEN_DARGS =
ifdef LINKML_GENERATORS_MARKDOWN_ARGS
GEN_DARGS = ${LINKML_GENERATORS_MARKDOWN_ARGS}
endif


all: gen
gen: project
clean:
	rm -rf target/
	rm -rf docs/

t:
	echo $(SCHEMA_NAMES)

echo:
	echo $(patsubst %,gen-%,$(TGTS))

test: all

install:
	. environment.sh
	pip install -r requirements.txt

tdir-%:
	mkdir -p target/$*
docs:
	mkdir $@

docs/index.md: $(SOURCE_FILES)
	cp src/docs/*.md docs/ ; \
	$(RUN) gen-doc -d docs $<
	#$(RUN) gen-markdown -I $@ -d docs $<

#project: project1 schema/owl/chemrof.owl.ttl
project: $(SOURCE_FILES)
#	gen-project -A 'owl: {metaclasses: false, type_objects: false}' -d schema $<
	$(RUN) gen-project ${GEN_PARGS} -d schema $<

#schema/owl/$(SCHEMA_NAME).owl.ttl: $(SOURCE_FILES)
#	$(RUN) gen-owl --no-metaclasses --no-type-objects $< > $@.tmp && mv $@.tmp $@


schema/sssom/chemrof.sssom.tsv: src/schema/chemrof.yaml
	$(RUN) gen-sssom $< -o $@

# test docs locally.
docserve:
	$(RUN) mkdocs serve

gh-deploy:
	$(RUN) mkdocs gh-deploy

include Makefile.etl
