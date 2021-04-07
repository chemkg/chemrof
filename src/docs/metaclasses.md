# Classes and Metaclasses

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTRo4FJ6iXpeBkj2u8ohAuwDZ0C8ntk7dk427GbLTG1gF2hzdeeyrlphx0CJ9LBHOppkoCp0cgfSNLo/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

We need an alternative classification of chemical atoms and elements
that is different than the existing CHEBI. There are deep problems
with classification of atoms and molecular entities in CHEBI. These
problems arise from a basic confusion about classes and
metaclasses. Sources like IUPAC represent chemical *species*,
instances of which are chemical *elements*, __NOT__ instances in the
OBO sense. This fundamental confusion means CHEBI does not work for
OBO.

The idea here is to provide a *schema* in which the instances are
classes in a chemical ontology. The schema could be thought of as an
ontology of metaclasses, but care must be taken here due to mixing of
different metamodel formalisms (this schema is closed-world and thus
not well represented in OWL).

The schema language used here is
[linkml](https://linkml.github.com/), which provides
powerful modeling framework that incorporates aspects of UML, ShEx,
and OWL, and is semantic-web ready.

The goal is to create instances of these schema classes
(e.g. carbon-14) which would be OWL classes, auto-populated with
standardized names and logical axioms. This could be done via a
compilation to dospd or robot, or direcly within the LinkML
framework (see [this
issue](https://github.com/INCATools/dead_simple_owl_design_patterns/issues/51)
). TBD.


