# How biochemical databases and metabolic-model resources assign charge states at physiological pH (pH ~7.0-7.4)

Notes compiled 2026-10-14. Where a source is older than about 2 years, its date is given. Coverage is uneven. Rhea, ChEBI, MetaCyc, ModelSEED, eQuilibrator and MetaNetX have primary sources. Recon/VMH and BiGG are only partly sourced. I found no primary sources for KEGG, LIPID MAPS or Reactome in this pass (see Gaps).

## Q1. For each resource, which tool computes charge states or pKa, and what is the source?

### Takeaway
Nearly every resource that assigns explicit protonation states uses ChemAxon Marvin (pKa / major-microspecies plugin, run through cxcalc or the MarvinBeans Java API). This includes Rhea and ChEBI at pH 7.3, MetaCyc at pH 7.3, ModelSEED at pH 7.0, eQuilibrator for pKa ensembles, and MetaNetX, which uses MarvinBeans in its pipeline. The resources differ in reference pH (7.0, 7.2, 7.3, ~7.4 in HMDB-style predicted properties) and in whether curators can override the result. Rhea's mapping file has 898 rows with ORIGIN "curation".

### Cited Findings

**Rhea**
- Rhea reaction participants are "represented by the major micro-species at pH 7.3", "verified using the Marvin pKa calculator from ChemAxon (version 6.2.0)". The paper also acknowledges ChemAxon's software contributions. — [Morgat et al. 2015, NAR, "Updates in Rhea"](https://pmc.ncbi.nlm.nih.gov/articles/PMC4384025)
- The 2012 Rhea paper says each master reaction is "uniquely represented at an arbitrarily chosen pH of 7.3". It uses Marvin to "select the major species of each compound found at pH 7.3 and at a temperature of 298 K". It gives phosphate as a caveat: HPO4(2-) is only slightly in excess of H2PO4(-) at pH 7.3, so the representation "is a simplification of the actual state". — [Alcántara et al. 2012, NAR (PMC3245052)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3245052) (as summarized by search; quoted fragments appear in search snippets)
- The Rhea help page "Which ChEBIs are used in Rhea?" says Rhea uses only ChEBI entities that are the major microspecies at pH 7.3. This "follows the policy used by MetaCyc". The page also says Rhea uses Marvin from ChemAxon to compute the major microspecies at pH 7.3 for all ChEBI entities, and links other forms via `has_major_microspecies_at_pH_7_3`, with D-alanine as the example. — [rhea-db.org/help/chebi-in-rhea](https://www.rhea-db.org/help/chebi-in-rhea) (direct fetch returned HTTP 403; content taken from search-result snippets)
- The Rhea "Reaction curation" help page says curators use software to check that participants are the major microspecies at pH 7.3 and that reactions are mass- and charge-balanced. — [rhea-db.org/help/reaction-curation](https://api.rhea-db.org/help/reaction-curation) (from search snippet)
- Rhea 2022: "Rhea selects only one protonation state for each chemical entity by default, that which represents the major protonation state at pH 7.3. The Rhea search engine maps ChEBI identifiers for other protonation states to the major protonation state used in Rhea, using a precomputed mapping of chemical structures available at https://www.rhea-db.org/help/download." This also applies to Exact searches. The paper acknowledges ChemAxon (https://www.chemaxon.com/products/marvin/). — [Bansal et al. 2022, NAR "Rhea, the reaction knowledgebase in 2022" (PMC8728268)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728268)
- The Rhea 2019 paper (SPARQL) also "gratefully acknowledge[s] the software contributions of ChemAxon". — [Lombardot et al. 2019 (PMC6324061)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6324061)
- **Direct analysis of `chebi_pH7_3_mapping.tsv`** (Rhea release 142, 2026-09-02, downloaded 2026-10-14) — [ftp.expasy.org/databases/rhea/tsv/chebi_pH7_3_mapping.tsv](https://ftp.expasy.org/databases/rhea/tsv/chebi_pH7_3_mapping.tsv); [rhea-release.properties](https://ftp.expasy.org/databases/rhea/rhea-release.properties):
  - The file has columns `CHEBI  CHEBI_PH7_3  ORIGIN` and 122,732 data rows.
  - ORIGIN=`computation` accounts for 121,834 rows. In 8,900 of these the pH 7.3 form differs from the input ChEBI ID, and in 112,934 it is the same.
  - ORIGIN=`curation` accounts for 898 rows. In **all** of them CHEBI == CHEBI_PH7_3 (self-mappings, e.g. 4194→4194, 4705→4705, 5834→5834).
  - Examples: ATP CHEBI:15422 → CHEBI:30616 (ATP(4-)) [computation]; phosphate CHEBI:18367 → CHEBI:43474 (hydrogenphosphate) [computation]; water CHEBI:15377 → itself.

**ChEBI**
- ChEBI entries for pH 7.3 forms carry a definition comment such as "major microspecies at pH 7.3 (according to Marvin v 6.2.0.)", together with "is conjugate base of" / "is conjugate acid of" relations to the parent acid or base. Examples are aurachin B(1−) and mugineate(1−). Some newer entries (e.g. (aminooxy)acetate) say only "Major microspecies at pH 7.3" without naming Marvin. — [CHEBI:90784](https://www.ebi.ac.uk/chebi/CHEBI:90784); [CHEBI:77826](https://www.ebi.ac.uk/chebi/CHEBI:77826); [CHEBI:157642](https://www.ebi.ac.uk/chebi/CHEBI:157642) (from search snippets)
- The ChEBI 2016 paper full text contains no description of the pH 7.3 / Marvin procedure (searched the full text for ChemAxon, Marvin, pKa, protonation and microspecies). — [Hastings et al. 2016 (PMC4702775)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4702775)

**UniProtKB/Swiss-Prot**
- Cross-references "are automatically added from Rhea to UniProtKB/Swiss-Prot", and Rhea is developed as "a vocabulary for the functional annotation of enzymes in UniProtKB". UniProt catalytic-activity annotations therefore inherit Rhea's pH 7.3 ChEBI forms. — [Morgat et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4384025)

**MetaCyc / BioCyc (Pathway Tools)**
- "Starting with version 13.0, all MetaCyc compounds have been adjusted to a consistent protonation state for a reference pH of 7.3, common in the cellular cytosol."
- The PGDB Concepts Guide says Marvin computes the protonation state of protoisomerization centers via pKa values obtained from partial-charge distributions. When proto-isomers are close in abundance, Marvin "will select the most likely proto-isomer based on a comparison of the floating point value of the relative abundance". Reactions imbalanced only in H were computationally balanced by adding or removing protons. The pH 7.3 value is taken from an E. coli cytoplasmic pH paper. — [PGDB Concepts Guide](https://metacyc.org/PGDBConceptsGuide.shtml); [MetaCyc 2010 NAR](https://academic.oup.com/nar/article/38/suppl_1/D473/3112230); [MetaCyc 2019 update (PMC6943030)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6943030/); [Guide to MetaCyc](https://www.metacyc.org/MetaCycUserGuide.shtml) (from search summaries)
- A ChemAxon forum thread from the SRI/EcoCyc side describes using the Marvin API to protonate compounds at pH 7.3. For ATP, Marvin predicted about 57% in the −3 form and 43% in the −4 form, so it picked −3. The curator noted this is not black-and-white. — [ChemAxon forum, "Problems with pKa plug-in accuracy"](https://forum.chemaxon.com/6/4114/problems-with-pka-plugin-accuracy/) (date not verified; older forum post, from search summary)
- Pathway Tools thermodynamics computes MetaCyc standard Gibbs energies at pH 7.3 and ionic strength 0.25. — [Pathway Tools v28.0 (arXiv 1510.03964)](https://arxiv.org/pdf/1510.03964) (search summary)

**ModelSEED / KBase**
- "Marvin from ChemAxon was used to protonate all molecular structures at a pH of 7 and to convert every molecular structure into InChI and SMILES format, Marvin 19.1". "Due to limitations in (i) the molecular structures, (ii) the InChI format and (iii) Marvin, we are unable to protonate or convert every molecular structure". The fallback is the protonated InChI, then the unprotonated SMILES. Formula and charge are then derived with **RDKit 2020.03.1.0 and OpenBabel 2.4.1** ("each would fail or report errors on a small but differing set of molecular structures"). Reactions that are imbalanced only in protons get protons added or removed. Gibbs energies come from eQuilibrator 0.2.5 at pH 7.0 and I = 0.25 M. — [Seaver et al. 2021, NAR (PMC7778927)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7778927)
- **New (Sept 2026):** ModelSEEDDatabase PR #295, "Regenerate the pH 7 protonation bundles with Marvin 26.1", was opened by freiburgermsu on 2026-09-18 and merged by samseaver on 2026-09-21. Findings from the PR:
  - "Net charge at pH 7 is unchanged for 79.7% of shared compounds and different for 20.3%", which the author calls "an upper bound on the tautomer effect".
  - Structures are bridged through RDKit into molblocks before Marvin sees them.
  - The `TautomerizationPlugin` requires the "Isomers Plugin Group" licence, but the runs use only a "Protonation-group" licence.
  - No open replacement is named.
  — [github.com/ModelSEED/ModelSEEDDatabase/pull/295](https://github.com/ModelSEED/ModelSEEDDatabase/pull/295)

**eQuilibrator / equilibrator-assets / component contribution**
- "estimating acid-base dissociation constants was done using Marvin Calculator, Calculator version 21.13.0, ChemAxon … under an academic license". The rest of the suite depends on open packages (OpenBabel, RDKit, NumPy…). Each compound is treated as an ensemble of pseudoisomers (protonation and Mg2+ binding states). — [Beber et al. 2022, "eQuilibrator 3.0", NAR (PMC8728285)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728285)
- The equilibrator-assets README says: "Marvin (by ChemAxon) - get a license and install it on your system. Make sure that the command cxcalc is in the shell PATH as it is called directly using subprocess.run()." — [PyPI equilibrator-assets](https://pypi.org/project/equilibrator-assets)
- equilibrator-cheminfo provides a uniform interface over Open Babel, RDKit or ChemAxon. ChemAxon needs a licence and `CHEMAXON_HOME`. — [PyPI equilibrator-cheminfo](https://pypi.org/project/equilibrator-cheminfo); [GitLab](https://gitlab.com/equilibrator/equilibrator-cheminfo)
- The local-cache documentation offers a `bypass_chemaxon` option that creates a compound from the user structure without pKa computation. This is a workaround, not a pKa replacement. — [equilibrator.readthedocs.io local_cache](https://equilibrator.readthedocs.io/en/latest/local_cache.html)

**MetaNetX / MNXref**
- The pipeline uses "InChI 1.0.5, Chemaxon MarvinBeans 19.26, Gurobi 9.0.2, Blast…, COBRA Toolbox…, LibSBML". The paper does not state what MarvinBeans is used for.
- MNXref metabolite IDs merge external entries for which "distinctions in protonation states, tautomeric forms or isotopes are typically ignored". "Pairs of tautomers or acid-bases can be validly merged". Rewritten equations "may differ from the original equation, for example, with respect to proton balancing". Since v2.0, transported protons (MNXM01) are distinguished from balancing protons (MNXM1). — [Moretti et al. 2021, NAR (PMC7778905)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7778905/); [MetaNetX CHANGELOG](https://www.metanetx.org/ftp/4.4/CHANGELOG)
- The MetaNetX ontology notes: "Typically, acid-base reactions become empty as the reconciliation merges different protonation states of a given metabolite." — [rdf.metanetx.org](https://rdf.metanetx.org/schema/CPLX)

**Recon 2 / Recon 2.2 / Recon3D / VMH, BiGG**
- Recon 2 (Thiele et al. 2013): metabolite formula and charge "were calculated based on their ionization state at pH 7.2, which for simplicity was presumed to be constant across all compartments". This is from the Recon 2 methods as reproduced in a patent document. The tool used is not stated in the retrieved text. — [Thiele et al. 2013, Nat Biotech](https://www.nature.com/articles/nbt.2488) (via search summary of supplementary text)
- Recon 2.2: "All metabolites have definitive chemical formulae and charges specified". The model uses automated linear-programming mass and charge balancing that adds missing protons and water. The paper does not mention ChemAxon, pKa or pH 7.2. — [Swainston et al. 2016 (PMC4896983)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4896983/)
- BiGG represents each metabolite as a formula plus an integer charge for the charged species. For example, Recon3D `3hmp_c` is C4H7O3 with charge −1. The legacy BiGG site notes that its data have not been updated since 2019. — [BiGG 3hmp_c](https://biggdata.ucsd.edu/models/Recon3D/metabolites/3hmp_c); [BiGG Models 2020 (PMC7145653)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7145653)

**HMDB**
- HMDB metabolite pages list ChemAxon-predicted properties in a predicted-properties table: "pKa (Strongest Acidic)", "pKa (Strongest Basic)" and "Physiological Charge" (e.g. −1, 0, −5), along with ChemAxon logP and PSA. — e.g. [HMDB0040256](https://hmdb.ca/metabolites/HMDB0040256); [BMDB0000822](https://bovinedb.ca/metabolites/BMDB0000822)

### Inferences
- Rhea's ORIGIN column likely works as follows. `computation` means Marvin's major-microspecies prediction was matched back to an existing ChEBI entity. `curation` means a curator asserted that the entity itself is the pH 7.3 form to be used. This can be a curator override where Marvin disagrees or fails (e.g. generic/R-group entities or polymers).
  - Evidence: all 898 curation rows are self-mappings, which fits "curator says use this entity as-is".
  - I found no Rhea documentation that defines ORIGIN explicitly, so this reading is inferred from the data.
- ChEBI's "major microspecies at pH 7.3" entities and the conjugate acid/base links appear to be produced with Marvin 6.2.0, the version cited in both Rhea 2015 and ChEBI entry comments. They are part of the Rhea/ChEBI curation collaboration at SIB/EBI. Version 6.2.0 dates from about 2014, which suggests many entries were created with that version and not necessarily recomputed.
- Rhea, MetaCyc and HMDB use slightly different pH values (7.3, 7.3 and likely 7.4). These differences, together with Marvin version changes, explain why borderline species (phosphate, ATP, imidazoles, thiols) can be assigned differently between resources.

### Gaps
- No explicit Rhea documentation defining ORIGIN `computation` vs `curation` was found. The Rhea help pages returned HTTP 403 to direct fetch.
- The current Marvin version used by Rhea/ChEBI is not documented after 6.2.0 (2015).
- Recon3D/VMH charge-assignment tool (ChemAxon or other) is unconfirmed. The Recon3D full text (PMC5840010) was not retrievable via Europe PMC.
- KEGG, LIPID MAPS and Reactome:
  - No primary documentation was retrieved. My unverified understanding is that KEGG and LIPID MAPS mostly depict neutral (uncharged) structures, and that Reactome reuses ChEBI identifiers.
  - None of this is sourced here and it should not be cited without verification.
- HMDB's own definition of "Physiological Charge" (the pH used) was not confirmed from HMDB documentation.

## Q2. Has any resource published plans or work to replace ChemAxon with an open tool?

### Takeaway
I found no resource that has actually replaced ChemAxon for production protonation or pKa. As of Sept 2026, ModelSEED was still regenerating its pH 7 data with Marvin 26.1. The eQuilibrator developers have repeatedly acknowledged the proprietary dependency, and the clearest community move toward an open alternative is a pKa-benchmarking proposal. That proposal names Dimorphite-DL and pkasolver and involves SIB (MetaNetX/Rhea), with Elad Noor initially listed.

### Cited Findings
- Elad Noor (June 2020) wrote: "The problem is, indeed, the fact that we rely on ChemAxon (a proprietary software) for the pKa calculation". He added that "we designed equilibrator-api to be fully open source and as easy to install as possible", and that an alternative could be added "as an 'extension' package to equilibrator". Users also reported that cxcalc on macOS did not support InChI input. — [equilibrator-users Google Group](https://groups.google.com/g/equilibrator-users/c/BXvntaUswIg)
- eQuilibrator 3.0 (2022) still uses Marvin 21.13.0 under an academic licence. — [PMC8728285](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728285)
- BioHackathon Europe 2024 proposal by Sébastien Moretti (SIB, ELIXIR-CH; MetaNetX), Robert Giessmann, and Elad Noor (entry struck through):
  - Goal: benchmark pKa predictors for biomolecules and propose a community standard.
  - It calls Marvin "One of the most commonly used predictors for pKa", says "their validation process is opaque", and notes ChemAxon "has recently changed its free academic license making it much more restrictive".
  - It says "few alternatives exist, and there is a dire need for open-source tools", and plans to evaluate Dimorphite-DL and pkasolver.
  — [HackMD: BioHackathon 2024 ideas](https://hackmd.io/@smoretti/SJ-bYnPx0T)
- ModelSEED's 2026 regeneration still uses Marvin 26.1, with RDKit only as a structure bridge. It is limited by ChemAxon licence groups: tautomerization needs the "Isomers Plugin Group" licence, which is not available. — [ModelSEEDDatabase PR #295](https://github.com/ModelSEED/ModelSEEDDatabase/pull/295)

### Inferences
- ChemAxon's tightened academic licensing is a documented pressure point mentioned by SIB staff. ModelSEED's licence-group limitation shows the same issue in practice. Both point to demand for an open pH 7.3 major-microspecies predictor (e.g. built on Dimorphite-DL, pkasolver, or similar ML pKa models), but no resource has yet announced a switch.

### Gaps
- I did not check the eQuilibrator GitLab issue tracker for later (2023-2026) work on open pKa. The outcome of the BioHackathon 2024 project (any publication or preprint) was not found.
- I found no Rhea, ChEBI or MetaCyc statements about replacing ChemAxon.

## Q3. What is documented about Rhea's pH 7.3 computation, and is ChemAxon named?

### Takeaway
Yes. ChemAxon Marvin is named explicitly. The 2012 Rhea paper describes the pKa calculator at pH 7.3 and 298 K. The 2015 paper gives the version (Marvin 6.2.0) and says curators verify participants with it. The Rhea help page says Marvin computes the major microspecies for all ChEBI entities. The 2022 paper describes the precomputed mapping file used by search. The ORIGIN column is not explained in the documents I found.

### Cited Findings
- Alcántara et al. 2012: pH 7.3 chosen "arbitrarily"; Marvin pKa calculator at 298 K; phosphate caveat. — [PMC3245052](https://pmc.ncbi.nlm.nih.gov/articles/PMC3245052)
- Morgat et al. 2015: "verified using the Marvin pKa calculator from ChemAxon (version 6.2.0)". — [PMC4384025](https://pmc.ncbi.nlm.nih.gov/articles/PMC4384025)
- Rhea help: Rhea uses Marvin to compute the major microspecies at pH 7.3 for all ChEBI entities and follows MetaCyc's policy. — [Rhea help](https://www.rhea-db.org/help/chebi-in-rhea)
- Bansal et al. 2022: a precomputed mapping of other protonation states to the pH 7.3 form is used in search, including exact search, and is downloadable. — [PMC8728268](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728268)
- In release 142, the mapping file has 121,834 `computation` rows (8,900 non-identity) and 898 `curation` rows (all identity). — [chebi_pH7_3_mapping.tsv](https://ftp.expasy.org/databases/rhea/tsv/chebi_pH7_3_mapping.tsv)

### Inferences
- Rhea is downstream of MetaCyc's pH 7.3 convention, and both use Marvin. Agreement between Rhea and MetaCyc on charge states is therefore partly by construction, not independent validation.

### Gaps
- No release notes were found that document Marvin version upgrades in Rhea, or a re-run of the mapping, after 2015.

## Q4. Are there documented disagreements between resources over the charge state of common metabolites?

### Takeaway
Explicit metabolite-by-metabolite disagreement reports were not found. The disagreement is documented structurally:
- MetaNetX deliberately merges protonation states, so cross-resource charge differences disappear and acid-base reactions become empty.
- ModelSEED reports protonation differences as a reaction-matching category against BiGG's iJR904, and a 20.3% net-charge change between Marvin versions/pipelines.
- MetaCyc's own forum post shows ATP as a near 57/43 split at pH 7.3.
- Rhea flags phosphate as a simplification.

### Cited Findings
- MNXref ignores "distinctions in protonation states" when merging, and its equations "may differ … with respect to proton balancing". — [PMC7778905](https://pmc.ncbi.nlm.nih.gov/articles/PMC7778905/)
- ModelSEED's comparison with E. coli iJR904 (BiGG) uses "identity matching with protonation comparison" as a category. This shows that protonation and charge differences between ModelSEED (pH 7) and BiGG models are common enough to be tracked. — [Seaver et al. 2021, Fig. 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC7778927)
- Regenerating ModelSEED with Marvin 26.1 changed net charge at pH 7 for 20.3% of shared compounds, an upper bound attributed partly to tautomer handling. — [PR #295](https://github.com/ModelSEED/ModelSEEDDatabase/pull/295)
- At pH 7.3, Marvin predicts ATP as about 57% −3 and 43% −4, and MetaCyc picked −3. — [ChemAxon forum](https://forum.chemaxon.com/6/4114/problems-with-pka-plugin-accuracy/)
- Contrast: in the Rhea mapping file (release 142), ATP CHEBI:15422 maps to CHEBI:30616, ATP(4−). Rhea therefore uses ATP(4−), whereas the older MetaCyc forum post reports Marvin choosing ATP(3−) at the time. — [Rhea mapping](https://ftp.expasy.org/databases/rhea/tsv/chebi_pH7_3_mapping.tsv) vs [ChemAxon forum](https://forum.chemaxon.com/6/4114/problems-with-pka-plugin-accuracy/)
- Phosphate: Rhea maps CHEBI:18367 → CHEBI:43474 (HPO4(2−)), and the 2012 paper flags this as a simplification because H2PO4(−) is close in abundance. — [PMC3245052](https://pmc.ncbi.nlm.nih.gov/articles/PMC3245052)
- Recon 2 uses pH 7.2 for all compartments, ModelSEED uses 7.0, and Rhea/MetaCyc use 7.3. These differing reference pHs are a source of systematic charge differences. — [Thiele 2013](https://www.nature.com/articles/nbt.2488); [Seaver 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7778927); [Bansal 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728268)

### Inferences
- The ATP difference (MetaCyc forum: −3; current Rhea mapping: −4) suggests that Marvin versions or curation changed the call for a borderline species. It may also reflect that MetaCyc later moved to ATP(4−). Current MetaCyc ATP charge was not verified here.

### Gaps
- No MetaNetX reconciliation notes listing specific charge conflicts were found.
- I did not check current MetaCyc ATP charge, or KEGG, LIPID MAPS or Reactome representations.
- No systematic published comparison of charge states across Rhea, MetaCyc, BiGG and ModelSEED was found.
