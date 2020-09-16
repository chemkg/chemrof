# Auto generated from chemont.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-09-15 19:13
# Schema: chemont
#
# id: chemont
# description: A data model describing metaclasses for chemical ontology classes
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import Bool
from includes.types import Boolean, Float, Integer, String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMINF = CurieNamespace('CHEMINF', 'http://semanticscience.org/resource/CHEMINF_')
COB = CurieNamespace('COB', 'http://purl.obolibrary.org/obo/COB_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
CHEMONT = CurieNamespace('chemont', 'http://w3id.org/chemont')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CHEMONT


# Types
class Count(int):
    type_class_uri = XSD.int
    type_class_curie = "xsd:int"
    type_name = "count"
    type_model_uri = CHEMONT.Count


class NumberOfYears(int):
    type_class_uri = XSD.int
    type_class_curie = "xsd:int"
    type_name = "number of years"
    type_model_uri = CHEMONT.NumberOfYears


class ChemicalEncoding(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "chemical encoding"
    type_model_uri = CHEMONT.ChemicalEncoding


# Class references



class Pattern(YAMLRoot):
    """
    A pattern observed in nature. Instances of this class may be owl classes in a realist/OBO framework
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "pattern"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Pattern


class GroupingClass(YAMLRoot):
    """
    A non-specific entity. For example "amino acid" is a grouping for "serine", "leucine" etc; ester is a grouping for
    nitroglycerin; alkane is a grouping for pentane, butane, methane, etc
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.GroupingClass
    class_class_curie: ClassVar[str] = "chemont:GroupingClass"
    class_name: ClassVar[str] = "grouping class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.GroupingClass


class ChemicalEntity(Pattern):
    """
    An entity that can be described using using chemical properties.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalEntity
    class_class_curie: ClassVar[str] = "chemont:ChemicalEntity"
    class_name: ClassVar[str] = "chemical entity"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalEntity


class SubatomicParticle(ChemicalEntity):
    """
    A chemical entity below the granularity of an atom.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.SubatomicParticle
    class_class_curie: ClassVar[str] = "chemont:SubatomicParticle"
    class_name: ClassVar[str] = "subatomic particle"
    class_model_uri: ClassVar[URIRef] = CHEMONT.SubatomicParticle


class Nucleon(SubatomicParticle):
    """
    A neutron or proton
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Nucleon
    class_class_curie: ClassVar[str] = "chemont:Nucleon"
    class_name: ClassVar[str] = "nucleon"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Nucleon


class Neutron(Nucleon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Neutron
    class_class_curie: ClassVar[str] = "chemont:Neutron"
    class_name: ClassVar[str] = "neutron"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Neutron


class Proton(Nucleon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Proton
    class_class_curie: ClassVar[str] = "chemont:Proton"
    class_name: ClassVar[str] = "proton"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Proton


class Electron(SubatomicParticle):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Electron
    class_class_curie: ClassVar[str] = "chemont:Electron"
    class_name: ClassVar[str] = "electron"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Electron


@dataclass
class Molecule(ChemicalEntity):
    """
    A chemical entity that consists of two or more atoms where all atoms are connected via bonds
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Molecule
    class_class_curie: ClassVar[str] = "chemont:Molecule"
    class_name: ClassVar[str] = "molecule"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Molecule

    has_atom_occurrences: List[Union[dict, "AtomOccurrence"]] = empty_list()
    has_bonds: List[Union[dict, "AtomicBond"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.has_atom_occurrences = [AtomOccurrence(*e) for e in self.has_atom_occurrences.items()] if isinstance(self.has_atom_occurrences, dict) \
                                     else [v if isinstance(v, AtomOccurrence) else AtomOccurrence(**v)
                                           for v in ([self.has_atom_occurrences] if isinstance(self.has_atom_occurrences, str) else self.has_atom_occurrences)]
        self.has_bonds = [AtomicBond(*e) for e in self.has_bonds.items()] if isinstance(self.has_bonds, dict) \
                          else [v if isinstance(v, AtomicBond) else AtomicBond(**v)
                                for v in ([self.has_bonds] if isinstance(self.has_bonds, str) else self.has_bonds)]
        super().__post_init__(**kwargs)


class MolecularSpecies(Molecule):
    """
    A molecule in which the units are identical. Example: methyl
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularSpecies
    class_class_curie: ClassVar[str] = "chemont:MolecularSpecies"
    class_name: ClassVar[str] = "molecular species"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularSpecies


class NonSpeciesMolecule(Molecule):
    """
    A molecule in which the units are not identical. Example: sodium chloride
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.NonSpeciesMolecule
    class_class_curie: ClassVar[str] = "chemont:NonSpeciesMolecule"
    class_name: ClassVar[str] = "non species molecule"
    class_model_uri: ClassVar[URIRef] = CHEMONT.NonSpeciesMolecule


class PolyatomicIon(Molecule):
    """
    A molecule that has a charge. For example, nitrate (NO3-).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.PolyatomicIon
    class_class_curie: ClassVar[str] = "chemont:PolyatomicIon"
    class_name: ClassVar[str] = "polyatomic ion"
    class_model_uri: ClassVar[URIRef] = CHEMONT.PolyatomicIon


class MolecularCation(PolyatomicIon):
    """
    A polyatomic ion that is positive
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularCation
    class_class_curie: ClassVar[str] = "chemont:MolecularCation"
    class_name: ClassVar[str] = "molecular cation"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularCation


class MolecularAnion(PolyatomicIon):
    """
    A polyatomic ion that is negative
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularAnion
    class_class_curie: ClassVar[str] = "chemont:MolecularAnion"
    class_name: ClassVar[str] = "molecular anion"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularAnion


@dataclass
class UnchargedMolecule(Molecule):
    """
    A molecule that has no charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.UnchargedMolecule
    class_class_curie: ClassVar[str] = "chemont:UnchargedMolecule"
    class_name: ClassVar[str] = "uncharged molecule"
    class_model_uri: ClassVar[URIRef] = CHEMONT.UnchargedMolecule

    elemental_charge: Optional[int] = None

@dataclass
class Atom(ChemicalEntity):
    """
    A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Atom
    class_class_curie: ClassVar[str] = "chemont:Atom"
    class_name: ClassVar[str] = "atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Atom

    atomic_number: Optional[int] = None
    symbol: Optional[str] = None
    name: Optional[str] = None

class GenericAtom(Atom):
    """
    generic form of an atom, with unspecified neutron or charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.GenericAtom
    class_class_curie: ClassVar[str] = "chemont:GenericAtom"
    class_name: ClassVar[str] = "generic atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.GenericAtom


@dataclass
class Isotope(Atom):
    """
    A specific subtype of an atom with a specified neutron number
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Isotope
    class_class_curie: ClassVar[str] = "chemont:Isotope"
    class_name: ClassVar[str] = "isotope"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Isotope

    neutron_number: Optional[int] = None
    isotope_of: Optional[Union[dict, "Isotope"]] = None
    half_life: Optional[int] = None
    decay_product: Optional[Union[dict, "Isotope"]] = None
    decay_mode: Optional[str] = None
    decay_energy: Optional[str] = None
    mode_of_formation: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.isotope_of is not None and not isinstance(self.isotope_of, Isotope):
            self.isotope_of = Isotope(**self.isotope_of)
        if self.decay_product is not None and not isinstance(self.decay_product, Isotope):
            self.decay_product = Isotope(**self.decay_product)
        super().__post_init__(**kwargs)


@dataclass
class Nuclide(Atom):
    """
    an atomic species characterized by the specific constitution of its nucleus
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Nuclide
    class_class_curie: ClassVar[str] = "chemont:Nuclide"
    class_name: ClassVar[str] = "nuclide"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Nuclide

    energy_level: Optional[str] = None

class Radionuclide(Nuclide):
    """
    an atom that has excess nuclear energy, making it unstable
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Radionuclide
    class_class_curie: ClassVar[str] = "chemont:Radionuclide"
    class_name: ClassVar[str] = "radionuclide"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Radionuclide


@dataclass
class AtomIonicForm(Atom):
    """
    an atom type in which charge state is specified. Also known as (atom) ionic species
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomIonicForm
    class_class_curie: ClassVar[str] = "chemont:AtomIonicForm"
    class_name: ClassVar[str] = "atom ionic form"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomIonicForm

    elemental_charge: Optional[int] = None

class UnchargedAtom(AtomIonicForm):
    """
    An atom that has no charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.UnchargedAtom
    class_class_curie: ClassVar[str] = "chemont:UnchargedAtom"
    class_name: ClassVar[str] = "uncharged atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.UnchargedAtom


class MonoatomicIon(Atom):
    """
    An atom that has a charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MonoatomicIon
    class_class_curie: ClassVar[str] = "chemont:MonoatomicIon"
    class_name: ClassVar[str] = "monoatomic ion"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MonoatomicIon


@dataclass
class AtomAnion(MonoatomicIon):
    """
    A monoatomic ion that is negative
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomAnion
    class_class_curie: ClassVar[str] = "chemont:AtomAnion"
    class_name: ClassVar[str] = "atom anion"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomAnion

    elemental_charge: Optional[int] = None

@dataclass
class AtomCation(MonoatomicIon):
    """
    A monoatomic ion that is positive
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomCation
    class_class_curie: ClassVar[str] = "chemont:AtomCation"
    class_name: ClassVar[str] = "atom cation"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomCation

    elemental_charge: Optional[int] = None

@dataclass
class FullySpecifiedAtom(Atom):
    """
    An atom (class) that has subatomic particle counts specified
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.FullySpecifiedAtom
    class_class_curie: ClassVar[str] = "chemont:FullySpecifiedAtom"
    class_name: ClassVar[str] = "fully specified atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.FullySpecifiedAtom

    elemental_charge: Optional[int] = None
    neutron_number: Optional[int] = None

@dataclass
class AtomicBond(Pattern):
    """
    A connection between two atoms. Note this is the reified form of 'atomically connected to'
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomicBond
    class_class_curie: ClassVar[str] = "chemont:AtomicBond"
    class_name: ClassVar[str] = "atomic bond"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomicBond

    has_atom_occurrences: List[Union[dict, "AtomOccurrence"]] = empty_list()
    bond_order: Optional[int] = None
    bond_type: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.has_atom_occurrences = [AtomOccurrence(*e) for e in self.has_atom_occurrences.items()] if isinstance(self.has_atom_occurrences, dict) \
                                     else [v if isinstance(v, AtomOccurrence) else AtomOccurrence(**v)
                                           for v in ([self.has_atom_occurrences] if isinstance(self.has_atom_occurrences, str) else self.has_atom_occurrences)]
        super().__post_init__(**kwargs)


@dataclass
class AtomOccurrence(Pattern):
    """
    An occurrence of an atom in the context of a particular molecule. For example, one of two occurrences of oxygen in
    nitrate
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomOccurrence
    class_class_curie: ClassVar[str] = "chemont:AtomOccurrence"
    class_name: ClassVar[str] = "atom occurrence"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomOccurrence

    of_atom: Optional[Union[dict, Atom]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.of_atom is not None and not isinstance(self.of_atom, Atom):
            self.of_atom = Atom(**self.of_atom)
        super().__post_init__(**kwargs)


@dataclass
class Acid(Molecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Acid
    class_class_curie: ClassVar[str] = "chemont:Acid"
    class_name: ClassVar[str] = "acid"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Acid

    acidity: Optional[float] = None

@dataclass
class Salt(ChemicalEntity):
    """
    a chemical compound consisting of an ionic assembly of cations and anions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Salt
    class_class_curie: ClassVar[str] = "chemont:Salt"
    class_name: ClassVar[str] = "salt"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Salt

    elemental_charge: Optional[int] = None

@dataclass
class Enantiomer(Molecule):
    """
    one of two stereoisomers of a chiral molecule that are mirror images. Example: R-thalidomide
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Enantiomer
    class_class_curie: ClassVar[str] = "chemont:Enantiomer"
    class_name: ClassVar[str] = "enantiomer"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Enantiomer

    relative_configuration: Optional[str] = None
    optical_configuration: Optional[str] = None
    absolute_configuration: Optional[str] = None
    enantiomer_form_of: Optional[Union[dict, Molecule]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.enantiomer_form_of is not None and not isinstance(self.enantiomer_form_of, Molecule):
            self.enantiomer_form_of = Molecule(**self.enantiomer_form_of)
        super().__post_init__(**kwargs)


@dataclass
class RacemicMixture(ChemicalEntity):
    """
    a chemical compound that has equal amounts of left- and right-handed enantiomers of a chiral molecule. An example
    is Thalidomide
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.RacemicMixture
    class_class_curie: ClassVar[str] = "chemont:RacemicMixture"
    class_name: ClassVar[str] = "racemic mixture"
    class_model_uri: ClassVar[URIRef] = CHEMONT.RacemicMixture

    has_left_enantiomer: Union[dict, Enantiomer] = None
    has_right_enantiomer: Union[dict, Enantiomer] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_left_enantiomer is None:
            raise ValueError(f"has_left_enantiomer must be supplied")
        if not isinstance(self.has_left_enantiomer, Enantiomer):
            self.has_left_enantiomer = Enantiomer(**self.has_left_enantiomer)
        if self.has_right_enantiomer is None:
            raise ValueError(f"has_right_enantiomer must be supplied")
        if not isinstance(self.has_right_enantiomer, Enantiomer):
            self.has_right_enantiomer = Enantiomer(**self.has_right_enantiomer)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.name = Slot(uri=CHEMONT.name, name="name", curie=CHEMONT.curie('name'),
                      model_uri=CHEMONT.name, domain=None, range=Optional[str])

slots.symbol = Slot(uri=CHEMONT.symbol, name="symbol", curie=CHEMONT.curie('symbol'),
                      model_uri=CHEMONT.symbol, domain=None, range=Optional[str])

slots.atomic_number = Slot(uri=CHEMONT.atomic_number, name="atomic number", curie=CHEMONT.curie('atomic_number'),
                      model_uri=CHEMONT.atomic_number, domain=Atom, range=Optional[int], mappings = [CHEMINF["000079"]])

slots.neutron_number = Slot(uri=CHEMONT.neutron_number, name="neutron number", curie=CHEMONT.curie('neutron_number'),
                      model_uri=CHEMONT.neutron_number, domain=Atom, range=Optional[int], mappings = [CHEMINF["000078"]])

slots.nucleon_number = Slot(uri=CHEMONT.nucleon_number, name="nucleon number", curie=CHEMONT.curie('nucleon_number'),
                      model_uri=CHEMONT.nucleon_number, domain=Atom, range=Optional[int])

slots.elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.elemental_charge, domain=Atom, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.alternate_form_of = Slot(uri=CHEMONT.alternate_form_of, name="alternate form of", curie=CHEMONT.curie('alternate_form_of'),
                      model_uri=CHEMONT.alternate_form_of, domain=ChemicalEntity, range=Optional[Union[dict, "ChemicalEntity"]])

slots.isotope_of = Slot(uri=CHEMONT.isotope_of, name="isotope of", curie=CHEMONT.curie('isotope_of'),
                      model_uri=CHEMONT.isotope_of, domain=Isotope, range=Optional[Union[dict, "Isotope"]])

slots.isotone_of = Slot(uri=CHEMONT.isotone_of, name="isotone of", curie=CHEMONT.curie('isotone_of'),
                      model_uri=CHEMONT.isotone_of, domain=Isotope, range=Optional[Union[dict, "Isotope"]])

slots.nuclear_isomer_of = Slot(uri=CHEMONT.nuclear_isomer_of, name="nuclear isomer of", curie=CHEMONT.curie('nuclear_isomer_of'),
                      model_uri=CHEMONT.nuclear_isomer_of, domain=Isotope, range=Optional[Union[dict, "Isotope"]])

slots.isobar_of = Slot(uri=CHEMONT.isobar_of, name="isobar of", curie=CHEMONT.curie('isobar_of'),
                      model_uri=CHEMONT.isobar_of, domain=ChemicalEntity, range=Optional[Union[dict, "ChemicalEntity"]])

slots.has_part = Slot(uri=CHEMONT.has_part, name="has part", curie=CHEMONT.curie('has_part'),
                      model_uri=CHEMONT.has_part, domain=None, range=Optional[str], mappings = [BFO["0000050"]])

slots.has_atom = Slot(uri=CHEMONT.has_atom, name="has atom", curie=CHEMONT.curie('has_atom'),
                      model_uri=CHEMONT.has_atom, domain=Molecule, range=Optional[Union[dict, "Atom"]])

slots.has_group = Slot(uri=CHEMONT.has_group, name="has group", curie=CHEMONT.curie('has_group'),
                      model_uri=CHEMONT.has_group, domain=Atom, range=Optional[str])

slots.energy_level = Slot(uri=CHEMONT.energy_level, name="energy level", curie=CHEMONT.curie('energy_level'),
                      model_uri=CHEMONT.energy_level, domain=None, range=Optional[str])

slots.has_atom_occurrences = Slot(uri=CHEMONT.has_atom_occurrences, name="has atom occurrences", curie=CHEMONT.curie('has_atom_occurrences'),
                      model_uri=CHEMONT.has_atom_occurrences, domain=None, range=List[Union[dict, AtomOccurrence]])

slots.has_bonds = Slot(uri=CHEMONT.has_bonds, name="has bonds", curie=CHEMONT.curie('has_bonds'),
                      model_uri=CHEMONT.has_bonds, domain=Molecule, range=List[Union[dict, "AtomicBond"]])

slots.half_life = Slot(uri=CHEMONT.half_life, name="half life", curie=CHEMONT.curie('half_life'),
                      model_uri=CHEMONT.half_life, domain=Isotope, range=Optional[int])

slots.decay_mode = Slot(uri=CHEMONT.decay_mode, name="decay mode", curie=CHEMONT.curie('decay_mode'),
                      model_uri=CHEMONT.decay_mode, domain=Isotope, range=Optional[str])

slots.decay_product = Slot(uri=CHEMONT.decay_product, name="decay product", curie=CHEMONT.curie('decay_product'),
                      model_uri=CHEMONT.decay_product, domain=Isotope, range=Optional[Union[dict, "Isotope"]])

slots.decay_energy = Slot(uri=CHEMONT.decay_energy, name="decay energy", curie=CHEMONT.curie('decay_energy'),
                      model_uri=CHEMONT.decay_energy, domain=Isotope, range=Optional[str])

slots.mode_of_formation = Slot(uri=CHEMONT.mode_of_formation, name="mode of formation", curie=CHEMONT.curie('mode_of_formation'),
                      model_uri=CHEMONT.mode_of_formation, domain=Isotope, range=Optional[str])

slots.has_cyclic_structure = Slot(uri=CHEMONT.has_cyclic_structure, name="has cyclic structure", curie=CHEMONT.curie('has_cyclic_structure'),
                      model_uri=CHEMONT.has_cyclic_structure, domain=Molecule, range=Optional[Bool], mappings = [CHEMINF["000067"]])

slots.chemical_formula = Slot(uri=CHEMONT.chemical_formula, name="chemical formula", curie=CHEMONT.curie('chemical_formula'),
                      model_uri=CHEMONT.chemical_formula, domain=ChemicalEntity, range=Optional[str])

slots.molecular_formula = Slot(uri=CHEMONT.molecular_formula, name="molecular formula", curie=CHEMONT.curie('molecular_formula'),
                      model_uri=CHEMONT.molecular_formula, domain=ChemicalEntity, range=Optional[str], mappings = [CHEMINF["000042"]])

slots.empirical_formula = Slot(uri=CHEMONT.empirical_formula, name="empirical formula", curie=CHEMONT.curie('empirical_formula'),
                      model_uri=CHEMONT.empirical_formula, domain=ChemicalEntity, range=Optional[str])

slots.smiles_string = Slot(uri=CHEMONT.smiles_string, name="smiles string", curie=CHEMONT.curie('smiles_string'),
                      model_uri=CHEMONT.smiles_string, domain=ChemicalEntity, range=List[str])

slots.atomically_connected_to = Slot(uri=CHEMONT.atomically_connected_to, name="atomically connected to", curie=CHEMONT.curie('atomically_connected_to'),
                      model_uri=CHEMONT.atomically_connected_to, domain=AtomOccurrence, range=List[Union[dict, "AtomOccurrence"]])

slots.acidity = Slot(uri=CHEMONT.acidity, name="acidity", curie=CHEMONT.curie('acidity'),
                      model_uri=CHEMONT.acidity, domain=Acid, range=Optional[float])

slots.next_in_homologous_series_from = Slot(uri=CHEMONT.next_in_homologous_series_from, name="next in homologous series from", curie=CHEMONT.curie('next_in_homologous_series_from'),
                      model_uri=CHEMONT.next_in_homologous_series_from, domain=Molecule, range=Optional[Union[dict, "Molecule"]])

slots.chemical_isomer_of = Slot(uri=CHEMONT.chemical_isomer_of, name="chemical isomer of", curie=CHEMONT.curie('chemical_isomer_of'),
                      model_uri=CHEMONT.chemical_isomer_of, domain=Molecule, range=List[Union[dict, "Molecule"]])

slots.structural_isomer_of = Slot(uri=CHEMONT.structural_isomer_of, name="structural isomer of", curie=CHEMONT.curie('structural_isomer_of'),
                      model_uri=CHEMONT.structural_isomer_of, domain=Molecule, range=List[Union[dict, "Molecule"]])

slots.skeletal_isomer_of = Slot(uri=CHEMONT.skeletal_isomer_of, name="skeletal isomer of", curie=CHEMONT.curie('skeletal_isomer_of'),
                      model_uri=CHEMONT.skeletal_isomer_of, domain=Molecule, range=List[Union[dict, "Molecule"]])

slots.position_isomer_of = Slot(uri=CHEMONT.position_isomer_of, name="position isomer of", curie=CHEMONT.curie('position_isomer_of'),
                      model_uri=CHEMONT.position_isomer_of, domain=Molecule, range=List[Union[dict, "Molecule"]])

slots.functional_isomer_of = Slot(uri=CHEMONT.functional_isomer_of, name="functional isomer of", curie=CHEMONT.curie('functional_isomer_of'),
                      model_uri=CHEMONT.functional_isomer_of, domain=Molecule, range=List[Union[dict, "Molecule"]])

slots.tautomer_of = Slot(uri=CHEMONT.tautomer_of, name="tautomer of", curie=CHEMONT.curie('tautomer_of'),
                      model_uri=CHEMONT.tautomer_of, domain=Molecule, range=List[Union[dict, "Molecule"]])

slots.stereoisomer_of = Slot(uri=CHEMONT.stereoisomer_of, name="stereoisomer of", curie=CHEMONT.curie('stereoisomer_of'),
                      model_uri=CHEMONT.stereoisomer_of, domain=Molecule, range=List[Union[dict, "Molecule"]])

slots.enantiomer_of = Slot(uri=CHEMONT.enantiomer_of, name="enantiomer of", curie=CHEMONT.curie('enantiomer_of'),
                      model_uri=CHEMONT.enantiomer_of, domain=Molecule, range=List[Union[dict, "Molecule"]])

slots.bond_order = Slot(uri=CHEMONT.bond_order, name="bond order", curie=CHEMONT.curie('bond_order'),
                      model_uri=CHEMONT.bond_order, domain=AtomicBond, range=Optional[int])

slots.bond_length = Slot(uri=CHEMONT.bond_length, name="bond length", curie=CHEMONT.curie('bond_length'),
                      model_uri=CHEMONT.bond_length, domain=AtomicBond, range=Optional[float])

slots.bond_energy = Slot(uri=CHEMONT.bond_energy, name="bond energy", curie=CHEMONT.curie('bond_energy'),
                      model_uri=CHEMONT.bond_energy, domain=AtomicBond, range=Optional[float])

slots.bond_type = Slot(uri=CHEMONT.bond_type, name="bond type", curie=CHEMONT.curie('bond_type'),
                      model_uri=CHEMONT.bond_type, domain=None, range=Optional[str])

slots.of_atom = Slot(uri=CHEMONT.of_atom, name="of atom", curie=CHEMONT.curie('of_atom'),
                      model_uri=CHEMONT.of_atom, domain=None, range=Optional[Union[dict, Atom]])

slots.relative_configuration = Slot(uri=CHEMONT.relative_configuration, name="relative configuration", curie=CHEMONT.curie('relative_configuration'),
                      model_uri=CHEMONT.relative_configuration, domain=None, range=Optional[str])

slots.optical_configuration = Slot(uri=CHEMONT.optical_configuration, name="optical configuration", curie=CHEMONT.curie('optical_configuration'),
                      model_uri=CHEMONT.optical_configuration, domain=None, range=Optional[str])

slots.absolute_configuration = Slot(uri=CHEMONT.absolute_configuration, name="absolute configuration", curie=CHEMONT.curie('absolute_configuration'),
                      model_uri=CHEMONT.absolute_configuration, domain=None, range=Optional[str])

slots.enantiomer_form_of = Slot(uri=CHEMONT.enantiomer_form_of, name="enantiomer form of", curie=CHEMONT.curie('enantiomer_form_of'),
                      model_uri=CHEMONT.enantiomer_form_of, domain=None, range=Optional[Union[dict, Molecule]])

slots.has_left_enantiomer = Slot(uri=CHEMONT.has_left_enantiomer, name="has left enantiomer", curie=CHEMONT.curie('has_left_enantiomer'),
                      model_uri=CHEMONT.has_left_enantiomer, domain=None, range=Union[dict, Enantiomer])

slots.has_right_enantiomer = Slot(uri=CHEMONT.has_right_enantiomer, name="has right enantiomer", curie=CHEMONT.curie('has_right_enantiomer'),
                      model_uri=CHEMONT.has_right_enantiomer, domain=None, range=Union[dict, Enantiomer])

slots.anion_state_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="anion state_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.anion_state_elemental_charge, domain=None, range=Optional[int])

slots.cation_state_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="cation state_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.cation_state_elemental_charge, domain=None, range=Optional[int])

slots.uncharged_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="uncharged_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.uncharged_elemental_charge, domain=None, range=Optional[int])

slots.molecule_has_atom_occurrences = Slot(uri=CHEMONT.has_atom_occurrences, name="molecule_has atom occurrences", curie=CHEMONT.curie('has_atom_occurrences'),
                      model_uri=CHEMONT.molecule_has_atom_occurrences, domain=Molecule, range=List[Union[dict, "AtomOccurrence"]])

slots.molecule_has_bonds = Slot(uri=CHEMONT.has_bonds, name="molecule_has bonds", curie=CHEMONT.curie('has_bonds'),
                      model_uri=CHEMONT.molecule_has_bonds, domain=Molecule, range=List[Union[dict, "AtomicBond"]])

slots.atom_anion_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="atom anion_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.atom_anion_elemental_charge, domain=AtomAnion, range=Optional[int])

slots.atom_cation_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="atom cation_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.atom_cation_elemental_charge, domain=AtomCation, range=Optional[int])

slots.atomic_bond_has_atom_occurrences = Slot(uri=CHEMONT.has_atom_occurrences, name="atomic bond_has atom occurrences", curie=CHEMONT.curie('has_atom_occurrences'),
                      model_uri=CHEMONT.atomic_bond_has_atom_occurrences, domain=AtomicBond, range=List[Union[dict, "AtomOccurrence"]])

slots.atomic_bond_bond_type = Slot(uri=CHEMONT.bond_type, name="atomic bond_bond type", curie=CHEMONT.curie('bond_type'),
                      model_uri=CHEMONT.atomic_bond_bond_type, domain=AtomicBond, range=Optional[str])

slots.atom_occurrence_of_atom = Slot(uri=CHEMONT.of_atom, name="atom occurrence_of atom", curie=CHEMONT.curie('of_atom'),
                      model_uri=CHEMONT.atom_occurrence_of_atom, domain=AtomOccurrence, range=Optional[Union[dict, Atom]])

slots.salt_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="salt_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.salt_elemental_charge, domain=Salt, range=Optional[int])

slots.enantiomer_relative_configuration = Slot(uri=CHEMONT.relative_configuration, name="enantiomer_relative configuration", curie=CHEMONT.curie('relative_configuration'),
                      model_uri=CHEMONT.enantiomer_relative_configuration, domain=Enantiomer, range=Optional[str])

slots.enantiomer_optical_configuration = Slot(uri=CHEMONT.optical_configuration, name="enantiomer_optical configuration", curie=CHEMONT.curie('optical_configuration'),
                      model_uri=CHEMONT.enantiomer_optical_configuration, domain=Enantiomer, range=Optional[str])

slots.enantiomer_absolute_configuration = Slot(uri=CHEMONT.absolute_configuration, name="enantiomer_absolute configuration", curie=CHEMONT.curie('absolute_configuration'),
                      model_uri=CHEMONT.enantiomer_absolute_configuration, domain=Enantiomer, range=Optional[str])

slots.enantiomer_enantiomer_form_of = Slot(uri=CHEMONT.enantiomer_form_of, name="enantiomer_enantiomer form of", curie=CHEMONT.curie('enantiomer_form_of'),
                      model_uri=CHEMONT.enantiomer_enantiomer_form_of, domain=Enantiomer, range=Optional[Union[dict, Molecule]])

slots.racemic_mixture_has_left_enantiomer = Slot(uri=CHEMONT.has_left_enantiomer, name="racemic mixture_has left enantiomer", curie=CHEMONT.curie('has_left_enantiomer'),
                      model_uri=CHEMONT.racemic_mixture_has_left_enantiomer, domain=RacemicMixture, range=Union[dict, Enantiomer])

slots.racemic_mixture_has_right_enantiomer = Slot(uri=CHEMONT.has_right_enantiomer, name="racemic mixture_has right enantiomer", curie=CHEMONT.curie('has_right_enantiomer'),
                      model_uri=CHEMONT.racemic_mixture_has_right_enantiomer, domain=RacemicMixture, range=Union[dict, Enantiomer])
