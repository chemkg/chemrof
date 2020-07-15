# Auto generated from chemont.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-07-14 18:42
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
from includes.types import Integer, String

metamodel_version = "1.5.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
COB = CurieNamespace('COB', 'http://purl.obolibrary.org/obo/COB_')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
CHEMONT = CurieNamespace('chemont', 'http://w3id.org/chemont')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
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


class ChemicalEnitity(Pattern):
    """
    An entity that can be described using using chemical properties.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalEnitity
    class_class_curie: ClassVar[str] = "chemont:ChemicalEnitity"
    class_name: ClassVar[str] = "chemical enitity"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalEnitity


class SubatomicParticle(ChemicalEnitity):
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
class Molecule(ChemicalEnitity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Molecule
    class_class_curie: ClassVar[str] = "chemont:Molecule"
    class_name: ClassVar[str] = "molecule"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Molecule

    has_atoms: Optional[Union[dict, "Atom"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_atoms is not None and not isinstance(self.has_atoms, Atom):
            self.has_atoms = Atom(**self.has_atoms)
        super().__post_init__(**kwargs)


class PolyatomicIon(Molecule):
    """
    A molecule that has a charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.PolyatomicIon
    class_class_curie: ClassVar[str] = "chemont:PolyatomicIon"
    class_name: ClassVar[str] = "polyatomic ion"
    class_model_uri: ClassVar[URIRef] = CHEMONT.PolyatomicIon


@dataclass
class UnchargedMolecule(Molecule):
    """
    A molecule that in uncharged charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.UnchargedMolecule
    class_class_curie: ClassVar[str] = "chemont:UnchargedMolecule"
    class_name: ClassVar[str] = "uncharged molecule"
    class_model_uri: ClassVar[URIRef] = CHEMONT.UnchargedMolecule

    elemental_charge: Optional[int] = None

@dataclass
class Atom(ChemicalEnitity):
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

class GenericAtom(YAMLRoot):
    """
    generic form of an atom, with unspecified neutron or charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.GenericAtom
    class_class_curie: ClassVar[str] = "chemont:GenericAtom"
    class_name: ClassVar[str] = "generic atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.GenericAtom


@dataclass
class UnchargedAtom(Atom):
    """
    An atom that has no charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.UnchargedAtom
    class_class_curie: ClassVar[str] = "chemont:UnchargedAtom"
    class_name: ClassVar[str] = "uncharged atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.UnchargedAtom

    elemental_charge: Optional[int] = None

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomIonicForm
    class_class_curie: ClassVar[str] = "chemont:AtomIonicForm"
    class_name: ClassVar[str] = "atom ionic form"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomIonicForm

    elemental_charge: Optional[int] = None

class ChargedAtom(AtomIonicForm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChargedAtom
    class_class_curie: ClassVar[str] = "chemont:ChargedAtom"
    class_name: ClassVar[str] = "charged atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChargedAtom


@dataclass
class AtomAniom(ChargedAtom):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomAniom
    class_class_curie: ClassVar[str] = "chemont:AtomAniom"
    class_name: ClassVar[str] = "atom aniom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomAniom

    elemental_charge: Optional[int] = None

@dataclass
class AtomCation(ChargedAtom):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomCation
    class_class_curie: ClassVar[str] = "chemont:AtomCation"
    class_name: ClassVar[str] = "atom cation"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomCation

    elemental_charge: Optional[int] = None

@dataclass
class AtomNeutralForm(AtomIonicForm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomNeutralForm
    class_class_curie: ClassVar[str] = "chemont:AtomNeutralForm"
    class_name: ClassVar[str] = "atom neutral form"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomNeutralForm

    elemental_charge: Optional[int] = None

@dataclass
class FullySpecifiedAtom(Atom):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.FullySpecifiedAtom
    class_class_curie: ClassVar[str] = "chemont:FullySpecifiedAtom"
    class_name: ClassVar[str] = "fully specified atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.FullySpecifiedAtom

    elemental_charge: Optional[int] = None
    neutron_number: Optional[int] = None


# Slots
class slots:
    pass

slots.name = Slot(uri=CHEMONT.name, name="name", curie=CHEMONT.curie('name'),
                      model_uri=CHEMONT.name, domain=None, range=Optional[str])

slots.symbol = Slot(uri=CHEMONT.symbol, name="symbol", curie=CHEMONT.curie('symbol'),
                      model_uri=CHEMONT.symbol, domain=None, range=Optional[str])

slots.atomic_number = Slot(uri=CHEMONT.atomic_number, name="atomic number", curie=CHEMONT.curie('atomic_number'),
                      model_uri=CHEMONT.atomic_number, domain=Atom, range=Optional[int])

slots.neutron_number = Slot(uri=CHEMONT.neutron_number, name="neutron number", curie=CHEMONT.curie('neutron_number'),
                      model_uri=CHEMONT.neutron_number, domain=Atom, range=Optional[int])

slots.nucleon_number = Slot(uri=CHEMONT.nucleon_number, name="nucleon number", curie=CHEMONT.curie('nucleon_number'),
                      model_uri=CHEMONT.nucleon_number, domain=Atom, range=Optional[int])

slots.elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.elemental_charge, domain=Atom, range=Optional[int])

slots.isotope_of = Slot(uri=CHEMONT.isotope_of, name="isotope of", curie=CHEMONT.curie('isotope_of'),
                      model_uri=CHEMONT.isotope_of, domain=Isotope, range=Optional[Union[dict, "Isotope"]])

slots.isotone_of = Slot(uri=CHEMONT.isotone_of, name="isotone of", curie=CHEMONT.curie('isotone_of'),
                      model_uri=CHEMONT.isotone_of, domain=Isotope, range=Optional[Union[dict, "Isotope"]])

slots.nuclear_isomer_of = Slot(uri=CHEMONT.nuclear_isomer_of, name="nuclear isomer of", curie=CHEMONT.curie('nuclear_isomer_of'),
                      model_uri=CHEMONT.nuclear_isomer_of, domain=Isotope, range=Optional[Union[dict, "Isotope"]])

slots.isobar_of = Slot(uri=CHEMONT.isobar_of, name="isobar of", curie=CHEMONT.curie('isobar_of'),
                      model_uri=CHEMONT.isobar_of, domain=None, range=Optional[str])

slots.energy_level = Slot(uri=CHEMONT.energy_level, name="energy level", curie=CHEMONT.curie('energy_level'),
                      model_uri=CHEMONT.energy_level, domain=None, range=Optional[str])

slots.has_atoms = Slot(uri=CHEMONT.has_atoms, name="has atoms", curie=CHEMONT.curie('has_atoms'),
                      model_uri=CHEMONT.has_atoms, domain=Molecule, range=Optional[Union[dict, "Atom"]])

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

slots.uncharged_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="uncharged_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.uncharged_elemental_charge, domain=None, range=Optional[int])

slots.atom_aniom_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="atom aniom_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.atom_aniom_elemental_charge, domain=AtomAniom, range=Optional[int])

slots.atom_cation_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="atom cation_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.atom_cation_elemental_charge, domain=AtomCation, range=Optional[int])

slots.atom_neutral_form_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="atom neutral form_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                      model_uri=CHEMONT.atom_neutral_form_elemental_charge, domain=AtomNeutralForm, range=Optional[int])
