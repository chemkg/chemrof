# Open-source pKa and protonation-state (major microspecies) prediction tools for small molecules

Scope note: the research ran in October 2026 with a budget of about 20 tool calls. Primary sources were read for pkasolver, Baltruschat & Czodrowski, QupKake, Graph-pKa, Dimorphite-DL, Uni-pKa and MF-SuP-pKa (repositories), and for the 2026 pKaHub benchmark (Sipos-Szabó et al., JCIM 2026, read from the full PDF). The publisher page for MolGpKa (ACS) returned HTTP 403, so its provenance comes from secondary citations. OpenBabel phmodel, Gypsum-DL, MolTaut, pKaPredict, pKa-ANI, Chemprop pKa, PROPKA and PypKa were not verified in this session; they are listed under Gaps rather than given unsourced claims.

## Comparison table

Legend for the "Output" column: macro = macroscopic pKa; micro = per-site micro-pKa; site = which atom ionises; struct@pH = returns a protonated structure (or structures) at a target pH.

| Tool | Code licence | Weights / data licence | Method | Output | Training labels: experimental vs commercial | Reported accuracy | Status |
|---|---|---|---|---|---|---|---|
| Dimorphite-DL (Ropp et al. 2019) | Apache-2.0 | n/a (SMARTS rules + pKa ranges ship with the code) | Substructure rules, each with a mean pKa ± SD | struct@pH: enumerates protonated SMILES over a pH window (default 6.4–8.4). It can return several variants; it does not give one major species | Rules "fitted" to "measured data". The data source is not named in the README | No standard benchmark found | Active repo, 137 commits; no tagged release visible |
| Baltruschat & Czodrowski "Machine-learning-meets-pKa" (F1000Res 2020) | MIT (code and data) | MIT | Random forest and other ML on FCFP6 fingerprints and descriptors | Single most-relevant pKa per monoprotic molecule | Experimental (ChEMBL assays + DataWarrior). ChemAxon Marvin used for filtering. OpenEye QUACPAC used for protonation at pH 7.4 | Novartis RMSE 1.513; AvLiLuMoVe ("Literature") RMSE 0.785. Marvin: Novartis 1.166, Literature 0.865 | Archival (Zenodo 2020) |
| MolGpKa (Pan et al. JCIM 2021) | MIT | Weights on GitHub | GCN on site-centred graphs; SMARTS-defined sites | Micro-pKa per site (most acidic and most basic) | ACD/Labs-predicted pKa from ChEMBL (about 1.6 M compounds) | Not verified here (ACS page 403) | Code on GitHub (25 commits); web server xundrug.cn/molgpka |
| pkasolver (Mayr et al., Front Chem 2022) | MIT | "pkasolver-light" weights shipped. The Epik-pretrained "pkasolver-epic" weights are not distributable | GNN with transfer learning; Dimorphite-DL enumerates sites; sequential protonation | Micro-pKa sequence, plus one microstate per charge state (no tautomers) | Pretraining: ChEMBL pKa computed by Schrödinger Epik. Fine-tuning: 5,994 experimental values (Baltruschat), with protonation states from Marvin | pkasolver-epic: Novartis RMSE 0.93, Literature 0.82. Epik: 1.16 / 0.92. Marvin: 1.17 / 0.87 | Release v0.3 |
| Graph-pKa (Xiong et al., Bioinformatics 2022) | Not stated in paper; implementation in MF-SuP-pKa repo (Graph_pka folder) | Unknown | GNN with multi-instance learning; macro pKa deconvoluted to micro | Macro + micro-pKa | 16,595 compounds / 17,489 values described as experimental (literature, QSAR Toolbox, earlier datasets). No commercial labels reported | Test MAE ≈ 0.55. SAMPL6 RMSE 0.726 (MAE 0.594). SAMPL7 RMSE 0.934 (ChemAxon best: RMSE 0.708) | Web server pka.simm.ac.cn |
| MF-SuP-pKa (Wu et al., Acta Pharm Sin B 2023) | Not stated on repo page | Pretrained weights included in repo | Multi-fidelity GNN with subgraph pooling; pretrain on low-fidelity computed pKa, fine-tune on experimental data | pKa (predictions for SAMPL6/7, Novartis in repo) | "Low-fidelity computational pKa data" from augmented ChEMBL. The generating tool was not confirmed (see Gaps). Fine-tuned on DataWarrior | Not extracted | Repo exists; no maintenance info |
| QupKake (Abarbanel & Hutchison, JCTC 2024) | Open source (GitHub hutchisonlab/QupKake); licence not confirmed in paper text | Weights and data on GitHub | GNN + GFN2-xTB QM features; CREST-trained site-finder GNN; QM tautomer search | "The micro-pKa value of each reaction site." No macro or pH-species output | Pretraining: ChEMBL v32 ChemAxon (Marvin) acidic/basic pKa (about 2.5 M values). Fine-tuning: 5,637 experimental values (Baltruschat set) | RMSE: Novartis 0.79, Literature 0.54, SAMPL6 0.44, SAMPL7 1.04, SAMPL8 0.85 | Active as of 2024 |
| Uni-pKa (DP Technology, JACS Au) | Apache-2.0 (repo) | Weights not in repo; available via Bohrium notebook. Terms not stated | Template microstate enumerator (from MolGpKa SMARTS) + Uni-Mol free-energy model; Boltzmann → macro/micro | Macro + micro-pKa; microstate ensemble grouped by charge. A distribution at a given pH can be derived thermodynamically | Pretrained on ">1 million predicted pKas from ChemBL" (tool not named). Fine-tuned on "Dwar-iBond" experimental set | Paper claims SOTA. Best open tool in the 2026 pKaHub benchmark | Repo 23 commits |
| Commercial references | — | — | — | ChemAxon, Epik, ACD all give macro/micro pKa and species at pH | Proprietary training sets | See 2026 benchmark | — |

