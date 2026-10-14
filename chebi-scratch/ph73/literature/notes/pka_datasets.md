# Experimental aqueous pKa datasets for an open protonation-state predictor (catalogue, licences, site labels, metabolite coverage)

Research date: 2026-10-14. About 20 tool calls. Items marked **UNVERIFIED** come from background knowledge and were not confirmed against a source in this session; they are listed under Gaps and Inferences, not under Cited Findings.

## Q0. Dataset catalogue (size, content, labelling, licence, access)

### Takeaway
Only a few large experimental pKa sets are both open and machine-readable: the IUPAC Digitized set (CC BY-NC), the Baltruschat/Czodrowski extracts (CC BY 4.0 or MIT, depending on the source; see below), ChEMBL (CC BY-SA 3.0), DataWarrior's pKaInWater (provenance undocumented) and the new pKaHub (article CC BY 4.0; data licence unconfirmed). Several sets used ChemAxon tools at some stage: Marvin in Baltruschat/Czodrowski, and Molconvert for name-to-structure in IUPAC. DataWarrior's site labels were curated by hand, according to its developer.

### Cited Findings

**IUPAC Digitized pKa Dataset (Zheng & Lafontant-Joseph; v2.4a)**
- 24,211 rows covering 10,626 unique molecules (unique by InChI). About 1,275 ambiguous entries were excluded from the high-confidence set. — [GitHub IUPAC/Dissociation-Constants](https://github.com/IUPAC/Dissociation-Constants)
- Digitized from Serjeant & Dempsey (1979, organic acids), Perrin (1965, organic bases) and the Perrin Supplement (1972). These are the IUPAC "Dissociation Constants of Organic Acids/Bases" compilations, so this dataset is the digitized form of the Perrin/Serjeant books. — [GitHub](https://github.com/IUPAC/Dissociation-Constants)
- Licence: CC BY-NC 4.0, with the required attribution "Reproduced by permission of International Union of Pure and Applied Chemistry." — [GitHub](https://github.com/IUPAC/Dissociation-Constants)
- Fields:
  - Temperature `T` (°C), plus `original_T` when the value was standardized.
  - Pressure, method, assessment (Reliable/Approximate/Uncertain), remarks and cosolvent.
  - Ionic strength appears in the abbreviations, but the README does not list it as its own column.
  - `pka_type` (e.g. pKaH, pKb), with parenthetical site notes such as "pK(indole-ring)", and `acidity_label` (A/AH/B). — [GitHub](https://github.com/IUPAC/Dissociation-Constants)
- How labels were assigned:
  - Names were converted to SMILES with OPSIN, PubChem and the Chemical Identifier Resolver. ChemAxon Molconvert (commercial) also helped. Only unambiguous translations were kept.
  - When a molecule has two pK values, the lower one is assigned basic and the higher one acidic by rule. Molecules with more than two values were examined by hand.
  - OCR used Amazon Textract (proprietary).
  - Site labels therefore come from the source text and heuristics, not from new experiments. — [GitHub](https://github.com/IUPAC/Dissociation-Constants)
- Zenodo DOI: 10.5281/zenodo.7236452. There is an accompanying RSC Advances paper (Zheng, Lafontant-Joseph & Green). — [GitHub](https://github.com/IUPAC/Dissociation-Constants)
- IUPAC also described the project in Chemistry International ("FAIR datasets for acid dissociation constants"). — [De Gruyter, Chem. Int. 2023](https://www.degruyterbrill.com/document/doi/10.1515/ci-2023-0310/html?lang=en)

**Baltruschat & Czodrowski, "Machine learning meets pKa" (F1000Research 2020, 9:113)**
- ChEMBL25 extract: 1,140 assays searched. After restricting to exact ("=") values with structures, 8,111 pKa values remained. — [F1000Research v2](https://f1000research.com/articles/9-113/v2)
- DataWarrior extract: 7,911 entries with valid structures. — [F1000Research v2](https://f1000research.com/articles/9-113/v2)
- Combined training set: 5,994 unique monoprotic molecules after preprocessing. External test sets: Novartis (280) and AvLiLuMoVe (123, curated from the literature; Settimo et al. 2014). — [F1000Research v2](https://f1000research.com/articles/9-113/v2)
- **ChemAxon Marvin was used for filtering:**
  - Marvin predicted pKa values for every molecule. Only molecules with at most one predicted pKa in the 2–12 range were kept (the monoprotic filter).
  - Entries whose Marvin prediction differed from the experimental value by more than 4 units were dropped as outliers.
  - Protonation was set at pH 7.4 with OpenEye QUACPAC.
  - Molecules containing nitro groups, B, Se or Si were removed, Lipinski's rule of five was applied, and only values in the pKa range 2–12 were kept. — [F1000Research v2](https://f1000research.com/articles/9-113/v2)
- Licence conflict:
  - The GitHub README says "The datasets are licensed under the CC BY 4.0 license" (datasets/LICENSE.txt). The code is MIT. — [GitHub czodrowskilab](https://github.com/czodrowskilab/Machine-learning-meets-pKa)
  - The F1000 article says both code and data are under MIT.
  - Data is archived at Zenodo doi:10.5281/zenodo.3662245. — [F1000Research v2](https://f1000research.com/articles/9-113/v2)
- The Novartis file is described as an in-house set provided by Novartis (Lewis & Rodde). — [GitHub](https://github.com/czodrowskilab/Machine-learning-meets-pKa)

**ChEMBL pKa assay data**
- ChEMBL is licensed CC BY-SA 3.0 Unported. — [PubChem RDF source record](https://rdf.ncbi.nlm.nih.gov/pubchem/source/ChEMBL); [Bioregistry](https://bioregistry.io/chembl)
- About 8.1k exact pKa values were found across about 1,140 assays in ChEMBL25. — [F1000Research v2](https://f1000research.com/articles/9-113/v2)

**DataWarrior pKaInWater (origin)**
- Ships in the DataWarrior installation's "reference" folder.
- The developer says it was compiled from the literature and hand-curated so that structures show the correct protonation state, and that "the original paper reference got lost or was never collected."
- The file "was given to me about 20 years ago." Duplicate values for the same atom were averaged, giving "mean from n" entries. — [openmolecules.org forum](https://openmolecules.org/forum/pdf.php?th=96); [openmolecules forum msg](https://openmolecules.org/forum/pdf.php?msg=1299)
- Contains the strongest acidic and strongest basic aqueous pKa for 7,912 chemicals. — [Mansouri ASCCT 2018 poster](https://ntp.niehs.nih.gov/sites/default/files/iccvam/meetings/ascct-2018/mansouri-poster.pdf)
- The poster is attributed only to a user named "thomas". This was not confirmed to be Thomas Sander. — (same forum)

**OPERA / Mansouri et al. 2019 (EPA/NIEHS)**
- Built from the DataWarrior 7,912-chemical set, with acidic and basic values modelled separately. Structures were curated in KNIME and descriptors computed with PaDEL. — [ASCCT poster](https://ntp.niehs.nih.gov/sites/default/files/iccvam/meetings/ascct-2018/mansouri-poster.pdf)
- Published in J. Cheminform. as "Open-source QSAR models for pKa prediction", DOI 10.1186/s13321-019-0384-1. No experimental method was given for 901 chemicals. — [J Cheminform figure page](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0384-1/figures/1); [PMC5843579 / OPERA](https://pmc.ncbi.nlm.nih.gov/articles/PMC5843579)
- The OPERA suite's code and data are on GitHub (kmansouri/OPERA). — [data.gov OPERA listing](https://catalog-old.data.gov/dataset/opera-models-for-predicting-physicochemical-properties-and-environmental-fate-endpoints)
- The labels are "strongest acidic/basic" macro values per molecule, with no site labels.

**SAMPL6 pKa (Işık et al. 2018, JCAMD 32:1117, doi:10.1007/s10822-018-0168-0)**
- 24 kinase-inhibitor-like fragments. Macroscopic pKas were measured by UV-metric titration on a Sirius T3. — [bioRxiv 368787](https://www.biorxiv.org/content/10.1101/368787v2); [SAMPL6 GitHub](https://github.com/samplchallenges/SAMPL6/tree/master/physical_properties/pKa)
- "For several compounds in which the microscopic protonation states associated with macroscopic pKas were ambiguous, we performed follow-up NMR experiments to disambiguate the microstates." These are experimentally determined site labels, but only for a subset. — [bioRxiv](https://www.biorxiv.org/content/10.1101/368787v2)

**SAMPL7 pKa**
- 22 compounds, mainly N-acylsulfonamides and bioisosteres. pKa was measured by potentiometric titration on a Sirius T3, with no NMR site assignment reported.
- Participants' predictions matched the macro pKas reasonably well but disagreed on the microscopic transitions. — [SAMPL7 evaluation, Springer](https://link.springer.com/article/10.1007/s10822-021-00397-3); [PubMed 34169394](https://pubmed.ncbi.nlm.nih.gov/34169394/)

**pKaHub (Sipos-Szabó, Bajusz, Balogh, Keserű; J. Chem. Inf. Model. 2026, 66(8):4607–4619, doi:10.1021/acs.jcim.6c00107)**
- Over 90,000 experimental aqueous pKa values spanning over 31,000 unique molecules. Entries are annotated for charge-state transitions and microspecies distributions, and the data is available through the "pKahub" online database. — [REAL MTAK repository record](https://real.mtak.hu/247419/)
- Used to benchmark ACD/Labs, ChemAxon, Epik and four open-source ML models. — [REAL MTAK](https://real.mtak.hu/247419/)
- The article itself is CC BY 4.0. — [REAL MTAK PDF metadata](https://real.mtak.hu/247419/1/ci6c00107.pdf)

**iBonD (Cheng Jin-Pei; Nankai/Tsinghua)**
- iBonD 2.0 holds more than 30,000 pKa values for about 20,000 compounds in various solvents (largely DMSO, plus water and others), and about 7,500 bond dissociation energies. — [ChemistryViews](https://chemistryviews.org/?p=40280)
- The first edition had more than 22,000 pKa values. — [Nankai](https://chemen.nankai.edu.cn/2021/0708/c24549a380534/page.htm)
- Terms: "free of charge for non-profit academic use". No formal licence was found. — [SJTU lecture page](https://news.sjtu.edu.cn/xsjz/20201018/132513.html)
- Hosted at ibond.nankai.edu.cn and ibond.chem.tsinghua.edu.cn. — [Tsinghua news](https://www.tsinghua.edu.cn/info/1181/58245.htm)

**NIST SRD 46 (Critically Selected Stability Constants of Metal Complexes, v8.0)**
- 6,166 ligands in 112,559 lines of data. Includes protonation constants, with heats and entropies, "under specified conditions" of temperature and ionic strength. Based on Martell & Smith.
- The database is **discontinued**. The download is a 32-bit Windows program. — [NIST SRD 46](https://www.nist.gov/srd/nist46)
- SRD copyright belongs to the US Secretary of Commerce under the Standard Reference Data Act (15 U.S.C. 290e). The required notice is "©Copyright … by the U.S. Secretary of Commerce … All rights reserved." Licensing is handled per product. — [NIST copyright/fair-use statements](https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications)
- One NIST SRD site states that SRD may not be reproduced "in any form or by any means … without prior permission." — [ICSD/NIST copyright](https://icsd.nist.gov/copyright.html)
- Non-SRD NIST works fall under 17 U.S.C. §105 (not copyrighted in the US). Redistribution is allowed with acknowledgement and a note of any changes. — [NIST statements](https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications)

**Goldberg/Tewari NIST TECRDB (Thermodynamics of Enzyme-Catalyzed Reactions)**
- About 1,000 papers covering about 400 reactions (Goldberg, Tewari & Bhat, Bioinformatics 2004, 20:2874). — [BioNumbers 103383](https://bionumbers.hms.harvard.edu/bionumber.aspx?id=103383); [NIST](https://www.nist.gov/node/608971)
- The data also appears in the J. Phys. Chem. Ref. Data series. No licence or download terms were found. — [NIST publication](https://www.nist.gov/publications/thermodynamics-enzyme-catalyzed-reactions-1-oxidoreductases)

**eQuilibrator (Alberty-based pseudoisomer tables)**
- Uses Alberty's framework of pseudoisomer tables (protonation states) to compute transformed energies at any pH and ionic strength. — [eQuilibrator tutorial](https://equilibrator.readthedocs.io/en/latest/tutorial.html); [eQuilibrator 3.0, PMC8728285](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728285)
- A related code file (third-party, so secondary) shows ChemAxon pKa predictions in the pipeline, with manual overrides taken from Alberty's book for some compounds, such as bicarbonate and metal cations. — [dGPredictor compound.py on HF](https://huggingface.co/spaces/vuu10/dGPredictor/blob/8896f64c26ed43eccb8589146addb1b14b28e2f0/CC/compound.py)
- Downloads are available. — [eQuilibrator download](https://equilibrator.weizmann.ac.il/download)

**Wiki-pS0 (Avdeef)**
- An intrinsic-solubility database: 6,355 entries for 3,014 molecules from 1,325 citations (ADMET & DMPK 2020, doi:10.5599/admet.766). — [hrcak](https://hrcak.srce.hr/clanak/341580)
- Also covered in Avdeef's CRC 2024 handbook. — [Routledge](https://www.routledge.com/Predicting-Solubility-of-New-Drugs-Handbook-of-Critically-Curated-Data/Avdeef/p/book/9781032617671)
- No licence or open download was found. It is a solubility set: pKa values are used as inputs, but it is not a pKa dataset.

### Inferences
- The Baltruschat set's "experimental" values were filtered by agreement with Marvin predictions. That biases the set toward Marvin-predictable chemistry, and the monoprotic filter removes almost all metabolites (phosphates, polyacids, amino acids). It is a poor test set for biochemicals and is not "commercial-software-free."
- DataWarrior and OPERA give one strongest-acid and one strongest-base value per molecule, with no documented provenance. They are usable for macro-level testing only.
- SAMPL6 is the only set found here with NMR-confirmed microstates, but it covers just 24 drug-like fragments and no metabolites.

### Gaps
- Exact pKaHub data licence, source composition and the software used for microspecies annotation could not be read (PDF text extraction failed). Note that it benchmarks ChemAxon and Epik, so its microspecies annotations may depend on software. Check the SI at pubs.acs.org/doi/suppl/10.1021/acs.jcim.6c00107.
- The exact text of datasets/LICENSE.txt in czodrowskilab (CC BY 4.0 versus MIT) was not fetched because GitHub API access was blocked.
- SAMPL6 and SAMPL7 repository licences were not confirmed. **UNVERIFIED**: the samplchallenges repos carry MIT/CC-BY-style licences.
- OPERA pKa data licence not confirmed. **UNVERIFIED**: the OPERA GitHub is MIT, and EPA data is generally US-government public domain.
- **Not researched (no sources fetched):** Settimo 2014 (beyond its use as AvLiLuMoVe), Avdeef/Sirius/Pion sets, OChem pKa, Morgenthaler/Roche, AstraZeneca ChEMBL deposition, Williams/Evans tables, CRC/Lange's, Jencks & Regenstein, BRENDA/BioNumbers, AqSolDB.
  - **UNVERIFIED** recollections: AstraZeneca deposited a physicochemical set in ChEMBL (CHEMBL3301361), but it is logD/solubility rather than pKa. The Evans and Williams tables are freely viewable PDFs with no open licence. The CRC Handbook and Lange's are commercial copyrighted works. OChem data mixes licences per record.

## Q1. Which datasets are licence-compatible with CC0 or CC BY redistribution of derived rules/data?

### Takeaway
Only the Baltruschat/Czodrowski extracts (CC BY 4.0 or MIT), possibly pKaHub (unconfirmed) and US-government non-SRD data are clearly compatible with CC BY output. ChEMBL is share-alike, IUPAC is non-commercial, and iBonD is academic-only. NIST SRD 46 is copyrighted and needs permission.

### Cited Findings
- IUPAC Digitized: CC BY-NC 4.0, so it cannot be relicensed as CC0/CC BY or used commercially. — [GitHub](https://github.com/IUPAC/Dissociation-Constants)
- Baltruschat/Czodrowski datasets: CC BY 4.0 according to the README, MIT according to the F1000 article. Both are permissive. — [GitHub](https://github.com/czodrowskilab/Machine-learning-meets-pKa); [F1000](https://f1000research.com/articles/9-113/v2)
  - Caveat: the ChEMBL25 part comes from CC BY-SA 3.0 ChEMBL. — [PubChem RDF](https://rdf.ncbi.nlm.nih.gov/pubchem/source/ChEMBL)
- ChEMBL: CC BY-SA 3.0. Redistributed derived data must stay share-alike. — [Bioregistry](https://bioregistry.io/chembl)
- iBonD: "free of charge for non-profit academic use". — [SJTU](https://news.sjtu.edu.cn/xsjz/20201018/132513.html)
- NIST SRD 46: copyright held by the US Secretary of Commerce, "All rights reserved"; discontinued. — [NIST](https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications); [SRD46](https://www.nist.gov/srd/nist46)
- pKaHub article: CC BY 4.0 (data terms not found). — [REAL MTAK](https://real.mtak.hu/247419/)

### Inferences
- Individual pKa values are facts and are generally not copyrightable. The licence restrictions bite on the compilation (selection, structure SMILES, curation). A clean-room approach is defensible: re-extract individual values from primary literature, cite each one, and release under CC0/CC BY. Inheriting the CC BY-NC IUPAC table or the CC BY-SA ChEMBL tables wholesale is not.
- Derived rules (e.g. SMARTS with typical pKa ranges) learned from many sources are less likely to be considered a "substantial part" of any one database. They should still avoid one-to-one transcription of NC/SA tables.
- The ChEMBL portion of the Baltruschat set may arguably still carry CC BY-SA obligations despite the dataset's CC BY/MIT label. Treat it conservatively.

### Gaps
- No legal analysis was found specific to pKa tables. The facts-versus-compilation distinction is a general principle, not verified here for this case.

## Q2. Which datasets have explicit experimentally determined (e.g. NMR) site labels?

### Takeaway
Very few. SAMPL6 has NMR-resolved microstates for a subset of 24 compounds. IUPAC carries site notes from the original authors' text. DataWarrior has hand-curated protonation sites with no provenance. Baltruschat and pKaHub (possibly) rely on software.

### Cited Findings
- SAMPL6: NMR used to disambiguate microstates for "several compounds". — [bioRxiv](https://www.biorxiv.org/content/10.1101/368787v2)
- SAMPL7: Sirius T3 potentiometric macro pKa only; predicted microscopic transitions disagreed widely. — [Springer](https://link.springer.com/article/10.1007/s10822-021-00397-3)
- IUPAC: parenthetical site notes taken from the source books. Basic/acidic labels are assigned by a lower/higher rule for two-value molecules and by hand for the rest. — [GitHub](https://github.com/IUPAC/Dissociation-Constants)
- DataWarrior: structures hand-curated "such that the structures represent the correct protonation state", with no source references. — [openmolecules forum](https://openmolecules.org/forum/pdf.php?th=96)
- Baltruschat: Marvin used for the monoprotic filter and outlier removal; QUACPAC sets protonation. — [F1000](https://f1000research.com/articles/9-113/v2)
- NMR is considered the gold standard for site-resolved pKa, with about 0.1 unit error (protein context). — [PKADR manuscript](https://sites.krieger.jhu.edu/damjanovic-lab/files/2025/09/manuscript_PKADR.pdf)

### Inferences
- For metabolites, the best experimentally determined micro-pKa labels will come from primary NMR/titration papers, e.g. on amino acid zwitterions, phosphate versus adenine N1 in ATP, and the purine N7/N1 sites. These need manual curation; no open dataset was found that collects them.

### Gaps
- No open, NMR-derived micro-pKa compilation for small molecules or metabolites was found.

## Q3. Best open source of pKa values for common metabolites

### Takeaway
No single open, permissively licensed source was found.
- The IUPAC Digitized set (Perrin/Serjeant) likely has the broadest coverage of amino acids, organic acids, purines/pyrimidines and phosphates, but it is non-commercial.
- Alberty-style pseudoisomer tables (via eQuilibrator) cover ATP, NAD and sugar phosphates, but are partly backed by ChemAxon predictions.
- NIST SRD 46 (Martell & Smith) is the classic critical source for nucleotides and phosphates, but it is copyrighted and discontinued.

### Cited Findings
- IUPAC Digitized draws on Perrin 1965/1972 (bases) and Serjeant & Dempsey 1979 (acids). — [GitHub](https://github.com/IUPAC/Dissociation-Constants)
- NIST SRD 46 has protonation constants for 6,166 ligands with temperature and ionic-strength conditions. — [NIST SRD46](https://www.nist.gov/srd/nist46)
- eQuilibrator uses Alberty's pseudoisomer framework. Its pKa inputs mix ChemAxon predictions with manual Alberty overrides (secondary source). — [eQuilibrator docs](https://equilibrator.readthedocs.io/en/latest/tutorial.html); [compound.py](https://huggingface.co/spaces/vuu10/dGPredictor/blob/8896f64c26ed43eccb8589146addb1b14b28e2f0/CC/compound.py)
- TECRDB has equilibrium data for about 400 enzyme reactions, some with pK values and conditions; no licence was found. — [BioNumbers](https://bionumbers.hms.harvard.edu/bionumber.aspx?id=103383)

### Inferences
- A practical route for a CC0/CC BY metabolite set:
  1. Hand-curate about 100–300 metabolite pKa values from primary literature and from Alberty's published tables (Alberty's NIST-authored work may be US-government §105). Note: the 17 U.S.C. §105 status is inferred from the NIST statement on non-SRD works.
  2. Cite each value individually.
  3. Use IUPAC, NIST SRD 46 and iBonD only as cross-checks, not as redistributed sources.

### Gaps
- Coverage of each named metabolite class was not quantified in any dataset (no breakdown found). Flavins and CoA in particular were not verified in any source.
- Alberty's "Thermodynamics of Biochemical Reactions" tables (Mathematica packages) were not checked for licence. **UNVERIFIED**: they were distributed through MathSource/Wolfram Library.

## Q4. Database-right issues (EU sui generis) for compiled handbook tables

### Takeaway
The EU Database Directive 96/9/EC protects compilations that required substantial investment. It blocks extraction or reuse of all or a substantial part for 15 years, renewable on substantial change. Handbook pKa tables (CRC, Lange's, Perrin, Martell & Smith/NIST 46) are plausibly covered in the EU, so copying them wholesale into an open dataset is risky. Taking insubstantial parts, or re-sourcing values from primary literature, is safer.

### Cited Findings
- The sui generis right protects substantial investment in "obtaining, verifying or presenting" contents. It lets the maker prevent extraction or reuse of the whole or a substantial part, and lasts 15 years, renewable on substantial new investment. — [EUR-Lex summary](https://eur-lex.europa.eu/EN/legal-content/summary/legal-protection-databases.html); [Open Rights Group wiki](https://wiki.openrightsgroup.org/wiki/Databases)
- Non-original databases, including scientific compilations, can be protected if the investment was substantial. — [EC digital strategy evaluation](https://digital-strategy.ec.europa.eu/lv/node/3059)
- Lawful users may extract insubstantial parts. There is an exception for illustration in teaching or scientific research. — [EUR-Lex summary](https://eur-lex.europa.eu/EN/legal-content/summary/legal-protection-databases.html)
- ECJ case law from 2004 (secondary source) narrowed the right: investment in *creating* data, as opposed to obtaining existing data, does not count. — [IIP Japan bulletin](https://www.iip.or.jp/e/summary/pdf/detail2006/e18_15.pdf)

### Inferences
- The 15-year term means the older Perrin (1965/1972) and Serjeant (1979) compilations' sui generis rights may have lapsed unless they were renewed by substantial updates. The IUPAC digitization (2022+) is a new database with its own investment, and it also carries the CC BY-NC licence and copyright in the presentation.
- The research exception does not cover redistributing a CC0 dataset.
- US law has no sui generis right, so facts and non-creative compilations are freer there (Feist principle, not verified here). Licence terms (contract) still apply.

### Gaps
- The CJEU's British Horseracing Board (C-203/02) holding and the Feist precedent are cited from background knowledge only and were not fetched.
- No case law specific to scientific constant tables was found.
