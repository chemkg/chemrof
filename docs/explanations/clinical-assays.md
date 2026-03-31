# Clinical Assays and Chemical Precision

**TL;DR:** For representing biology, use the most specific CHEBI class available;
if you genuinely need a grouping class (e.g., "iron cation" to cover both Fe2+
and Fe3+), verify that the subsumption path in CHEBI actually works --- it often
doesn't. For assays, be wary of premature formalization. Tagging assays with
generic chemical terms is not wrong, but be aware that (a) CHEBI classes may not
group as you expect (the atom and ion branches are disjoint for many elements),
and (b) the relationship between an assay result and the underlying biology is
rarely a simple "measures X in Y" --- clinical interpretation typically requires
multiple analytes read together, and naive ontological definitions can produce
incorrect inferences like classifying pseudohypocalcemia as real hypocalcemia.

---

## The calcium problem

A standard blood panel includes a "calcium" measurement. But what exactly is being measured?
The answer depends on which assay is ordered, and the distinction matters more than
most ontologies acknowledge.

Blood contains calcium in three forms:

| Species | Fraction | Description |
|---|---|---|
| Free ionized Ca2+ | ~50% | The biologically active form, in aqueous solution |
| Albumin-bound Ca2+ | ~40% | Ca2+ coordinated to Asp/Glu residues on serum albumin |
| Anion-complexed Ca2+ | ~10% | Ca2+ bound to citrate, phosphate, bicarbonate |

All three are calcium in the +2 oxidation state. The difference is whether the ion
is free in solution or sequestered in a complex. Two distinct assays exist:

- **Total calcium** measures all three fractions together. Normal range: 8.5--10.5 mg/dL.
- **Ionized calcium** measures only free Ca2+, using an ion-selective electrode. Normal range: 4.5--5.6 mg/dL.