## Which tools' training data or labels derive from ChemAxon Marvin, Epik or ACD?

### Takeaway
Nearly every modern open deep-learning pKa model was pretrained on ChEMBL pKa values that a commercial program computed:
- MolGpKa: ACD/Labs
- pkasolver: Schrödinger Epik (and Marvin for fine-tuning protonation states)
- QupKake: ChemAxon Marvin
- Uni-pKa and MF-SuP-pKa: "predicted" ChEMBL values from an unnamed tool

Fine-tuning then uses public experimental sets. Graph-pKa and the Baltruschat RF models are the main ones trained on experimental labels, although Baltruschat used Marvin for filtering and OpenEye QUACPAC for protonation.

### Cited Findings
- **pkasolver, pretraining.** ChEMBL molecules got "a pK_a scan for the pH range between zero and 14" using "the Schrodinger tool Epik". Epik also supplied the protonation centres. The result was 286,816 molecules and 714,906 protonation states. — [Mayr et al. 2022, Front Chem](https://www.frontiersin.org/articles/10.3389/fchem.2022.866585/full)
- **pkasolver, fine-tuning.** Fine-tuned on 5,994 experimental pKa values (Baltruschat & Czodrowski), "with protonation states for this set provided by Marvin". The paper also states: "we are unable to distribute models trained using results generated with Epik". — [Mayr et al. 2022](https://www.frontiersin.org/articles/10.3389/fchem.2022.866585/full)
- **Baltruschat & Czodrowski.** Training data came from ChEMBL 25 assays and DataWarrior `pKaInWater.dwar`, giving 5,994 monoprotic molecules. Two commercial tools were used in curation:
  - "The Marvin tool from ChemAxon was used to filter out the multiprotic compounds". Entries where Marvin's pKa differed from the experimental value by more than 4 units were also removed.
  - OpenEye QUACPAC was used for "setting the protonation state to pH 7.4".
  - [Baltruschat & Czodrowski 2020, F1000Research](https://f1000research.com/articles/9-113)
- **Inherited curation in later models.** pkasolver, QupKake and others fine-tune on the Baltruschat set, so their "experimental" fine-tuning data was itself filtered by Marvin. — [Mayr et al. 2022](https://www.frontiersin.org/articles/10.3389/fchem.2022.866585/full); [QupKake, PMC11325546](https://pmc.ncbi.nlm.nih.gov/articles/PMC11325546/)
- **MolGpKa.** Trained on ChEMBL molecules carrying values predicted by ACD/Labs Physchem software, keeping only the most acidic and most basic values (about 1.6 M compounds). This comes from search-result summaries of the paper; the ACS page returned 403. — [Pan et al. 2021, JCIM doi:10.1021/acs.jcim.1c00075](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00075). Corroborated by the 2026 benchmark: "It was trained primarily on calculated pKa values (ACD/Labs) available through the ChEMBL v25 data set." — [Sipos-Szabó et al. 2026 JCIM](https://real.mtak.hu/247419/1/ci6c00107.pdf)
- **QupKake.** Pretraining used ChEMBL v32 "filtered to organic molecules with ChemAxon acidic or basic pKa values between 0 and 14" (about 2.5 M predicted values on about 1.5 M molecules). "The lowest-energy protomer or deprotomer was assigned to the predicted pKa value", with sites from CREST/GFN2-xTB scans rather than Marvin sites. Fine-tuning used 5,637 experimental values. — [QupKake, PMC11325546](https://pmc.ncbi.nlm.nih.gov/articles/PMC11325546/). The 2026 benchmark confirms that the calculations "were performed with Marvin (Chemaxon), rather than ACD/Labs". — [Sipos-Szabó et al. 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf)
- **QupKake vs Epik.** An earlier search summary said the QupKake workflow uses "enumeration of reaction sites using Epik". The PMC full text read here attributes sites to CREST, with Epik only as a comparator, and the 2026 benchmark says QupKake "employs a separate neural network to detect ionizable sites… trained using … CREST". Treat the "Epik enumeration" claim as unconfirmed. — [PMC11325546](https://pmc.ncbi.nlm.nih.gov/articles/PMC11325546/); [Sipos-Szabó 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf)
- **Uni-pKa.** "first pretrains on over 1 million predicted pKas from ChemBL"; fine-tuned on "Dwar-iBond". Its enumerator template "modifies and augments" the MolGpKa SMARTS template. — [Uni-pKa ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/64e8da3879853bbd786ca4eb); [Uni-pKa GitHub](https://github.com/dptech-corp/Uni-pKa)
- **MF-SuP-pKa.** "Low-fidelity computational pKa data" (augmented ChEMBL) is used for pretraining, then the model is fine-tuned on DataWarrior experimental data. — [MF-SuP-pKa record (Acta Pharm Sin B 2023)](https://doaj.org/article/0e9b2d370de74671970f23b33e9bc0d1); [GitHub](https://github.com/wujialu/MF-SuP-pKa)
- **Graph-pKa.** Uses 16,595 compounds / 17,489 values described as experimental, drawn from previous datasets, QSAR Toolbox and manual literature extraction. Sites are assigned by rules (acidic = heteroatom bearing H; basic = N without positive charge). No commercial labels are mentioned. — [Xiong et al. 2022, Bioinformatics (PMC8756178)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8756178)
- **Field-wide pattern.** The 2026 benchmark states: "almost every recently published method applies a pretraining-fine-tuning paradigm: in the pretraining phase, a large amount of calculated pKa values are utilized from the ChEMBL database." It also notes that the iBonD databank (over 40,000 values) has "no restricting license" but can only be browsed visually. — [Sipos-Szabó et al. 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf)

### Inferences
- If "no commercial-tool provenance" is a requirement, the cleanest options are:
  - Dimorphite-DL: rule-based; its sources are not documented, but no commercial-tool use is reported.
  - Graph-pKa: experimental labels only, but its code licence is unclear.
  - pkasolver-light: per the 2026 benchmark it "was trained using only the experimental data", but that data was Marvin-filtered (Baltruschat set).
- The ChEMBL pKa fields come from ACD (older releases) or ChemAxon (newer releases). Any model pretrained on "ChEMBL pKa" therefore inherits a commercial predictor's labels. This likely applies to Uni-pKa and MF-SuP-pKa, though neither source read here names the tool.

### Gaps
- The tool behind the Uni-pKa and MF-SuP-pKa ChEMBL labels was not confirmed; the JACS Au methods were not accessed.
- The MolGpKa paper text could not be fetched (403); provenance is from secondary summaries plus the 2026 benchmark.
- Dimorphite-DL's rule-derivation data source is not named in the README; the J Cheminform 2019 paper was not read.

## Which tools give a single major microspecies at a target pH, versus a list of pKa values?

### Takeaway
None of the ML pKa predictors directly emits "the major microspecies at pH X" as a single structure. They emit micro/macro pKa values; Uni-pKa and pkasolver also produce enumerated microstates, from which a population at a given pH can be computed. Dimorphite-DL is the only tool reviewed that emits protonated structures at a target pH, but it returns all plausible variants within a pH window rather than one species. Gypsum-DL and OpenBabel phmodel were not verified.

### Cited Findings
- **Dimorphite-DL** outputs protonated SMILES for a pH range (default 6.4–8.4). It enumerates several states when a group's pKa range overlaps the window, and `--precision` controls how many standard deviations around the mean are used. Its `--label_states` option tags each state as DEPROTONATED, PROTONATED or BOTH, and `--max_variants` defaults to 128. Licence: Apache-2.0. — [Dimorphite-DL GitHub](https://github.com/durrantlab/dimorphite_dl)
- **Dimorphite-DL known limitations:**
  - weakly basic aromatic N and some weak N-H acids are returned in both states;
  - acylguanidines are returned only as cations;
  - nucleobase, tetrazole and substituted-amine coverage is narrow;
  - metals are not supported.
  - Phosphates and polyprotic handling are not discussed.
  - [Dimorphite-DL GitHub](https://github.com/durrantlab/dimorphite_dl)
- **pkasolver** predicts micro-pKa for successive protonated/deprotonated pairs. Dimorphite-DL enumerates sites, so it generates "only one microstate per macrostate"; tautomers and mesomers are not changed. The pKa is the mean of 25 models, with an SD. — [Mayr et al. 2022](https://www.frontiersin.org/articles/10.3389/fchem.2022.866585/full)
- **QupKake** returns "the micro-pKa value of each reaction site". — [PMC11325546](https://pmc.ncbi.nlm.nih.gov/articles/PMC11325546/)
- **Uni-pKa** predicts the free energy of each enumerated microstate. "Macroscopic and microscopic pKa values can be derived via Boltzmann averaging", and the enumerator outputs microstates grouped by total charge. — [Sipos-Szabó 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf); [Uni-pKa GitHub](https://github.com/dptech-corp/Uni-pKa)
- **Graph-pKa** predicts macro-pKa and "automatically deconvolute[s] the predicted macro-pKa into discrete micro-pKa values". The web server does not support ionized input molecules. — [PMC8756178](https://pmc.ncbi.nlm.nih.gov/articles/PMC8756178)
- **Baltruschat** predicts a single pKa per (monoprotic) molecule. — [F1000Research](https://f1000research.com/articles/9-113)
- **pKaHub** (2026) offers the per-molecule experimental "microspecies distribution along with the dissociation constants annotated to macroscopic charge state transitions". This is useful as a reference dataset for species at pH. — [Sipos-Szabó 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf); [pKaHub GitHub](https://github.com/keserulab/pkahub)

### Inferences
- Uni-pKa is the most natural open route to "the dominant microspecies at pH 7.3":
  1. enumerate the microstates;
  2. predict the free energy of each;
  3. compute Boltzmann populations at that pH;
  4. take the argmax.
  The repo does not ship this as a one-line function.
- Dimorphite-DL with a narrow window and low precision approximates a single species, but it is rule-based with no site interaction. For polyprotic metabolites it may emit several variants.

### Gaps
- **OpenBabel `-p 7.4` (phmodel.txt).** Its rule-based SMARTS transforms with fixed pKa give one structure. Not verified this session; see [Open Babel](https://github.com/openbabel/openbabel) data/phmodel.txt.
- **Gypsum-DL.** Believed to call Dimorphite-DL internally. Not verified.
- **MolTaut** (tautomer + MolGpKa-based ionisation at pH). Not verified.
- **RDKit helpers.** RDKit `rdMolStandardize.Uncharger` and charge-parent utilities neutralise molecules; they do not protonate to a target pH. This is from background knowledge and not verified here.

## Which is most accurate on independent experimental benchmarks, and how do they compare with ChemAxon/Epik?

### Takeaway
The largest independent benchmark is pKaHub (Sipos-Szabó et al., JCIM 2026), with more than 31,000 molecules and more than 90,000 experimental values. It found that open tools "have caught up with commercial products" in accuracy, "especially Uni-pKa", while commercial tools keep much lower failure rates. Macro-pKa predictors beat micro-pKa predictors on polyprotic molecules. QupKake "significantly outperforms" ChemAxon, even though it was pretrained on ChemAxon labels. On the small classic sets, pkasolver and QupKake each report better RMSE than Epik and Marvin.

### Cited Findings
- **pKaHub benchmark design.**
  - Seven predictors: ACD/Labs, ChemAxon, Epik, MolGpKa, pKaSolver, QupKake and Uni-pKa.
  - Three test sets (monoprotic, amphoteric, polyprotic), "each with over a thousand data points that were not overlapping with the training data of any of the predictors".
  - Epik was "left out of the head-to-head comparison" because it was used to build the database.
  - [Sipos-Szabó et al. 2026, JCIM 66:4607](https://real.mtak.hu/247419/1/ci6c00107.pdf)
- **pKaHub key results:**
  - "open-source methods, and especially Uni-pKa, have caught up with commercial products".
  - "QupKake significantly outperforms the Chemaxon predictions, as this model was pretrained on Chemaxon-calculated pKa values".
  - "macro-pKa predictors usually outperform micro-pKa predictors". Large micro-pKa errors are "mostly attributed to molecules with multiple titratable groups".
  - Exception rates were below 1% for commercial tools, versus 6.6% for Uni-pKa (simple template) and 7.4% for pKaSolver.
  - [Sipos-Szabó 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf)
- **pKaHub caveats.** The authors note that it is "inadvisable to evaluate proprietary predictors on literature-derived data sets" because training overlap cannot be assessed. The Uni-pKa weights used (from Bohrium) "differ from those reported in the original publication". Per-tool MAE/RMSE values are in Supplementary Tables S4–S6, which were not extracted. — [Sipos-Szabó 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf)
- **pkasolver vs commercial tools (RMSE).**

  | Model | Novartis | Literature |
  |---|---|---|
  | pkasolver-epic | 0.93 | 0.82 |
  | pkasolver-light | 1.13 | 0.82 |
  | Epik | 1.16 | 0.92 |
  | Marvin | 1.17 | 0.87 |

  Epik's Novartis figure excludes 26 molecules with mismatched centres. — [Mayr et al. 2022](https://www.frontiersin.org/articles/10.3389/fchem.2022.866585/full)
- **QupKake (RMSE/MAE):**
  - Novartis 0.79/0.55; Literature 0.54/0.39; SAMPL6 0.44/0.32; SAMPL7 1.04/0.62; SAMPL8 0.85/0.67.
  - On SAMPL6, RMSE 0.44 vs 0.61 for Epik 7 Ensemble.
  - Comparator numbers for Novartis and Literature were taken from Mayr et al., not rerun.
  - [PMC11325546](https://pmc.ncbi.nlm.nih.gov/articles/PMC11325546/)
- **Baltruschat RF vs Marvin.** RF: Novartis RMSE 1.513, Literature 0.785. Marvin 20.1: 1.166 and 0.865. OPERA was far worse (3.059 and 2.182). — [F1000Research 2020](https://f1000research.com/articles/9-113)
- **Graph-pKa:**
  - SAMPL6: RMSE 0.726 (best RMSE in its table); ACD had the best MAE (0.550).
  - SAMPL7: RMSE 0.934; ChemAxon was best (RMSE 0.708).
  - Epik was run from Schrödinger 2017 and ChemAxon from Marvin 20.15.
  - [PMC8756178](https://pmc.ncbi.nlm.nih.gov/articles/PMC8756178)
- **Naming note.** "AvLiLuMoVe" is the SI filename for the Baltruschat "Literature" set. The Novartis set is "frequently misattributed to Liao et al." — [Sipos-Szabó 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf)
- **Other 2024–2026 models found** (not evaluated in depth):
  - GR-pKa (Briefings in Bioinformatics 2024, doi:10.1093/bib/bbae408) reports SAMPL7 RMSE 0.588. — [ECNU record](https://pure.ecnu.edu.cn/en/publications/gr-pksubasub-a-message-passing-neural-network-with-retention-mech/)
  - AcepKa (arXiv 2604.00841, 2026) retrains Uni-Mol with the Uni-pKa protocol; its ChEMBL set expands to more than 3 M protonation states. — [arXiv 2604.00841](https://arxiv.org/html/2604.00841v1)
  - Rowan's "Starling" macroscopic pKa model. — [Rowan blog](https://rowansci.substack.com/p/starling-macroscopic-pka-logd-and)

### Inferences
- **Overall best open tool.** Uni-pKa (macro, ensemble-based) appears to be the best overall open tool on independent data. QupKake is strong on micro-pKa benchmarks (SAMPL6/8).
- **Benchmark contamination.** SAMPL/Novartis/Literature sets are small (tens to hundreds of molecules) and drug-like, and some overlap with fine-tuning data. pKaHub is the more trustworthy comparison.
- **Ceiling on ChemAxon agreement.** For pipelines that must avoid ChemAxon-derived "truth", it matters that QupKake beats ChemAxon despite ChemAxon pretraining. Pretraining labels act as a prior, not a ceiling.

### Gaps
- Exact per-tool MAE/RMSE numbers from pKaHub Supplementary Tables S4–S6 were not retrieved.
- SAMPL6/7 overview (Işık et al.) rankings were not re-fetched in this session.

## Licences: are model weights or bundled data under non-commercial terms?

### Takeaway
Code licences are permissive:
- Dimorphite-DL and Uni-pKa: Apache-2.0.
- MolGpKa, pkasolver and Baltruschat: MIT.

The main weight restriction is pkasolver-epic, which cannot be distributed because of Epik licensing. Uni-pKa weights are not in the GitHub repo (only via a Bohrium notebook, terms unstated). Licences for QupKake, MF-SuP-pKa and Graph-pKa were not confirmed. ChEMBL-derived commercial predictions are redistributed under ChEMBL's terms; no explicit non-commercial clause was found for the tools reviewed.

### Cited Findings
- **Dimorphite-DL:** Apache-2.0. — [GitHub](https://github.com/durrantlab/dimorphite_dl)
- **pkasolver:** MIT. Light models are distributed. For the Epik-trained models: "we are unable to distribute models trained using results generated with Epik". — [Mayr 2022](https://www.frontiersin.org/articles/10.3389/fchem.2022.866585/full); [GitHub mayrf/pkasolver](https://github.com/mayrf/pkasolver)
- **Baltruschat & Czodrowski:** "Code and data are released under the MIT license." — [F1000Research](https://f1000research.com/articles/9-113); [GitHub](https://github.com/czodrowskilab/Machine-learning-meets-pKa)
- **MolGpKa:** MIT (repo sidebar). — [GitHub Xundrug/MolGpKa](https://github.com/Xundrug/MolGpKa)
- **Uni-pKa:**
  - Code is Apache-2.0.
  - Weights are not in the repo; the README points to a Bohrium demo "with available model weights".
  - The dataset (on AISSquare) has no licence stated.
  - The 2026 benchmark used weights that "differ from those reported in the original publication".
  - [GitHub dptech-corp/Uni-pKa](https://github.com/dptech-corp/Uni-pKa); [Sipos-Szabó 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf)
- **MF-SuP-pKa:** pretrained weights are in `model/`; no licence was shown on the fetched page. — [GitHub](https://github.com/wujialu/MF-SuP-pKa)
- **QupKake:** the paper says code and all data are on GitHub; the software licence is not in the paper text. — [PMC11325546](https://pmc.ncbi.nlm.nih.gov/articles/PMC11325546/); [GitHub Shualdon/QupKake](https://github.com/Shualdon/QupKake)
- **iBonD:** "no restricting license on these data". — [Sipos-Szabó 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf)

### Inferences
- Pretraining on ChEMBL-hosted ACD or ChemAxon predictions has not been treated as a licence encumbrance by these projects. Pretraining on self-generated Epik predictions has (pkasolver). Downstream users wanting clean provenance should check that distinction.

### Gaps
- LICENSE files for QupKake, MF-SuP-pKa and Graph-pKa were not read; Uni-pKa weight terms on Bohrium are unknown.
- **Suitability for biochemicals** (phosphates, polyprotic metabolites, zwitterions): no tool paper reviewed reports phosphate- or metabolite-specific accuracy.
  - The training sets were filtered towards drug-likeness. Baltruschat applied Lipinski filtering, used only monoprotic molecules and kept only pKa 2–12 ([F1000Research](https://f1000research.com/articles/9-113)), and pkasolver/QupKake fine-tune on this set.
  - The 2026 benchmark shows micro-pKa tools degrade on molecules with multiple titratable groups ([Sipos-Szabó 2026](https://real.mtak.hu/247419/1/ci6c00107.pdf)).
  - Inference: for polyprotic metabolites (phosphates, carboxylate/amine zwitterions), ensemble/macro approaches (Uni-pKa) or curated experimental data (pKaHub) are preferable to sequential micro-pKa tools. This was not directly tested.
- **Not researched this session:** PypKa/PROPKA (protein tools; outside small-molecule scope), pKa-ANI, pKaPredict, Chemprop-based pKa models, OpenBabel phmodel, Gypsum-DL, MolTaut.
