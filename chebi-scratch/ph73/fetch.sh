#!/bin/sh
# Download ChEBI structures and the Rhea pH 7.3 mapping into data/
set -e
mkdir -p data
curl -sSL -o data/structures.tsv.gz https://ftp.ebi.ac.uk/pub/databases/chebi/flat_files/structures.tsv.gz
curl -sSL -o data/compounds.tsv.gz https://ftp.ebi.ac.uk/pub/databases/chebi/flat_files/compounds.tsv.gz
curl -sSL -o data/chebi_pH7_3_mapping.tsv https://ftp.expasy.org/databases/rhea/tsv/chebi_pH7_3_mapping.tsv
