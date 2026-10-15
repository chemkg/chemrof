# Biochemical edge cases in predicting the major protonation state at pH ~7.3

Scope note: research conducted 2026-10-14 under a budget of about 15 tool calls. Many textbook pKa values I expected to cite could not be confirmed against a fetched source within that budget. Those values are listed under "Gaps" and should not be stated as sourced. Values marked "verified" below are ones where a search result gave the number with a URL. Most of the URLs are search-result pages or abstracts. I did not read the full texts.

## How do Rhea/ChEBI, eQuilibrator and metabolic models assign pH 7.3 forms, and what errors are documented?

### Takeaway
Rhea/ChEBI and eQuilibrator both get their protonation states from ChemAxon Marvin. Rhea and ChEBI use the "major microspecies at pH 7.3", and curators check it by hand. eQuilibrator uses Marvin pKa values to compute pseudoisomer distributions. I found no published, systematic list of ChemAxon errors for biochemicals. The documented problems are anecdotal: software bugs, errors of about 2 pH units for microstates of amphoteric or multiprotic compounds, and spurious pKa values for metal ions.

### Cited Findings
- Rhea uses only the ChEBI entity that is the major microspecies at pH 7.3, to keep reactions non-redundant and balanced. It computes that microspecies for all ChEBI entities with ChemAxon Marvin pKa software. The mapping is published as a download and as extra relationships in the ChEBI OWL file. — [Rhea help: ChEBI in Rhea](https://www.rhea-db.org/help/chebi-in-rhea)
- Rhea curators check that every reaction participant is the major microspecies at pH 7.3 and that mass and charge balance. — [Rhea help: reaction curation](https://www.rhea-db.org/help/reaction-curation)
- Documented ChemAxon bug: MarvinSketch 6.1.3 and 6.1.4 failed to compute the major microspecies of water at pH 7.3. The reporter described this calculation as a routine step in normalizing Rhea compounds. ChemAxon confirmed the bug and fixed it in 6.2. — [ChemAxon forum: Major Microspecies plugin does not work](https://forum.chemaxon.com/6/9347/major-microspecies-plugin-does-not-work/)
- ChEBI pH 7.3 entities are explicitly Marvin-derived. For example, ChEBI's "tetracycline zwitterion" (CHEBI:77932) is labelled the major microspecies at pH 7.3 "according to Marvin". The speciation is computed, not measured. — [ChEBI CHEBI:77932](https://www.ebi.ac.uk/chebi/CHEBI:77932)
- EnzChemRED notes that ChEBI has several protonation-state IDs per compound, so it mapped IDs to the pH 7.3 form. — [EnzChemRED, Sci Data 2024](https://www.nature.com/articles/s41597-024-03835-7)
- eQuilibrator 3.0 estimates acid-base dissociation constants with ChemAxon Marvin Calculator; the arXiv version cites Marvin 18.23.0. It also adds a Mg2+ correction because pKa and pMg together set the speciation of ATP and ADP. — [eQuilibrator 3.0, NAR 2022](https://academic.oup.com/nar/article/50/D1/D603/6445959); [arXiv 2103.00621](https://arxiv.org/pdf/2103.00621)
- A chemRxiv preprint (2024, not peer reviewed) says ChEMBL pKa values come from ChemAxon's calculator. It reports microstate pKa errors of nearly 2 pH units for EDTA and errors of about 2 units for amino acid microstates. — [chemRxiv 2024-msd0q-v2](https://chemrxiv.org/doi/pdf/10.26434/chemrxiv-2024-msd0q-v2)
- In the component-contribution / dGPredictor code that uses ChemAxon pKa output, the developers note that ChemAxon gives metal cations several pKa values, "which is obviously a bug", and override them by hand. — [dGPredictor compound.py (HuggingFace)](https://huggingface.co/spaces/vuu10/dGPredictor/blob/main/CC/compound.py)
- A ChemAxon-reported validation summary gives prediction error of 0.1 ± 1.1 for compounds with a single ionizable proton and 0.9 ± 3.2 for amphoteric substances. Amphoteric compounds (zwitterions, multiprotic metabolites) are the weak spot. — [ChemAxon validation results](https://dl.chemaxon.com/docs/HTML/docs1750/Validation_results.html) (as summarised in search results; not read in full)
- Liao and Nicklaus (J Chem Inf Model 2009, 49:2801) compared nine pKa predictors on 197 drugs (261 pKa values). The best mean absolute deviations were ADME Boxes 0.389, ACD/pKa DB 0.478 and SPARC 0.651. The quantum-chemical Jaguar had MAD 1.283. The set is pharmaceuticals, not metabolites. — [Liao & Nicklaus 2009 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7289148); [ChemAxon summary page](https://chemaxon.com/publication/Comparison-of-Nine-Programs-Predicting-pKa-Values-of-Pharmaceutical-Substances)

### Inferences
- A typical error of 0.5 to 1 pKa unit, and worse for amphoteric compounds, means any metabolite with a predicted pKa within about 1 unit of 7.3 has an uncertain "major microspecies" in Rhea/ChEBI. Curators should check these against measured values.
- Rhea, ChEBI, eQuilibrator and MetaNetX-derived models all use ChemAxon, so their errors are correlated, not independent. Agreement between them is not validation.

### Gaps
- I found no peer-reviewed benchmark of Marvin (or Epik, or ACD) against measured pKa values for a metabolite-focused set, and no published list of ChEBI pH 7.3 forms that were later corrected.
- I could not retrieve Haraldsdóttir et al. (Recon/Recon3D charge and directionality work) or the Human-GEM charge-curation papers within the budget. Their methods sections should be checked for documented disagreements between ChemAxon and measured values.
- MetaCyc's and BiGG's charge-assignment procedures (MetaCyc also states pH 7.3; BiGG inherits from model authors) were not verified here.

## Flavins (riboflavin, FMN, FAD)

### Takeaway
The isoalloxazine N3-H is weakly acidic (pKa about 10), so it is neutral at pH 7.3. The ionization that matters for FMN and FAD is on the phosphate groups. I did not verify the exact N3 value or the FMN phosphate pKa2 against a primary source.

### Cited Findings
- A Sigma-Aldrich riboflavin product sheet lists pKa = 9.69 without assigning the site. — [Sigma-Aldrich R9504 product information](https://perfqws.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/191/415/r9504pis.pdf)

### Inferences
- With N3-H pKa near 10, riboflavin is neutral at pH 7.3 and the ring is undissociated in FMN and FAD. The predicted charge of FMN depends mainly on its phosphate monoester pKa2 (about 6.2 if typical; not verified). With pKa2 about 1 unit below 7.3, FMN(2-) should dominate at roughly 90%. FAD's pyrophosphate diester is fully deprotonated, giving FAD(2-).

### Gaps
- No primary source verified for riboflavin N3 pKa (commonly given as about 10.0 to 10.2), the FMN phosphate pKa2, or the FAD ionization constants. Macheroux et al. (BMC Biochem 2005, reduced flavin ionization) was surfaced but not read.
- Reduced flavins (FMNH2, FADH2) have an N1 pKa of about 6.7 in the literature. I did not verify this, but if correct it is a borderline case close to 7.3.

## Purines and urate

### Takeaway
Uric acid (pKa1 5.4) is a monoanion at pH 7.3. Which ring nitrogen loses the proton (N3 vs N9) is contested. Xanthine is the classic borderline case: its N3-H pKa is close to 7.3, and it is roughly evenly split between neutral and anion at physiological pH. 1-Methyladenosine (pKa about 8.25) is mostly cationic at pH 7.3, and some sources wrongly call its charge "permanent".

### Cited Findings
- Uric acid is diprotic, pKa1 = 5.4 and pKa2 = 10.3, so urate predominates at physiological pH. — [chemistry-online: uric acid](https://www.chemistry-online.com/molecules/uric-acid/)
- DFT (B3LYP/6-311++G(d,p), PCM water, 2004): the N3-deprotonated monoanion is the most stable monoanion, and the N3,N9 dianion is the most stable dianion. The keto (lactam) neutral tautomer is the most stable. — [Int J Quantum Chem 100:801 (2004)](https://onlinelibrary-wiley-com-443.webvpn.zafu.edu.cn/doi/abs/10.1002/qua.20246)
- A 2023 Fukui-function study combining experimental pKa values with tautomerization energies found two monoanions of comparable relevance, differing in which ring is deprotonated. The monoanion site assignment is therefore not settled. — [Cumhuriyet repository record](https://acikerisim.cumhuriyet.edu.tr/items/aea07318-6dff-4ab4-9b69-da92d0ce9262)
- Xanthine shows essentially no tautomeric shifts in water but is nearly equally populated by anionic and neutral forms at physiological pH (first-principles study). — [UTMB: first-principles pKa and tautomers of xanthine](https://researchexperts.utmb.edu/en/publications/first-principles-calculations-of-the-pksubasub-values-and-tautome/)
- Xanthosine and its nucleotides ionize at N3 with pKa about 5.3 to 5.7 and are mainly or entirely monoanions at physiological pH. 9-Methylxanthine deprotonates more than 99% at N3-H. Guanine and hypoxanthine instead lose the N1-H, at higher pH. — [Acta Biochim Pol review on xanthine acid/base properties](https://abp.ptbioch.edu.pl/index.php/abp/article/download/3587/2645); [PMC2721690 fig. 2 (dX ionizes at N3, pKa about 5.7)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2721690/figure/F2)
- 1-Methyladenosine (m1A) has pKa about 8.25, compared with about 3.5 for adenosine N1, so N1 methylation leaves the base positively charged under physiological conditions. — [PMC101250](https://pmc.ncbi.nlm.nih.gov/articles/PMC101250); [Glen Research m1A](https://www.glenresearch.com/10-3005.html)
- Some commercial product pages call the m1A charge "permanent", which contradicts a pKa of 8.25. — [Smolecule product page](https://www.smolecule.com/products/s1493221) (low-quality source, cited only as an example of the error)

### Inferences
- Xanthine at pH 7.3 is a true borderline case (free-base N3 pKa reported about 7.4 to 7.5, not verified). Either the neutral or the N3-anion could be called "major". Database choices will differ by small shifts in the predicted pKa. Xanthosine and XMP are clearly anionic at the base (pKa about 5.7).
- For m1A, Henderson-Hasselbalch gives log(BH+/B) = 8.25 - 7.3 = 0.95, so about 90% cationic. The cation is the correct major microspecies, but this is a pKa-dependent charge, not a quaternary one. Free 1-methyladenine has a reported pKa of about 7.2 (not verified), which would make it borderline.
- The uric acid monoanion site (N3 vs N9) changes the SMILES and InChI of the pH 7.3 form but not the net charge (-1). Databases may legitimately disagree on the tautomer.

### Gaps
- No verified source for: adenine N1 pKa (about 4.2) and N9-H (about 9.8); guanine N1-H (about 9.2) and N7 (about 3.3); hypoxanthine N1-H (about 8.9); free xanthine N3 pKa (about 7.4 to 7.7); free 1-methyladenine pKa.

## Pyrimidines

### Takeaway
Uracil, thymine and cytosine are neutral at pH 7.3. 6-Azauridine (N3-H pKa about 6.8) is a notable exception: it is mostly anionic at pH 7.3, and predictors that treat it like uridine (pKa 9.3) will get it wrong.

### Cited Findings
- Introducing N6 lowers the uridine NH pKa from 9.3 to 6.8 in 6-azauridine. — [PMC3466602](https://pmc.ncbi.nlm.nih.gov/articles/PMC3466602)
- 6-Azauridine is about 100-fold more acidic than uridine. A fluorescent thiophene-modified 6-azauridine analogue gave pKa 6.7 to 6.9. — [PMC7726947 (ACS Omega)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7726947)

### Inferences
- With pKa 6.8, 6-azauridine at pH 7.3 is about 76% anionic (N3-). The anion is the major form, but only about 0.5 units from the boundary. 6-Azauracil (literature pKa about 7.0, not verified) would be about 67% anion and is borderline.
- 5-Fluorouracil (literature N3 pKa about 8.0, not verified) would be about 83% neutral at pH 7.3 and has a non-trivial anion fraction.

### Gaps
- No verified primary source for uracil (about 9.4), thymine (about 9.9), cytosine N3 (about 4.6), 5-fluorouracil (about 8.0) or free 6-azauracil pKa.

## Phosphates and phosphonates

### Takeaway
Inorganic phosphate (pKa2 7.21) is the canonical borderline case: at pH 7.3, HPO4(2-) and H2PO4(-) are about 55:45. Phosphate monoester and nucleotide pKa2 values (about 6 to 7) put the dianion in the majority, but they depend strongly on ionic strength and Mg2+. Literature values for ATP's terminal pKa range from about 6.5 to 7.6 depending on conditions. Phosphonate pKa2 values (higher than those of phosphate esters) make phosphonates borderline too, but I could not verify specific values.

### Cited Findings
- H3PO4: pKa 2.16, 7.21, 12.32 (25 °C). — [Saylor General Chemistry, appendix C](https://saylordotorg.github.io/text_general-chemistry-principles-patterns-and-applications-v1.0/s31-appendix-c-dissociation-consta.html)
- One compilation (Gnaiger 1994) gives HATP(3-) ⇌ ATP(4-) + H+ pK 7.60, HADP(2-) ⇌ ADP(3-) + H+ pK 7.18, and H2ATP(2-) ⇌ HATP(3-) pK 4.68. These are presumably zero-ionic-strength thermodynamic values, much higher than the commonly quoted apparent pKa of about 6.5 at physiological ionic strength. — [Gnaiger 1994, BTK-207](https://mitofit.org/images/a/a4/Gnaiger_1994_BTK-207.pdf)
- Alberty's framework treats ATP as a sum of species at specified pH, pMg and ionic strength. The tables are in *Thermodynamics of Biochemical Reactions* (2003), and IUBMB/IUPAC give recommendations for tables of biochemical thermodynamics. — [Alberty 1993, Biophys J (PMC1225844)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1225844); [IUBMB thermodynamics recommendations](https://iubmb.qmul.ac.uk/thermod/th1t3.html)
- eQuilibrator explicitly corrects for Mg2+ binding of ATP and ADP because pKa and pMg together set speciation. — [eQuilibrator 3.0](https://academic.oup.com/nar/article/50/D1/D603/6445959)
- Glyphosate pKa values vary between sources. ATSDR gives 0.8, about 3, about 6 and about 11 in one table and 2.6, 5.6, 10.6 in a figure. Another source gives 2.27, 5.58, 10.25. — [ATSDR Tox Profile 214 ch. 4](https://www.atsdr.cdc.gov/ToxProfiles/tp214-c4.pdf); [Imperial College glyphosate page](https://ch.ic.ac.uk/local/projects/j_england/reactiv.html)

### Inferences
- Pi at pH 7.3: log(HPO4/H2PO4) = 7.3 - 7.21 = 0.09, so the ratio is about 55:45. "Major microspecies" here is essentially arbitrary, and a predictor error of 0.1 units can flip it. Rhea uses hydrogenphosphate (HPO4(2-)) for Pi.
- ATP: whether the major form is ATP(4-) or HATP(3-) depends on whether you use pK 7.6 (I = 0) or about 6.5 to 6.9 (I about 0.1 to 0.25 M). The convention (ChEBI uses ATP(4-)) is defensible only with the ionic-strength-corrected value.
- Glyphosate at pH 7.3: the phosphonate second pKa (about 5.6 to 6) is below 7.3 and the amine pKa (about 10 to 11) is above it. That gives a net charge of -2 (two anionic sites on the phosphonate, carboxylate -1, ammonium +1), regardless of which compilation is used.

### Gaps
- Not verified: methylphosphonate pKa2 (about 7.5 to 7.7), fosfomycin pKa values (pKa2 about 6.5 to 7.5 reported variously), phosphoenolpyruvate pKa (about 6.3), sugar-phosphate monoester pKa2 (glucose 6-phosphate about 6.1), and Alberty-table values. I found none with a URL in this session.

## Polyamines

### Takeaway
Putrescine is +2 at pH 7.3. Spermidine is +3. Spermine is mostly +4, but its last pKa (reported values range from about 7.9 to 8.9) means the +3 form is significant. Published pKa sets for spermine differ by about 1 unit for the lowest step.

### Cited Findings
- A literature compilation table (Molecules 2018) lists spermine pK values 11.50, 10.95, 9.79, 8.90; spermidine 11.6, 10.8, 9.5; and putrescine 10.8, 9.4. — [Molecules 23:1112, table 1 (PMC6100306)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6100306/table/molecules-23-01112-t001)
- NMR (13C, 1H-15N) studies have determined protonation sequences and microscopic pKa values for spermine and spermidine. — [Anal Bioanal Chem 2003, s00216-003-2020-0](https://link.springer.com/article/10.1007/s00216-003-2020-0); [Amino Acids 2009, s00726-009-0409-6](https://link.springer.com/article/10.1007/s00726-009-0409-6)

### Inferences
- Spermine with lowest pKa 8.90: about 97.5% fully protonated (+4) at pH 7.3. If the lowest pKa is about 7.9 (an older value, not verified), then +4 is only about 80%. Either way +4 is the major species, but the effective charge is less than 4 in both cases.
- The lowest spermine pKa belongs to the secondary or primary amines through microscopic coupling, which is a case where "which N is deprotonated" in the +3 species is ill-defined.

### Gaps
- I did not obtain the microscopic constants from the NMR papers (full text not read).

## Tetracyclines, flavonoids and anthraquinones

### Takeaway
Tetracycline's middle pKa (7.7) lies close to 7.3, so at pH 7.3 the zwitterion (net 0) and the anion (net -1) are both substantial. ChEBI picks the zwitterion on the basis of Marvin. Quercetin's first pKa (about 7.0) makes it borderline as well, and predictor outputs for quercetin span a wide range.

### Cited Findings
- Tetracycline pKa 3.3, 7.7, 9.7 (25 °C). — [Sigma-Aldrich T3383 product information](https://perfqws.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/348/160/t3383pis.pdf)
- Site assignments: C3-OH (vinylogous acid) 3.3; C10 phenol/C12 enol system 7.7; dimethylammonium 9.7; isoelectric point about 4.8. — [Spektrum Lexikon der Chemie: Tetracycline](https://www.spektrum.de/lexikon/chemie/tetracycline/9080)
- ChEBI "tetracycline zwitterion" is the major microspecies at pH 7.3 according to Marvin. — [CHEBI:77932](https://www.ebi.ac.uk/chebi/CHEBI:77932)
- Quercetin spectrometric pK1 = 7.03, pK2 = 9.15 (site not assigned in the abstract). — [Z Naturforsch B 1998, znb-1998-0310](https://www.degruyterbrill.com/document/doi/10.1515/znb-1998-0310/html)
- Simulations Plus (2023) shows predicted flavonoid ionization differing widely between methods. — [Simulations Plus "Ionization of Flavonoids" (2023)](https://www.simulations-plus.com/wp-content/uploads/Ioniz-Flavonoids-14Nov2023.pdf)
- Biler et al. (PCCP 2017) studied position-specific deprotonation of quercetin and analogues. — [PCCP 2017, c7cp03845c](https://pubs.rsc.org/mk/content/articlelanding/2017/cp/c7cp03845c)

### Inferences
- Tetracycline at pH 7.3: with pKa2 7.7, the zwitterion is about 72% and the anion about 28%. Marvin's choice of the zwitterion agrees with the measured macro-pKa, but the protonation site of the anion (C10 vs C12) is a microspecies question.
- Quercetin at pH 7.3 (pK1 7.03): the anion is about 65%, so the major microspecies is the monoanion, but only marginally. The 7-OH is generally considered the most acidic site in flavones (not verified here). Databases that list neutral quercetin as the pH 7.3 form may be in error, and the case should be treated as borderline.

### Gaps
- No verified anthraquinone pKa values (for example emodin or alizarin) or other polyketide values were found within the budget.

## Imines and imino acids (P5C, P2C, Schiff bases)

### Takeaway
1-Pyrroline-5-carboxylate has a reported imine pKa of about 6.1. At pH 7.3 the neutral imine (net charge -1, carboxylate only) would dominate, not the iminium zwitterion. Predictors and databases often draw the iminium zwitterion by analogy with proline, so this needs checking.

### Cited Findings
- 1-Pyrroline-5-carboxylic acid: pKa 1.82 and 6.07 (sites not assigned on the page). It is in spontaneous equilibrium with glutamate-5-semialdehyde. — [Wikipedia: 1-Pyrroline-5-carboxylic acid](https://en.wikipedia.org/wiki/1-Pyrroline-5-carboxylic_acid)
- HMDB/ECMDB describe P5C as forming spontaneously when L-glutamate γ-semialdehyde dehydrates in water. — [HMDB0001301](https://www.hmdb.ca/metabolites/HMDB0001301)

### Inferences
- If 6.07 is the iminium pKa (the 1.82 value is plausibly the carboxyl), then at pH 7.3 about 94% of P5C is the anion with a neutral C=N. The major microspecies is the -1 anion, not the zwitterion. This is a plausible source of disagreement between ChEBI and models. Not verified against ChEBI's current pH 7.3 entry.
- P5C also shows ring-chain tautomerism with GSA and hydration. These are covalent equilibria, which a microspecies predictor does not represent.

### Gaps
- No primary measurement of the P5C imine pKa (the Wikipedia reference was not traced). Nothing found for 1-pyrroline-2-carboxylate or Schiff-base (PLP aldimine) pKa values.

## Amino acid side chains and peptide termini

### Takeaway
Histidine side chain (pKa about 6.0) is mostly neutral at pH 7.3, with about 5% cationic. Cysteine thiol (8.4) is mostly protonated. Tyrosine, lysine and arginine are unambiguous. Free amino acid α-amino pKa is about 9 to 10. Peptide N-terminal amines are lower (about 7.7 to 8 is the textbook figure, not verified), so they are mostly but not entirely protonated.

### Cited Findings
- Side chain pKa: His 6.00, Cys 8.39, Tyr 10.05, Lys 10.53. — [PMC2286538 table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC2286538/table/t3)
- Arg side chain about 12.48, with other tables giving 12.0 to 13.2. The tables also note that free amino acid values differ from values inside proteins. — [Keene State amino acid pKa table](https://academics.keene.edu/rblatchly/Chem220/hand/npaa/aawpka.htm); [Thermo Fisher amino acid properties](https://www.thermofisher.cn/cn/en/home/life-science/protein-biology/protein-biology-learning-center/protein-biology-resource-library/pierce-protein-methods/amino-acid-physical-properties.html)

### Inferences
- Imidazole itself (about 7.0, not verified) and histamine's ring are much closer to 7.3 than histidine's side chain, so they are borderline cases.
- Arginine pKa has been revised upward to about 13.8 in later literature (Fitch et al. 2015, not verified here). This makes no difference at pH 7.3.

### Gaps
- No verified source for the peptide N-terminal pKa, free imidazole or histamine pKa, or the revised arginine pKa of 13.8.

## Inorganic species (carbonate, sulfite, nitrite, phosphate)

### Takeaway
Bicarbonate (pKa1 6.35) is about 90% at pH 7.3 and is clearly major. Sulfite (pKa2 7.2) and phosphate (7.21) are true 50:50 borderline cases. Nitrite (pKa about 3.3) is fully anionic.

### Cited Findings
- H2CO3 pKa 6.35, 10.33; H2SO3 pKa 1.85, 7.2 (CRC-derived). — [LibreTexts Table E1](https://chem.libretexts.org/Bookshelves/Ancillary_Materials/Reference/Reference_Tables/Equilibrium_Constants/E1%3A_Acid_Dissociation_Constants_at_25C)
- H3PO4 pKa2 7.21. — [Saylor appendix C](https://saylordotorg.github.io/text_general-chemistry-principles-patterns-and-applications-v1.0/s31-appendix-c-dissociation-consta.html)

### Inferences
- The 6.35 value is an apparent pKa that lumps dissolved CO2 with H2CO3. Models that use CO2 as the participant rather than HCO3(-) carry different proton stoichiometry, which is a known source of proton-balance inconsistency between models.
- Sulfite at pH 7.3: SO3(2-):HSO3(-) is about 56:44. Rhea and models may differ on which form they use.

### Gaps
- Nitrous acid pKa (about 3.3) was not verified with a URL.

## Microspecies vs macroscopic pKa, tautomers, and borderline handling

### Takeaway
"Major microspecies" is well defined only when one microstate clearly dominates. If any macroscopic pKa is within about 0.5 units of 7.3, the minor form is at least 24% of the total (more than 33% at 0.3 units). Prediction errors of 0.5 to 1 unit can then flip the assignment. Databases should flag these cases rather than present a single form as definitive.

### Cited Findings
- Microstate pKa values reported by ChemAxon-derived pipelines can be about 2 units off for amphoteric molecules, and the terms "macro-pKa" and "micro-pKa" are widely misused. — [chemRxiv 2024 preprint on pKa terminology](https://chemrxiv.org/doi/pdf/10.26434/chemrxiv-2024-msd0q-v2)
- ChemAxon's charge outputs are defined on the "major microspecies at the given pH". — [mcule ChemAxon pKa docs](https://doc.mcule.com/chemaxoncalcpka)
- eQuilibrator avoids the single-form problem by summing over all pseudoisomers using pKa values (the Alberty transformed-Gibbs approach). — [eQuilibrator 3.0](https://academic.oup.com/nar/article/50/D1/D603/6445959); [Alberty 1993](https://pmc.ncbi.nlm.nih.gov/articles/PMC1225844)

### Inferences (recommendations)
- Borderline rule: if |pKa - 7.3| < 0.5, record both forms and the fraction of each, or flag the entry as "pH-sensitive". Take the measured macro-pKa in preference to the predicted one, and state ionic strength and temperature (phosphates and nucleotides shift by 0.5 to 1 unit between I = 0 and I = 0.25 M).
- Borderline cases from this survey (measured or reported macro-pKa within about 0.5 of 7.3): inorganic phosphate (7.21), sulfite (7.2), free xanthine (about 7.4, unverified), 6-azauridine (6.8), 6-azauracil (about 7.0, unverified), tetracycline pKa2 (7.7, about 0.4), quercetin pK1 (7.03), ATP terminal phosphate (depends on I), reduced flavin N1 (about 6.7, unverified), imidazole (about 7.0, unverified), 1-methyladenine (about 7.2, unverified).
- Cases where the database form may be qualitatively wrong (to check): P5C iminium vs imine; 1-methyladenosine treated as permanently charged; quercetin drawn neutral; spermine assumed fully +4.
- Tautomers (uric acid N3 vs N9 monoanion; xanthine N3 vs N7) change the structure identifiers without changing the net charge. A charge-balance check will not catch tautomer disagreements between databases.

### Gaps
- No published consensus standard for handling borderline pKa in Rhea, ChEBI, MetaCyc or BiGG was found. eQuilibrator's pseudoisomer approach is the main documented alternative.
