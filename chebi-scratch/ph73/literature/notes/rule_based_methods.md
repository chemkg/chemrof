# Rule-based, fragment-based and LFER (Hammett/Taft) approaches to pKa and protonation-state prediction

Scope: classical substituent-increment (Perrin/Hammett/Taft) methods, commercial rule/LFER engines (ACD/pKa, ChemAxon, SPARC, Epik Classic, OpenEye QUACPAC), open SMARTS-table tools (Dimorphite-DL, Open Babel), multi-site corrections, and how to derive the major microspecies at a given pH. Research date: October 2026.

Notes on sourcing. Claims marked "[DOI from prior knowledge]" are bibliographic identifiers I am confident of but did not re-fetch in this session. Some primary PDFs (EPA SPARC report, Jensen semi-empirical arXiv paper, the PMC benchmark) were downloaded but could not be text-extracted in this sandbox, and a PMC page was blocked by a browser check. These limits are listed under Gaps.

---

## Q1. What accuracy (RMSE in pKa units) do Hammett/Taft and Perrin-style methods achieve, by compound class, compared with ML methods?

### Takeaway
Inside a well-parameterised congeneric class (substituted benzoic acids, phenols, anilines, pyridines), Hammett/Perrin increments reach about 0.1 to 0.3 pKa units. For example, Clark & Perrin (1964) reported about ±0.07 for 25 benzoic acids and ±0.28 for 11 anilines. Across diverse drug-like molecules, the mature commercial LFER/rule engines have a mean absolute error (MAE) of about 0.4 to 0.7 (ACD/pKa DB MAE 0.478; SPARC MAE 0.651). Modern GNN models report RMSE of about 0.7 across mixed test sets (Epik 7: RMSE 0.72, median absolute error 0.42). The gap between good rule-based and ML methods on drug-like sets is therefore small. Rule methods fail sharply outside their fragment coverage (amines, flexible or multi-site molecules, unusual heterocycles). A naive one-value-per-group SMARTS table does much worse (standard deviation about 0.95; RMS about 1.65 on 22 drugs).