The ionized calcium assay maps cleanly to a single chemical entity:
[CHEBI:29108](http://purl.obolibrary.org/obo/CHEBI_29108) (calcium(2+)).
The total calcium assay does not --- it sums across multiple species, and its clinical
interpretation depends on another analyte entirely.

## Pseudohypocalcemia: where imprecision has consequences

When serum albumin is low (liver disease, nephrotic syndrome, malnutrition), there is
less protein available to bind Ca2+. Total calcium drops, but free ionized Ca2+ remains
normal. The patient has no symptoms --- no tetany, no QT prolongation, no seizure risk.
This is *pseudohypocalcemia*: a measurement artifact, not a physiological problem.

Clinicians handle this with a correction formula:

    Corrected Ca = Total Ca + 0.8 × (4.0 − albumin)

The reverse occurs in dehydration: albumin concentrates, total calcium rises,
but free Ca2+ is unchanged.

## Ontological consequences

HPO defines [hypocalcemia](http://purl.obolibrary.org/obo/HP_0002901) with reference
to generic "calcium" rather than the specific ion Ca2+ (CHEBI:29108). OBA's
[blood calcium amount](http://purl.obolibrary.org/obo/OBA_VT0001562) is defined as
"the amount of a calcium atom when measured in blood."

Take the formal semantics at face value: if "hypocalcemia" means low calcium
(generically) in blood, and total calcium *is* low in pseudohypocalcemia, then a
patient with pseudohypocalcemia formally satisfies the HPO definition. A reasoner
would classify them as having hypocalcemia.

This is wrong. Pseudohypocalcemia is explicitly *not* hypocalcemia --- the whole
point of the "pseudo" prefix is that the physiologically relevant quantity (free Ca2+)
is normal. No clinician would treat it.

The fix is straightforward: reference CHEBI:29108 (calcium(2+)) rather than the
generic grouping class. Under that tighter definition:

- True hypocalcemia (low ionized Ca2+) satisfies the definition.
- Pseudohypocalcemia (normal ionized Ca2+, low total) does not.

Which is exactly the clinical intent.

## The CHEBI hierarchy

For reference, the relevant CHEBI terms form a hierarchy:

- **CHEBI:22984** --- calcium atom (the element)
  - **CHEBI:39124** --- calcium ion (grouping class, charge-nonspecific)
    - **CHEBI:29108** --- calcium(2+) (the physiologically relevant ion)
    - **CHEBI:39099** --- calcium(1+) (exotic; not biologically relevant)

Bio-ontologies (GO, HPO, OBA) typically reference the element or the generic ion
class. This works most of the time because Ca2+ is the only biologically relevant
charge state. But "most of the time" and "always" are different things, and the
calcium/albumin interaction is a case where the ambiguity produces incorrect
inferences.

## Connecting assays to molecular biology

GO-CAM models the molecular side of calcium biology: gene products that transport,
sense, buffer, and signal with Ca2+. Terms like
[calcium ion homeostasis](http://purl.obolibrary.org/obo/GO_0055074) describe the
biological processes that collectively maintain blood calcium levels.

The blood panel assay measures the *outcome* of those processes. The conceptual chain:

    gene products (GO-CAM)
        → enable biological processes (GO)
            → maintain physiological state: [Ca2+ in blood]
                → measured by clinical assay
                    → abnormal values indicate phenotype (HPO)
                        → associated with disease (MONDO)

chemrof sits at the chemical entity layer. It can precisely represent Ca2+, the
calcium-albumin complex, and calcium-citrate as distinct species --- a level of
granularity that CHEBI provides in principle but that downstream ontologies
rarely exploit. Making these distinctions explicit in the schema creates the
formal foundation for tighter cross-references in HPO, OBA, and GO.

## The iron problem: a harder case

Calcium is relatively simple: only one oxidation state (Ca2+) matters biologically,
and CHEBI's "calcium ion" grouping class (CHEBI:39124) properly subsumes it.
Iron breaks both of these assumptions.

### Two oxidation states, both biologically active

Blood contains iron in two oxidation states, each with distinct biological roles:

| Carrier | Iron state | Biological role |
|---|---|---|
| Transferrin | Fe3+ (ferric) | Circulating iron transport |
| Ferritin | Fe3+ | Intracellular iron storage |
| Hemoglobin | Fe2+ (ferrous) | Oxygen binding in red blood cells |
| DMT1 (transporter) | Fe2+ | Intestinal iron absorption |
| Non-transferrin-bound iron (NTBI) | Fe2+/Fe3+ | Pathological; appears in iron overload |

The redox cycling between Fe2+ and Fe3+ is not incidental --- it is the mechanism.
Ferrireductases convert Fe3+ to Fe2+ for transport across membranes. Ceruloplasmin
oxidizes Fe2+ back to Fe3+ for loading onto transferrin. Iron-sulfur clusters and
cytochromes depend on this redox chemistry. A representation that treats "iron" as
a single entity misses the central fact about iron biology.

### GO gets this partly right

GO distinguishes oxidation states where it matters at the molecular function level:

- [GO:0015093](http://purl.obolibrary.org/obo/GO_0015093) --- ferrous iron
  transmembrane transporter activity (explicitly Fe2+)
- [GO:0015091](http://purl.obolibrary.org/obo/GO_0015091) --- ferric iron
  transmembrane transporter activity (explicitly Fe3+)
- [GO:0006826](http://purl.obolibrary.org/obo/GO_0006826) --- iron ion transport
  (generic parent)

This three-level structure is appropriate: the generic parent covers cases where
the oxidation state is unknown or irrelevant, while specific children exist for
annotations where it matters. DMT1 is annotated to the ferrous term; transferrin
receptor to the ferric term.

### HPO and OBA do not

HPO's [Increased circulating iron concentration](http://purl.obolibrary.org/obo/HP_0003452)
is defined simply as "The concentration of iron in the blood circulation is above the
upper limit of normal." OBA's [blood iron amount](http://purl.obolibrary.org/obo/OBA_VT0004152)
is "The amount of a iron atom when measured in blood." UPHENO's equivalent is "increased
level of iron atom in blood serum."

All three reference generic "iron" or "iron atom" (CHEBI:18248).

### The CHEBI hierarchy disconnect

For calcium, the ontological imprecision is at least structurally recoverable:
"calcium ion" (CHEBI:39124) properly subsumes calcium(2+) (CHEBI:29108), so a
reasoner navigating upward from Ca2+ can reach the grouping class that HPO references.

For iron, this is not the case. The CHEBI hierarchy has two separate branches:

**Atom branch:**
```
chemical entity → atom → metal atom → transition element atom
    → iron group element atom → iron atom (CHEBI:18248)
```

**Ion branch:**
```
chemical entity → molecular entity → ... → iron molecular entity
    → elemental iron (CHEBI:82663) → iron cation (CHEBI:24875)
        ├── iron(2+) (CHEBI:29033)
        └── iron(3+) (CHEBI:29034)
```

"Iron atom" (CHEBI:18248) and "iron cation" (CHEBI:24875) are in **completely
disjoint branches**. There is no subsumption path from iron(2+) or iron(3+) up
to iron atom. A reasoner querying "what phenotypes involve iron(2+)?" by
traversing ancestors of CHEBI:29033 would never reach CHEBI:18248 and therefore
never find the HPO terms.

Three problems compound:

1. HPO/OBA reference "iron atom" rather than the specific ions.
2. The term they chose is not even a superclass of the ions in CHEBI.
3. Both oxidation states are biologically active, so a grouping class
   that collapses them loses real information.

If HPO/OBA had referenced "iron cation" (CHEBI:24875) instead, at least the
subsumption path would be intact. A reasoner could traverse from Fe2+ or Fe3+
up to iron cation and find the phenotype terms. Using "iron atom" breaks this
entirely.

### Anemia of chronic disease: iron's pseudohypocalcemia

Iron has its own version of a misleading assay result. In chronic inflammation,
hepcidin levels rise. Hepcidin blocks ferroportin, the sole iron exporter on
macrophages and enterocytes. Iron gets trapped inside cells. Serum iron drops.
Ferritin stays high or rises (it is both an iron storage protein and an acute
phase reactant).

A naive reading of "low serum iron" as "iron deficiency" leads to the wrong
treatment. Iron supplementation in anemia of chronic disease is at best
ineffective and at worst harmful --- the patient has adequate iron stores,
they just cannot mobilize them. The correct intervention targets the
underlying inflammation, not the iron level.

Formally, the "serum iron" assay measures total iron in serum (mostly
transferrin-bound Fe3+) without distinguishing it from storage iron, free
iron, or heme iron. The clinical interpretation depends on ferritin, TIBC,
and transferrin saturation together --- no single "iron amount" captures the
physiological state. An ontology that defines the phenotype as simply
"decreased iron atom in blood" cannot represent the distinction between true
iron deficiency and inflammatory iron sequestration.

## Comparing the two cases

| | Calcium | Iron |
|---|---|---|
| Biologically relevant states | Ca2+ only | Fe2+ and Fe3+ |
| CHEBI grouping class | calcium ion (CHEBI:39124) subsumes Ca2+ | iron cation (CHEBI:24875) subsumes Fe2+ and Fe3+ |
| What HPO/OBA reference | calcium atom (CHEBI:22984) | iron atom (CHEBI:18248) |
| Subsumption intact? | Partially --- calcium ion does subsume Ca2+ | **No** --- iron atom is in a different branch |
| GO oxidation state terms? | No (not needed; Ca1+ irrelevant) | Yes --- ferrous and ferric transporter terms |
| Misleading assay pattern | Pseudohypocalcemia (low albumin) | Anemia of chronic disease (high hepcidin) |
| Clinical consequence of conflation | May treat a measurement artifact | May give iron to a patient who doesn't need it |

Calcium is the simpler case: one relevant ion, a structurally recoverable (if
imprecise) grouping class, and a well-known correction formula. Iron is harder:
two relevant oxidation states with distinct biology, a broken subsumption path
in CHEBI, and clinical interpretation that requires multiple assays read together.

## How SNOMED/LOINC handles calcium

The CHEBI/HPO problems described above are not unique to the OBO world. The
LOINC-SNOMED CT cooperative package --- the main standard for formal axiomatization
of laboratory observables --- runs into the same issues from a different angle.

### The SNOMED calcium hierarchy

SNOMED represents calcium with two substance concepts:

```
5540006 | Calcium (substance) |
    └── 259295006 | Calcium electrolyte (substance) |
```

"Calcium (substance)" is the generic grouper. "Calcium electrolyte" approximates
free ionized Ca2+, though SNOMED does not formally map it to CHEBI:29108.

### How the two assays are axiomatized

The total calcium panel (LOINC 17861-6) uses the generic `Calcium (substance)` as
its Component. The ionized calcium panel (LOINC 1994-3) uses the more specific
`Calcium electrolyte (substance)`. Both are modeled as SNOMED Observable entities
with structured role groups (Component, Property, Time, Direct site, Scale).

This is pragmatically sensible: querying "give me all calcium-related observables"
returns the right results, because `Calcium electrolyte` IS-A `Calcium (substance)`.
The hierarchy works for clinical query subsumption.

### Where the axiomatization falls short

Three problems have been identified with this treatment, and they parallel what
we see in the CHEBI/HPO world:

**Total is not generic.** The total calcium panel measures a *sum* across three
chemical species (free Ca2+, albumin-bound, anion-complexed). Assigning the
generic `Calcium (substance)` as the Component conflates a chemical *type* with an
operational *aggregate*. "Total calcium" is better understood as a quality of the
sample --- a calcium content defined by the assay method --- than as a reference
to the element.

**Protein-bound calcium is invisible.** Roughly 40% of serum calcium is
albumin-bound, and 10% is complexed with small anions. Neither species appears
in the SNOMED substance hierarchy. The axioms therefore cannot formally express
what distinguishes total from ionized calcium beyond the Component and Property
values. The three-way speciation that makes pseudohypocalcemia possible is absent
from the representation.

**Speciation is modeled as IS-A.** "Calcium electrolyte" IS-A "Calcium (substance)"
is SNOMED's way of saying that ionized calcium is a kind of calcium. This has
drawn criticism: some analyses suggest that the relationship between Ca2+ and
generic calcium is better modeled with a dedicated relation like `is-species-of`
or `is-ionic-form-of`, rather than taxonomic subsumption.

### The IS-A critique is off target

The suggestion to replace IS-A with `is-species-of` misidentifies the problem.
In a TBox ontology like SNOMED, IS-A means set-theoretic subsumption: the set of
Ca2+ instances is a subset of the set of calcium instances. That is straightforwardly
true. There is nothing wrong with the IS-A edge per se.

The real problem is a class/metaclass confusion --- the same one that motivates
chemrof. SNOMED (like CHEBI) uses a single hierarchy to represent two different
things:

1. **Schema-level types**: what *kind* of chemical entity something is (atom, ion,
   complex, element, etc.)
2. **Instance-level identity**: *which specific* chemical entity it is (Ca2+,
   Fe3+, copper atom, etc.)

When `Calcium electrolyte IS-A Calcium (substance)`, SNOMED is trying to say
both "Ca2+ is a kind of calcium" (true) and "the ionic form of calcium is a
subtype of the elemental form" (confused). These are different claims operating
at different metamodel levels.

chemrof resolves this by separating the two levels explicitly:

- The **class hierarchy** (`AtomCation` subClassOf `MonoatomicIon` subClassOf ...)
  describes *types of chemical entities* at the schema level.
- **Instance properties** (`has_element: Ca`, `elemental_charge: 2`) describe
  *which specific entity* an instance represents.
- The relationship between Ca2+ and calcium the element is captured via
  `has_element`, not via IS-A. Ca2+ is an instance of `AtomCation`, not a
  subclass of `CalciumAtom`.

This makes the SNOMED problem dissolve. You do not need a new `is-species-of`
relation; you need a schema that puts type information and identity information
in their proper places. The IS-A edges in the class hierarchy then carry their
intended meaning (taxonomic subsumption of chemical entity types), and the
element-ion relationships are explicit object properties that reasoners can
follow.

### Converging evidence

The SNOMED/LOINC case and the CHEBI/HPO case arrive at the same structural
problem from different directions:

| Framework | What it does | Where it breaks |
|---|---|---|
| CHEBI | Classifies chemical entities | Atom and ion branches are disjoint; no subsumption path |
| HPO/OBA | References CHEBI for phenotype definitions | Uses "atom" terms that don't subsume the actual ions |
| SNOMED | Classifies substances for clinical use | Conflates type hierarchy with speciation |
| LOINC axioms | Assigns substances to observables | Generic substance stands in for an operational aggregate |

All four frameworks work acceptably for simple queries. All four break when
formal reasoning requires precise chemical identity --- exactly the scenario
that arises when connecting clinical assays to molecular biology.

## Relevance to chemrof

These examples illustrate one of chemrof's motivations: existing chemical ontologies
and their consumers often conflate chemical species that are formally distinct.
For atoms and simple ions this may seem pedantic, but clinical reasoning over
ontologies can produce real errors when the distinctions are elided.

The iron case demonstrates that the problem goes beyond imprecision into
structural disconnection. When HPO references a CHEBI term that is not even
an ancestor of the actual chemical species being measured, inference over the
combined ontology graph silently fails. No error is raised; results are simply
incomplete.

The SNOMED/LOINC case shows the same problem from the clinical standards side:
a class/metaclass confusion that no amount of new relation types can fix without
separating the two metamodel levels.

A schema that forces precision at the chemical level --- distinguishing free ions
from their complexes, specific charge states from generic grouping classes, and
ensuring that element-ion relationships are explicit properties rather than
implicit IS-A edges --- prevents these errors from propagating into phenotype
and disease ontologies. chemrof's explicit separation of schema-level types from
instance-level identity provides the formal foundation that downstream ontologies
need but currently lack.
