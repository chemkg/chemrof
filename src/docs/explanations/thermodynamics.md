# Reaction Thermodynamics

ChEMROF reactions can carry estimated or measured thermodynamic quantities
through the `has_thermodynamic_estimate` slot, and a reaction enricher fills
those in from [eQuilibrator](https://equilibrator.readthedocs.io/).

This page explains why the representation looks the way it does. The short
version: a biochemical free energy is not a property of a reaction alone, so a
bare number on a reaction would be meaningless.

## 1. Microspecies and pseudoisomer groups

"ATP" is not one molecule in solution. At any pH it is an equilibrium mixture of
distinct chemical species — ATP⁴⁻, HATP³⁻, H₂ATP²⁻, MgATP²⁻, MgHATP⁻ and so on.
Each of those is a **microspecies**: a species with a definite charge, a definite
proton count, a definite magnesium count, and its own standard formation energy.

Their proportions shift continuously with pH and with free Mg²⁺ activity. At pH 7
with no magnesium, ATP is roughly two-thirds ATP⁴⁻ and one-third HATP³⁻; at
millimolar magnesium, MgATP²⁻ dominates.

The set of all microspecies of one compound is a **pseudoisomer group**.
Biochemistry works with the group, not the individual species, because that is
what experiments report: an assay measures total ATP, not ATP⁴⁻ specifically.

This is legitimate because the microspecies interconvert far faster than any
enzymatic step — proton transfer is diffusion-limited — so they stay at internal
equilibrium. The group's effective energy is their Boltzmann-weighted aggregate:

```
ΔfG'°(group) = −RT · ln Σᵢ exp( −ΔfG'°ᵢ / RT )
```

where each microspecies is first corrected for the conditions:

```
ΔfG'°ᵢ = ΔfG°ᵢ + nH,ᵢ · RT·ln10 · pH + nMg,ᵢ · RT·ln10 · pMg − (Debye–Hückel term)
```

## 2. Why the prime matters

That correction is a **Legendre transform**: it trades "a fixed amount of H⁺" for
"a fixed chemical potential of H⁺", the same move that turns enthalpy into Gibbs
energy. The primed (transformed) quantities that come out of it behave
differently from chemical ΔG° in two ways that matter for data modeling.

**Protons and water disappear as reactants.** Their contribution is already
inside the transform. A reaction written for use with ΔG'° must therefore *not*
balance protons — an explicit H⁺ participant would count it twice. This is why
ChEMROF's `Reaction-atp_phosphohydrolase` example lists only ATP, water, ADP and
phosphate, even though the balanced chemical equation releases a proton.

**The value depends on pH even when no proton is transferred**, because the
composition of each pseudoisomer group changes.

So a primed quantity is only interpretable alongside the pH, ionic strength, pMg
and temperature it was computed at. That is the whole reason
`ThermodynamicEstimate` is a reified class rather than a float on `Reaction`: the
conditions travel with the value, and one reaction can carry several estimates at
different conditions.

## 3. The quantities

`ThermodynamicQuantityTypeEnum` distinguishes:

| Value | Meaning |
|-------|---------|
| `standard_gibbs_free_energy_change` | Untransformed chemical ΔG°, every species at a definite protonation state. Protons must be balanced. |
| `standard_transformed_gibbs_free_energy_change` | ΔG'° at the recorded conditions, all reactants at 1 M. |
| `physiological_transformed_gibbs_free_energy_change` | ΔG'm — as above but aqueous reactants at 1 mM, gaseous at 1 mbar. |
| `standard_transformed_reduction_potential` | E'° for a half reaction. |
| `ln_reversibility_index` | Dimensionless; how far a reaction can be driven from equilibrium within physiological concentration bounds. |
| `ln_equilibrium_constant` | ln K'. |

The difference between the standard and physiological variants is purely the
reference concentration. For ATP hydrolysis the two differ by about 17 kJ/mol,
which is `RT ln(10⁻³)` for a reaction with one net extra product.

## 4. The component contribution method

Direct measurements of ΔG° exist for only a few hundred reactions, so
eQuilibrator estimates the rest with **component contribution**, which combines:

- **reactant contribution** — measured formation and equilibrium data, accurate
  but sparse; and
- **group contribution** — decompose each molecule into functional groups and sum
  group energies, broad but less accurate.

The two are combined by projecting each reaction onto the subspace where reactant
contribution applies and falling back to group contribution on the orthogonal
complement. The point of that construction is **thermodynamic consistency**: no
free energy is created around a cycle.

It also yields a full **covariance matrix**. The `standard_error` recorded on an
estimate is the square root of one diagonal element, so errors are *correlated
between reactions* and must not be added in quadrature when summing over a
pathway. The slot's comments say so.

## 5. Running the enricher

```bash
pip install 'chemrof[thermo]'
chemrof enrich-reactions reactions.yaml
```

The first run downloads eQuilibrator's compound cache, which is several
gigabytes. Afterwards it works offline.

```bash
# Non-default conditions: pH 7, 100 mM ionic strength, magnesium-free
chemrof enrich-reactions reactions.yaml --p-h 7.0 --ionic-strength 0.1 --p-mg 14

# Also estimate the reversibility index
chemrof enrich-reactions reactions.yaml --reversibility-index
```

### How participants are resolved

Participants are looked up by their ChEMROF id, in this order:

1. an explicit override supplied by the caller;
2. for an `INCHIKEY:` id, an InChIKey search that **drops the final
   (protonation) block** — eQuilibrator stores one compound per pseudoisomer
   group, so `ZKHQWZAMYRWXGA-KQYNXXCUSA-J` (ATP⁴⁻) would never match the stored
   key. Skeleton-plus-stereo is tried first, then the skeleton alone;
3. for any other CURIE, a registry lookup. `CHEBI:30616`, `KEGG:C00002` and
   `bigg.metabolite:atp` all work directly;
4. an exact InChI from the participant's own ChEMROF record, when the document
   provides one.

Because of step 2, `INCHIKEY:ZKHQWZAMYRWXGA-KQYNXXCUSA-J` and `CHEBI:30616`
produce identical estimates — which is the correct behaviour, and a useful
consistency check.

### What the enricher refuses to do

Three cases produce no estimate rather than a misleading number:

**Unbalanced reactions.** eQuilibrator will return a free energy for a reaction
that does not balance, but it is not a physical quantity. An unbalanced reaction
gets `is_balanced: false` and nothing else. Pass `require_balanced=False` to the
enricher class to override this. Note that the balance check ignores hydrogen, as
it must, given point 2 above.

**Reactions it cannot cover.** For a reaction reachable by neither reactant nor
group contribution, eQuilibrator signals failure by returning an uncertainty of
`rmse_inf` — 10⁵ kJ/mol by default — rather than by raising. Those estimates are
dropped.

**Compounds that cannot be transformed.** A participant with no structure, or one
ChemAxon never analysed, has no microspecies ladder and so no meaningful pH
dependence. Such participants are listed in `unresolved_participants` on the
estimate, which marks it as unreliable without discarding it.

## 6. Limits

- The microspecies energies behind every pH correction come from **predicted**
  pKa values (ChemAxon `cxcalc`), not measurements. Polyprotic species accumulate
  error across several pKas, and results degrade as you move away from pH 7.
- Magnesium dissociation constants are curated for far fewer compounds, so
  raising `--p-mg` is a no-op for most non-nucleotides — silently, not with an
  error.
- Tautomers are *not* microspecies. The transform covers protonation and
  magnesium binding at one skeleton; keto–enol or ring/open-chain tautomers are
  separate compounds that eQuilibrator does not aggregate. Picking the wrong
  tautomer gives a different answer.

## 7. Related ChEMROF elements

- `ThermodynamicEstimate` — the reified estimate, with conditions and provenance.
- `has_thermodynamic_estimate` on `Reaction` — multivalued, one entry per
  quantity and condition set.
- `has_major_microspecies_at_pH7_3` — ChEBI-style link to a single dominant
  protonation state. Note this is strictly weaker than a pseudoisomer group: it
  names one microspecies without the rest of the distribution, so it cannot be
  transformed to another pH.
- `pka_ionization_constant` and its `pka_temperature` / `pka_ionic_strength` /
  `pka_solvent` / `pka_pressure` context slots — the measurement-level data that
  a microspecies ladder would be built from.

## References

- Noor et al. (2013), *Consistent Estimation of Gibbs Energy Using Component
  Contributions*. <https://doi.org/10.1371/journal.pcbi.1003098>
- Beber et al. (2022), *eQuilibrator 3.0: a database solution for thermodynamic
  constant estimation*. <https://doi.org/10.1093/nar/gkab1106>
- Alberty, *Thermodynamics of Biochemical Reactions* — the origin of the
  transformed-quantity convention.