### Cited Findings
**Classical Perrin / Hammett / Taft**
- The Perrin, Dempsey & Serjeant monograph *pKa Prediction for Organic Acids and Bases* (Chapman & Hall, 1981; Springer reprint) is organised by class: aliphatic acids and bases, phenols, aromatic carboxylic acids, amines and heterocycles. Each class gets its own Hammett or Taft equation (pKa = pKa0 − ρΣσ). — [Springer book page](https://www.springer.com/gp/book/9789400958852); [Google Books](https://books.google.com/books/about/pKa_Prediction_for_Organic_Acids_and_Bas.html?id=IjTrCAAAQBAJ)
- Clark & Perrin (1964) predicted 25 substituted benzoic acids with an average error of about ±0.07 units and 11 substituted anilines with about ±0.28 units. This figure is quoted in an excerpt of the Perrin book; it is a secondary quotation and I did not see the 1964 paper itself. — [Scribd excerpt of Perrin et al.](https://www.scribd.com/document/521452239/PK-a-Prediction-for-Organic-Acids-and-Bases). The original is Clark & Perrin, Q. Rev. Chem. Soc. 1964, 18, 295, DOI 10.1039/QR9641800295 [DOI from prior knowledge].
- The book's own description says LFER-based predictions are typically good to "several tenths of a pH unit". — [Barnes & Noble listing (publisher blurb)](https://www.barnesandnoble.com/w/pka-prediction-for-organic-acids-and-bases-d-perrin/1119161190)
- Example class-specific equations, as encoded in a Daylight (Sayle, EuroMUG 2000) implementation:
  - benzoic acids: pKa0 = 4.20, ρ = 1.00 (the definitional Hammett reference)
  - phenols: pKa0 = 9.92, ρ = 2.23

  The implementation encoded more than 170 Hammett/Taft equations from the Perrin/Serjeant compilation and sigma constants for "several thousand" groups from Hansch & Leo. Only 63 of 100 common substituents had measured σ. Ertl used AM1 charges to estimate σ for more than 80,000 groups. Caveat: the page's worked example (4-chloro-3,5-dimethylphenol, predicted 9.70 vs experimental 9.71) does not match its own arithmetic: 9.92 − 2.23×(0.24−0.06−0.06) = 9.65. — [Sayle, "Physiological ionization and pKa prediction", Daylight EuroMUG 2000](https://www.daylight.com/meetings/emug00/Sayle/pkapredict.html)
- On a small external set (25 acids and bases from Perrin's data set), Meloun & Bordovská found that the PERRIN algorithm had "the best predictive power and the most accurate results" among PALLAS, MARVIN, PERRIN and SYBYL. The set is small and drawn from Perrin's own domain, so in-domain bias is likely. — [Meloun et al., J. Math. Chem. (2009), DOI 10.1007/s10910-009-9609-2](https://link.springer.com/doi/10.1007/s10910-009-9609-2); [manuscript PDF](https://meloun.upce.cz/docs/publication/178-manus.pdf)

**Naive SMARTS / atom-type lookup (no substituent increments)**
- Sayle's atom-typing table assigns pKa from local atom types (at most two neighbour shells), e.g. aromatic COOH 4.20, phenol 10.00, aliphatic alcohol 15.50. On 22 drugs it gave R² = 0.800 and a reported standard deviation of 0.95. Recomputing from the page's table gives RMS about 1.65 and a mean signed error about +0.99. The largest errors were chloramphenicol (+4.47) and lidocaine (+2.56). By comparison, ACD/pKa (Hammett/Taft-based) on the same set gave R² = 0.978 and standard deviation 0.39. — [Sayle, Daylight](https://www.daylight.com/meetings/emug00/Sayle/pkapredict.html)

**Commercial LFER / rule engines on drug-like sets**
- Liao & Nicklaus (2009) benchmarked nine programs on 197 pharmaceuticals (261 pKa values). Top MAEs:

  | Program | MAE | r² |
  |---|---|---|
  | ADME Boxes 4.9 | 0.389 | |
  | ACD/pKa DB 12.0 | 0.478 | |
  | SPARC 4.2 | 0.651 | 0.894 |

  SPARC failed to predict 18 sites. The quantum-mechanical program Jaguar 7.5 was worst (MAE 1.283, r² 0.579). Epik 1.6, a version close to the 2007 Hammett-Taft method, was not in the top three. — [Certara summary](https://www.certara.com/publication/comparison-of-nine-programs-predicting-pka-values-of-pharmaceutical-substances/); [ChemAxon summary](https://chemaxon.com/publication/Comparison-of-Nine-Programs-Predicting-pKa-Values-of-Pharmaceutical-Substances). Paper: J. Chem. Inf. Model. 2009, 49, 2801, DOI 10.1021/ci900289x [DOI from prior knowledge].
- A secondary summary of that benchmark gives r² ranging from 0.58 to 0.94 and RMSE from 0.65 to 1.8 across the nine programs. It cautions that better-performing methods may have had test compounds in their training sets. — [Optibrium "Predicting pKa" paper](https://optibrium.com/downloads/Predicting_pKa_Paper.pdf)
- ChemAxon's microconstant method (partial charge plus polarizability increments) reports r = 0.95 against experiment on 1670 compounds (vendor document). — [ChemAxon: Prediction of dissociation constant using microconstants (PDF)](https://dl.chemaxon.com/docs/HTML/docs1750/attachments_49191984_1_Prediction_of_dissociation_constant_using_microconstants.pdf). This URL now redirects to the docs home, so the content is quoted via search snippet.
- Empirical tools (ACD, ChemAxon, Epik) are fast, but empirical methods are "particularly prone to failure for amines". — search snippet from [Benchmarking pKa prediction, PMC1513386](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1513386/). The full text was not accessible, so the attribution is unverified.
- Hammett-Taft approaches become less reliable for large, flexible molecules where steric effects and conformations matter. — [Lee & Crippen, "Predicting pKa", J. Chem. Inf. Model. 2009, 49, 2013–2033 (ResearchGate)](https://www.researchgate.net/publication/26762524_Predicting_pK), DOI 10.1021/ci8004190 [DOI from prior knowledge]

**ML comparators**
- Epik 7 (Johnston et al. 2023) is an ensemble of atomic graph convolutional networks trained on more than 42,000 pKa values. It reports 0.42 median absolute error and 0.72 RMSE across seven test sets, recovers 95% of the most-populated protonation states relative to previous Epik versions, and runs in about 47 ms per ligand. — [ChemRxiv preprint](https://chemrxiv.org/engage/chemrxiv/article-details/64188769dab08ad68f6bc895); [ACS figshare](https://acs.figshare.com/articles/dataset/Epik_p_i_K_i_sub_a_sub_and_Protonation_State_Prediction_through_Machine_Learning/22572748). Published as J. Chem. Theory Comput. 2023 [journal DOI not verified here].
- Schrödinger marketing claims under 0.5 log-unit accuracy for both Epik Classic and Epik 7. This is a vendor claim, not an independent benchmark. — [Schrödinger white paper PDF](https://www.schrodinger.com/wp-content/uploads/2023/05/Small-Molecule-Protonation-State-Enumeration-and-pKa-Prediction-Marketing.pdf)
- pkasolver (Mayr et al. 2022) is an open-source GNN pre-trained on Epik-calculated ChEMBL microstate pKas and fine-tuned on experimental data. It reports MAE/RMSE, so it is the open ML comparator. — [Frontiers in Chemistry 2022, DOI 10.3389/fchem.2022.866585](https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2022.866585/full)
- The SAMPL6 blind challenge evaluated both microscopic and macroscopic pKa predictions. It is a standard reference for multi-site accuracy. — [SAMPL6 overview](https://www.choderalab.org/publications/tag/Bas+Rustenburg)

### Inferences
- For a biochemical-compound (metabolite) use case, Perrin-style increments should do well, with errors of about 0.1 to 0.5, for the common acid classes: carboxylic acids, phosphates, phenols, and aliphatic amines with σ* (Taft). Most metabolite acid/base groups are far from pH 7.3 (COOH about 2 to 5; amines about 9 to 11), so modest errors rarely change the major microspecies.
- The risky groups are those with pKa within about ±1.5 of 7.3: imidazoles, phosphate second dissociation, pyridines/purines and other heteroaromatic N, sulfonamides, thiols, and some phenols and anilines. Neither rule-based nor ML methods are reliably below 0.5 for these.
- The RMSE gap between good rule-based engines (MAE about 0.4 to 0.65) and current GNNs (RMSE about 0.7, MAE about 0.4 to 0.5) is small on drug-like sets. The main practical advantages of rule-based methods are transparency and provenance; the main disadvantage is coverage.

### Gaps
- I could not retrieve per-class RMSE tables from Perrin et al. (1981), Lee & Crippen (2009), Manchester et al. (2010; DOI 10.1021/ci100019p [prior knowledge]), Settimo et al. (2014; Pharm. Res., DOI 10.1007/s11095-013-1232-z [prior knowledge]), Fraczkiewicz (2013) or Wu et al. 2024 reviews. Per-class numbers (amines vs acids vs heterocycles) for Hammett/Taft therefore rest on Clark & Perrin's 1964 figures and the general statements above.
- The SPARC RMS on its 4,500-pKa training/validation set (Hilal, Karickhoff & Carreira, EPA/600/R-03/030, 2003) was not extractable. Only the Liao & Nicklaus MAE (0.651) is confirmed.
- No independent accuracy figure for Epik Classic (2007) on its own was found.

---

## Q2. Are sigma constants and rho values available in open, licence-clean tables?

### Takeaway
The canonical σ/ρ compilations are copyrighted publications with no open data licence:
- Hansch, Leo & Taft, Chem. Rev. 1991, 91, 165–195, with Table 1 σm/σp values on pp. 168–175
- the Perrin/Dempsey/Serjeant ρ tables
- Hansch & Leo's books

Individual numerical constants are facts and are widely reproduced in textbooks and teaching handouts. An open project would need to re-compile values with per-value citations, or derive them from open sources. I found no openly licensed, machine-readable master table of Hammett σ and class ρ values.

### Cited Findings
- Hansch, Leo & Taft, "A survey of Hammett substituent constants and resonance and field parameters", *Chem. Rev.* 1991, 91, 165–195. Patents cite Table 1 (pp. 168–175) as the standard source of σm/σp. — [USPTO patent citing it](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12084448); DOI 10.1021/cr00002a004 [DOI from prior knowledge]
- A university teaching handout reproduces selected σp/σm/σp+ values attributed to Hansch-Leo-Taft, e.g. NMe2 σp −0.83, NO2 +0.78, CN +0.66. This shows the values circulate freely but without a licence statement. — [Zipse (LMU Munich) Hammett handout PDF](https://zipse.cup.uni-muenchen.de/site/assets/files/1480/hammett_19_06_02.pdf)
- Recent open-access papers publish σ-derived datasets in their supplementary information:
  - Rakotonirina, Bragato, Heinen & von Lilienfeld (Digital Discovery 2024, RSC open access) extend Hammett σ to organometallic ligands with Δ-ML and validate against published Hammett constants. — [Digital Discovery article](https://pubs.rsc.org/en/content/articlehtml/2024/dd/d4dd00228h); [arXiv 2405.07747](https://arxiv.org/pdf/2405.07747)
  - Saini & Kumar (PCCP 2025) apply ML to predict meta/para σ for more than 900 benzoic-acid derivatives. Their ESI has σ tables, but full open release is unconfirmed. — [PCCP 2025, d5cp01184a](https://pubs.rsc.org/en/content/articlehtml/2025/cp/d5cp01184a); [ESI](https://www.rsc.org/suppdata/d5/cp/d5cp01184a/d5cp01184a1.pdf)
- Measured σ values are sparse: only 63 of 100 common substituents had measured σ. Ertl estimated σ for more than 80,000 groups from AM1 charges. Computed σ is therefore a route to coverage. — [Sayle, Daylight](https://www.daylight.com/meetings/emug00/Sayle/pkapredict.html)
- Open Babel ships `phmodel.txt` (GPL-2 as part of Open Babel). It contains SMARTS transforms paired with a single pKa per group (e.g. `O=C[OD1-0:1] >> O=C[O-:1] 4.0`), but no σ/ρ. — [Open Babel OBPhModel docs](https://openbabel.org/api/3.0/classOpenBabel_1_1OBPhModel.shtml); [phmodel.txt mirror](https://eddie.galaxyproject.org/repos/greg/gregs_test_repo/file/389056b8864a/CADDSuite-1.0.1/data/OpenBabel/phmodel.txt)
- Dimorphite-DL's substructure pKa table (mean and standard deviation per moiety) is open source under Apache-2.0 [licence from prior knowledge; check the repo]. It was derived from 1,938 molecules with single ionizable sites and mostly experimental pKa. — [Dimorphite-DL paper, J. Cheminform. 2019, DOI 10.1186/s13321-019-0336-9](https://www.doi.org/10.1186/s13321-019-0336-9); [PyPI](https://pypi.org/project/dimorphite-dl)

### Inferences
- Numerical constants are generally not copyrightable as facts in the US. A curated table that re-enters σ values with citations to Hansch-Leo-Taft, and ρ values to Perrin et al. or the primary literature, is likely licence-clean, but a wholesale copy of the review's table layout is not. This is a legal inference, not legal advice.
- The practical open route is to:
  1. Build σ tables by re-deriving from open experimental pKa data, e.g. benzoic acid pKa in water, σ = pKa(H) − pKa(X) with ρ = 1.
  2. Fit class ρ values to open pKa datasets: IUPAC Digitized pKa Dataset (CC-BY), Dimorphite source data, or the Czodrowski-lab open experimental set.

### Gaps
- I did not verify the exact licence of the IUPAC digitized dissociation-constant dataset or of Dimorphite-DL's source data in this session.
- I found no open, machine-readable table of Perrin's per-class ρ values.

---

## Q3. How do rule-based methods handle multi-site molecules, and what is the standard way to derive the major microspecies at a given pH?

### Takeaway
Rule-based engines handle polyprotic molecules in one of three ways:
1. **Iteratively:** protonate the most basic or deprotonate the most acidic site, recompute the remaining pKas with the new charge as a substituent (σ of –COO⁻, –NH3⁺ etc.), and repeat until convergence. This is used by Sayle/Daylight, Open Babel (simpler) and Epik Classic.
2. **Via microconstants:** predict a micro-pKa for every site in every relevant microstate, then build the microstate partition function. This is used by ChemAxon and SPARC.

Corrections include:
- statistical factors (±log 2 = 0.30 for equivalent sites)
- electrostatic or Bjerrum-type distance-dependent interaction terms
- "charge cancellation / charge spreading" and nearest-neighbour suppression rules

The standard way to get the major microspecies is to compute each microstate's relative free energy from micro-pKas along a thermodynamic path and take Boltzmann weights at the target pH. For a single site this reduces to Henderson–Hasselbalch.

### Cited Findings
**Iterative greedy approach**
- Sayle's physiological-ionization algorithm starts from the input or neutral form. It repeatedly protonates the most basic site or deprotonates the most acidic site, recalculating pKas each iteration so they reflect the current ionization state. It stops when no site remains to change at the target pH or when a loop is detected. Starting from neutral lets it detect predominantly zwitterionic molecules. Targets are pH 7.2 to 7.4 (arterial blood 7.40). — [Sayle, Daylight](https://www.daylight.com/meetings/emug00/Sayle/pkapredict.html)
- Open Babel's OBPhModel applies the `phmodel.txt` transforms in file order. It uses Henderson–Hasselbalch per group ([BH+]/[B] = 10^(pKa − pH)) to choose the dominant protonated or unprotonated form. There is no site–site interaction, and users report it is unreliable. — [Open Babel OBPhModel](https://openbabel.org/api/3.0/classOpenBabel_1_1OBPhModel.shtml); [KNIME forum](https://forum.knime.com/t/molecule-protonation-state/3491)

**Hammett-Taft engines with interaction terms**
- Epik Classic (Shelley et al. 2007) extends the Hammett-Taft approach with mesomer standardization, charge cancellation and charge spreading, plus an iterative procedure to generate and rank protonation states. It is designed for large libraries. — [ProQuest record of Shelley et al., J. Comput.-Aided Mol. Des. 2007](https://www.proquest.com/docview/737270775); DOI 10.1007/s10822-007-9133-z [DOI from prior knowledge]
- Schrödinger describes Epik Classic as using Hammett-Taft LFER with SMARTS-pattern rules that ignore conformational and stereochemical effects. — [Schrödinger science article](https://www.schrodinger.com/science-articles/schrodinger-solutions-small-molecule-protonation-state-enumeration-and-pka)

**Microconstant engines**
- ChemAxon (Szegezdi & Csizmadia) computes micro-ionization constants from the partial-charge distribution and atomic polarizability of each microspecies, using empirical (non)linear regression equations per site type. A structure-specific term covers steric strain and H-bond corrections. Macro pKa values come from combining microconstants. ChemAxon argues that a more stable ionized site has a more polarizable environment, and that partial charges themselves alter polarizability. — [ChemAxon "Calculating pKa values of small and large molecules" (PDF)](https://dl.chemaxon.com/docs/HTML/docs1750/attachments_49191983_1_Calculating_pKa_values_of_small_and_large_molecules.pdf); [microconstants PDF](https://dl.chemaxon.com/docs/HTML/docs1750/attachments_49191984_1_Prediction_of_dissociation_constant_using_microconstants.pdf); [Marvin calculator-plugin help](https://cms.gutow.uwosh.edu/gutow/marvin.1/chemaxon/marvin/help/calculator-plugins.html)
- SPARC (EPA; Hilal, Karickhoff & Carreira) treats pKa as a reference pKa of the ionizing "reaction centre" perturbed by structure. The perturbation terms are electrostatic/field, resonance (delocalisation), H-bonding and solvation, and the models were trained on more than 4,500 ionization pKas. It extends to the gas phase, organic solvents and temperature dependence. — [EPA/600/R-03/030 report](https://archive.epa.gov/athens/archive-athens/web/pdf/epa_600_r03_030.pdf) (as summarised in search results; full text not extracted)

**SMARTS-table enumerators**
- OpenEye QUACPAC has two tools. FixpKa sets "the ionization state ... using a rule based system". pKaTyper enumerates protonation states and assesses ligand pKas. OEMultistatepKaModel (added in release 2.1.4) assesses atomic pKa ranges and enumerates ionization states at pH 7.4 "based on a heuristic pKa model". It generates no microstates if the projected count exceeds a user cap. — [QUACPAC intro](https://docs.eyesopen.com/applications/quacpac/introduction.html); [Quacpac TK 2.1.4 release notes](https://docs.eyesopen.com/toolkits/cpp/quacpactk/releasenotes/version2_1_4.html); [OEMultistatepKaModelOptions](https://docs.eyesopen.com/toolkits/python/quacpactk/OEProtonClasses/OEMultistatepKaModelOptions.html)
- Dimorphite-DL uses SMARTS substructures, each with a mean pKa µ and standard deviation σ. A site is enumerated in both forms if pH falls within [µ − nσ, µ + nσ], where n is the "pKa precision factor" (default 1.0, default pH window 6.4 to 8.4). It enumerates combinatorially rather than computing populations or site–site interactions. Reported results trade off "correct" against "excess" states as n changes; approximate values read from a garbled table extraction are 70.9% correct at n = 0, 58.8% at n = 1, and 22.1% at n = 3, with excess rising. A known bug treats tertiary amides as basic amines, because amide SMARTS require N–H. — [Dimorphite-DL paper](https://www.doi.org/10.1186/s13321-019-0336-9); [Table 2](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0336-9/tables/2); [GitHub mirror README](https://github.com/UnixJunkie/dimorphite_dl); [PyPI](https://pypi.org/project/dimorphite-dl)

**Theory of micro- vs macro-states**
- Macroscopic pKas mark where the total proton count changes. Microscopic pKas identify which tautomeric or protomeric microstates are involved. Potentiometric and UV methods measure only macroscopic pKas for polyprotic molecules, which cannot be assigned to sites without other evidence such as NMR. — [SAMPL6 overview](https://www.choderalab.org/publications/tag/Bas+Rustenburg); [Wilson et al. 2023 ChemRxiv](https://www.mpinat.mpg.de/4917080/Wilson_2023_chemRxiv.pdf)
- Ullmann, "Relations between protonation constants and titration curves in polyprotic acids: a critical view", J. Phys. Chem. B 2003, 107, 1263–1271, is the standard formal treatment. It covers macro constants via the binding polynomial, and shows that conditional microstate probabilities within a macrostate are pH-independent while macrostate probabilities depend on pH. — cited in [Wilson et al. 2023](https://www.mpinat.mpg.de/4917080/Wilson_2023_chemRxiv.pdf)

**Standard recipe (textbook thermodynamics)**

The relations in this list follow from the cited framework (Ullmann 2003; SAMPL6). They are written out here, not quoted.
- Choose a reference microstate (e.g. fully neutral). For microstate *i* reached by a path of micro-deprotonations with micro-pKas pKa_j:
  - ΔG_i(pH)/(RT ln10) = Σ_j (pKa_j − pH) over protons removed, minus the same sum over protons added.
- Weight each state by p_i = 10^(−ΔG_i/RT ln10) / Σ_k 10^(−ΔG_k/RT ln10). The major microspecies is argmax p_i.
- Micro-pKas must be path-consistent (thermodynamic cycles close), so the rule engine must predict each micro-pKa *in the context of* the current charge state. This is what the iterative or charge-as-substituent schemes approximate.
- For one site this reduces to Henderson–Hasselbalch: fraction deprotonated = 1/(1+10^(pKa−pH)).
- Statistical factors for n equivalent sites shift the macro pKa by log10 of the symmetry ratio, e.g. ±0.30 for two equivalent carboxylates in a symmetric diacid.

### Inferences
- An open, transparent implementation for biochemical compounds could be built as follows:
  1. A curated SMARTS table of ionizable groups (start from Dimorphite-DL/Open Babel and extend for phosphates, phosphonates, sulfates, guanidines, amidines, imidazoles, thiols and enols), each with a parent pKa0 and a class ρ (or Taft ρ*).
  2. σ/σ* increments for substituents within one to three bonds, attenuated by distance (commonly about 0.4 to 0.5 per intervening CH2 for aliphatic Taft). Charged neighbours (–COO⁻, –NH3⁺, –OPO3²⁻) are treated as substituents with their own σ, which gives nearest-neighbour charge suppression automatically.
  3. Enumerate microstates, or iterate greedily like Sayle/Epik Classic for large molecules, recomputing micro-pKas per state.
  4. Compute Boltzmann populations at pH 7.3 and report the major microspecies with a margin (e.g. flag if p_max < 0.8 or if any site has |pKa − pH| < 1). This gives uncertainty transparency that Dimorphite's ±nσ window only approximates.
- The cheapest validation for metabolites is against ChEBI/MetaCyc "major microspecies at pH 7.3" assignments, which are themselves largely produced by ChemAxon. This is an inference; verify with the relevant chemistry-database researcher notes.

### Gaps
- I did not obtain OpenEye pKaTyper theory text (the documentation pages fetched were navigation-only), so whether its heuristic model uses Hammett terms is unconfirmed.
- I did not retrieve the explicit Bjerrum/electrostatic distance formulas used by SPARC or Perrin's per-charge attenuation parameters.

---

## Q4. Are there open implementations of Perrin/Hammett-style pKa prediction in RDKit, CDK or elsewhere?

### Takeaway
I found no maintained, open-source implementation of full Perrin/Hammett-Taft increment pKa prediction in RDKit or CDK. The open options fall into four groups:
- **Lookup-only SMARTS tables without substituent increments:** Open Babel `phmodel.txt` (one pKa per group, Henderson–Hasselbalch, file-order application), Dimorphite-DL (µ±nσ per substructure, enumeration only), and a small Rust package (chematic, 15 SMARTS rules).
- **Open ML models:** pkasolver, MolGpKa, and Czodrowski-lab tools using 24 SMARTS site-locators.
- **Closed engines:** all Hammett/Taft engines (ACD/pKa, Epik Classic, Pipeline Pilot/Daylight-era scripts) and charge-based engines (ChemAxon, SPARC) are closed or vendor-run.
- **Descriptions only:** the Sayle/Daylight 2000 write-up is the most detailed public description of a Hammett/Taft plus iterative-ionization implementation, but no code is released.

### Cited Findings
- Open Babel OBPhModel / `phmodel.txt`: SMARTS transform plus a single pKa, applied in order, with Henderson–Hasselbalch. — [Open Babel API](https://openbabel.org/api/3.0/classOpenBabel_1_1OBPhModel.shtml); [phmodel.h source](https://openbabel.org/api/3.0/phmodel_8h_source.shtml)
- Dimorphite-DL is an open Python/RDKit tool. Its 2019 paper describes 1,938 single-site molecules used to derive per-substructure pKa means and standard deviations. — [paper](https://www.doi.org/10.1186/s13321-019-0336-9); [PyPI](https://pypi.org/project/dimorphite-dl/1.3.0)
- chematic (PyPI; MIT/Apache-2.0, Rust) advertises "pKa prediction (15 SMARTS rules)". Whether these rules use Hammett increments is unknown. — [chematic on PyPI](https://pypi.org/project/chematic/0.8.1/)
- The Czodrowski lab (TU Dortmund) built an open ML pKa tool on exclusively experimental data, using 24 SMARTS patterns that locate about 90% of titratable groups. — [TU Dortmund Eldorado record](https://eldorado.tu-dortmund.de/items/cd9098e5-59c3-4c97-bbc6-d3319a0db3f2); [Zenodo record](https://zenodo.org/record/4415743)
- pkasolver is an open GNN that outputs microstate pKas sequentially (open-source counterpart to Epik). — [Mayr et al. 2022](https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2022.866585/full)
- The Sayle/Daylight implementation encoded more than 170 Hammett/Taft equations from Perrin/Serjeant and σ for thousands of groups from Hansch & Leo. It is a description only, not open code. — [Daylight EuroMUG 2000](https://www.daylight.com/meetings/emug00/Sayle/pkapredict.html)
- Other non-ML open approaches use quantum or charge descriptors: the PM6 semi-empirical pKa approach and EEM-charge-based QSPR (Masaryk Univ.). — [PM6 pKa (Jensen group, PMC4991863)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4991863/); [arXiv 1512.00701](https://arxiv.org/pdf/1512.00701); [Predicting pKa values from EEM atomic charges](https://ics.muni.cz/en/research/publications/1110036)

### Inferences
- A transparent Perrin/Hammett engine for ChEMROF-style biochemical compounds would be new open infrastructure. The most direct route is:
  1. Take Dimorphite-DL's SMARTS table as the site detector and parent-pKa source.
  2. Add a per-class (pKa0, ρ) table and a σ/σ* substituent table with per-row citations.
  3. Implement Sayle-style iterative ionization or full microstate weighting in RDKit.
  4. Benchmark against an open experimental pKa set (IUPAC digitized dataset; Czodrowski-lab data) and SAMPL6/7.
- Because ChEBI's major-microspecies annotations come from ChemAxon, an open rule engine could be scored on agreement with ChEBI at pH 7.3 as a pragmatic proxy, with disagreements triaged by hand.

### Gaps
- No search confirmed or excluded a CDK pKa module, so absence in CDK is inferred from not finding one. A GitHub search for "Hammett pKa" repositories turned up nothing relevant.
- I did not inspect the full rule lists of Open Babel `phmodel.txt` or Dimorphite-DL's `site_substructures.smarts` to count groups covered.
