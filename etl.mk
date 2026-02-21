# See   https://chemkg.github.io/chemrof/database/
INJECTS = ChemicalGroupingByCharge
WD_CLASSES = ChemicalElement Isotope
CHEBI_CLASSES = MonoatomicIon
PCHEBI_CLASSES = RacemicMixture Enantiomer
METACLASSES = $(WD_CLASSES) $(CHEBI_CLASSES)  $(PCHEBI_CLASSES) $(INJECTS)
REASONER = HERMIT
OWL_SCHEMA = src/chemrof/schema/owl/chemrof.owl.ttl

all: owl/chemrof-ontology.owl

# -- Ontology --

# pre-reason prior to release
ontology/chemrof-ontology.owl: owl/chemrof-ontology-asserted.owl
	robot reason -r $(REASONER) -i $< -o $@

# merge all sub-ontologies into one
owl/chemrof-ontology-asserted.owl: owl/gen
	robot merge -i src/ontology/chem-edit.owl.ttl $(patsubst %, -i owl/gen/%.owl, $(METACLASSES)) -o $@
.PRECIOUS: owl/chemrof-ontology-asserted.owl

# translate abox database to owl tbox using metaclass-specific SPARQL queries
owl/gen/%.owl: database/chem.ttl
	robot query -i $< -q sparql/owlgen/gen-$*.rq $@

# -- Database --
# (Ontology as ABox)

# create chem abox database
INJECT_FILES = $(patsubst %, database/inject/inject-%.ttl, $(INJECTS))
database/chem.ttl: database/all-merged.ttl $(INJECT_FILES)
	robot merge -i $< $(patsubst %, -i database/inject/inject-%.ttl, $(INJECTS)) -o $@
.PRECIOUS: database/chem.ttl

# merge database with schema
database/%-merged.owl.ttl: database/%.ttl $(OWL_SCHEMA)
	robot merge -i $< -i $(OWL_SCHEMA) -o $@

# merge chebi and wd databases together
database/all.ttl: database/wd database/chebi database/pchebi
	riot database/*/*.ttl > $@.tmp && mv $@.tmp $@
.PRECIOUS: database/wd-all.ttl

# injection of additional facts
database/inject/inject-%.ttl: database/all-merged.ttl sparql/inject-%.rq
	robot query -i $< -q sparql/inject-$*.rq $@
.PRECIOUS: database/inject/inject-%.ttl

all-wd: $(patsubst %, database/wd/%.ttl, $(WD_CLASSES))

# metaclass specific sub-databases, from Wikidata
database/wd/%.ttl: sparql/construct-wd-%.rq
	curl --header "Accept: text/turtle"  -G 'https://query.wikidata.org/sparql' --data-urlencode "query@sparql/construct-wd-$*.rq" > $@.tmp && mv $@.tmp $@
.PRECIOUS: database/wd/%.ttl

all-chebi: $(patsubst %, database/chebi/%.ttl, $(CHEBI_CLASSES))

# metaclass specific sub-databases, from CHEBI
database/chebi/%.ttl: sparql/construct-chebi-%.rq
	curl --header "Accept: text/turtle"  -G 'https://sparql.hegroup.org/sparql' --data-urlencode "query@$<" > $@.tmp && mv $@.tmp $@
.PRECIOUS: database/wd/%.ttl

# merge all wd together
database/wd-all.ttl: database/wd/
	riot database/wd/*.ttl > $@.tmp && mv $@.tmp $@
.PRECIOUS: database/wd-all.ttl



## TODO

SP = pl2sparql -i obo_prefixes  -u obo_metadata/oio  -A ~/repos/onto-mirror/void.ttl -m obo=http://purl.obolibrary.org/obo/


extract/wd-info-%.tsv:
	pq-wikidata -f tsv "$*(S),rdf(S,P,O)" > $@.tmp && mv $@.tmp $@
extract/wd-edge-%.tsv:
	pq-wikidata -f tsv "$*(S),rdf(S,P,O),rdf_is_iri(O)" -l -L enlabel > $@.tmp && mv $@.tmp $@
extract/wd-all-nodeprop-%.tsv:
	pq-wikidata -f tsv "$*(S),rdf(S,P,O),\+rdf_is_iri(O)" -l -L enlabel > $@.tmp && mv $@.tmp $@
extract/wd-en-nodeprop-%.tsv:
	pq-wikidata -f tsv "$*(S),rdf(S,P,O),is_en(O)" -l -L enlabel > $@.tmp && mv $@.tmp $@


extract/wd-chemical_element.tsv:
	pq-wikidata -f tsv --header id,label,symbol,atomic_number "chemical_element(S),enlabel(S,L),element_symbol(S,Sym),atomic_number(S,N)"  > $@.tmp && mv $@.tmp $@

extract/chebi-inchi.tsv:
	$(SP) -f tsv --header inchi,chemid,label -e -i chebi "rdf(X,'http://purl.obolibrary.org/obo/chebi/inchi',Y),label(X,XN)" "x(Y,X,XN)"  > $@.tmp && mv $@.tmp $@
extract/chebi-inchi-summary.tsv:
	$(SP) -f tsv --header inchi,count,chemids,labels -e -i chebi "setof(C,rdf(C,'http://purl.obolibrary.org/obo/chebi/inchi',F),Cs),length(Cs,Len),maplist(label,Cs,CNs)" "x(F,Len,Cs,CNs)"  > $@.tmp && mv $@.tmp $@
extract/chebi-smiles-summary.tsv:
	$(SP) -f tsv --header smiles,count,chemids,labels -e -i chebi "setof(C,rdf(C,'http://purl.obolibrary.org/obo/chebi/smiles',F),Cs),length(Cs,Len),maplist(label,Cs,CNs)" "x(F,Len,Cs,CNs)"  > $@.tmp && mv $@.tmp $@

extract/chebi-RacemicMixture.tsv:
	pq-ontobee -e --consult src/prolog/chebi.pro report racemic_mixture > $@.tmp && mv $@.tmp $@

all-pchebi: $(patsubst %, database/pchebi/%.ttl, $(PCHEBI_CLASSES))

database/pchebi/%.ttl: src/prolog/chebi.pro
	pq-ontobee -e --consult src/prolog/chebi.pro "save_triples('$*','$@.tmp')" && mv $@.tmp $@


database/%.jsonld: database/%.ttl
	riot --output=JSONLD --syntax=TURTLE $< > $@.tmp && mv $@.tmp $@

# RHEA
database/chebi_pH7_3_mapping.tsv:
	curl -L -s https://ftp.expasy.org/databases/rhea/tsv/chebi_pH7_3_mapping.tsv | perl -npe 's@@CHEBI:@;s@\t@\tCHEBI:@;s@^CHEBI:CHEBI.*@id\thas_physiological_stable_form\tsource@' > $@.tmp && mv $@.tmp $@

