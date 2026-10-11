# Hill-climbing log

Acceptance rule, fixed before any IUPAC failure was read:

- train (Rhea + IUPAC) must fix more than it breaks;
- dev (Rhea + IUPAC) must fix more than it breaks, with no significant
  regression on either dev set;
- at the end, the cumulative change must beat noise on dev before the sealed
  sets are scored, once.

Each round is one change aimed at one root cause found in *train* failures.
Fixed/broken counts are rows (Rhea) or molecules (IUPAC).

| round | change | Rhea train | Rhea dev | IUPAC train | IUPAC dev | decision |
|---|---|---|---|---|---|---|
| 1 | bug: 4-aminopyridine rule matched nitro N (4-nitropyridine protonated) | 0/0 | 0/0 | +1/−0 | +2/−0 | accept |
| 2 | sulfinic acids deprotonated (Rhea: 16/16 anion) | +17/−0 | +2/−0 | +2/−0 | +2/−1 | accept |
| 3 | thiophenols (benzene ring only; Rhea heteroaryl thiols stay neutral) | 0/0 | 0/0 | +5/−0 | +3/−2 | accept |
| 4 | exocyclic imine on a non-fused azine/azole ring protonated (2-iminopyrimidines etc.). First version also hit fused N1-ribosyl adenines (3 Rhea train breaks); restricted to non-fused rings | 0/0 | 0/0 | +15/−0 | +21/−0 | accept (IUPAC dev beyond noise) |
| 5 | bug: crash when the acidic H is an explicit atom (deuterium); site now skipped | 0/0 | 0/0 | 0/0 | 0/0 | accept (crash fix, score-neutral) |
| 6 | tropolone OH deprotonated when no other anion is present (Rhea stipitatate keeps it neutral beside a carboxylate) | 0/0 | 0/0 | +4/−0 | +3/−0 | accept |
| 7 | gem-dinitro C–H acids (R–CH(NO2)2, pKa ~5) deprotonated | 0/0 | 0/0 | +19/−0 | +15/−1 | accept (both IUPAC beyond noise) |
| 8 | cyclic 1,3-diketones (keto form) drawn as enolate; acyclic (acetylacetone, pKa 9) untouched | 0/0 | 0/0 | +4/−0 | +1/−0 | accept |
| 9 | amines with two beta electron-withdrawing groups left neutral (Rhea: 1/1 neutral; single beta group stays protonated 6/9) | 0/0 | 0/0 | +3/−0 | +2/−0 | accept |
| — | benchmark fix: ChEBI flat-file SMILES drop the H on some aromatic NH (indoles, purines, pterins); 13,089 structures rebuilt from molfiles. Benchmark grows from 107,437 to 113,385 rows (changed: 7,706 → 8,402); old rows and splits unchanged | | | | | |
| 10 | aza-/nitro-imide NH flanked by two C=O deprotonated (azauracils). The first try crashed (one-atom SMARTS), and the scorer had hidden the errors; both scorers now count them | 0/−1 | 0/0 | +3/−1 | +1/−0 | accept (marginal; the Rhea break is 6-azauridine-MP, where Rhea's neutral form conflicts with pKa 6.7) |

## Final check (2026-10-11)

Cumulative change, final rules vs the rules as first committed (`p_original`):

| set | result | decision |
|---|---|---|
| Rhea train | changed +17/−1 (the break is 6-azauridine-MP), unchanged +6/−0 | |
| Rhea dev | changed +2/−0, unchanged +1/−0 | no regression |
| IUPAC train | 0.849 → 0.915, +56/−1 | |
| IUPAC dev | 0.866 → 0.918, +5.2 points [3.5, 6.9], +50/−4 | beyond noise → unseal |
| **Rhea sealed** | 0.908 → 0.908 on changed rows; unchanged +1/−0 | no regression |
| **IUPAC sealed** | 0.870 → 0.918, +4.8 points [3.7, 5.9], +84/−5 | gain replicates |

The sealed sets were scored once, after hill-climbing ended (3 entries in
`data/unseal.log`: Rhea compare, IUPAC compare, IUPAC table).
