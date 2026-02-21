# Auto generated from chemrof.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-09T19:21:55
# Schema: chemrof
#
# id: https://w3id.org/chemrof
# description: A data model for managing information about chemical entities, ranging from atoms through molecules to complex mixtures.
#   Aspects of this have been cribbed from various sources including CHEBI, SIO, Wikipedia/Wikidata, the NCATS Translator Chemical Working Group, but all mistakes are my own.
#   For full context/motivation see the [GitHub repo](https://github.com/chemkg/chemrof).
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = "0.0.1"

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CHEMINF = CurieNamespace('CHEMINF', 'http://semanticscience.org/resource/CHEMINF_')
COB = CurieNamespace('COB', 'http://purl.obolibrary.org/obo/COB_')
DRUGBANK = CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/')
EC = CurieNamespace('EC', 'https://enzyme.expasy.org/EC/')
FIX = CurieNamespace('FIX', 'http://purl.obolibrary.org/obo/FIX_')
GO = CurieNamespace('GO', 'http://identifiers.org/go/')
GLYTOUCAN = CurieNamespace('GlyTouCan', 'http://identifiers.org/glytoucan/')
HMDB = CurieNamespace('HMDB', 'http://identifiers.org/hmdb/')
INCHI = CurieNamespace('INCHI', 'http://identifiers.org/inchi/')
INCHIKEY = CurieNamespace('INCHIKEY', 'http://identifiers.org/inchikey/')
KEGG = CurieNamespace('KEGG', 'http://identifiers.org/kegg/')
KEGG_GLYCAN = CurieNamespace('KEGG_GLYCAN', 'http://identifiers.org/kegg.glycan/')
KEGG_REACTION = CurieNamespace('KEGG_REACTION', 'http://identifiers.org/kegg.reaction/')
LANL_ELEMENT = CurieNamespace('LANL_ELEMENT', 'https://periodic.lanl.gov/')
MESH = CurieNamespace('MESH', 'http://identifiers.org/mesh/')
MI = CurieNamespace('MI', 'http://purl.obolibrary.org/obo/MI_')
MOP = CurieNamespace('MOP', 'http://purl.obolibrary.org/obo/MOP_')
METACYC = CurieNamespace('MetaCyc', 'http://identifiers.org/MetaCyc/')
METANETX_CHEMICAL = CurieNamespace('MetaNetX_chemical', 'http://identifiers.org/metanetx.chemical/')
METANETX_REACTION = CurieNamespace('MetaNetX_reaction', 'http://identifiers.org/metanetx.reaction/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
ONTORXN = CurieNamespace('OntoRXN', 'http://www.semanticweb.com/OntoRxn#')
ONTORXN = CurieNamespace('OntoRxn', 'http://www.semanticweb.com/OntoRxn#')
PDG = CurieNamespace('PDG', 'https://pdgapi.lbl.gov/summaries/')
PR = CurieNamespace('PR', 'http://identifiers.org/pr/')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
PUBCHEM_ELEMENT = CurieNamespace('PUBCHEM_ELEMENT', 'https://pubchem.ncbi.nlm.nih.gov/element/')
REACT = CurieNamespace('REACT', 'http://identifiers.org/reactome/')
REX = CurieNamespace('REX', 'http://purl.obolibrary.org/obo/REX_')
RHEA = CurieNamespace('RHEA', 'http://identifiers.org/rhea/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RXNO = CurieNamespace('RXNO', 'http://purl.obolibrary.org/obo/RXNO_')
RETRORULES = CurieNamespace('RetroRules', 'http://example.org/UNKNOWN/RetroRules/')
SEED = CurieNamespace('SEED', 'http://identifiers.org/seed/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
UNII = CurieNamespace('UNII', 'http://identifiers.org/unii/')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://purl.uniprot.org/uniprot/')
WIKIPEDIA = CurieNamespace('Wikipedia', 'https://en.wikipedia.org/wiki/')
BIGG_METABOLITE = CurieNamespace('bigg_metabolite', 'http://identifiers.org/bigg.metabolite/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
BIOPTOP = CurieNamespace('bioptop', 'http://purl.org/biotop/biotop.owl#')
BIOTOP = CurieNamespace('biotop', 'http://purl.org/biotop/biotop.owl#')
BO = CurieNamespace('bo', 'http://www.blueobelisk.org/dict/terminology')
CHEBI_PROPERTY = CurieNamespace('chebi_property', 'http://purl.obolibrary.org/obo/chebi/')
CHEMROF = CurieNamespace('chemrof', 'https://w3id.org/chemrof/')
CML = CurieNamespace('cml', 'http://www.xml-cml.org/schema/')
COMPTOX = CurieNamespace('comptox', 'https://bioregistry.io/reference/comptox:')
DAMLPT = CurieNamespace('damlpt', 'http://www.daml.org/2003/01/periodictable/PeriodicTable#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EDAM = CurieNamespace('edam', 'http://identifiers.org/edam/')
GC = CurieNamespace('gc', 'http://purl.org/gc/')
GLYCOSCIENCESDB = CurieNamespace('glycosciencesdb', 'https://bioregistry.io/glycosciencesdb:')
GOLDBOOK = CurieNamespace('goldbook', 'https://goldbook.iupac.org/terms/view/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NPATLAS = CurieNamespace('npatlas', 'http://identifiers.org/npatlas/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PDG = CurieNamespace('pdg', 'https://pdgapi.lbl.gov/summaries/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WD = CurieNamespace('wd', 'http://www.wikidata.org/entity/')
WDESCHEMA = CurieNamespace('wdeschema', 'https://www.wikidata.org/wiki/Special:EntitySchemaText/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CHEMROF


# Types
class PeriodicTableGroup(int):
    type_class_uri = XSD["int"]
    type_class_curie = "xsd:int"
    type_name = "PeriodicTableGroup"
    type_model_uri = CHEMROF.PeriodicTableGroup


class Count(int):
    type_class_uri = XSD["int"]
    type_class_curie = "xsd:int"
    type_name = "Count"
    type_model_uri = CHEMROF.Count


class NumberOfYears(int):
    type_class_uri = XSD["int"]
    type_class_curie = "xsd:int"
    type_name = "NumberOfYears"
    type_model_uri = CHEMROF.NumberOfYears


class ChemicalEncoding(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ChemicalEncoding"
    type_model_uri = CHEMROF.ChemicalEncoding


class SequenceString(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "SequenceString"
    type_model_uri = CHEMROF.SequenceString


class AminoAcidSequenceString(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "AminoAcidSequenceString"
    type_model_uri = CHEMROF.AminoAcidSequenceString


class DNASequenceString(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "DNASequenceString"
    type_model_uri = CHEMROF.DNASequenceString


class FileLocation(str):
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "FileLocation"
    type_model_uri = CHEMROF.FileLocation


# Class references
class DomainEntityId(extended_str):
    pass


class PhysicochemicalEntityId(DomainEntityId):
    pass


class ChemicalEntityId(PhysicochemicalEntityId):
    pass


class SubatomicParticleId(PhysicochemicalEntityId):
    pass


class GroupingClassId(extended_str):
    pass


class PhysicochemicalEntityGroupingClassId(GroupingClassId):
    pass


class ChemicalGroupingClassId(PhysicochemicalEntityGroupingClassId):
    pass


class ReactionGroupingClassId(GroupingClassId):
    pass


class MaterialGroupingClassId(PhysicochemicalEntityGroupingClassId):
    pass


class ChemicalGroupingByChargeId(ChemicalGroupingClassId):
    pass


class MoleculeGroupingClassId(ChemicalGroupingClassId):
    pass


class MolecularComponentGroupingClassId(ChemicalGroupingClassId):
    pass


class MolecularDerivativeGroupingClassId(MoleculeGroupingClassId):
    pass


class MoleculeGroupingClassDefinedByComponentsId(MoleculeGroupingClassId):
    pass


class MoleculeGroupingClassDefinedByAdditionOfAGroupId(MoleculeGroupingClassId):
    pass


class ChemicalSaltGroupingClassId(MoleculeGroupingClassId):
    pass


class ChemicalSaltByCationId(ChemicalSaltGroupingClassId):
    pass


class ChemicalSaltByAnionId(ChemicalSaltGroupingClassId):
    pass


class GeneralizedMolecularStructureClassId(MoleculeGroupingClassId):
    pass


class MonomericPolymericGroupingClassId(GeneralizedMolecularStructureClassId):
    pass


class GroupingClassForAcidsOrBasesId(MoleculeGroupingClassId):
    pass


class AcidAnionGroupingClassId(GroupingClassForAcidsOrBasesId):
    pass


class GeneralAcidBaseGroupingClassId(GroupingClassForAcidsOrBasesId):
    pass


class AcidBaseConflationClassId(GroupingClassForAcidsOrBasesId):
    pass


class AtomGroupingClassId(ChemicalGroupingClassId):
    pass


class AtomGroupingByPeriodicTablePlacementId(AtomGroupingClassId):
    pass


class AtomGroupingByPeriodicTableGroupId(AtomGroupingByPeriodicTablePlacementId):
    pass


class AtomGroupingByPeriodicTableBlockId(AtomGroupingByPeriodicTablePlacementId):
    pass


class AtomGroupingByPropertyId(AtomGroupingClassId):
    pass


class MaterialId(PhysicochemicalEntityId):
    pass


class NanomaterialId(MaterialId):
    pass


class MineralId(MaterialId):
    pass


class PolyatomicEntityId(ChemicalEntityId):
    pass


class MolecularComponentId(PolyatomicEntityId):
    pass


class PolymerPartId(MolecularComponentId):
    pass


class MonomerId(PolymerPartId):
    pass


class MolecularSubsequenceId(PolymerPartId):
    pass


class ChemicalGroupId(MolecularComponentId):
    pass


class ChemicalMixtureId(PolyatomicEntityId):
    pass


class PreciseChemicalMixtureId(ChemicalMixtureId):
    pass


class MolecularComplexId(PreciseChemicalMixtureId):
    pass


class SupramolecularPolymerId(MolecularComplexId):
    pass


class ImpreciseChemicalMixtureId(ChemicalMixtureId):
    pass


class MoleculeId(PolyatomicEntityId):
    pass


class SmallMoleculeId(MoleculeId):
    pass


class MacromoleculeId(MoleculeId):
    pass


class PeptideId(MacromoleculeId):
    pass


class ProteinId(MacromoleculeId):
    pass


class GlycanId(MacromoleculeId):
    pass


class MonomolecularPolymerId(MacromoleculeId):
    pass


class CopolymerId(MonomolecularPolymerId):
    pass


class HomopolymerId(MonomolecularPolymerId):
    pass


class NaturalProductId(MoleculeId):
    pass


class MoietyId(MolecularComponentId):
    pass


class SequenceIntervalId(MolecularComponentId):
    pass


class AminoAcidSequenceIntervalId(SequenceIntervalId):
    pass


class NucleotideSequenceIntervalId(SequenceIntervalId):
    pass


class DNASequenceIntervalId(NucleotideSequenceIntervalId):
    pass


class RNASequenceIntervalId(NucleotideSequenceIntervalId):
    pass


class FunctionalGroupId(MolecularComponentId):
    pass


class MolecularSpeciesId(MoleculeId):
    pass


class NonSpeciesMoleculeId(MoleculeId):
    pass


class MoleculeByChargeStateId(MoleculeId):
    pass


class PolyatomicIonId(MoleculeByChargeStateId):
    pass


class MolecularCationId(PolyatomicIonId):
    pass


class MolecularAnionId(PolyatomicIonId):
    pass


class NetUnchargedMoleculeId(MoleculeByChargeStateId):
    pass


class ZwitterionId(NetUnchargedMoleculeId):
    pass


class NeutralMoleculeId(NetUnchargedMoleculeId):
    pass


class AtomId(ChemicalEntityId):
    pass


class PartiallySpecifiedAtomId(AtomId):
    pass


class ChemicalElementId(PartiallySpecifiedAtomId):
    pass


class NuclideId(PartiallySpecifiedAtomId):
    pass


class RadionuclideId(NuclideId):
    pass


class IsotopeId(NuclideId):
    pass


class IsobarId(NuclideId):
    pass


class AtomIonicFormId(PartiallySpecifiedAtomId):
    pass


class UnchargedAtomId(AtomIonicFormId):
    pass


class MonoatomicIonId(AtomIonicFormId):
    pass


class AtomAnionId(MonoatomicIonId):
    pass


class AtomCationId(MonoatomicIonId):
    pass


class FullySpecifiedAtomId(AtomId):
    pass


class AtomOccurrenceName(extended_str):
    pass


class ChemicalSaltId(PreciseChemicalMixtureId):
    pass


class EsterId(MoleculeId):
    pass


class StereoisomerId(MoleculeId):
    pass


class EnantiomerId(StereoisomerId):
    pass


class RacemicMixtureId(PreciseChemicalMixtureId):
    pass


class AllotropeId(MoleculeId):
    pass


class ReactionId(DomainEntityId):
    pass


class IsomeraseReactionId(ReactionId):
    pass


@dataclass(repr=False)
class Collection(YAMLRoot):
    """
    This utility class serves to collect a set of domain entities, and to be the top level object in tree-based
    representations such as JSON.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Collection"]
    class_class_curie: ClassVar[str] = "chemrof:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Collection

    entities: Optional[Union[dict[Union[str, DomainEntityId], Union[dict, "DomainEntity"]], list[Union[dict, "DomainEntity"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="entities", slot_type=DomainEntity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DomainEntity(YAMLRoot):
    """
    A discrete, specific named entity in the domain of chemistry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["DomainEntity"]
    class_class_curie: ClassVar[str] = "chemrof:DomainEntity"
    class_name: ClassVar[str] = "DomainEntity"
    class_model_uri: ClassVar[URIRef] = CHEMROF.DomainEntity

    id: Union[str, DomainEntityId] = None
    name: Optional[str] = None
    type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DomainEntityId):
            self.id = DomainEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self.type = str(self.class_class_curie)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class PhysicochemicalEntity(DomainEntity):
    """
    A discrete chemical structure, material structure, or subatomic particle type
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["PhysicochemicalEntity"]
    class_class_curie: ClassVar[str] = "chemrof:PhysicochemicalEntity"
    class_name: ClassVar[str] = "PhysicochemicalEntity"
    class_model_uri: ClassVar[URIRef] = CHEMROF.PhysicochemicalEntity

    id: Union[str, PhysicochemicalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class ChemicalEntity(PhysicochemicalEntity):
    """
    A discrete structure that is one or more atoms that can be described by a chemical formula.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["24431"]
    class_class_curie: ClassVar[str] = "CHEBI:24431"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    IUPAC_name: Optional[str] = None
    is_radical: Optional[Union[bool, Bool]] = None
    has_chemical_role: Optional[Union[dict, "ChemicalRole"]] = None
    inchi_string: Optional[str] = None
    inchi_chemical_sublayer: Optional[str] = None
    inchi_atom_connections_sublayer: Optional[str] = None
    inchi_hydrogen_connections_sublayer: Optional[str] = None
    inchi_charge_sublayer: Optional[str] = None
    inchi_proton_sublayer: Optional[str] = None
    inchi_stereochemical_double_bond_sublayer: Optional[str] = None
    inchi_tetrahedral_stereochemical_sublayer: Optional[str] = None
    inchi_stereochemical_type_sublayer: Optional[str] = None
    inchi_isotopic_layer: Optional[str] = None
    smiles_string: Optional[str] = None
    empirical_formula: Optional[str] = None
    has_major_microspecies_at_pH7_3: Optional[Union[str, ChemicalEntityId]] = None
    molecular_mass: Optional[float] = None
    water_solubility: Optional[float] = None
    pka_ionization_constant: Optional[Union[float, list[float]]] = empty_list()
    pka_temperature: Optional[float] = None
    pka_ionic_strength: Optional[float] = None
    pka_solvent: Optional[str] = None
    pka_pressure: Optional[float] = None
    owl_subclass_of: Optional[Union[dict, "OwlClass"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.IUPAC_name is not None and not isinstance(self.IUPAC_name, str):
            self.IUPAC_name = str(self.IUPAC_name)

        if self.is_radical is not None and not isinstance(self.is_radical, Bool):
            self.is_radical = Bool(self.is_radical)

        if self.has_chemical_role is not None and not isinstance(self.has_chemical_role, ChemicalRole):
            self.has_chemical_role = ChemicalRole(**as_dict(self.has_chemical_role))

        if self.inchi_string is not None and not isinstance(self.inchi_string, str):
            self.inchi_string = str(self.inchi_string)

        if self.inchi_chemical_sublayer is not None and not isinstance(self.inchi_chemical_sublayer, str):
            self.inchi_chemical_sublayer = str(self.inchi_chemical_sublayer)

        if self.inchi_atom_connections_sublayer is not None and not isinstance(self.inchi_atom_connections_sublayer, str):
            self.inchi_atom_connections_sublayer = str(self.inchi_atom_connections_sublayer)

        if self.inchi_hydrogen_connections_sublayer is not None and not isinstance(self.inchi_hydrogen_connections_sublayer, str):
            self.inchi_hydrogen_connections_sublayer = str(self.inchi_hydrogen_connections_sublayer)

        if self.inchi_charge_sublayer is not None and not isinstance(self.inchi_charge_sublayer, str):
            self.inchi_charge_sublayer = str(self.inchi_charge_sublayer)

        if self.inchi_proton_sublayer is not None and not isinstance(self.inchi_proton_sublayer, str):
            self.inchi_proton_sublayer = str(self.inchi_proton_sublayer)

        if self.inchi_stereochemical_double_bond_sublayer is not None and not isinstance(self.inchi_stereochemical_double_bond_sublayer, str):
            self.inchi_stereochemical_double_bond_sublayer = str(self.inchi_stereochemical_double_bond_sublayer)

        if self.inchi_tetrahedral_stereochemical_sublayer is not None and not isinstance(self.inchi_tetrahedral_stereochemical_sublayer, str):
            self.inchi_tetrahedral_stereochemical_sublayer = str(self.inchi_tetrahedral_stereochemical_sublayer)

        if self.inchi_stereochemical_type_sublayer is not None and not isinstance(self.inchi_stereochemical_type_sublayer, str):
            self.inchi_stereochemical_type_sublayer = str(self.inchi_stereochemical_type_sublayer)

        if self.inchi_isotopic_layer is not None and not isinstance(self.inchi_isotopic_layer, str):
            self.inchi_isotopic_layer = str(self.inchi_isotopic_layer)

        if self.smiles_string is not None and not isinstance(self.smiles_string, str):
            self.smiles_string = str(self.smiles_string)

        if self.empirical_formula is not None and not isinstance(self.empirical_formula, str):
            self.empirical_formula = str(self.empirical_formula)

        if self.has_major_microspecies_at_pH7_3 is not None and not isinstance(self.has_major_microspecies_at_pH7_3, ChemicalEntityId):
            self.has_major_microspecies_at_pH7_3 = ChemicalEntityId(self.has_major_microspecies_at_pH7_3)

        if self.molecular_mass is not None and not isinstance(self.molecular_mass, float):
            self.molecular_mass = float(self.molecular_mass)

        if self.water_solubility is not None and not isinstance(self.water_solubility, float):
            self.water_solubility = float(self.water_solubility)

        if not isinstance(self.pka_ionization_constant, list):
            self.pka_ionization_constant = [self.pka_ionization_constant] if self.pka_ionization_constant is not None else []
        self.pka_ionization_constant = [v if isinstance(v, float) else float(v) for v in self.pka_ionization_constant]

        if self.pka_temperature is not None and not isinstance(self.pka_temperature, float):
            self.pka_temperature = float(self.pka_temperature)

        if self.pka_ionic_strength is not None and not isinstance(self.pka_ionic_strength, float):
            self.pka_ionic_strength = float(self.pka_ionic_strength)

        if self.pka_solvent is not None and not isinstance(self.pka_solvent, str):
            self.pka_solvent = str(self.pka_solvent)

        if self.pka_pressure is not None and not isinstance(self.pka_pressure, float):
            self.pka_pressure = float(self.pka_pressure)

        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**as_dict(self.owl_subclass_of))

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class SubatomicParticle(PhysicochemicalEntity):
    """
    A chemical entity below the granularity of an atom.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["SubatomicParticle"]
    class_class_curie: ClassVar[str] = "chemrof:SubatomicParticle"
    class_name: ClassVar[str] = "SubatomicParticle"
    class_model_uri: ClassVar[URIRef] = CHEMROF.SubatomicParticle

    id: Union[str, SubatomicParticleId] = None
    subatomic_particle_type: Optional[Union[str, "SubatomicParticleEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubatomicParticleId):
            self.id = SubatomicParticleId(self.id)

        if self.subatomic_particle_type is not None and not isinstance(self.subatomic_particle_type, SubatomicParticleEnum):
            self.subatomic_particle_type = SubatomicParticleEnum(self.subatomic_particle_type)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class OwlClass(YAMLRoot):
    """
    instances of this class mixin are OWL Classes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Class"]
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "OwlClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.OwlClass

    owl_subclass_of: Optional[Union[dict, "OwlClass"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**as_dict(self.owl_subclass_of))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GroupingClass(YAMLRoot):
    """
    Instances of this class represent generic concepts that can be used to group more specific concepts, or to
    classify entities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["GroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:GroupingClass"
    class_name: ClassVar[str] = "GroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.GroupingClass

    id: Union[str, GroupingClassId] = None
    name: Optional[str] = None
    subtype_of: Optional[Union[Union[str, GroupingClassId], list[Union[str, GroupingClassId]]]] = empty_list()
    owl_subclass_of: Optional[Union[dict, OwlClass]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GroupingClassId):
            self.id = GroupingClassId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of] if self.subtype_of is not None else []
        self.subtype_of = [v if isinstance(v, GroupingClassId) else GroupingClassId(v) for v in self.subtype_of]

        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**as_dict(self.owl_subclass_of))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicochemicalEntityGroupingClass(GroupingClass):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["PhysicochemicalEntityGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:PhysicochemicalEntityGroupingClass"
    class_name: ClassVar[str] = "PhysicochemicalEntityGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.PhysicochemicalEntityGroupingClass

    id: Union[str, PhysicochemicalEntityGroupingClassId] = None
    subtype_of: Optional[Union[Union[str, PhysicochemicalEntityGroupingClassId], list[Union[str, PhysicochemicalEntityGroupingClassId]]]] = empty_list()
    classifies: Optional[Union[str, PhysicochemicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of] if self.subtype_of is not None else []
        self.subtype_of = [v if isinstance(v, PhysicochemicalEntityGroupingClassId) else PhysicochemicalEntityGroupingClassId(v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, PhysicochemicalEntityId):
            self.classifies = PhysicochemicalEntityId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalGroupingClass(PhysicochemicalEntityGroupingClass):
    """
    Instances of this class represent generic chemical concepts that can be used to group more specific concepts, or
    to classify entities. For example "amino acid" is a grouping for "serine", "leucine" etc; ester is a grouping for
    nitroglycerin; alkane is a grouping for pentane, butane, methane, etc
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalGroupingClass"
    class_name: ClassVar[str] = "ChemicalGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalGroupingClass

    id: Union[str, ChemicalGroupingClassId] = None
    owl_subclass_of: Optional[Union[dict, OwlClass]] = None
    smarts_string: Optional[str] = None
    markush_string: Optional[str] = None
    subtype_of: Optional[Union[Union[str, ChemicalGroupingClassId], list[Union[str, ChemicalGroupingClassId]]]] = empty_list()
    classifies: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalGroupingClassId):
            self.id = ChemicalGroupingClassId(self.id)

        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**as_dict(self.owl_subclass_of))

        if self.smarts_string is not None and not isinstance(self.smarts_string, str):
            self.smarts_string = str(self.smarts_string)

        if self.markush_string is not None and not isinstance(self.markush_string, str):
            self.markush_string = str(self.markush_string)

        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of] if self.subtype_of is not None else []
        self.subtype_of = [v if isinstance(v, ChemicalGroupingClassId) else ChemicalGroupingClassId(v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, ChemicalEntityId):
            self.classifies = ChemicalEntityId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReactionGroupingClass(GroupingClass):
    """
    A grouping class for reactions, for example, dehalogenase; breaking of covalent bond
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ReactionGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:ReactionGroupingClass"
    class_name: ClassVar[str] = "ReactionGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ReactionGroupingClass

    id: Union[str, ReactionGroupingClassId] = None
    subtype_of: Optional[Union[Union[str, ReactionGroupingClassId], list[Union[str, ReactionGroupingClassId]]]] = empty_list()
    classifies: Optional[Union[str, ReactionId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionGroupingClassId):
            self.id = ReactionGroupingClassId(self.id)

        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of] if self.subtype_of is not None else []
        self.subtype_of = [v if isinstance(v, ReactionGroupingClassId) else ReactionGroupingClassId(v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, ReactionId):
            self.classifies = ReactionId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialGroupingClass(PhysicochemicalEntityGroupingClass):
    """
    A grouping class that classifies materials
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MaterialGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:MaterialGroupingClass"
    class_name: ClassVar[str] = "MaterialGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MaterialGroupingClass

    id: Union[str, MaterialGroupingClassId] = None
    subtype_of: Optional[Union[Union[str, MaterialGroupingClassId], list[Union[str, MaterialGroupingClassId]]]] = empty_list()
    classifies: Optional[Union[str, MaterialId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialGroupingClassId):
            self.id = MaterialGroupingClassId(self.id)

        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of] if self.subtype_of is not None else []
        self.subtype_of = [v if isinstance(v, MaterialGroupingClassId) else MaterialGroupingClassId(v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, MaterialId):
            self.classifies = MaterialId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalGroupingByCharge(ChemicalGroupingClass):
    """
    A grouping class that refines a charge-neutral entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalGroupingByCharge"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalGroupingByCharge"
    class_name: ClassVar[str] = "ChemicalGroupingByCharge"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalGroupingByCharge

    id: Union[str, ChemicalGroupingByChargeId] = None
    subtype_of: Optional[Union[Union[str, MoleculeGroupingClassId], list[Union[str, MoleculeGroupingClassId]]]] = empty_list()
    has_charge_state: Optional[Union[str, URIorCURIE]] = None
    charge_agnostic_entity: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalGroupingByChargeId):
            self.id = ChemicalGroupingByChargeId(self.id)

        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of] if self.subtype_of is not None else []
        self.subtype_of = [v if isinstance(v, MoleculeGroupingClassId) else MoleculeGroupingClassId(v) for v in self.subtype_of]

        if self.has_charge_state is not None and not isinstance(self.has_charge_state, URIorCURIE):
            self.has_charge_state = URIorCURIE(self.has_charge_state)

        if self.charge_agnostic_entity is not None and not isinstance(self.charge_agnostic_entity, ChemicalEntityId):
            self.charge_agnostic_entity = ChemicalEntityId(self.charge_agnostic_entity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MoleculeGroupingClass(ChemicalGroupingClass):
    """
    A grouping class that classifies molecules. Example: carbohydrate, monosaccharide, amino acid, polyacrylamide
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MoleculeGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:MoleculeGroupingClass"
    class_name: ClassVar[str] = "MoleculeGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MoleculeGroupingClass

    id: Union[str, MoleculeGroupingClassId] = None
    subtype_of: Optional[Union[Union[str, MoleculeGroupingClassId], list[Union[str, MoleculeGroupingClassId]]]] = empty_list()
    classifies: Optional[Union[str, MoleculeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoleculeGroupingClassId):
            self.id = MoleculeGroupingClassId(self.id)

        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of] if self.subtype_of is not None else []
        self.subtype_of = [v if isinstance(v, MoleculeGroupingClassId) else MoleculeGroupingClassId(v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, MoleculeId):
            self.classifies = MoleculeId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularComponentGroupingClass(ChemicalGroupingClass):
    """
    A grouping class that classifies molecular components. Example: inorganic anion group
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MolecularComponentGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:MolecularComponentGroupingClass"
    class_name: ClassVar[str] = "MolecularComponentGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MolecularComponentGroupingClass

    id: Union[str, MolecularComponentGroupingClassId] = None
    subtype_of: Optional[Union[Union[str, MolecularComponentGroupingClassId], list[Union[str, MolecularComponentGroupingClassId]]]] = empty_list()
    classifies: Optional[Union[str, MolecularComponentId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularComponentGroupingClassId):
            self.id = MolecularComponentGroupingClassId(self.id)

        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of] if self.subtype_of is not None else []
        self.subtype_of = [v if isinstance(v, MolecularComponentGroupingClassId) else MolecularComponentGroupingClassId(v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, MolecularComponentId):
            self.classifies = MolecularComponentId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularDerivativeGroupingClass(MoleculeGroupingClass):
    """
    A grouping class defined as a derivative of another molecule or molecular grouping class
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MolecularDerivativeGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:MolecularDerivativeGroupingClass"
    class_name: ClassVar[str] = "MolecularDerivativeGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MolecularDerivativeGroupingClass

    id: Union[str, MolecularDerivativeGroupingClassId] = None
    derivative_of: Optional[Union[str, DomainEntityId]] = None
    name: Optional[str] = None
    classifies: Optional[Union[str, MoleculeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularDerivativeGroupingClassId):
            self.id = MolecularDerivativeGroupingClassId(self.id)

        if self.derivative_of is not None and not isinstance(self.derivative_of, DomainEntityId):
            self.derivative_of = DomainEntityId(self.derivative_of)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.classifies is not None and not isinstance(self.classifies, MoleculeId):
            self.classifies = MoleculeId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MoleculeGroupingClassDefinedByComponents(MoleculeGroupingClass):
    """
    A grouping class defined as an exhaustive list of components
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MoleculeGroupingClassDefinedByComponents"]
    class_class_curie: ClassVar[str] = "chemrof:MoleculeGroupingClassDefinedByComponents"
    class_name: ClassVar[str] = "MoleculeGroupingClassDefinedByComponents"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MoleculeGroupingClassDefinedByComponents

    id: Union[str, MoleculeGroupingClassDefinedByComponentsId] = None
    has_part: Optional[Union[dict, "ChemicalEntityOrGrouping"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoleculeGroupingClassDefinedByComponentsId):
            self.id = MoleculeGroupingClassDefinedByComponentsId(self.id)

        if self.has_part is not None and not isinstance(self.has_part, ChemicalEntityOrGrouping):
            self.has_part = ChemicalEntityOrGrouping()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MoleculeGroupingClassDefinedByAdditionOfAGroup(MoleculeGroupingClass):
    """
    A grouping class defined in terms of a derivative of a molecule and the addition of a group
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MoleculeGroupingClassDefinedByAdditionOfAGroup"]
    class_class_curie: ClassVar[str] = "chemrof:MoleculeGroupingClassDefinedByAdditionOfAGroup"
    class_name: ClassVar[str] = "MoleculeGroupingClassDefinedByAdditionOfAGroup"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MoleculeGroupingClassDefinedByAdditionOfAGroup

    id: Union[str, MoleculeGroupingClassDefinedByAdditionOfAGroupId] = None
    has_group: Optional[Union[Union[str, ChemicalGroupId], list[Union[str, ChemicalGroupId]]]] = empty_list()
    derivative_of: Optional[Union[str, PolyatomicEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoleculeGroupingClassDefinedByAdditionOfAGroupId):
            self.id = MoleculeGroupingClassDefinedByAdditionOfAGroupId(self.id)

        if not isinstance(self.has_group, list):
            self.has_group = [self.has_group] if self.has_group is not None else []
        self.has_group = [v if isinstance(v, ChemicalGroupId) else ChemicalGroupId(v) for v in self.has_group]

        if self.derivative_of is not None and not isinstance(self.derivative_of, PolyatomicEntityId):
            self.derivative_of = PolyatomicEntityId(self.derivative_of)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalSaltGroupingClass(MoleculeGroupingClass):
    """
    A grouping class for a chemical salt
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalSaltGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalSaltGroupingClass"
    class_name: ClassVar[str] = "ChemicalSaltGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalSaltGroupingClass

    id: Union[str, ChemicalSaltGroupingClassId] = None
    has_anionic_component: Optional[str] = None
    has_cationic_component: Optional[str] = None
    name: Optional[str] = None
    classifies: Optional[Union[str, ChemicalSaltId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalSaltGroupingClassId):
            self.id = ChemicalSaltGroupingClassId(self.id)

        if self.has_anionic_component is not None and not isinstance(self.has_anionic_component, str):
            self.has_anionic_component = str(self.has_anionic_component)

        if self.has_cationic_component is not None and not isinstance(self.has_cationic_component, str):
            self.has_cationic_component = str(self.has_cationic_component)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.classifies is not None and not isinstance(self.classifies, ChemicalSaltId):
            self.classifies = ChemicalSaltId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalSaltByCation(ChemicalSaltGroupingClass):
    """
    A grouping class for a chemical salt named by cation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalSaltByCation"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalSaltByCation"
    class_name: ClassVar[str] = "ChemicalSaltByCation"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalSaltByCation

    id: Union[str, ChemicalSaltByCationId] = None
    has_cationic_component: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalSaltByCationId):
            self.id = ChemicalSaltByCationId(self.id)

        if self.has_cationic_component is not None and not isinstance(self.has_cationic_component, str):
            self.has_cationic_component = str(self.has_cationic_component)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalSaltByAnion(ChemicalSaltGroupingClass):
    """
    A grouping class for a chemical salt named by anion
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalSaltByAnion"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalSaltByAnion"
    class_name: ClassVar[str] = "ChemicalSaltByAnion"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalSaltByAnion

    id: Union[str, ChemicalSaltByAnionId] = None
    has_anionic_component: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalSaltByAnionId):
            self.id = ChemicalSaltByAnionId(self.id)

        if self.has_anionic_component is not None and not isinstance(self.has_anionic_component, str):
            self.has_anionic_component = str(self.has_anionic_component)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneralizedMolecularStructureClass(MoleculeGroupingClass):
    """
    A molecule grouping class that can be written using a chemical formula using variables (e.g. n), or arithmetic
    expressions uing variables (e.g. 2n+2), plus optionally constraints on those variables (e.g. n>3). An example is
    alkane; CnH2n+2, which groups specific molecules such as methane
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["GeneralizedMolecularStructureClass"]
    class_class_curie: ClassVar[str] = "chemrof:GeneralizedMolecularStructureClass"
    class_name: ClassVar[str] = "GeneralizedMolecularStructureClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.GeneralizedMolecularStructureClass

    id: Union[str, GeneralizedMolecularStructureClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneralizedMolecularStructureClassId):
            self.id = GeneralizedMolecularStructureClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonomericPolymericGroupingClass(GeneralizedMolecularStructureClass):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MonomericPolymericGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:MonomericPolymericGroupingClass"
    class_name: ClassVar[str] = "MonomericPolymericGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MonomericPolymericGroupingClass

    id: Union[str, MonomericPolymericGroupingClassId] = None
    has_repeat_unit: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonomericPolymericGroupingClassId):
            self.id = MonomericPolymericGroupingClassId(self.id)

        if self.has_repeat_unit is not None and not isinstance(self.has_repeat_unit, ChemicalEntityId):
            self.has_repeat_unit = ChemicalEntityId(self.has_repeat_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GroupingClassForAcidsOrBases(MoleculeGroupingClass):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["GroupingClassForAcidsOrBases"]
    class_class_curie: ClassVar[str] = "chemrof:GroupingClassForAcidsOrBases"
    class_name: ClassVar[str] = "GroupingClassForAcidsOrBases"
    class_model_uri: ClassVar[URIRef] = CHEMROF.GroupingClassForAcidsOrBases

    id: Union[str, GroupingClassForAcidsOrBasesId] = None
    conjugate_base_of: Optional[Union[str, DomainEntityId]] = None
    conjugate_acid_of: Optional[Union[str, DomainEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.conjugate_base_of is not None and not isinstance(self.conjugate_base_of, DomainEntityId):
            self.conjugate_base_of = DomainEntityId(self.conjugate_base_of)

        if self.conjugate_acid_of is not None and not isinstance(self.conjugate_acid_of, DomainEntityId):
            self.conjugate_acid_of = DomainEntityId(self.conjugate_acid_of)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcidAnionGroupingClass(GroupingClassForAcidsOrBases):
    """
    A molecule grouping class that groups the different ion forms of the base of an acid
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AcidAnionGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:AcidAnionGroupingClass"
    class_name: ClassVar[str] = "AcidAnionGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AcidAnionGroupingClass

    id: Union[str, AcidAnionGroupingClassId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcidAnionGroupingClassId):
            self.id = AcidAnionGroupingClassId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneralAcidBaseGroupingClass(GroupingClassForAcidsOrBases):
    """
    A molecule grouping class that can groups an acid together with all its conjugate bases. physiological
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["GeneralAcidBaseGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:GeneralAcidBaseGroupingClass"
    class_name: ClassVar[str] = "GeneralAcidBaseGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.GeneralAcidBaseGroupingClass

    id: Union[str, GeneralAcidBaseGroupingClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneralAcidBaseGroupingClassId):
            self.id = GeneralAcidBaseGroupingClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcidBaseConflationClass(GroupingClassForAcidsOrBases):
    """
    A molecule grouping class that can groups an acid together with all its conjugate bases. physiological
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AcidBaseConflationClass"]
    class_class_curie: ClassVar[str] = "chemrof:AcidBaseConflationClass"
    class_name: ClassVar[str] = "AcidBaseConflationClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AcidBaseConflationClass

    id: Union[str, AcidBaseConflationClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcidBaseConflationClassId):
            self.id = AcidBaseConflationClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtomGroupingClass(ChemicalGroupingClass):
    """
    A grouping class that classifies atoms. For example, metal atom
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AtomGroupingClass"]
    class_class_curie: ClassVar[str] = "chemrof:AtomGroupingClass"
    class_name: ClassVar[str] = "AtomGroupingClass"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomGroupingClass

    id: Union[str, AtomGroupingClassId] = None
    subtype_of: Optional[Union[Union[str, MoleculeGroupingClassId], list[Union[str, MoleculeGroupingClassId]]]] = empty_list()
    classifies: Optional[Union[str, AtomId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AtomGroupingClassId):
            self.id = AtomGroupingClassId(self.id)

        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of] if self.subtype_of is not None else []
        self.subtype_of = [v if isinstance(v, MoleculeGroupingClassId) else MoleculeGroupingClassId(v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, AtomId):
            self.classifies = AtomId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtomGroupingByPeriodicTablePlacement(AtomGroupingClass):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AtomGroupingByPeriodicTablePlacement"]
    class_class_curie: ClassVar[str] = "chemrof:AtomGroupingByPeriodicTablePlacement"
    class_name: ClassVar[str] = "AtomGroupingByPeriodicTablePlacement"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomGroupingByPeriodicTablePlacement

    id: Union[str, AtomGroupingByPeriodicTablePlacementId] = None

@dataclass(repr=False)
class AtomGroupingByPeriodicTableGroup(AtomGroupingByPeriodicTablePlacement):
    """
    Example: p-block atom
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AtomGroupingByPeriodicTableGroup"]
    class_class_curie: ClassVar[str] = "chemrof:AtomGroupingByPeriodicTableGroup"
    class_name: ClassVar[str] = "AtomGroupingByPeriodicTableGroup"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomGroupingByPeriodicTableGroup

    id: Union[str, AtomGroupingByPeriodicTableGroupId] = None
    in_periodic_table_group: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AtomGroupingByPeriodicTableGroupId):
            self.id = AtomGroupingByPeriodicTableGroupId(self.id)

        if self.in_periodic_table_group is not None and not isinstance(self.in_periodic_table_group, int):
            self.in_periodic_table_group = int(self.in_periodic_table_group)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtomGroupingByPeriodicTableBlock(AtomGroupingByPeriodicTablePlacement):
    """
    Example: group 13 atom
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AtomGroupingByPeriodicTableBlock"]
    class_class_curie: ClassVar[str] = "chemrof:AtomGroupingByPeriodicTableBlock"
    class_name: ClassVar[str] = "AtomGroupingByPeriodicTableBlock"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomGroupingByPeriodicTableBlock

    id: Union[str, AtomGroupingByPeriodicTableBlockId] = None
    in_periodic_table_block: Optional[Union[str, "PeriodicTableBlockEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AtomGroupingByPeriodicTableBlockId):
            self.id = AtomGroupingByPeriodicTableBlockId(self.id)

        if self.in_periodic_table_block is not None and not isinstance(self.in_periodic_table_block, PeriodicTableBlockEnum):
            self.in_periodic_table_block = PeriodicTableBlockEnum(self.in_periodic_table_block)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtomGroupingByProperty(AtomGroupingClass):
    """
    Example: metal atom
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AtomGroupingByProperty"]
    class_class_curie: ClassVar[str] = "chemrof:AtomGroupingByProperty"
    class_name: ClassVar[str] = "AtomGroupingByProperty"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomGroupingByProperty

    id: Union[str, AtomGroupingByPropertyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AtomGroupingByPropertyId):
            self.id = AtomGroupingByPropertyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Material(PhysicochemicalEntity):
    """
    A substance composed of repeated chemical units that has a specific arrangement of atoms or molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Material"]
    class_class_curie: ClassVar[str] = "chemrof:Material"
    class_name: ClassVar[str] = "Material"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Material

    id: Union[str, MaterialId] = None
    has_repeat_unit: Optional[Union[str, ChemicalEntityId]] = None
    has_part: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialId):
            self.id = MaterialId(self.id)

        if self.has_repeat_unit is not None and not isinstance(self.has_repeat_unit, ChemicalEntityId):
            self.has_repeat_unit = ChemicalEntityId(self.has_repeat_unit)

        if self.has_part is not None and not isinstance(self.has_part, ChemicalEntityId):
            self.has_part = ChemicalEntityId(self.has_part)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Nanomaterial(Material):
    """
    A material of which a single unit is sized (in at least one dimension) between 1 and 100 nm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Nanomaterial"]
    class_class_curie: ClassVar[str] = "chemrof:Nanomaterial"
    class_name: ClassVar[str] = "Nanomaterial"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Nanomaterial

    id: Union[str, NanomaterialId] = None
    has_morphological_category: Optional[Union[str, "NanostructureMorphologyEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NanomaterialId):
            self.id = NanomaterialId(self.id)

        if self.has_morphological_category is not None and not isinstance(self.has_morphological_category, NanostructureMorphologyEnum):
            self.has_morphological_category = NanostructureMorphologyEnum(self.has_morphological_category)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Mineral(Material):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Mineral"]
    class_class_curie: ClassVar[str] = "chemrof:Mineral"
    class_name: ClassVar[str] = "Mineral"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Mineral

    id: Union[str, MineralId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MineralId):
            self.id = MineralId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


class ChemicalEntityOrGrouping(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalEntityOrGrouping"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalEntityOrGrouping"
    class_name: ClassVar[str] = "ChemicalEntityOrGrouping"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalEntityOrGrouping


class Connectivity(YAMLRoot):
    """
    Abstract grouping for slots that related chemical entities via a connectivity relationships
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Connectivity"]
    class_class_curie: ClassVar[str] = "chemrof:Connectivity"
    class_name: ClassVar[str] = "Connectivity"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Connectivity


class FullyCovalentlyBonded(Connectivity):
    """
    All pairs of atoms in this entity are transitively connected via covalent bonds
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["FullyCovalentlyBonded"]
    class_class_curie: ClassVar[str] = "chemrof:FullyCovalentlyBonded"
    class_name: ClassVar[str] = "FullyCovalentlyBonded"
    class_model_uri: ClassVar[URIRef] = CHEMROF.FullyCovalentlyBonded


class WeaklyBonded(Connectivity):
    """
    Not covalently bonded
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["WeaklyBonded"]
    class_class_curie: ClassVar[str] = "chemrof:WeaklyBonded"
    class_name: ClassVar[str] = "WeaklyBonded"
    class_model_uri: ClassVar[URIRef] = CHEMROF.WeaklyBonded


class State(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["State"]
    class_class_curie: ClassVar[str] = "chemrof:State"
    class_name: ClassVar[str] = "State"
    class_model_uri: ClassVar[URIRef] = CHEMROF.State


@dataclass(repr=False)
class ChargeState(State):
    """
    Applies to entities that have a charge state, which may be positive, negative, or neutral
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChargeState"]
    class_class_curie: ClassVar[str] = "chemrof:ChargeState"
    class_name: ClassVar[str] = "ChargeState"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChargeState

    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Uncharged(ChargeState):
    """
    Applies to entities that are uncharged, i.e. have an elemental charge of zero
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Uncharged"]
    class_class_curie: ClassVar[str] = "chemrof:Uncharged"
    class_name: ClassVar[str] = "Uncharged"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Uncharged

    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


class Charged(ChargeState):
    """
    Applies to entities that are charged, either positive or negative
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Charged"]
    class_class_curie: ClassVar[str] = "chemrof:Charged"
    class_name: ClassVar[str] = "Charged"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Charged


@dataclass(repr=False)
class AnionState(Charged):
    """
    This mixin is applied on an entity (atom or molecule) that is negatively charged
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AnionState"]
    class_class_curie: ClassVar[str] = "chemrof:AnionState"
    class_name: ClassVar[str] = "AnionState"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AnionState

    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CationState(Charged):
    """
    This mixin is applied on an entity (atom or molecule) that is positively charged
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["CationState"]
    class_class_curie: ClassVar[str] = "chemrof:CationState"
    class_name: ClassVar[str] = "CationState"
    class_model_uri: ClassVar[URIRef] = CHEMROF.CationState

    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PolyatomicEntity(ChemicalEntity):
    """
    Any chemical entity consisting of more than one atom.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["PolyatomicEntity"]
    class_class_curie: ClassVar[str] = "chemrof:PolyatomicEntity"
    class_name: ClassVar[str] = "PolyatomicEntity"
    class_model_uri: ClassVar[URIRef] = CHEMROF.PolyatomicEntity

    id: Union[str, PolyatomicEntityId] = None
    inchi_atom_connections_sublayer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.inchi_atom_connections_sublayer is not None and not isinstance(self.inchi_atom_connections_sublayer, str):
            self.inchi_atom_connections_sublayer = str(self.inchi_atom_connections_sublayer)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class MolecularComponent(PolyatomicEntity):
    """
    A proper part of a molecule that is larger than an atom
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MolecularComponent"]
    class_class_curie: ClassVar[str] = "chemrof:MolecularComponent"
    class_name: ClassVar[str] = "MolecularComponent"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MolecularComponent

    id: Union[str, MolecularComponentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularComponentId):
            self.id = MolecularComponentId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class PolymerPart(MolecularComponent):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["PolymerPart"]
    class_class_curie: ClassVar[str] = "chemrof:PolymerPart"
    class_name: ClassVar[str] = "PolymerPart"
    class_model_uri: ClassVar[URIRef] = CHEMROF.PolymerPart

    id: Union[str, PolymerPartId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolymerPartId):
            self.id = PolymerPartId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Monomer(PolymerPart):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Monomer"]
    class_class_curie: ClassVar[str] = "chemrof:Monomer"
    class_name: ClassVar[str] = "Monomer"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Monomer

    id: Union[str, MonomerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonomerId):
            self.id = MonomerId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class MolecularSubsequence(PolymerPart):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MolecularSubsequence"]
    class_class_curie: ClassVar[str] = "chemrof:MolecularSubsequence"
    class_name: ClassVar[str] = "MolecularSubsequence"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MolecularSubsequence

    id: Union[str, MolecularSubsequenceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularSubsequenceId):
            self.id = MolecularSubsequenceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class ChemicalGroup(MolecularComponent):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalGroup"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalGroup"
    class_name: ClassVar[str] = "ChemicalGroup"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalGroup

    id: Union[str, ChemicalGroupId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalGroupId):
            self.id = ChemicalGroupId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class ChemicalMixture(PolyatomicEntity):
    """
    A polyatomic entity that consists of two or more parts that are weakly bound, may be of known or unknown
    stoichiometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalMixture"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalMixture"
    class_name: ClassVar[str] = "ChemicalMixture"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalMixture

    id: Union[str, ChemicalMixtureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class PreciseChemicalMixture(ChemicalMixture):
    """
    A polyatomic entity that consists of two or more parts that are weakly bound, and of known stoichiometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["PreciseChemicalMixture"]
    class_class_curie: ClassVar[str] = "chemrof:PreciseChemicalMixture"
    class_name: ClassVar[str] = "PreciseChemicalMixture"
    class_model_uri: ClassVar[URIRef] = CHEMROF.PreciseChemicalMixture

    id: Union[str, PreciseChemicalMixtureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class MolecularComplex(PreciseChemicalMixture):
    """
    A molecular complex is a chemical complex composed of at least one weakly interacting molecule.[SIO] Examples:
    chromosome, double-standed DNA, protein-containing macromolecular complex
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MolecularComplex"]
    class_class_curie: ClassVar[str] = "chemrof:MolecularComplex"
    class_name: ClassVar[str] = "MolecularComplex"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MolecularComplex

    id: Union[str, MolecularComplexId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularComplexId):
            self.id = MolecularComplexId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class SupramolecularPolymer(MolecularComplex):
    """
    polymeric arrays of monomeric units that are connected by reversible and highly directional secondary
    interactions–that is, non-covalent bonds
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["SupramolecularPolymer"]
    class_class_curie: ClassVar[str] = "chemrof:SupramolecularPolymer"
    class_name: ClassVar[str] = "SupramolecularPolymer"
    class_model_uri: ClassVar[URIRef] = CHEMROF.SupramolecularPolymer

    id: Union[str, SupramolecularPolymerId] = None
    polymer_of: Optional[Union[str, MacromoleculeId]] = None
    has_repeat_unit: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SupramolecularPolymerId):
            self.id = SupramolecularPolymerId(self.id)

        if self.polymer_of is not None and not isinstance(self.polymer_of, MacromoleculeId):
            self.polymer_of = MacromoleculeId(self.polymer_of)

        if self.has_repeat_unit is not None and not isinstance(self.has_repeat_unit, ChemicalEntityId):
            self.has_repeat_unit = ChemicalEntityId(self.has_repeat_unit)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class ImpreciseChemicalMixture(ChemicalMixture):
    """
    A macroscopic polyatomic entity that consists of multiple chemical entities where the stoichiometry is not
    specified and the spatial arrangement of the ingredients is not defined. Examples include coal, tea tree oil,
    toothpaste, organometallic compounds, heterogeneous metals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ImpreciseChemicalMixture"]
    class_class_curie: ClassVar[str] = "chemrof:ImpreciseChemicalMixture"
    class_name: ClassVar[str] = "ImpreciseChemicalMixture"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ImpreciseChemicalMixture

    id: Union[str, ImpreciseChemicalMixtureId] = None
    has_proportional_parts: Optional[Union[Union[dict, "ProportionalPart"], list[Union[dict, "ProportionalPart"]]]] = empty_list()
    has_mixfile_location: Optional[str] = None
    has_minchi_representation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImpreciseChemicalMixtureId):
            self.id = ImpreciseChemicalMixtureId(self.id)

        if not isinstance(self.has_proportional_parts, list):
            self.has_proportional_parts = [self.has_proportional_parts] if self.has_proportional_parts is not None else []
        self.has_proportional_parts = [v if isinstance(v, ProportionalPart) else ProportionalPart(**as_dict(v)) for v in self.has_proportional_parts]

        if self.has_mixfile_location is not None and not isinstance(self.has_mixfile_location, str):
            self.has_mixfile_location = str(self.has_mixfile_location)

        if self.has_minchi_representation is not None and not isinstance(self.has_minchi_representation, str):
            self.has_minchi_representation = str(self.has_minchi_representation)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Molecule(PolyatomicEntity):
    """
    A chemical entity that consists of two or more atoms where all atoms are connected via covalent bonds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Molecule"]
    class_class_curie: ClassVar[str] = "chemrof:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Molecule

    id: Union[str, MoleculeId] = None
    has_atom_occurrences: Optional[Union[dict[Union[str, AtomOccurrenceName], Union[dict, "AtomOccurrence"]], list[Union[dict, "AtomOccurrence"]]]] = empty_dict()
    has_bonds: Optional[Union[Union[dict, "AtomicBond"], list[Union[dict, "AtomicBond"]]]] = empty_list()
    has_submolecules: Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]] = empty_list()
    has_atoms: Optional[Union[Union[str, AtomId], list[Union[str, AtomId]]]] = empty_list()
    is_organic: Optional[Union[bool, Bool]] = None
    has_part: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoleculeId):
            self.id = MoleculeId(self.id)

        self._normalize_inlined_as_list(slot_name="has_atom_occurrences", slot_type=AtomOccurrence, key_name="name", keyed=True)

        if not isinstance(self.has_bonds, list):
            self.has_bonds = [self.has_bonds] if self.has_bonds is not None else []
        self.has_bonds = [v if isinstance(v, AtomicBond) else AtomicBond(**as_dict(v)) for v in self.has_bonds]

        if not isinstance(self.has_submolecules, list):
            self.has_submolecules = [self.has_submolecules] if self.has_submolecules is not None else []
        self.has_submolecules = [v if isinstance(v, MoleculeId) else MoleculeId(v) for v in self.has_submolecules]

        if not isinstance(self.has_atoms, list):
            self.has_atoms = [self.has_atoms] if self.has_atoms is not None else []
        self.has_atoms = [v if isinstance(v, AtomId) else AtomId(v) for v in self.has_atoms]

        if self.is_organic is not None and not isinstance(self.is_organic, Bool):
            self.is_organic = Bool(self.is_organic)

        if self.has_part is not None and not isinstance(self.has_part, str):
            self.has_part = str(self.has_part)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class SmallMolecule(Molecule):
    """
    A molecule characterized by availability in small-molecule databases
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["SmallMolecule"]
    class_class_curie: ClassVar[str] = "chemrof:SmallMolecule"
    class_name: ClassVar[str] = "SmallMolecule"
    class_model_uri: ClassVar[URIRef] = CHEMROF.SmallMolecule

    id: Union[str, SmallMoleculeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SmallMoleculeId):
            self.id = SmallMoleculeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Macromolecule(Molecule):
    """
    A large molecule, such as a polymer, lipid, or macrocycle
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Macromolecule"]
    class_class_curie: ClassVar[str] = "chemrof:Macromolecule"
    class_name: ClassVar[str] = "Macromolecule"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Macromolecule

    id: Union[str, MacromoleculeId] = None
    has_submolecules: Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MacromoleculeId):
            self.id = MacromoleculeId(self.id)

        if not isinstance(self.has_submolecules, list):
            self.has_submolecules = [self.has_submolecules] if self.has_submolecules is not None else []
        self.has_submolecules = [v if isinstance(v, MoleculeId) else MoleculeId(v) for v in self.has_submolecules]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Peptide(Macromolecule):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Peptide"]
    class_class_curie: ClassVar[str] = "chemrof:Peptide"
    class_name: ClassVar[str] = "Peptide"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Peptide

    id: Union[str, PeptideId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PeptideId):
            self.id = PeptideId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Protein(Macromolecule):
    """
    A macromolecule composed of one or more polypeptide chains of amino acids that fold into a specific
    three-dimensional structure and perform biological functions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Protein"]
    class_class_curie: ClassVar[str] = "chemrof:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Protein

    id: Union[str, ProteinId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Glycan(Macromolecule):
    """
    A macromolecule consisting of a large number of monosaccharides linked glycosidically
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Glycan"]
    class_class_curie: ClassVar[str] = "chemrof:Glycan"
    class_name: ClassVar[str] = "Glycan"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Glycan

    id: Union[str, GlycanId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GlycanId):
            self.id = GlycanId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class MonomolecularPolymer(Macromolecule):
    """
    A macromolecule composed of repeating subunits. Examples: cellulose
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MonomolecularPolymer"]
    class_class_curie: ClassVar[str] = "chemrof:MonomolecularPolymer"
    class_name: ClassVar[str] = "MonomolecularPolymer"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MonomolecularPolymer

    id: Union[str, MonomolecularPolymerId] = None
    polymer_of: Optional[Union[str, MacromoleculeId]] = None
    has_repeat_unit: Optional[Union[str, ChemicalEntityId]] = None
    is_branched: Optional[Union[bool, Bool]] = None
    polymer_architecture_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonomolecularPolymerId):
            self.id = MonomolecularPolymerId(self.id)

        if self.polymer_of is not None and not isinstance(self.polymer_of, MacromoleculeId):
            self.polymer_of = MacromoleculeId(self.polymer_of)

        if self.has_repeat_unit is not None and not isinstance(self.has_repeat_unit, ChemicalEntityId):
            self.has_repeat_unit = ChemicalEntityId(self.has_repeat_unit)

        if self.is_branched is not None and not isinstance(self.is_branched, Bool):
            self.is_branched = Bool(self.is_branched)

        if self.polymer_architecture_type is not None and not isinstance(self.polymer_architecture_type, str):
            self.polymer_architecture_type = str(self.polymer_architecture_type)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Copolymer(MonomolecularPolymer):
    """
    a polymer with a more than one type of repeating unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Copolymer"]
    class_class_curie: ClassVar[str] = "chemrof:Copolymer"
    class_name: ClassVar[str] = "Copolymer"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Copolymer

    id: Union[str, CopolymerId] = None
    polymer_of: Optional[Union[Union[str, MacromoleculeId], list[Union[str, MacromoleculeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CopolymerId):
            self.id = CopolymerId(self.id)

        if not isinstance(self.polymer_of, list):
            self.polymer_of = [self.polymer_of] if self.polymer_of is not None else []
        self.polymer_of = [v if isinstance(v, MacromoleculeId) else MacromoleculeId(v) for v in self.polymer_of]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Homopolymer(MonomolecularPolymer):
    """
    a polymer with a single type of repeating unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Homopolymer"]
    class_class_curie: ClassVar[str] = "chemrof:Homopolymer"
    class_name: ClassVar[str] = "Homopolymer"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Homopolymer

    id: Union[str, HomopolymerId] = None
    polymer_of: Optional[Union[str, MacromoleculeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HomopolymerId):
            self.id = HomopolymerId(self.id)

        if self.polymer_of is not None and not isinstance(self.polymer_of, MacromoleculeId):
            self.polymer_of = MacromoleculeId(self.polymer_of)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class NaturalProduct(Molecule):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["NaturalProduct"]
    class_class_curie: ClassVar[str] = "chemrof:NaturalProduct"
    class_name: ClassVar[str] = "NaturalProduct"
    class_model_uri: ClassVar[URIRef] = CHEMROF.NaturalProduct

    id: Union[str, NaturalProductId] = None
    derived_from_organisms: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NaturalProductId):
            self.id = NaturalProductId(self.id)

        if not isinstance(self.derived_from_organisms, list):
            self.derived_from_organisms = [self.derived_from_organisms] if self.derived_from_organisms is not None else []
        self.derived_from_organisms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.derived_from_organisms]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Moiety(MolecularComponent):
    """
    a named part of a molecule. In some instances moieties may be composed of yet smaller moieties and functional
    groups
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Moiety"]
    class_class_curie: ClassVar[str] = "chemrof:Moiety"
    class_name: ClassVar[str] = "Moiety"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Moiety

    id: Union[str, MoietyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoietyId):
            self.id = MoietyId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class SequenceInterval(MolecularComponent):
    """
    a chain of connected monomers in a linear polymer - for example, a sub-region of an amino acid or nucleotide
    sequence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["SequenceInterval"]
    class_class_curie: ClassVar[str] = "chemrof:SequenceInterval"
    class_name: ClassVar[str] = "SequenceInterval"
    class_model_uri: ClassVar[URIRef] = CHEMROF.SequenceInterval

    id: Union[str, SequenceIntervalId] = None
    has_sequence_representation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_sequence_representation is not None and not isinstance(self.has_sequence_representation, str):
            self.has_sequence_representation = str(self.has_sequence_representation)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class AminoAcidSequenceInterval(SequenceInterval):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AminoAcidSequenceInterval"]
    class_class_curie: ClassVar[str] = "chemrof:AminoAcidSequenceInterval"
    class_name: ClassVar[str] = "AminoAcidSequenceInterval"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AminoAcidSequenceInterval

    id: Union[str, AminoAcidSequenceIntervalId] = None
    has_sequence_representation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AminoAcidSequenceIntervalId):
            self.id = AminoAcidSequenceIntervalId(self.id)

        if self.has_sequence_representation is not None and not isinstance(self.has_sequence_representation, str):
            self.has_sequence_representation = str(self.has_sequence_representation)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class NucleotideSequenceInterval(SequenceInterval):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["NucleotideSequenceInterval"]
    class_class_curie: ClassVar[str] = "chemrof:NucleotideSequenceInterval"
    class_name: ClassVar[str] = "NucleotideSequenceInterval"
    class_model_uri: ClassVar[URIRef] = CHEMROF.NucleotideSequenceInterval

    id: Union[str, NucleotideSequenceIntervalId] = None
    has_sequence_representation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NucleotideSequenceIntervalId):
            self.id = NucleotideSequenceIntervalId(self.id)

        if self.has_sequence_representation is not None and not isinstance(self.has_sequence_representation, str):
            self.has_sequence_representation = str(self.has_sequence_representation)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class DNASequenceInterval(NucleotideSequenceInterval):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["DNASequenceInterval"]
    class_class_curie: ClassVar[str] = "chemrof:DNASequenceInterval"
    class_name: ClassVar[str] = "DNASequenceInterval"
    class_model_uri: ClassVar[URIRef] = CHEMROF.DNASequenceInterval

    id: Union[str, DNASequenceIntervalId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DNASequenceIntervalId):
            self.id = DNASequenceIntervalId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class RNASequenceInterval(NucleotideSequenceInterval):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["RNASequenceInterval"]
    class_class_curie: ClassVar[str] = "chemrof:RNASequenceInterval"
    class_name: ClassVar[str] = "RNASequenceInterval"
    class_model_uri: ClassVar[URIRef] = CHEMROF.RNASequenceInterval

    id: Union[str, RNASequenceIntervalId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RNASequenceIntervalId):
            self.id = RNASequenceIntervalId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class FunctionalGroup(MolecularComponent):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["FunctionalGroup"]
    class_class_curie: ClassVar[str] = "chemrof:FunctionalGroup"
    class_name: ClassVar[str] = "FunctionalGroup"
    class_model_uri: ClassVar[URIRef] = CHEMROF.FunctionalGroup

    id: Union[str, FunctionalGroupId] = None
    is_substitutent_group_from: Optional[Union[str, MoleculeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalGroupId):
            self.id = FunctionalGroupId(self.id)

        if self.is_substitutent_group_from is not None and not isinstance(self.is_substitutent_group_from, MoleculeId):
            self.is_substitutent_group_from = MoleculeId(self.is_substitutent_group_from)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class MolecularSpecies(Molecule):
    """
    A molecule in which the units are identical. Example: methyl
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MolecularSpecies"]
    class_class_curie: ClassVar[str] = "chemrof:MolecularSpecies"
    class_name: ClassVar[str] = "MolecularSpecies"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MolecularSpecies

    id: Union[str, MolecularSpeciesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularSpeciesId):
            self.id = MolecularSpeciesId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class NonSpeciesMolecule(Molecule):
    """
    A molecule in which the units are not identical. TODO: move this higher
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["NonSpeciesMolecule"]
    class_class_curie: ClassVar[str] = "chemrof:NonSpeciesMolecule"
    class_name: ClassVar[str] = "NonSpeciesMolecule"
    class_model_uri: ClassVar[URIRef] = CHEMROF.NonSpeciesMolecule

    id: Union[str, NonSpeciesMoleculeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonSpeciesMoleculeId):
            self.id = NonSpeciesMoleculeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class MoleculeByChargeState(Molecule):
    """
    A molecule that has a charge state specified
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MoleculeByChargeState"]
    class_class_curie: ClassVar[str] = "chemrof:MoleculeByChargeState"
    class_name: ClassVar[str] = "MoleculeByChargeState"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MoleculeByChargeState

    id: Union[str, MoleculeByChargeStateId] = None
    bronsted_acid_base_role: Optional[Union[str, "BronstedAcidBaseRoleEnum"]] = None
    acidity: Optional[float] = None
    hard_or_soft: Optional[Union[str, "HardOrSoftEnum"]] = None
    acid_form_of: Optional[Union[Union[str, MoleculeByChargeStateId], list[Union[str, MoleculeByChargeStateId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.bronsted_acid_base_role is not None and not isinstance(self.bronsted_acid_base_role, BronstedAcidBaseRoleEnum):
            self.bronsted_acid_base_role = BronstedAcidBaseRoleEnum(self.bronsted_acid_base_role)

        if self.acidity is not None and not isinstance(self.acidity, float):
            self.acidity = float(self.acidity)

        if self.hard_or_soft is not None and not isinstance(self.hard_or_soft, HardOrSoftEnum):
            self.hard_or_soft = HardOrSoftEnum(self.hard_or_soft)

        if not isinstance(self.acid_form_of, list):
            self.acid_form_of = [self.acid_form_of] if self.acid_form_of is not None else []
        self.acid_form_of = [v if isinstance(v, MoleculeByChargeStateId) else MoleculeByChargeStateId(v) for v in self.acid_form_of]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class PolyatomicIon(MoleculeByChargeState):
    """
    A molecule that has a net charge. For example, nitrate is a molecular and ionic species; its formula is (NO3-).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["PolyatomicIon"]
    class_class_curie: ClassVar[str] = "chemrof:PolyatomicIon"
    class_name: ClassVar[str] = "PolyatomicIon"
    class_model_uri: ClassVar[URIRef] = CHEMROF.PolyatomicIon

    id: Union[str, PolyatomicIonId] = None
    conjugate_base_of: Optional[Union[str, DomainEntityId]] = None
    conjugate_acid_of: Optional[Union[str, DomainEntityId]] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolyatomicIonId):
            self.id = PolyatomicIonId(self.id)

        if self.conjugate_base_of is not None and not isinstance(self.conjugate_base_of, DomainEntityId):
            self.conjugate_base_of = DomainEntityId(self.conjugate_base_of)

        if self.conjugate_acid_of is not None and not isinstance(self.conjugate_acid_of, DomainEntityId):
            self.conjugate_acid_of = DomainEntityId(self.conjugate_acid_of)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class MolecularCation(PolyatomicIon):
    """
    A polyatomic ion that is positive
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MolecularCation"]
    class_class_curie: ClassVar[str] = "chemrof:MolecularCation"
    class_name: ClassVar[str] = "MolecularCation"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MolecularCation

    id: Union[str, MolecularCationId] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularCationId):
            self.id = MolecularCationId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class MolecularAnion(PolyatomicIon):
    """
    A polyatomic ion that is negative
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MolecularAnion"]
    class_class_curie: ClassVar[str] = "chemrof:MolecularAnion"
    class_name: ClassVar[str] = "MolecularAnion"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MolecularAnion

    id: Union[str, MolecularAnionId] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularAnionId):
            self.id = MolecularAnionId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class NetUnchargedMolecule(MoleculeByChargeState):
    """
    A molecule that has no net charge
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["NetUnchargedMolecule"]
    class_class_curie: ClassVar[str] = "chemrof:NetUnchargedMolecule"
    class_name: ClassVar[str] = "NetUnchargedMolecule"
    class_model_uri: ClassVar[URIRef] = CHEMROF.NetUnchargedMolecule

    id: Union[str, NetUnchargedMoleculeId] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetUnchargedMoleculeId):
            self.id = NetUnchargedMoleculeId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Zwitterion(NetUnchargedMolecule):
    """
    A molecule that has both a positive and negative charges but is net neutral
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Zwitterion"]
    class_class_curie: ClassVar[str] = "chemrof:Zwitterion"
    class_name: ClassVar[str] = "Zwitterion"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Zwitterion

    id: Union[str, ZwitterionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ZwitterionId):
            self.id = ZwitterionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class NeutralMolecule(NetUnchargedMolecule):
    """
    A molecule that has no net charge and is not a zwitterion
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["NeutralMolecule"]
    class_class_curie: ClassVar[str] = "chemrof:NeutralMolecule"
    class_name: ClassVar[str] = "NeutralMolecule"
    class_model_uri: ClassVar[URIRef] = CHEMROF.NeutralMolecule

    id: Union[str, NeutralMoleculeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NeutralMoleculeId):
            self.id = NeutralMoleculeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Atom(ChemicalEntity):
    """
    A chemical entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Atom"]
    class_class_curie: ClassVar[str] = "chemrof:Atom"
    class_name: ClassVar[str] = "Atom"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Atom

    id: Union[str, AtomId] = None
    atomic_number: Optional[int] = None
    symbol: Optional[str] = None
    name: Optional[str] = None
    has_nuclear_parts: Optional[Union[dict, "SubatomicParticleOccurrence"]] = None
    has_part: Optional[Union[str, SubatomicParticleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.atomic_number is not None and not isinstance(self.atomic_number, int):
            self.atomic_number = int(self.atomic_number)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.has_nuclear_parts is not None and not isinstance(self.has_nuclear_parts, SubatomicParticleOccurrence):
            self.has_nuclear_parts = SubatomicParticleOccurrence(**as_dict(self.has_nuclear_parts))

        if self.has_part is not None and not isinstance(self.has_part, SubatomicParticleId):
            self.has_part = SubatomicParticleId(self.has_part)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class PartiallySpecifiedAtom(Atom):
    """
    An atom type that only has a subset of properties (has atomic number, charge, and neutron number) stated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["PartiallySpecifiedAtom"]
    class_class_curie: ClassVar[str] = "chemrof:PartiallySpecifiedAtom"
    class_name: ClassVar[str] = "PartiallySpecifiedAtom"
    class_model_uri: ClassVar[URIRef] = CHEMROF.PartiallySpecifiedAtom

    id: Union[str, PartiallySpecifiedAtomId] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class ChemicalElement(PartiallySpecifiedAtom):
    """
    generic form of an atom, with unspecified neutron or charge
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalElement"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalElement"
    class_name: ClassVar[str] = "ChemicalElement"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalElement

    id: Union[str, ChemicalElementId] = None
    in_periodic_table_group: Optional[int] = None
    in_periodic_table_block: Optional[Union[str, "PeriodicTableBlockEnum"]] = None
    symbol: Optional[str] = None
    boiling_point_in_celcius: Optional[float] = None
    melting_point_in_celcius: Optional[float] = None
    standard_atomic_weight: Optional[float] = None
    mass: Optional[float] = None
    monoisotopic_mass: Optional[float] = None
    electron_configuration: Optional[str] = None
    has_stereocenter: Optional[Union[Union[dict, "Stereocenter"], list[Union[dict, "Stereocenter"]]]] = empty_list()
    has_major_microspecies_at_pH7_3: Optional[Union[str, ChemicalElementId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalElementId):
            self.id = ChemicalElementId(self.id)

        if self.in_periodic_table_group is not None and not isinstance(self.in_periodic_table_group, int):
            self.in_periodic_table_group = int(self.in_periodic_table_group)

        if self.in_periodic_table_block is not None and not isinstance(self.in_periodic_table_block, PeriodicTableBlockEnum):
            self.in_periodic_table_block = PeriodicTableBlockEnum(self.in_periodic_table_block)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.boiling_point_in_celcius is not None and not isinstance(self.boiling_point_in_celcius, float):
            self.boiling_point_in_celcius = float(self.boiling_point_in_celcius)

        if self.melting_point_in_celcius is not None and not isinstance(self.melting_point_in_celcius, float):
            self.melting_point_in_celcius = float(self.melting_point_in_celcius)

        if self.standard_atomic_weight is not None and not isinstance(self.standard_atomic_weight, float):
            self.standard_atomic_weight = float(self.standard_atomic_weight)

        if self.mass is not None and not isinstance(self.mass, float):
            self.mass = float(self.mass)

        if self.monoisotopic_mass is not None and not isinstance(self.monoisotopic_mass, float):
            self.monoisotopic_mass = float(self.monoisotopic_mass)

        if self.electron_configuration is not None and not isinstance(self.electron_configuration, str):
            self.electron_configuration = str(self.electron_configuration)

        if not isinstance(self.has_stereocenter, list):
            self.has_stereocenter = [self.has_stereocenter] if self.has_stereocenter is not None else []
        self.has_stereocenter = [v if isinstance(v, Stereocenter) else Stereocenter(**as_dict(v)) for v in self.has_stereocenter]

        if self.has_major_microspecies_at_pH7_3 is not None and not isinstance(self.has_major_microspecies_at_pH7_3, ChemicalElementId):
            self.has_major_microspecies_at_pH7_3 = ChemicalElementId(self.has_major_microspecies_at_pH7_3)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Nuclide(PartiallySpecifiedAtom):
    """
    an atomic species characterized by the specific constitution of its nucleus
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Nuclide"]
    class_class_curie: ClassVar[str] = "chemrof:Nuclide"
    class_name: ClassVar[str] = "Nuclide"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Nuclide

    id: Union[str, NuclideId] = None
    energy_level: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NuclideId):
            self.id = NuclideId(self.id)

        if self.energy_level is not None and not isinstance(self.energy_level, str):
            self.energy_level = str(self.energy_level)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Radionuclide(Nuclide):
    """
    an atom that has excess nuclear energy, making it unstable
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Radionuclide"]
    class_class_curie: ClassVar[str] = "chemrof:Radionuclide"
    class_name: ClassVar[str] = "Radionuclide"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Radionuclide

    id: Union[str, RadionuclideId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RadionuclideId):
            self.id = RadionuclideId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Isotope(Nuclide):
    """
    A specific subtype of an atom with a specified neutron number
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Isotope"]
    class_class_curie: ClassVar[str] = "chemrof:Isotope"
    class_name: ClassVar[str] = "Isotope"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Isotope

    id: Union[str, IsotopeId] = None
    has_element: Optional[Union[str, ChemicalElementId]] = None
    neutron_number: Optional[int] = None
    isotope_of: Optional[Union[str, IsotopeId]] = None
    half_life: Optional[int] = None
    decay_product: Optional[Union[str, IsotopeId]] = None
    decay_mode: Optional[str] = None
    decay_energy: Optional[str] = None
    mode_of_formation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsotopeId):
            self.id = IsotopeId(self.id)

        if self.has_element is not None and not isinstance(self.has_element, ChemicalElementId):
            self.has_element = ChemicalElementId(self.has_element)

        if self.neutron_number is not None and not isinstance(self.neutron_number, int):
            self.neutron_number = int(self.neutron_number)

        if self.isotope_of is not None and not isinstance(self.isotope_of, IsotopeId):
            self.isotope_of = IsotopeId(self.isotope_of)

        if self.half_life is not None and not isinstance(self.half_life, int):
            self.half_life = int(self.half_life)

        if self.decay_product is not None and not isinstance(self.decay_product, IsotopeId):
            self.decay_product = IsotopeId(self.decay_product)

        if self.decay_mode is not None and not isinstance(self.decay_mode, str):
            self.decay_mode = str(self.decay_mode)

        if self.decay_energy is not None and not isinstance(self.decay_energy, str):
            self.decay_energy = str(self.decay_energy)

        if self.mode_of_formation is not None and not isinstance(self.mode_of_formation, str):
            self.mode_of_formation = str(self.mode_of_formation)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Isobar(Nuclide):
    """
    Isobars are atoms (nuclides) of different chemical elements that have the same number of nucleons.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Isobar"]
    class_class_curie: ClassVar[str] = "chemrof:Isobar"
    class_name: ClassVar[str] = "Isobar"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Isobar

    id: Union[str, IsobarId] = None
    has_element: Optional[Union[str, ChemicalElementId]] = None
    nucleon_number: Optional[int] = None
    isobar_of: Optional[Union[str, ChemicalEntityId]] = None
    half_life: Optional[int] = None
    decay_product: Optional[Union[str, IsotopeId]] = None
    decay_mode: Optional[str] = None
    decay_energy: Optional[str] = None
    mode_of_formation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsobarId):
            self.id = IsobarId(self.id)

        if self.has_element is not None and not isinstance(self.has_element, ChemicalElementId):
            self.has_element = ChemicalElementId(self.has_element)

        if self.nucleon_number is not None and not isinstance(self.nucleon_number, int):
            self.nucleon_number = int(self.nucleon_number)

        if self.isobar_of is not None and not isinstance(self.isobar_of, ChemicalEntityId):
            self.isobar_of = ChemicalEntityId(self.isobar_of)

        if self.half_life is not None and not isinstance(self.half_life, int):
            self.half_life = int(self.half_life)

        if self.decay_product is not None and not isinstance(self.decay_product, IsotopeId):
            self.decay_product = IsotopeId(self.decay_product)

        if self.decay_mode is not None and not isinstance(self.decay_mode, str):
            self.decay_mode = str(self.decay_mode)

        if self.decay_energy is not None and not isinstance(self.decay_energy, str):
            self.decay_energy = str(self.decay_energy)

        if self.mode_of_formation is not None and not isinstance(self.mode_of_formation, str):
            self.mode_of_formation = str(self.mode_of_formation)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class AtomIonicForm(PartiallySpecifiedAtom):
    """
    an atom type in which only charge state is specified, designated by the element followed by charge
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AtomIonicForm"]
    class_class_curie: ClassVar[str] = "chemrof:AtomIonicForm"
    class_name: ClassVar[str] = "AtomIonicForm"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomIonicForm

    id: Union[str, AtomIonicFormId] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class UnchargedAtom(AtomIonicForm):
    """
    An atom type that has no charge
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["UnchargedAtom"]
    class_class_curie: ClassVar[str] = "chemrof:UnchargedAtom"
    class_name: ClassVar[str] = "UnchargedAtom"
    class_model_uri: ClassVar[URIRef] = CHEMROF.UnchargedAtom

    id: Union[str, UnchargedAtomId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnchargedAtomId):
            self.id = UnchargedAtomId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class MonoatomicIon(AtomIonicForm):
    """
    An atom type that has a charge
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MonoatomicIon"]
    class_class_curie: ClassVar[str] = "chemrof:MonoatomicIon"
    class_name: ClassVar[str] = "MonoatomicIon"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MonoatomicIon

    id: Union[str, MonoatomicIonId] = None
    has_element: Optional[Union[str, ChemicalElementId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonoatomicIonId):
            self.id = MonoatomicIonId(self.id)

        if self.has_element is not None and not isinstance(self.has_element, ChemicalElementId):
            self.has_element = ChemicalElementId(self.has_element)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class AtomAnion(MonoatomicIon):
    """
    A monoatomic ion that is negative
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AtomAnion"]
    class_class_curie: ClassVar[str] = "chemrof:AtomAnion"
    class_name: ClassVar[str] = "AtomAnion"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomAnion

    id: Union[str, AtomAnionId] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AtomAnionId):
            self.id = AtomAnionId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class AtomCation(MonoatomicIon):
    """
    A monoatomic ion that is positive, e.g Cu(2+)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AtomCation"]
    class_class_curie: ClassVar[str] = "chemrof:AtomCation"
    class_name: ClassVar[str] = "AtomCation"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomCation

    id: Union[str, AtomCationId] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AtomCationId):
            self.id = AtomCationId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class FullySpecifiedAtom(Atom):
    """
    An atom type that has atomic number, charge, and neutron number stated (equivalently: protons + mass + charge)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["FullySpecifiedAtom"]
    class_class_curie: ClassVar[str] = "chemrof:FullySpecifiedAtom"
    class_name: ClassVar[str] = "FullySpecifiedAtom"
    class_model_uri: ClassVar[URIRef] = CHEMROF.FullySpecifiedAtom

    id: Union[str, FullySpecifiedAtomId] = None
    elemental_charge: Optional[int] = None
    neutron_number: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FullySpecifiedAtomId):
            self.id = FullySpecifiedAtomId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        if self.neutron_number is not None and not isinstance(self.neutron_number, int):
            self.neutron_number = int(self.neutron_number)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


class ChemicalInformation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalInformation"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalInformation"
    class_name: ClassVar[str] = "ChemicalInformation"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalInformation


class PeriodicTablePlacement(ChemicalInformation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["PeriodicTablePlacement"]
    class_class_curie: ClassVar[str] = "chemrof:PeriodicTablePlacement"
    class_name: ClassVar[str] = "PeriodicTablePlacement"
    class_model_uri: ClassVar[URIRef] = CHEMROF.PeriodicTablePlacement


class InchiObject(ChemicalInformation):
    """
    A representation of an InChI string as an object, composed of distinct sublayers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["InchiObject"]
    class_class_curie: ClassVar[str] = "chemrof:InchiObject"
    class_name: ClassVar[str] = "InchiObject"
    class_model_uri: ClassVar[URIRef] = CHEMROF.InchiObject


@dataclass(repr=False)
class StandardInchiObject(InchiObject):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["StandardInchiObject"]
    class_class_curie: ClassVar[str] = "chemrof:StandardInchiObject"
    class_name: ClassVar[str] = "StandardInchiObject"
    class_model_uri: ClassVar[URIRef] = CHEMROF.StandardInchiObject

    inchi_version_string: str = None
    inchi_chemical_sublayer: Optional[str] = None
    inchi_atom_connections_sublayer: Optional[str] = None
    inchi_hydrogen_connections_sublayer: Optional[str] = None
    inchi_charge_sublayer: Optional[str] = None
    inchi_proton_sublayer: Optional[str] = None
    inchi_stereochemical_double_bond_sublayer: Optional[str] = None
    inchi_tetrahedral_stereochemical_sublayer: Optional[str] = None
    inchi_stereochemical_type_sublayer: Optional[str] = None
    inchi_isotopic_layer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.inchi_version_string):
            self.MissingRequiredField("inchi_version_string")
        if not isinstance(self.inchi_version_string, str):
            self.inchi_version_string = str(self.inchi_version_string)

        if self.inchi_chemical_sublayer is not None and not isinstance(self.inchi_chemical_sublayer, str):
            self.inchi_chemical_sublayer = str(self.inchi_chemical_sublayer)

        if self.inchi_atom_connections_sublayer is not None and not isinstance(self.inchi_atom_connections_sublayer, str):
            self.inchi_atom_connections_sublayer = str(self.inchi_atom_connections_sublayer)

        if self.inchi_hydrogen_connections_sublayer is not None and not isinstance(self.inchi_hydrogen_connections_sublayer, str):
            self.inchi_hydrogen_connections_sublayer = str(self.inchi_hydrogen_connections_sublayer)

        if self.inchi_charge_sublayer is not None and not isinstance(self.inchi_charge_sublayer, str):
            self.inchi_charge_sublayer = str(self.inchi_charge_sublayer)

        if self.inchi_proton_sublayer is not None and not isinstance(self.inchi_proton_sublayer, str):
            self.inchi_proton_sublayer = str(self.inchi_proton_sublayer)

        if self.inchi_stereochemical_double_bond_sublayer is not None and not isinstance(self.inchi_stereochemical_double_bond_sublayer, str):
            self.inchi_stereochemical_double_bond_sublayer = str(self.inchi_stereochemical_double_bond_sublayer)

        if self.inchi_tetrahedral_stereochemical_sublayer is not None and not isinstance(self.inchi_tetrahedral_stereochemical_sublayer, str):
            self.inchi_tetrahedral_stereochemical_sublayer = str(self.inchi_tetrahedral_stereochemical_sublayer)

        if self.inchi_stereochemical_type_sublayer is not None and not isinstance(self.inchi_stereochemical_type_sublayer, str):
            self.inchi_stereochemical_type_sublayer = str(self.inchi_stereochemical_type_sublayer)

        if self.inchi_isotopic_layer is not None and not isinstance(self.inchi_isotopic_layer, str):
            self.inchi_isotopic_layer = str(self.inchi_isotopic_layer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalRelationship(YAMLRoot):
    """
    A reified relationship
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalRelationship"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalRelationship"
    class_name: ClassVar[str] = "ChemicalRelationship"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalRelationship

    owl_subclass_of: Optional[Union[dict, OwlClass]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**as_dict(self.owl_subclass_of))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalRole(YAMLRoot):
    """
    A characteristic of a chemical entity that is realized under particular conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["50906"]
    class_class_curie: ClassVar[str] = "CHEBI:50906"
    class_name: ClassVar[str] = "ChemicalRole"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalRole

    owl_subclass_of: Optional[Union[dict, OwlClass]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**as_dict(self.owl_subclass_of))

        super().__post_init__(**kwargs)


class Location(YAMLRoot):
    """
    Abstract grouping for entities that represent abstract or concrete locations of chemical entities or their parts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Location"]
    class_class_curie: ClassVar[str] = "chemrof:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Location


class Stereocenter(Location):
    """
    a geometric point in a molecule in which the interchanging of two substituents creates a stereoisomer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Stereocenter"]
    class_class_curie: ClassVar[str] = "chemrof:Stereocenter"
    class_name: ClassVar[str] = "Stereocenter"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Stereocenter


class ChiralityCenter(Stereocenter):
    """
    a stereocenter consisting of an atom holding a set of ligands (atoms or groups of atoms) in a spatial arrangement
    which is not superimposable on its mirror image.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChiralityCenter"]
    class_class_curie: ClassVar[str] = "chemrof:ChiralityCenter"
    class_name: ClassVar[str] = "ChiralityCenter"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChiralityCenter


@dataclass(repr=False)
class AtomicBond(ChemicalRelationship):
    """
    A connection between two atoms. Note this is the reified form of 'atomically connected to'.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GC["Bond"]
    class_class_curie: ClassVar[str] = "gc:Bond"
    class_name: ClassVar[str] = "AtomicBond"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomicBond

    owl_subclass_of: Optional[Union[dict, OwlClass]] = None
    subject: Optional[Union[str, AtomOccurrenceName]] = None
    object: Optional[Union[str, AtomOccurrenceName]] = None
    bond_type: Optional[Union[str, "BondTypeEnum"]] = None
    bond_order: Optional[int] = None
    bond_length: Optional[float] = None
    bond_energy: Optional[float] = None
    bond_length_in_angstroms: Optional[float] = None
    bond_angle: Optional[float] = None
    torsional_angle: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**as_dict(self.owl_subclass_of))

        if self.subject is not None and not isinstance(self.subject, AtomOccurrenceName):
            self.subject = AtomOccurrenceName(self.subject)

        if self.object is not None and not isinstance(self.object, AtomOccurrenceName):
            self.object = AtomOccurrenceName(self.object)

        if self.bond_type is not None and not isinstance(self.bond_type, BondTypeEnum):
            self.bond_type = BondTypeEnum(self.bond_type)

        if self.bond_order is not None and not isinstance(self.bond_order, int):
            self.bond_order = int(self.bond_order)

        if self.bond_length is not None and not isinstance(self.bond_length, float):
            self.bond_length = float(self.bond_length)

        if self.bond_energy is not None and not isinstance(self.bond_energy, float):
            self.bond_energy = float(self.bond_energy)

        if self.bond_length_in_angstroms is not None and not isinstance(self.bond_length_in_angstroms, float):
            self.bond_length_in_angstroms = float(self.bond_length_in_angstroms)

        if self.bond_angle is not None and not isinstance(self.bond_angle, float):
            self.bond_angle = float(self.bond_angle)

        if self.torsional_angle is not None and not isinstance(self.torsional_angle, float):
            self.torsional_angle = float(self.torsional_angle)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubatomicParticleOccurrence(ChemicalRelationship):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["SubatomicParticleOccurrence"]
    class_class_curie: ClassVar[str] = "chemrof:SubatomicParticleOccurrence"
    class_name: ClassVar[str] = "SubatomicParticleOccurrence"
    class_model_uri: ClassVar[URIRef] = CHEMROF.SubatomicParticleOccurrence

    occurrence_of: Union[str, SubatomicParticleId] = None
    owl_subclass_of: Optional[Union[dict, OwlClass]] = None
    Count: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.occurrence_of):
            self.MissingRequiredField("occurrence_of")
        if not isinstance(self.occurrence_of, SubatomicParticleId):
            self.occurrence_of = SubatomicParticleId(self.occurrence_of)

        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**as_dict(self.owl_subclass_of))

        if self.Count is not None and not isinstance(self.Count, int):
            self.Count = int(self.Count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtomOccurrence(ChemicalRelationship):
    """
    An occurrence of an atom in the context of a particular molecule. For example, one of two occurrences of oxygen in
    nitrate
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["AtomOccurrence"]
    class_class_curie: ClassVar[str] = "chemrof:AtomOccurrence"
    class_name: ClassVar[str] = "AtomOccurrence"
    class_model_uri: ClassVar[URIRef] = CHEMROF.AtomOccurrence

    name: Union[str, AtomOccurrenceName] = None
    occurrence_of: Union[str, AtomId] = None
    owl_subclass_of: Optional[Union[dict, OwlClass]] = None
    valence: Optional[int] = None
    oxidation_number: Optional[int] = None
    formal_charge: Optional[int] = None
    coordination_number: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, AtomOccurrenceName):
            self.name = AtomOccurrenceName(self.name)

        if self._is_empty(self.occurrence_of):
            self.MissingRequiredField("occurrence_of")
        if not isinstance(self.occurrence_of, AtomId):
            self.occurrence_of = AtomId(self.occurrence_of)

        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**as_dict(self.owl_subclass_of))

        if self.valence is not None and not isinstance(self.valence, int):
            self.valence = int(self.valence)

        if self.oxidation_number is not None and not isinstance(self.oxidation_number, int):
            self.oxidation_number = int(self.oxidation_number)

        if self.formal_charge is not None and not isinstance(self.formal_charge, int):
            self.formal_charge = int(self.formal_charge)

        if self.coordination_number is not None and not isinstance(self.coordination_number, int):
            self.coordination_number = int(self.coordination_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalSalt(PreciseChemicalMixture):
    """
    a chemical compound consisting of an ionic assembly of cations and anions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalSalt"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalSalt"
    class_name: ClassVar[str] = "ChemicalSalt"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalSalt

    id: Union[str, ChemicalSaltId] = None
    elemental_charge: Optional[int] = None
    has_cationic_component: Optional[Union[dict, CationState]] = None
    has_anionic_component: Optional[Union[dict, AnionState]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalSaltId):
            self.id = ChemicalSaltId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        if self.has_cationic_component is not None and not isinstance(self.has_cationic_component, CationState):
            self.has_cationic_component = CationState(**as_dict(self.has_cationic_component))

        if self.has_anionic_component is not None and not isinstance(self.has_anionic_component, AnionState):
            self.has_anionic_component = AnionState(**as_dict(self.has_anionic_component))

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Ester(Molecule):
    """
    An ester is a chemical compound derived from an acid (organic or inorganic) in which at least one –OH hydroxyl
    group is replaced by an –O– alkyl (alkoxy) group
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Ester"]
    class_class_curie: ClassVar[str] = "chemrof:Ester"
    class_name: ClassVar[str] = "Ester"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Ester

    id: Union[str, EsterId] = None
    has_parent_alcohol: Optional[Union[str, ChemicalEntityId]] = None
    has_parent_acid: Optional[Union[str, MoleculeByChargeStateId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EsterId):
            self.id = EsterId(self.id)

        if self.has_parent_alcohol is not None and not isinstance(self.has_parent_alcohol, ChemicalEntityId):
            self.has_parent_alcohol = ChemicalEntityId(self.has_parent_alcohol)

        if self.has_parent_acid is not None and not isinstance(self.has_parent_acid, MoleculeByChargeStateId):
            self.has_parent_acid = MoleculeByChargeStateId(self.has_parent_acid)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Stereoisomer(Molecule):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Stereoisomer"]
    class_class_curie: ClassVar[str] = "chemrof:Stereoisomer"
    class_name: ClassVar[str] = "Stereoisomer"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Stereoisomer

    id: Union[str, StereoisomerId] = None
    isomeric_smiles_string: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StereoisomerId):
            self.id = StereoisomerId(self.id)

        if self.isomeric_smiles_string is not None and not isinstance(self.isomeric_smiles_string, str):
            self.isomeric_smiles_string = str(self.isomeric_smiles_string)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Enantiomer(Stereoisomer):
    """
    one of two stereoisomers of a chiral molecule that are mirror images. Example: R-thalidomide
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Enantiomer"]
    class_class_curie: ClassVar[str] = "chemrof:Enantiomer"
    class_name: ClassVar[str] = "Enantiomer"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Enantiomer

    id: Union[str, EnantiomerId] = None
    inchi_tetrahedral_stereochemical_sublayer: str = None
    inchi_stereochemical_type_sublayer: str = None
    relative_configuration: Optional[str] = None
    optical_configuration: Optional[str] = None
    absolute_configuration: Optional[str] = None
    enantiomer_form_of: Optional[Union[str, MoleculeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnantiomerId):
            self.id = EnantiomerId(self.id)

        if self._is_empty(self.inchi_tetrahedral_stereochemical_sublayer):
            self.MissingRequiredField("inchi_tetrahedral_stereochemical_sublayer")
        if not isinstance(self.inchi_tetrahedral_stereochemical_sublayer, str):
            self.inchi_tetrahedral_stereochemical_sublayer = str(self.inchi_tetrahedral_stereochemical_sublayer)

        if self._is_empty(self.inchi_stereochemical_type_sublayer):
            self.MissingRequiredField("inchi_stereochemical_type_sublayer")
        if not isinstance(self.inchi_stereochemical_type_sublayer, str):
            self.inchi_stereochemical_type_sublayer = str(self.inchi_stereochemical_type_sublayer)

        if self.relative_configuration is not None and not isinstance(self.relative_configuration, str):
            self.relative_configuration = str(self.relative_configuration)

        if self.optical_configuration is not None and not isinstance(self.optical_configuration, str):
            self.optical_configuration = str(self.optical_configuration)

        if self.absolute_configuration is not None and not isinstance(self.absolute_configuration, str):
            self.absolute_configuration = str(self.absolute_configuration)

        if self.enantiomer_form_of is not None and not isinstance(self.enantiomer_form_of, MoleculeId):
            self.enantiomer_form_of = MoleculeId(self.enantiomer_form_of)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class RacemicMixture(PreciseChemicalMixture):
    """
    a chemical compound that has equal amounts of left- and right-handed enantiomers of a chiral molecule. An example
    is Thalidomide
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["RacemicMixture"]
    class_class_curie: ClassVar[str] = "chemrof:RacemicMixture"
    class_name: ClassVar[str] = "RacemicMixture"
    class_model_uri: ClassVar[URIRef] = CHEMROF.RacemicMixture

    id: Union[str, RacemicMixtureId] = None
    has_left_enantiomer: Union[str, EnantiomerId] = None
    has_right_enantiomer: Union[str, EnantiomerId] = None
    chirality_agnostic_form: Optional[Union[str, MoleculeId]] = None
    IUPAC_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RacemicMixtureId):
            self.id = RacemicMixtureId(self.id)

        if self._is_empty(self.has_left_enantiomer):
            self.MissingRequiredField("has_left_enantiomer")
        if not isinstance(self.has_left_enantiomer, EnantiomerId):
            self.has_left_enantiomer = EnantiomerId(self.has_left_enantiomer)

        if self._is_empty(self.has_right_enantiomer):
            self.MissingRequiredField("has_right_enantiomer")
        if not isinstance(self.has_right_enantiomer, EnantiomerId):
            self.has_right_enantiomer = EnantiomerId(self.has_right_enantiomer)

        if self.chirality_agnostic_form is not None and not isinstance(self.chirality_agnostic_form, MoleculeId):
            self.chirality_agnostic_form = MoleculeId(self.chirality_agnostic_form)

        if self.IUPAC_name is not None and not isinstance(self.IUPAC_name, str):
            self.IUPAC_name = str(self.IUPAC_name)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class Allotrope(Molecule):
    """
    A molecule consisting of atoms of the same element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["Allotrope"]
    class_class_curie: ClassVar[str] = "chemrof:Allotrope"
    class_name: ClassVar[str] = "Allotrope"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Allotrope

    id: Union[str, AllotropeId] = None
    allotropic_analog_of: Union[str, ChemicalElementId] = None
    has_bonding_structure: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AllotropeId):
            self.id = AllotropeId(self.id)

        if self._is_empty(self.allotropic_analog_of):
            self.MissingRequiredField("allotropic_analog_of")
        if not isinstance(self.allotropic_analog_of, ChemicalElementId):
            self.allotropic_analog_of = ChemicalElementId(self.allotropic_analog_of)

        if self._is_empty(self.has_bonding_structure):
            self.MissingRequiredField("has_bonding_structure")
        if not isinstance(self.has_bonding_structure, str):
            self.has_bonding_structure = str(self.has_bonding_structure)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class PolymerRepeatUnit(ChemicalRelationship):
    """
    An abstract part of a polymer that is all instances of a repeated monomer of a single type
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["PolymerRepeatUnit"]
    class_class_curie: ClassVar[str] = "chemrof:PolymerRepeatUnit"
    class_name: ClassVar[str] = "PolymerRepeatUnit"
    class_model_uri: ClassVar[URIRef] = CHEMROF.PolymerRepeatUnit

    repetition_of: Optional[Union[str, MoleculeId]] = None
    degree_of_polymerization: Optional[int] = None
    mass: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.repetition_of is not None and not isinstance(self.repetition_of, MoleculeId):
            self.repetition_of = MoleculeId(self.repetition_of)

        if self.degree_of_polymerization is not None and not isinstance(self.degree_of_polymerization, int):
            self.degree_of_polymerization = int(self.degree_of_polymerization)

        if self.mass is not None and not isinstance(self.mass, float):
            self.mass = float(self.mass)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reaction(DomainEntity):
    """
    Reaction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RXNO["0000000"]
    class_class_curie: ClassVar[str] = "RXNO:0000000"
    class_name: ClassVar[str] = "Reaction"
    class_model_uri: ClassVar[URIRef] = CHEMROF.Reaction

    id: Union[str, ReactionId] = None
    left_participants: Optional[Union[Union[dict, "ReactionParticipant"], list[Union[dict, "ReactionParticipant"]]]] = empty_list()
    right_participants: Optional[Union[Union[dict, "ReactionParticipant"], list[Union[dict, "ReactionParticipant"]]]] = empty_list()
    direction: Optional[str] = None
    is_diastereoselective: Optional[Union[bool, Bool]] = None
    is_stereo: Optional[Union[bool, Bool]] = None
    is_balanced: Optional[Union[bool, Bool]] = None
    is_transport: Optional[Union[bool, Bool]] = None
    is_fully_characterized: Optional[Union[bool, Bool]] = None
    reaction_center: Optional[str] = None
    has_rinchi_representation: Optional[str] = None
    has_reaction_smiles_representation: Optional[str] = None
    reaction_rate_coefficient: Optional[float] = None
    reaction_rate: Optional[float] = None
    reaction_type: Optional[Union[str, "ReactionTypeEnum"]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionId):
            self.id = ReactionId(self.id)

        if not isinstance(self.left_participants, list):
            self.left_participants = [self.left_participants] if self.left_participants is not None else []
        self.left_participants = [v if isinstance(v, ReactionParticipant) else ReactionParticipant(**as_dict(v)) for v in self.left_participants]

        if not isinstance(self.right_participants, list):
            self.right_participants = [self.right_participants] if self.right_participants is not None else []
        self.right_participants = [v if isinstance(v, ReactionParticipant) else ReactionParticipant(**as_dict(v)) for v in self.right_participants]

        if self.direction is not None and not isinstance(self.direction, str):
            self.direction = str(self.direction)

        if self.is_diastereoselective is not None and not isinstance(self.is_diastereoselective, Bool):
            self.is_diastereoselective = Bool(self.is_diastereoselective)

        if self.is_stereo is not None and not isinstance(self.is_stereo, Bool):
            self.is_stereo = Bool(self.is_stereo)

        if self.is_balanced is not None and not isinstance(self.is_balanced, Bool):
            self.is_balanced = Bool(self.is_balanced)

        if self.is_transport is not None and not isinstance(self.is_transport, Bool):
            self.is_transport = Bool(self.is_transport)

        if self.is_fully_characterized is not None and not isinstance(self.is_fully_characterized, Bool):
            self.is_fully_characterized = Bool(self.is_fully_characterized)

        if self.reaction_center is not None and not isinstance(self.reaction_center, str):
            self.reaction_center = str(self.reaction_center)

        if self.has_rinchi_representation is not None and not isinstance(self.has_rinchi_representation, str):
            self.has_rinchi_representation = str(self.has_rinchi_representation)

        if self.has_reaction_smiles_representation is not None and not isinstance(self.has_reaction_smiles_representation, str):
            self.has_reaction_smiles_representation = str(self.has_reaction_smiles_representation)

        if self.reaction_rate_coefficient is not None and not isinstance(self.reaction_rate_coefficient, float):
            self.reaction_rate_coefficient = float(self.reaction_rate_coefficient)

        if self.reaction_rate is not None and not isinstance(self.reaction_rate, float):
            self.reaction_rate = float(self.reaction_rate)

        if self.reaction_type is not None and not isinstance(self.reaction_type, ReactionTypeEnum):
            self.reaction_type = ReactionTypeEnum(self.reaction_type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class IsomeraseReaction(Reaction):
    """
    A reaction that converts a molecule from one isomer to another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["IsomeraseReaction"]
    class_class_curie: ClassVar[str] = "chemrof:IsomeraseReaction"
    class_name: ClassVar[str] = "IsomeraseReaction"
    class_model_uri: ClassVar[URIRef] = CHEMROF.IsomeraseReaction

    id: Union[str, IsomeraseReactionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsomeraseReactionId):
            self.id = IsomeraseReactionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie)


@dataclass(repr=False)
class ReactionParticipant(ChemicalRelationship):
    """
    Instances of this link a reaction to a chemical entity participant
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ReactionParticipant"]
    class_class_curie: ClassVar[str] = "chemrof:ReactionParticipant"
    class_name: ClassVar[str] = "ReactionParticipant"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ReactionParticipant

    participant: Optional[Union[str, ChemicalEntityId]] = None
    stoichiometry: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.participant is not None and not isinstance(self.participant, ChemicalEntityId):
            self.participant = ChemicalEntityId(self.participant)

        if self.stoichiometry is not None and not isinstance(self.stoichiometry, int):
            self.stoichiometry = int(self.stoichiometry)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProportionalPart(ChemicalRelationship):
    """
    A part of a complex mixture that is of uniform composition
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ProportionalPart"]
    class_class_curie: ClassVar[str] = "chemrof:ProportionalPart"
    class_name: ClassVar[str] = "ProportionalPart"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ProportionalPart

    has_role: Optional[Union[str, "IngredientRoleEnum"]] = None
    composed_of: Optional[Union[str, ChemicalEntityId]] = None
    minimal_percentage: Optional[float] = None
    maximum_percentage: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_role is not None and not isinstance(self.has_role, IngredientRoleEnum):
            self.has_role = IngredientRoleEnum(self.has_role)

        if self.composed_of is not None and not isinstance(self.composed_of, ChemicalEntityId):
            self.composed_of = ChemicalEntityId(self.composed_of)

        if self.minimal_percentage is not None and not isinstance(self.minimal_percentage, float):
            self.minimal_percentage = float(self.minimal_percentage)

        if self.maximum_percentage is not None and not isinstance(self.maximum_percentage, float):
            self.maximum_percentage = float(self.maximum_percentage)

        super().__post_init__(**kwargs)


class ChemicalSimilarity(ChemicalRelationship):
    """
    A relationship between two or more chemical entities where there is some degree of similarity between these
    entities on their similarity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["ChemicalSimilarity"]
    class_class_curie: ClassVar[str] = "chemrof:ChemicalSimilarity"
    class_name: ClassVar[str] = "ChemicalSimilarity"
    class_model_uri: ClassVar[URIRef] = CHEMROF.ChemicalSimilarity


@dataclass(repr=False)
class MoleculePairwiseSimilarity(ChemicalSimilarity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["MoleculePairwiseSimilarity"]
    class_class_curie: ClassVar[str] = "chemrof:MoleculePairwiseSimilarity"
    class_name: ClassVar[str] = "MoleculePairwiseSimilarity"
    class_model_uri: ClassVar[URIRef] = CHEMROF.MoleculePairwiseSimilarity

    left_molecule: Optional[Union[str, MoleculeId]] = None
    right_molecule: Optional[Union[str, MoleculeId]] = None
    score: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.left_molecule is not None and not isinstance(self.left_molecule, MoleculeId):
            self.left_molecule = MoleculeId(self.left_molecule)

        if self.right_molecule is not None and not isinstance(self.right_molecule, MoleculeId):
            self.right_molecule = MoleculeId(self.right_molecule)

        if self.score is not None and not isinstance(self.score, float):
            self.score = float(self.score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TanimotoSimilarity(MoleculePairwiseSimilarity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["TanimotoSimilarity"]
    class_class_curie: ClassVar[str] = "chemrof:TanimotoSimilarity"
    class_name: ClassVar[str] = "TanimotoSimilarity"
    class_model_uri: ClassVar[URIRef] = CHEMROF.TanimotoSimilarity

    score: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.score is not None and not isinstance(self.score, float):
            self.score = float(self.score)

        super().__post_init__(**kwargs)


class SpecificityMixin(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["SpecificityMixin"]
    class_class_curie: ClassVar[str] = "chemrof:SpecificityMixin"
    class_name: ClassVar[str] = "SpecificityMixin"
    class_model_uri: ClassVar[URIRef] = CHEMROF.SpecificityMixin


@dataclass(repr=False)
class EntityWithAtomsEnumerated(SpecificityMixin):
    """
    A mixin for an entity that consists of one or more atoms where the atoms and the number of occurrences is counted
    (corresponding to the chemical layer in InChI)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["EntityWithAtomsEnumerated"]
    class_class_curie: ClassVar[str] = "chemrof:EntityWithAtomsEnumerated"
    class_name: ClassVar[str] = "EntityWithAtomsEnumerated"
    class_model_uri: ClassVar[URIRef] = CHEMROF.EntityWithAtomsEnumerated

    inchi_chemical_sublayer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.inchi_chemical_sublayer is not None and not isinstance(self.inchi_chemical_sublayer, str):
            self.inchi_chemical_sublayer = str(self.inchi_chemical_sublayer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityWithConnectivitySpecificied(SpecificityMixin):
    """
    A mixin for an entity that consists of two or more atom occurrences where the connectivity is specified
    (corresponding to the /c layer in InChI)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["EntityWithConnectivitySpecificied"]
    class_class_curie: ClassVar[str] = "chemrof:EntityWithConnectivitySpecificied"
    class_name: ClassVar[str] = "EntityWithConnectivitySpecificied"
    class_model_uri: ClassVar[URIRef] = CHEMROF.EntityWithConnectivitySpecificied

    inchi_atom_connections_sublayer: Optional[str] = None
    inchi_hydrogen_connections_sublayer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.inchi_atom_connections_sublayer is not None and not isinstance(self.inchi_atom_connections_sublayer, str):
            self.inchi_atom_connections_sublayer = str(self.inchi_atom_connections_sublayer)

        if self.inchi_hydrogen_connections_sublayer is not None and not isinstance(self.inchi_hydrogen_connections_sublayer, str):
            self.inchi_hydrogen_connections_sublayer = str(self.inchi_hydrogen_connections_sublayer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityWithChargeSpecified(SpecificityMixin):
    """
    A mixin for an entity where the charge is explicitly specified (corresponding to the /q layer in InChI)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["EntityWithChargeSpecified"]
    class_class_curie: ClassVar[str] = "chemrof:EntityWithChargeSpecified"
    class_name: ClassVar[str] = "EntityWithChargeSpecified"
    class_model_uri: ClassVar[URIRef] = CHEMROF.EntityWithChargeSpecified

    inchi_charge_sublayer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.inchi_charge_sublayer is not None and not isinstance(self.inchi_charge_sublayer, str):
            self.inchi_charge_sublayer = str(self.inchi_charge_sublayer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityWithStereochemistrySpecified(SpecificityMixin):
    """
    A mixin for an entity where the stereochemistry is explicitly specified (corresponding to the /t, m/, and /s
    layers in InChI)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["EntityWithStereochemistrySpecified"]
    class_class_curie: ClassVar[str] = "chemrof:EntityWithStereochemistrySpecified"
    class_name: ClassVar[str] = "EntityWithStereochemistrySpecified"
    class_model_uri: ClassVar[URIRef] = CHEMROF.EntityWithStereochemistrySpecified

    inchi_stereochemical_double_bond_sublayer: Optional[str] = None
    inchi_tetrahedral_stereochemical_sublayer: Optional[str] = None
    inchi_stereochemical_type_sublayer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.inchi_stereochemical_double_bond_sublayer is not None and not isinstance(self.inchi_stereochemical_double_bond_sublayer, str):
            self.inchi_stereochemical_double_bond_sublayer = str(self.inchi_stereochemical_double_bond_sublayer)

        if self.inchi_tetrahedral_stereochemical_sublayer is not None and not isinstance(self.inchi_tetrahedral_stereochemical_sublayer, str):
            self.inchi_tetrahedral_stereochemical_sublayer = str(self.inchi_tetrahedral_stereochemical_sublayer)

        if self.inchi_stereochemical_type_sublayer is not None and not isinstance(self.inchi_stereochemical_type_sublayer, str):
            self.inchi_stereochemical_type_sublayer = str(self.inchi_stereochemical_type_sublayer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityWithIsotopeSpecified(SpecificityMixin):
    """
    A mixin for an entity where the charge is explicitly specified (corresponding to the /q layer in InChI)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMROF["EntityWithIsotopeSpecified"]
    class_class_curie: ClassVar[str] = "chemrof:EntityWithIsotopeSpecified"
    class_name: ClassVar[str] = "EntityWithIsotopeSpecified"
    class_model_uri: ClassVar[URIRef] = CHEMROF.EntityWithIsotopeSpecified

    inchi_isotopic_layer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.inchi_isotopic_layer is not None and not isinstance(self.inchi_isotopic_layer, str):
            self.inchi_isotopic_layer = str(self.inchi_isotopic_layer)

        super().__post_init__(**kwargs)


# Enumerations
class MoleculeClassificationEnum(EnumDefinitionImpl):

    lipid = PermissibleValue(
        text="lipid",
        meaning=CHEBI["18059"])
    ester = PermissibleValue(
        text="ester",
        meaning=CHEBI["35701"])

    _defn = EnumDefinition(
        name="MoleculeClassificationEnum",
    )

class ClassificationLevelEnum(EnumDefinitionImpl):

    Uncategorized = PermissibleValue(text="Uncategorized")
    Class = PermissibleValue(text="Class")
    Species = PermissibleValue(text="Species")
    Category = PermissibleValue(text="Category")
    Subspecies = PermissibleValue(text="Subspecies")
    StructuralSubspecies = PermissibleValue(text="StructuralSubspecies")
    IsomericSubspecies = PermissibleValue(text="IsomericSubspecies")
    MolecularSubspecies = PermissibleValue(text="MolecularSubspecies")

    _defn = EnumDefinition(
        name="ClassificationLevelEnum",
    )

class NanostructureMorphologyEnum(EnumDefinitionImpl):

    nanotube = PermissibleValue(
        text="nanotube",
        meaning=CHEBI["50796"])
    nanoparticle = PermissibleValue(
        text="nanoparticle",
        meaning=CHEBI["50803"])
    nanorod = PermissibleValue(
        text="nanorod",
        meaning=CHEBI["50805"])
    nanotubosome = PermissibleValue(
        text="nanotubosome",
        meaning=CHEBI["50806"])
    nanofibre = PermissibleValue(
        text="nanofibre",
        meaning=CHEBI["52518"])
    nanocrystal = PermissibleValue(
        text="nanocrystal",
        meaning=CHEBI["52529"])
    nanoribbon = PermissibleValue(
        text="nanoribbon",
        meaning=CHEBI["52530"])
    nanosheet = PermissibleValue(
        text="nanosheet",
        meaning=CHEBI["52531"])
    nanowire = PermissibleValue(
        text="nanowire",
        meaning=CHEBI["52593"])

    _defn = EnumDefinition(
        name="NanostructureMorphologyEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "quantum dot",
            PermissibleValue(
                text="quantum dot",
                meaning=CHEBI["50853"]))

class PeriodicTableBlockEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="PeriodicTableBlockEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "s-block",
            PermissibleValue(
                text="s-block",
                meaning=CHEBI["33674"]))
        setattr(cls, "p-block",
            PermissibleValue(
                text="p-block",
                meaning=CHEBI["33675"]))
        setattr(cls, "d-block",
            PermissibleValue(
                text="d-block",
                meaning=CHEBI["33561"]))
        setattr(cls, "f-block",
            PermissibleValue(
                text="f-block",
                meaning=CHEBI["33562"]))
        setattr(cls, "g-block",
            PermissibleValue(
                text="g-block",
                description="The g-block is a hypothetical region in the periodic table of the elements."))

class ElementFamilyEnum(EnumDefinitionImpl):

    Alkali_Earth = PermissibleValue(text="Alkali_Earth")
    Alkaline_Earth = PermissibleValue(text="Alkaline_Earth")
    Halogen = PermissibleValue(text="Halogen")
    Metalloids = PermissibleValue(text="Metalloids")
    Noblegas = PermissibleValue(text="Noblegas")
    Other_Metal = PermissibleValue(text="Other_Metal")
    Rare_Earth = PermissibleValue(text="Rare_Earth")
    Transition = PermissibleValue(text="Transition")

    _defn = EnumDefinition(
        name="ElementFamilyEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Non-Metal",
            PermissibleValue(text="Non-Metal"))

class ElementMetallicClassification(EnumDefinitionImpl):

    Metallic = PermissibleValue(
        text="Metallic",
        meaning=DAMLPT["Metallic"])

    _defn = EnumDefinition(
        name="ElementMetallicClassification",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Non-Metallic",
            PermissibleValue(
                text="Non-Metallic",
                meaning=DAMLPT["Non-Metallic"]))
        setattr(cls, "Semi-Metallic",
            PermissibleValue(
                text="Semi-Metallic",
                meaning=DAMLPT["Semi-Metallic"]))

class IngredientRoleEnum(EnumDefinitionImpl):

    excipient = PermissibleValue(text="excipient")
    solvent = PermissibleValue(text="solvent")

    _defn = EnumDefinition(
        name="IngredientRoleEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "active ingredient",
            PermissibleValue(text="active ingredient"))
        setattr(cls, "inactive ingredient",
            PermissibleValue(text="inactive ingredient"))

class BondTypeEnum(EnumDefinitionImpl):

    covalent = PermissibleValue(
        text="covalent",
        description="""A covalent bond is a chemical bond that involves the sharing of pairs of electrons between atoms. This sharing results in a stable balance of attractive and repulsive forces between those atoms.""",
        meaning=GC["NormalBond"])
    aromatic = PermissibleValue(
        text="aromatic",
        meaning=GC["AromaticBond"])
    single = PermissibleValue(
        text="single",
        meaning=GC["Single"])
    double = PermissibleValue(
        text="double",
        meaning=GC["Double"])
    triple = PermissibleValue(
        text="triple",
        meaning=GC["Triple"])
    quadruple = PermissibleValue(
        text="quadruple",
        meaning=GC["Quadruple"])
    hydrogen = PermissibleValue(
        text="hydrogen",
        meaning=GC["HydrogenBond"])
    ionic = PermissibleValue(text="ionic")
    polycentric = PermissibleValue(text="polycentric")
    sigma = PermissibleValue(text="sigma")

    _defn = EnumDefinition(
        name="BondTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "metal-metal",
            PermissibleValue(text="metal-metal"))
        setattr(cls, "salt bridge",
            PermissibleValue(text="salt bridge"))
        setattr(cls, "polar covalent",
            PermissibleValue(text="polar covalent"))

class HardOrSoftEnum(EnumDefinitionImpl):

    hard = PermissibleValue(text="hard")
    soft = PermissibleValue(text="soft")
    borderline = PermissibleValue(text="borderline")

    _defn = EnumDefinition(
        name="HardOrSoftEnum",
    )

class BronstedAcidBaseRoleEnum(EnumDefinitionImpl):

    acid = PermissibleValue(
        text="acid",
        description="CHEBI:39141")
    base = PermissibleValue(
        text="base",
        description="CHEBI:39142")

    _defn = EnumDefinition(
        name="BronstedAcidBaseRoleEnum",
    )

class ReactionTypeEnum(EnumDefinitionImpl):
    """
    Classification of chemical reactions based on mechanistic and functional categories
    """
    functional_group_interconversion = PermissibleValue(
        text="functional_group_interconversion",
        description="Conversion of one functional group to another without changing the carbon skeleton",
        meaning=RXNO["0000057"])
    bond_formation = PermissibleValue(
        text="bond_formation",
        description="Reactions that create new bonds between atoms or groups")
    bond_breaking = PermissibleValue(
        text="bond_breaking",
        description="Reactions that break existing bonds to form fragments or rearrange structures")
    oxidation = PermissibleValue(
        text="oxidation",
        description="A functional group modification reaction where a functional group is oxidised",
        meaning=RXNO["0000012"])
    reduction = PermissibleValue(
        text="reduction",
        description="A functional group modification reaction where a functional group is reduced",
        meaning=RXNO["0000037"])
    acylation = PermissibleValue(
        text="acylation",
        description="Formation of an acyl group bond, typically involving carboxylic acid derivatives",
        meaning=RXNO["0000016"])
    carbon_carbon_bond_formation = PermissibleValue(
        text="carbon_carbon_bond_formation",
        description="Reactions that form new carbon-carbon bonds",
        meaning=RXNO["0000018"])
    heteroatom_alkylation_arylation = PermissibleValue(
        text="heteroatom_alkylation_arylation",
        description="Alkylation or arylation of heteroatoms such as nitrogen, oxygen, or sulfur",
        meaning=RXNO["0000019"])
    addition = PermissibleValue(
        text="addition",
        description="Reactions that add atoms or groups across multiple bonds",
        meaning=RXNO["0000041"])
    cyclization = PermissibleValue(
        text="cyclization",
        description="Formation of cyclic structures from linear precursors",
        meaning=RXNO["0000005"])
    condensation = PermissibleValue(
        text="condensation",
        description="""A reaction in which two or more reactants yield a single main product with accompanying formation of a small molecule""",
        meaning=MOP["0000627"])
    elimination = PermissibleValue(
        text="elimination",
        description="""A molecular process where two groups are lost with concomitant formation of an unsaturation in the molecule or formation of a new ring""",
        meaning=RXNO["0000656"])
    ring_opening = PermissibleValue(
        text="ring_opening",
        description="Cleavage of cyclic structures to form linear products")
    hydrolysis = PermissibleValue(
        text="hydrolysis",
        description="A solvolysis reaction where the solvent material is water",
        meaning=RXNO["0000619"])
    substitution = PermissibleValue(
        text="substitution",
        description="A reaction step where one atom or group is replaced with another",
        meaning=RXNO["0000331"])
    isomerization = PermissibleValue(
        text="isomerization",
        description="Rearrangement reactions that convert one isomer to another",
        meaning=RXNO["0000025"])
    functional_group_addition = PermissibleValue(
        text="functional_group_addition",
        description="Addition of functional groups to unsaturated bonds or reactive centers")
    aromatic_heterocycle_formation = PermissibleValue(
        text="aromatic_heterocycle_formation",
        description="Formation of aromatic rings containing heteroatoms")
    protection = PermissibleValue(
        text="protection",
        description="Introduction of protecting groups to temporarily mask reactive functionalities")
    deprotection = PermissibleValue(
        text="deprotection",
        description="Removal of protecting groups to restore original functionalities")
    resolution = PermissibleValue(
        text="resolution",
        description="Separation of enantiomers or other stereoisomers")

    _defn = EnumDefinition(
        name="ReactionTypeEnum",
        description="Classification of chemical reactions based on mechanistic and functional categories",
    )

class SubatomicParticleEnum(EnumDefinitionImpl):

    proton = PermissibleValue(
        text="proton",
        description="Nuclear particle of charge number +1, spin 1/2 and rest mass of 1.007276470(12) u.",
        meaning=CHEBI["24636"])
    positron = PermissibleValue(
        text="positron",
        description="""Elementary particle not affected by the strong force having a spin 1/2, a positive elementary charge and a rest mass of 0.000548579903(13) u, or 0.51099906(15) MeV.""",
        meaning=CHEBI["30225"])
    muon = PermissibleValue(
        text="muon",
        description="""Elementary particle not affected by the strong force having a spin 1/2, a negative elementary charge and a rest mass of 0.113428913(17) u, or 105.658389(34) MeV.""",
        meaning=CHEBI["36356"])
    hyperon = PermissibleValue(
        text="hyperon",
        description="""A baryon which contain one or more strange quarks. Hyperons are short-lived and heavier than nucleons.""",
        meaning=CHEBI["36365"])
    boson = PermissibleValue(
        text="boson",
        description="""Particle of integer spin quantum number following Bose-Einstein statistics. Bosons are named after Satyendra Nath Bose.""",
        meaning=CHEBI["36341"])
    fermion = PermissibleValue(
        text="fermion",
        description="""Particle of half-integer spin quantum number following Fermi-Dirac statistics. Fermions are named after Enrico Fermi.""",
        meaning=CHEBI["36340"])
    baryon = PermissibleValue(
        text="baryon",
        description="""Baryon is a fermion that does experience the strong force (strong interaction). The term is derived from the Greek betaalpharhoupsilonsigma (heavy).""",
        meaning=CHEBI["36339"])
    hydron = PermissibleValue(
        text="hydron",
        description="""The general name for the hydrogen nucleus, to be used without regard to the hydrogen nuclear mass (either for hydrogen in its natural abundance or where it is not desired to distinguish between the isotopes).""",
        meaning=CHEBI["15378"])
    nucleon = PermissibleValue(
        text="nucleon",
        description="Heavy nuclear particle: proton or neutron.",
        meaning=CHEBI["33253"])
    triton = PermissibleValue(
        text="triton",
        description="Nucleus of the (3)H atom.",
        meaning=CHEBI["29234"])
    deuteron = PermissibleValue(
        text="deuteron",
        description="Nucleus of the (2)H atom.",
        meaning=CHEBI["29233"])
    neutrino = PermissibleValue(
        text="neutrino",
        description="""An elementary particle of spin 1/2, zero electric charge and negligible rest mass. Three known types (flavors) of neutrino are electron neutrino, muon neutrino and tau neutrino, named after their charged partner leptons.""",
        meaning=CHEBI["36352"])
    meson = PermissibleValue(
        text="meson",
        description="""A hadron with zero or integer spin; a strongly interacting boson. The term is derived from the Greek muepsilonsigmaomicronsigma (medium, middle).""",
        meaning=CHEBI["36345"])
    quark = PermissibleValue(
        text="quark",
        description="""Quarks comprise one of two classes of the fundamental particles. Quarks possess fractional electric charges and are not observed in free state.""",
        meaning=CHEBI["36346"])
    SubatomicParticle = PermissibleValue(
        text="SubatomicParticle",
        description="A particle smaller than an atom.",
        meaning=CHEBI["36342"])
    photon = PermissibleValue(
        text="photon",
        description="""Particle of zero charge, zero rest mass, spin quantum number 1, energy hnu and momentum hnu/c (h is the Planck constant, nu the frequency of radiation and c the speed of light), carrier of electromagnetic force.""",
        meaning=CHEBI["30212"])
    antimuon = PermissibleValue(
        text="antimuon",
        description="""Elementary particle not affected by the strong force having a spin 1/2, a positive elementary charge and a rest mass of 0.113428913(17) u, or 105.658389(34) MeV.""",
        meaning=CHEBI["30214"])
    hadron = PermissibleValue(
        text="hadron",
        description="Hadron is a subatomic particle which experiences the strong force.",
        meaning=CHEBI["36344"])
    electron = PermissibleValue(
        text="electron",
        description="""Elementary particle not affected by the strong force having a spin 1/2, a negative elementary charge and a rest mass of 0.000548579903(13) u, or 0.51099906(15) MeV.""",
        meaning=CHEBI["10545"])
    neutron = PermissibleValue(
        text="neutron",
        description="Nuclear particle of zero charge, spin 1/2 and rest mass of 1.008664904(14) u.",
        meaning=CHEBI["30222"])
    lepton = PermissibleValue(
        text="lepton",
        description="""Lepton is a fermion that does not experience the strong force (strong interaction). The term is derived from the Greek lambdaepsilonpitauomicronsigma (small, thin).""",
        meaning=CHEBI["36338"])
    helion = PermissibleValue(
        text="helion",
        description="Nucleus of the (3)He atom.",
        meaning=CHEBI["30220"])

    _defn = EnumDefinition(
        name="SubatomicParticleEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "alpha particle",
            PermissibleValue(
                text="alpha particle",
                description="Nucleus of the (4)He atom.",
                meaning=CHEBI["30216"]))
        setattr(cls, "tau neutrino",
            PermissibleValue(
                text="tau neutrino",
                meaning=CHEBI["36354"]))
        setattr(cls, "top quark",
            PermissibleValue(
                text="top quark",
                description="A third-generation quark with a charge of +2/3.",
                meaning=CHEBI["36371"]))
        setattr(cls, "muon neutrino",
            PermissibleValue(
                text="muon neutrino",
                meaning=CHEBI["36353"]))
        setattr(cls, "nuclear particle",
            PermissibleValue(
                text="nuclear particle",
                description="A nucleus or any of its constituents in any of their energy states.",
                meaning=CHEBI["36347"]))
        setattr(cls, "pi minus meson",
            PermissibleValue(
                text="pi minus meson",
                description="""A subatomic particle of charge number -1, zero spin and rest mass of 0.1498323(8) u, or 139.5679(7) MeV.""",
                meaning=CHEBI["36350"]))
        setattr(cls, "pi meson",
            PermissibleValue(
                text="pi meson",
                description="The collective name for zero-spin mesons pi(+), pi(-) and pi(0).",
                meaning=CHEBI["36348"]))
        setattr(cls, "Higgs boson",
            PermissibleValue(
                text="Higgs boson",
                description="""A boson that is its own antiparticle, has no spin, zero electric charge and zero colour charge.""",
                meaning=CHEBI["146278"]))
        setattr(cls, "fundamental particle",
            PermissibleValue(
                text="fundamental particle",
                description="A particle not known to have substructure.",
                meaning=CHEBI["33233"]))
        setattr(cls, "electron neutrino",
            PermissibleValue(
                text="electron neutrino",
                meaning=CHEBI["30223"]))
        setattr(cls, "tau lepton",
            PermissibleValue(
                text="tau lepton",
                description="""Elementary particle not affected by the strong force having a spin 1/2, a negative elementary charge and a rest mass of 1777.05 MeV.""",
                meaning=CHEBI["36355"]))
        setattr(cls, "up quark",
            PermissibleValue(
                text="up quark",
                description="""A first-generation quark with a charge of +2/3. The up and down quarks are the fundamental constituents of the nucleons.""",
                meaning=CHEBI["36366"]))
        setattr(cls, "strange quark",
            PermissibleValue(
                text="strange quark",
                description="A second-generation quark with a charge of -1/3 and a strangeness of -1.",
                meaning=CHEBI["36368"]))
        setattr(cls, "Delta baryon",
            PermissibleValue(
                text="Delta baryon",
                meaning=CHEBI["36375"]))
        setattr(cls, "pi zero meson",
            PermissibleValue(
                text="pi zero meson",
                description="""A subatomic particle of zero charge, zero spin and rest mass of 0.1449008(9) u, or 134.9743(8) MeV.""",
                meaning=CHEBI["36351"]))
        setattr(cls, "bottom quark",
            PermissibleValue(
                text="bottom quark",
                description="A third-generation quark with a charge of -1/3.",
                meaning=CHEBI["36370"]))
        setattr(cls, "composite particle",
            PermissibleValue(
                text="composite particle",
                description="""A subatomic particle known to have substructure (i.e. consisting of smaller particles).""",
                meaning=CHEBI["36343"]))
        setattr(cls, "charm quark",
            PermissibleValue(
                text="charm quark",
                description="A second-generation quark with a charge of +2/3.",
                meaning=CHEBI["36369"]))
        setattr(cls, "down quark",
            PermissibleValue(
                text="down quark",
                description="""A first-generation quark with a charge of -1/3. The up and down quarks are the fundamental constituents of the nucleons.""",
                meaning=CHEBI["36367"]))
        setattr(cls, "pi positive meson",
            PermissibleValue(
                text="pi positive meson",
                description="""A subatomic particle of charge number +1, zero spin and rest mass of 0.1498323(8) u, or 139.5679(7) MeV.""",
                meaning=CHEBI["36349"]))

# Slots
class slots:
    pass

slots.chemical_to_chemical_relationship = Slot(uri=CHEMROF.chemical_to_chemical_relationship, name="chemical_to_chemical_relationship", curie=CHEMROF.curie('chemical_to_chemical_relationship'),
                   model_uri=CHEMROF.chemical_to_chemical_relationship, domain=None, range=Optional[str])

slots.chemical_property = Slot(uri=CHEMROF.chemical_property, name="chemical_property", curie=CHEMROF.curie('chemical_property'),
                   model_uri=CHEMROF.chemical_property, domain=None, range=Optional[str])

slots.information_property = Slot(uri=CHEMROF.information_property, name="information_property", curie=CHEMROF.curie('information_property'),
                   model_uri=CHEMROF.information_property, domain=None, range=Optional[str])

slots.in_periodic_table_group = Slot(uri=CHEMROF.in_periodic_table_group, name="in_periodic_table_group", curie=CHEMROF.curie('in_periodic_table_group'),
                   model_uri=CHEMROF.in_periodic_table_group, domain=None, range=Optional[int])

slots.in_periodic_table_block = Slot(uri=CHEMROF.in_periodic_table_block, name="in_periodic_table_block", curie=CHEMROF.curie('in_periodic_table_block'),
                   model_uri=CHEMROF.in_periodic_table_block, domain=None, range=Optional[Union[str, "PeriodicTableBlockEnum"]])

slots.id = Slot(uri=CHEMROF.id, name="id", curie=CHEMROF.curie('id'),
                   model_uri=CHEMROF.id, domain=None, range=URIRef, mappings = [SCHEMA["identifier"]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CHEMROF.name, domain=None, range=Optional[str])

slots.symbol = Slot(uri=BO.symbol, name="symbol", curie=BO.curie('symbol'),
                   model_uri=CHEMROF.symbol, domain=None, range=Optional[str])

slots.type = Slot(uri=CHEMROF.type, name="type", curie=CHEMROF.curie('type'),
                   model_uri=CHEMROF.type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.IUPAC_name = Slot(uri=CHEMROF.IUPAC_name, name="IUPAC_name", curie=CHEMROF.curie('IUPAC_name'),
                   model_uri=CHEMROF.IUPAC_name, domain=None, range=Optional[str])

slots.property_of_atom = Slot(uri=CHEMROF.property_of_atom, name="property_of_atom", curie=CHEMROF.curie('property_of_atom'),
                   model_uri=CHEMROF.property_of_atom, domain=Atom, range=Optional[str])

slots.subatomic_particle_count = Slot(uri=CHEMROF.subatomic_particle_count, name="subatomic_particle_count", curie=CHEMROF.curie('subatomic_particle_count'),
                   model_uri=CHEMROF.subatomic_particle_count, domain=Atom, range=Optional[str])

slots.has_nuclear_parts = Slot(uri=CHEMROF.has_nuclear_parts, name="has_nuclear_parts", curie=CHEMROF.curie('has_nuclear_parts'),
                   model_uri=CHEMROF.has_nuclear_parts, domain=Atom, range=Optional[Union[dict, "SubatomicParticleOccurrence"]])

slots.atomic_number = Slot(uri=BO.atomicNumber, name="atomic_number", curie=BO.curie('atomicNumber'),
                   model_uri=CHEMROF.atomic_number, domain=Atom, range=Optional[int], mappings = [CHEMINF["000079"]])

slots.neutron_number = Slot(uri=CHEMROF.neutron_number, name="neutron_number", curie=CHEMROF.curie('neutron_number'),
                   model_uri=CHEMROF.neutron_number, domain=Atom, range=Optional[int], mappings = [CHEMINF["000078"]])

slots.nucleon_number = Slot(uri=CHEMROF.nucleon_number, name="nucleon_number", curie=CHEMROF.curie('nucleon_number'),
                   model_uri=CHEMROF.nucleon_number, domain=Atom, range=Optional[int])

slots.charge = Slot(uri=CHEMROF.charge, name="charge", curie=CHEMROF.curie('charge'),
                   model_uri=CHEMROF.charge, domain=None, range=Optional[str])

slots.elemental_charge = Slot(uri=CHEMROF.elemental_charge, name="elemental_charge", curie=CHEMROF.curie('elemental_charge'),
                   model_uri=CHEMROF.elemental_charge, domain=ChemicalEntity, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.alternate_form_of = Slot(uri=CHEMROF.alternate_form_of, name="alternate_form_of", curie=CHEMROF.curie('alternate_form_of'),
                   model_uri=CHEMROF.alternate_form_of, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.has_element = Slot(uri=CHEMROF.has_element, name="has_element", curie=CHEMROF.curie('has_element'),
                   model_uri=CHEMROF.has_element, domain=ChemicalEntity, range=Optional[Union[str, ChemicalElementId]])

slots.allotropic_analog_of = Slot(uri=CHEMROF.allotropic_analog_of, name="allotropic_analog_of", curie=CHEMROF.curie('allotropic_analog_of'),
                   model_uri=CHEMROF.allotropic_analog_of, domain=Allotrope, range=Optional[Union[str, AllotropeId]])

slots.isotope_of = Slot(uri=CHEMROF.isotope_of, name="isotope_of", curie=CHEMROF.curie('isotope_of'),
                   model_uri=CHEMROF.isotope_of, domain=Isotope, range=Optional[Union[str, IsotopeId]])

slots.isotone_of = Slot(uri=CHEMROF.isotone_of, name="isotone_of", curie=CHEMROF.curie('isotone_of'),
                   model_uri=CHEMROF.isotone_of, domain=Isotope, range=Optional[Union[str, IsotopeId]])

slots.nuclear_isomer_of = Slot(uri=CHEMROF.nuclear_isomer_of, name="nuclear_isomer_of", curie=CHEMROF.curie('nuclear_isomer_of'),
                   model_uri=CHEMROF.nuclear_isomer_of, domain=Isotope, range=Optional[Union[str, IsotopeId]])

slots.isobar_of = Slot(uri=CHEMROF.isobar_of, name="isobar_of", curie=CHEMROF.curie('isobar_of'),
                   model_uri=CHEMROF.isobar_of, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.has_different_charge_state_from = Slot(uri=CHEMROF.has_different_charge_state_from, name="has_different_charge_state_from", curie=CHEMROF.curie('has_different_charge_state_from'),
                   model_uri=CHEMROF.has_different_charge_state_from, domain=None, range=Optional[str])

slots.has_lower_charge_from = Slot(uri=CHEMROF.has_lower_charge_from, name="has_lower_charge_from", curie=CHEMROF.curie('has_lower_charge_from'),
                   model_uri=CHEMROF.has_lower_charge_from, domain=None, range=Optional[str])

slots.has_higher_charge_from = Slot(uri=CHEMROF.has_higher_charge_from, name="has_higher_charge_from", curie=CHEMROF.curie('has_higher_charge_from'),
                   model_uri=CHEMROF.has_higher_charge_from, domain=None, range=Optional[str])

slots.derivative_of = Slot(uri=CHEMROF.derivative_of, name="derivative_of", curie=CHEMROF.curie('derivative_of'),
                   model_uri=CHEMROF.derivative_of, domain=ChemicalEntity, range=Optional[Union[str, DomainEntityId]])

slots.has_derivative = Slot(uri=CHEMROF.has_derivative, name="has_derivative", curie=CHEMROF.curie('has_derivative'),
                   model_uri=CHEMROF.has_derivative, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.transitive_conjugatated_form_of = Slot(uri=CHEMROF.transitive_conjugatated_form_of, name="transitive_conjugatated_form_of", curie=CHEMROF.curie('transitive_conjugatated_form_of'),
                   model_uri=CHEMROF.transitive_conjugatated_form_of, domain=ChemicalEntity, range=Optional[Union[str, DomainEntityId]])

slots.direct_conjugatated_form_of = Slot(uri=CHEMROF.direct_conjugatated_form_of, name="direct_conjugatated_form_of", curie=CHEMROF.curie('direct_conjugatated_form_of'),
                   model_uri=CHEMROF.direct_conjugatated_form_of, domain=ChemicalEntity, range=Optional[Union[str, DomainEntityId]])

slots.conjugate_base_of = Slot(uri=CHEMROF.conjugate_base_of, name="conjugate_base_of", curie=CHEMROF.curie('conjugate_base_of'),
                   model_uri=CHEMROF.conjugate_base_of, domain=ChemicalEntity, range=Optional[Union[str, DomainEntityId]])

slots.conjugate_acid_of = Slot(uri=CHEMROF.conjugate_acid_of, name="conjugate_acid_of", curie=CHEMROF.curie('conjugate_acid_of'),
                   model_uri=CHEMROF.conjugate_acid_of, domain=ChemicalEntity, range=Optional[Union[str, DomainEntityId]])

slots.acid_form_of = Slot(uri=CHEMROF.acid_form_of, name="acid_form_of", curie=CHEMROF.curie('acid_form_of'),
                   model_uri=CHEMROF.acid_form_of, domain=ChemicalEntity, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.has_physiologically_stable_form = Slot(uri=CHEMROF.has_physiologically_stable_form, name="has_physiologically_stable_form", curie=CHEMROF.curie('has_physiologically_stable_form'),
                   model_uri=CHEMROF.has_physiologically_stable_form, domain=None, range=Optional[str])

slots.has_acid_form = Slot(uri=CHEMROF.has_acid_form, name="has_acid_form", curie=CHEMROF.curie('has_acid_form'),
                   model_uri=CHEMROF.has_acid_form, domain=MoleculeByChargeState, range=Optional[Union[str, MoleculeByChargeStateId]])

slots.has_chemical_role = Slot(uri=RO['0000087'], name="has_chemical_role", curie=RO.curie('0000087'),
                   model_uri=CHEMROF.has_chemical_role, domain=None, range=Optional[Union[dict, ChemicalRole]])

slots.has_part = Slot(uri=BFO['0000051'], name="has_part", curie=BFO.curie('0000051'),
                   model_uri=CHEMROF.has_part, domain=None, range=Optional[str], mappings = [BFO["0000050"], SCHEMA["hasBioChemEntityPart"]])

slots.has_repeat_unit = Slot(uri=CHEMROF.has_repeat_unit, name="has_repeat_unit", curie=CHEMROF.curie('has_repeat_unit'),
                   model_uri=CHEMROF.has_repeat_unit, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.polymer_of = Slot(uri=CHEMROF.polymer_of, name="polymer_of", curie=CHEMROF.curie('polymer_of'),
                   model_uri=CHEMROF.polymer_of, domain=None, range=Optional[Union[str, MacromoleculeId]])

slots.has_polymer_repeat_units = Slot(uri=CHEMROF.has_polymer_repeat_units, name="has_polymer_repeat_units", curie=CHEMROF.curie('has_polymer_repeat_units'),
                   model_uri=CHEMROF.has_polymer_repeat_units, domain=None, range=Optional[Union[Union[dict, PolymerRepeatUnit], list[Union[dict, PolymerRepeatUnit]]]])

slots.is_branched = Slot(uri=CHEMROF.is_branched, name="is_branched", curie=CHEMROF.curie('is_branched'),
                   model_uri=CHEMROF.is_branched, domain=None, range=Optional[Union[bool, Bool]])

slots.polymer_architecture_type = Slot(uri=CHEMROF.polymer_architecture_type, name="polymer_architecture_type", curie=CHEMROF.curie('polymer_architecture_type'),
                   model_uri=CHEMROF.polymer_architecture_type, domain=None, range=Optional[str])

slots.has_atoms = Slot(uri=CHEMROF.has_atoms, name="has_atoms", curie=CHEMROF.curie('has_atoms'),
                   model_uri=CHEMROF.has_atoms, domain=Molecule, range=Optional[Union[Union[str, AtomId], list[Union[str, AtomId]]]])

slots.has_submolecules = Slot(uri=CHEMROF.has_submolecules, name="has_submolecules", curie=CHEMROF.curie('has_submolecules'),
                   model_uri=CHEMROF.has_submolecules, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.has_ionic_component = Slot(uri=CHEMROF.has_ionic_component, name="has_ionic_component", curie=CHEMROF.curie('has_ionic_component'),
                   model_uri=CHEMROF.has_ionic_component, domain=None, range=Optional[str])

slots.has_cationic_component = Slot(uri=CHEMROF.has_cationic_component, name="has_cationic_component", curie=CHEMROF.curie('has_cationic_component'),
                   model_uri=CHEMROF.has_cationic_component, domain=None, range=Optional[str])

slots.has_anionic_component = Slot(uri=CHEMROF.has_anionic_component, name="has_anionic_component", curie=CHEMROF.curie('has_anionic_component'),
                   model_uri=CHEMROF.has_anionic_component, domain=None, range=Optional[str])

slots.has_group = Slot(uri=CHEMROF.has_group, name="has_group", curie=CHEMROF.curie('has_group'),
                   model_uri=CHEMROF.has_group, domain=Atom, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.has_proportional_parts = Slot(uri=CHEMROF.has_proportional_parts, name="has_proportional_parts", curie=CHEMROF.curie('has_proportional_parts'),
                   model_uri=CHEMROF.has_proportional_parts, domain=ImpreciseChemicalMixture, range=Optional[Union[Union[dict, "ProportionalPart"], list[Union[dict, "ProportionalPart"]]]])

slots.energy_level = Slot(uri=CHEMROF.energy_level, name="energy_level", curie=CHEMROF.curie('energy_level'),
                   model_uri=CHEMROF.energy_level, domain=None, range=Optional[str])

slots.has_atom_occurrences = Slot(uri=CHEMROF.has_atom_occurrences, name="has_atom_occurrences", curie=CHEMROF.curie('has_atom_occurrences'),
                   model_uri=CHEMROF.has_atom_occurrences, domain=None, range=Optional[Union[dict[Union[str, AtomOccurrenceName], Union[dict, AtomOccurrence]], list[Union[dict, AtomOccurrence]]]])

slots.has_bonds = Slot(uri=CHEMROF.has_bonds, name="has_bonds", curie=CHEMROF.curie('has_bonds'),
                   model_uri=CHEMROF.has_bonds, domain=Molecule, range=Optional[Union[Union[dict, "AtomicBond"], list[Union[dict, "AtomicBond"]]]])

slots.half_life = Slot(uri=CHEMROF.half_life, name="half_life", curie=CHEMROF.curie('half_life'),
                   model_uri=CHEMROF.half_life, domain=Isotope, range=Optional[int])

slots.decay_mode = Slot(uri=CHEMROF.decay_mode, name="decay_mode", curie=CHEMROF.curie('decay_mode'),
                   model_uri=CHEMROF.decay_mode, domain=Isotope, range=Optional[str])

slots.decay_product = Slot(uri=CHEMROF.decay_product, name="decay_product", curie=CHEMROF.curie('decay_product'),
                   model_uri=CHEMROF.decay_product, domain=Isotope, range=Optional[Union[str, IsotopeId]])

slots.decay_energy = Slot(uri=CHEMROF.decay_energy, name="decay_energy", curie=CHEMROF.curie('decay_energy'),
                   model_uri=CHEMROF.decay_energy, domain=Isotope, range=Optional[str])

slots.mode_of_formation = Slot(uri=CHEMROF.mode_of_formation, name="mode_of_formation", curie=CHEMROF.curie('mode_of_formation'),
                   model_uri=CHEMROF.mode_of_formation, domain=Isotope, range=Optional[str])

slots.number_of_heavy_atoms = Slot(uri=CHEMROF.number_of_heavy_atoms, name="number_of_heavy_atoms", curie=CHEMROF.curie('number_of_heavy_atoms'),
                   model_uri=CHEMROF.number_of_heavy_atoms, domain=None, range=Optional[str])

slots.number_of_rings = Slot(uri=CHEMROF.number_of_rings, name="number_of_rings", curie=CHEMROF.curie('number_of_rings'),
                   model_uri=CHEMROF.number_of_rings, domain=None, range=Optional[str])

slots.number_of_aromatic_rings = Slot(uri=CHEMROF.number_of_aromatic_rings, name="number_of_aromatic_rings", curie=CHEMROF.curie('number_of_aromatic_rings'),
                   model_uri=CHEMROF.number_of_aromatic_rings, domain=None, range=Optional[str])

slots.number_of_rotatable_bonds = Slot(uri=CHEMROF.number_of_rotatable_bonds, name="number_of_rotatable_bonds", curie=CHEMROF.curie('number_of_rotatable_bonds'),
                   model_uri=CHEMROF.number_of_rotatable_bonds, domain=None, range=Optional[str])

slots.van_der_waals_molecular_volume = Slot(uri=CHEMROF.van_der_waals_molecular_volume, name="van_der_waals_molecular_volume", curie=CHEMROF.curie('van_der_waals_molecular_volume'),
                   model_uri=CHEMROF.van_der_waals_molecular_volume, domain=None, range=Optional[str])

slots.topological_polar_surface_area = Slot(uri=CHEMROF.topological_polar_surface_area, name="topological_polar_surface_area", curie=CHEMROF.curie('topological_polar_surface_area'),
                   model_uri=CHEMROF.topological_polar_surface_area, domain=None, range=Optional[str])

slots.number_of_hydrogen_bond_donors = Slot(uri=CHEMROF.number_of_hydrogen_bond_donors, name="number_of_hydrogen_bond_donors", curie=CHEMROF.curie('number_of_hydrogen_bond_donors'),
                   model_uri=CHEMROF.number_of_hydrogen_bond_donors, domain=None, range=Optional[str])

slots.number_of_hydrogen_bond_acceptors = Slot(uri=CHEMROF.number_of_hydrogen_bond_acceptors, name="number_of_hydrogen_bond_acceptors", curie=CHEMROF.curie('number_of_hydrogen_bond_acceptors'),
                   model_uri=CHEMROF.number_of_hydrogen_bond_acceptors, domain=None, range=Optional[str])

slots.logP6_partition_coefficient = Slot(uri=CHEMROF.logP6_partition_coefficient, name="logP6_partition_coefficient", curie=CHEMROF.curie('logP6_partition_coefficient'),
                   model_uri=CHEMROF.logP6_partition_coefficient, domain=None, range=Optional[str])

slots.molar_refractivity = Slot(uri=CHEMROF.molar_refractivity, name="molar_refractivity", curie=CHEMROF.curie('molar_refractivity'),
                   model_uri=CHEMROF.molar_refractivity, domain=None, range=Optional[str])

slots.thermophysical_property = Slot(uri=CHEMROF.thermophysical_property, name="thermophysical_property", curie=CHEMROF.curie('thermophysical_property'),
                   model_uri=CHEMROF.thermophysical_property, domain=None, range=Optional[str])

slots.molar_value = Slot(uri=CHEMROF.molar_value, name="molar_value", curie=CHEMROF.curie('molar_value'),
                   model_uri=CHEMROF.molar_value, domain=None, range=Optional[str])

slots.molar_cohesive_energy = Slot(uri=CHEMROF.molar_cohesive_energy, name="molar_cohesive_energy", curie=CHEMROF.curie('molar_cohesive_energy'),
                   model_uri=CHEMROF.molar_cohesive_energy, domain=None, range=Optional[str])

slots.has_cyclic_structure = Slot(uri=CHEMROF.has_cyclic_structure, name="has_cyclic_structure", curie=CHEMROF.curie('has_cyclic_structure'),
                   model_uri=CHEMROF.has_cyclic_structure, domain=Molecule, range=Optional[Union[bool, Bool]], mappings = [CHEMINF["000067"]])

slots.molecular_property = Slot(uri=CHEMROF.molecular_property, name="molecular_property", curie=CHEMROF.curie('molecular_property'),
                   model_uri=CHEMROF.molecular_property, domain=None, range=Optional[str])

slots.molecular_electronic_absorption_spectroscopy = Slot(uri=CHEMROF.molecular_electronic_absorption_spectroscopy, name="molecular_electronic_absorption_spectroscopy", curie=CHEMROF.curie('molecular_electronic_absorption_spectroscopy'),
                   model_uri=CHEMROF.molecular_electronic_absorption_spectroscopy, domain=None, range=Optional[str])

slots.molecular_spectroscopy_by_energy_state = Slot(uri=CHEMROF.molecular_spectroscopy_by_energy_state, name="molecular_spectroscopy_by_energy_state", curie=CHEMROF.curie('molecular_spectroscopy_by_energy_state'),
                   model_uri=CHEMROF.molecular_spectroscopy_by_energy_state, domain=None, range=Optional[str])

slots.molecular_spectroscopy = Slot(uri=CHEMROF.molecular_spectroscopy, name="molecular_spectroscopy", curie=CHEMROF.curie('molecular_spectroscopy'),
                   model_uri=CHEMROF.molecular_spectroscopy, domain=None, range=Optional[str])

slots.molecular_replacement = Slot(uri=CHEMROF.molecular_replacement, name="molecular_replacement", curie=CHEMROF.curie('molecular_replacement'),
                   model_uri=CHEMROF.molecular_replacement, domain=None, range=Optional[str])

slots.molecular_mass = Slot(uri=CHEMROF.molecular_mass, name="molecular_mass", curie=CHEMROF.curie('molecular_mass'),
                   model_uri=CHEMROF.molecular_mass, domain=None, range=Optional[float])

slots.molecular_size = Slot(uri=CHEMROF.molecular_size, name="molecular_size", curie=CHEMROF.curie('molecular_size'),
                   model_uri=CHEMROF.molecular_size, domain=None, range=Optional[float])

slots.molecular_hydration = Slot(uri=CHEMROF.molecular_hydration, name="molecular_hydration", curie=CHEMROF.curie('molecular_hydration'),
                   model_uri=CHEMROF.molecular_hydration, domain=None, range=Optional[int])

slots.molecular_shape = Slot(uri=CHEMROF.molecular_shape, name="molecular_shape", curie=CHEMROF.curie('molecular_shape'),
                   model_uri=CHEMROF.molecular_shape, domain=None, range=Optional[str])

slots.molecular_charge = Slot(uri=CHEMROF.molecular_charge, name="molecular_charge", curie=CHEMROF.curie('molecular_charge'),
                   model_uri=CHEMROF.molecular_charge, domain=None, range=Optional[int])

slots.molecular_structure = Slot(uri=CHEMROF.molecular_structure, name="molecular_structure", curie=CHEMROF.curie('molecular_structure'),
                   model_uri=CHEMROF.molecular_structure, domain=None, range=Optional[str])

slots.molecular_heat_capacity = Slot(uri=CHEMROF.molecular_heat_capacity, name="molecular_heat_capacity", curie=CHEMROF.curie('molecular_heat_capacity'),
                   model_uri=CHEMROF.molecular_heat_capacity, domain=None, range=Optional[float])

slots.molecular_electronic_spectroscopy = Slot(uri=CHEMROF.molecular_electronic_spectroscopy, name="molecular_electronic_spectroscopy", curie=CHEMROF.curie('molecular_electronic_spectroscopy'),
                   model_uri=CHEMROF.molecular_electronic_spectroscopy, domain=None, range=Optional[str])

slots.water_solubility = Slot(uri=CHEMROF.water_solubility, name="water_solubility", curie=CHEMROF.curie('water_solubility'),
                   model_uri=CHEMROF.water_solubility, domain=None, range=Optional[float])

slots.pka_ionization_constant = Slot(uri=CHEMROF.pka_ionization_constant, name="pka_ionization_constant", curie=CHEMROF.curie('pka_ionization_constant'),
                   model_uri=CHEMROF.pka_ionization_constant, domain=None, range=Optional[Union[float, list[float]]])

slots.pka_temperature = Slot(uri=CHEMROF.pka_temperature, name="pka_temperature", curie=CHEMROF.curie('pka_temperature'),
                   model_uri=CHEMROF.pka_temperature, domain=None, range=Optional[float])

slots.pka_ionic_strength = Slot(uri=CHEMROF.pka_ionic_strength, name="pka_ionic_strength", curie=CHEMROF.curie('pka_ionic_strength'),
                   model_uri=CHEMROF.pka_ionic_strength, domain=None, range=Optional[float])

slots.pka_solvent = Slot(uri=CHEMROF.pka_solvent, name="pka_solvent", curie=CHEMROF.curie('pka_solvent'),
                   model_uri=CHEMROF.pka_solvent, domain=None, range=Optional[str])

slots.pka_pressure = Slot(uri=CHEMROF.pka_pressure, name="pka_pressure", curie=CHEMROF.curie('pka_pressure'),
                   model_uri=CHEMROF.pka_pressure, domain=None, range=Optional[float])

slots.chemical_representation = Slot(uri=CHEMROF.chemical_representation, name="chemical_representation", curie=CHEMROF.curie('chemical_representation'),
                   model_uri=CHEMROF.chemical_representation, domain=ChemicalEntity, range=Optional[str])

slots.has_minchi_representation = Slot(uri=CHEMROF.has_minchi_representation, name="has_minchi_representation", curie=CHEMROF.curie('has_minchi_representation'),
                   model_uri=CHEMROF.has_minchi_representation, domain=ChemicalEntity, range=Optional[str])

slots.has_rinchi_representation = Slot(uri=CHEMROF.has_rinchi_representation, name="has_rinchi_representation", curie=CHEMROF.curie('has_rinchi_representation'),
                   model_uri=CHEMROF.has_rinchi_representation, domain=ChemicalEntity, range=Optional[str])

slots.has_reaction_representation = Slot(uri=CHEMROF.has_reaction_representation, name="has_reaction_representation", curie=CHEMROF.curie('has_reaction_representation'),
                   model_uri=CHEMROF.has_reaction_representation, domain=ChemicalEntity, range=Optional[str])

slots.has_reaction_smiles_representation = Slot(uri=CHEMROF.has_reaction_smiles_representation, name="has_reaction_smiles_representation", curie=CHEMROF.curie('has_reaction_smiles_representation'),
                   model_uri=CHEMROF.has_reaction_smiles_representation, domain=ChemicalEntity, range=Optional[str])

slots.has_reaction_smarts_representation = Slot(uri=CHEMROF.has_reaction_smarts_representation, name="has_reaction_smarts_representation", curie=CHEMROF.curie('has_reaction_smarts_representation'),
                   model_uri=CHEMROF.has_reaction_smarts_representation, domain=ChemicalEntity, range=Optional[str])

slots.has_smirks_representation = Slot(uri=CHEMROF.has_smirks_representation, name="has_smirks_representation", curie=CHEMROF.curie('has_smirks_representation'),
                   model_uri=CHEMROF.has_smirks_representation, domain=ChemicalEntity, range=Optional[str])

slots.has_rauxinfo_representation = Slot(uri=CHEMROF.has_rauxinfo_representation, name="has_rauxinfo_representation", curie=CHEMROF.curie('has_rauxinfo_representation'),
                   model_uri=CHEMROF.has_rauxinfo_representation, domain=ChemicalEntity, range=Union[str, ChemicalEntityId])

slots.rinchi_key_string = Slot(uri=CHEMROF.rinchi_key_string, name="rinchi_key_string", curie=CHEMROF.curie('rinchi_key_string'),
                   model_uri=CHEMROF.rinchi_key_string, domain=ChemicalEntity, range=Union[str, ChemicalEntityId])

slots.long_rinchi_key_string = Slot(uri=CHEMROF.long_rinchi_key_string, name="long_rinchi_key_string", curie=CHEMROF.curie('long_rinchi_key_string'),
                   model_uri=CHEMROF.long_rinchi_key_string, domain=ChemicalEntity, range=Union[str, ChemicalEntityId])

slots.short_rinchi_key_string = Slot(uri=CHEMROF.short_rinchi_key_string, name="short_rinchi_key_string", curie=CHEMROF.curie('short_rinchi_key_string'),
                   model_uri=CHEMROF.short_rinchi_key_string, domain=ChemicalEntity, range=Union[str, ChemicalEntityId])

slots.reaction_rate = Slot(uri=CHEMROF.reaction_rate, name="reaction_rate", curie=CHEMROF.curie('reaction_rate'),
                   model_uri=CHEMROF.reaction_rate, domain=None, range=Optional[float])

slots.reaction_rate_coefficient = Slot(uri=CHEMROF.reaction_rate_coefficient, name="reaction_rate_coefficient", curie=CHEMROF.curie('reaction_rate_coefficient'),
                   model_uri=CHEMROF.reaction_rate_coefficient, domain=None, range=Optional[float])

slots.reaction_type = Slot(uri=CHEMROF.reaction_type, name="reaction_type", curie=CHEMROF.curie('reaction_type'),
                   model_uri=CHEMROF.reaction_type, domain=None, range=Optional[Union[str, "ReactionTypeEnum"]])

slots.kcat = Slot(uri=CHEMROF.kcat, name="kcat", curie=CHEMROF.curie('kcat'),
                   model_uri=CHEMROF.kcat, domain=None, range=Optional[str])

slots.michaelis_constant = Slot(uri=CHEMROF.michaelis_constant, name="michaelis_constant", curie=CHEMROF.curie('michaelis_constant'),
                   model_uri=CHEMROF.michaelis_constant, domain=None, range=Optional[str])

slots.has_sequence_representation = Slot(uri=CHEMROF.has_sequence_representation, name="has_sequence_representation", curie=CHEMROF.curie('has_sequence_representation'),
                   model_uri=CHEMROF.has_sequence_representation, domain=ChemicalEntity, range=Optional[str])

slots.AZE_notation_html = Slot(uri=CHEMROF.AZE_notation_html, name="AZE_notation_html", curie=CHEMROF.curie('AZE_notation_html'),
                   model_uri=CHEMROF.AZE_notation_html, domain=ChemicalEntity, range=Optional[str])

slots.carboydrate_representation = Slot(uri=CHEMROF.carboydrate_representation, name="carboydrate_representation", curie=CHEMROF.curie('carboydrate_representation'),
                   model_uri=CHEMROF.carboydrate_representation, domain=ChemicalEntity, range=Optional[str])

slots.wurcs_representation = Slot(uri=CHEMROF.wurcs_representation, name="wurcs_representation", curie=CHEMROF.curie('wurcs_representation'),
                   model_uri=CHEMROF.wurcs_representation, domain=ChemicalEntity, range=Optional[str],
                   pattern=re.compile(r'^WURCS=Version/.*'))

slots.carbbank_representation = Slot(uri=CHEMROF.carbbank_representation, name="carbbank_representation", curie=CHEMROF.curie('carbbank_representation'),
                   model_uri=CHEMROF.carbbank_representation, domain=ChemicalEntity, range=Optional[str])

slots.linucs_representation = Slot(uri=CHEMROF.linucs_representation, name="linucs_representation", curie=CHEMROF.curie('linucs_representation'),
                   model_uri=CHEMROF.linucs_representation, domain=ChemicalEntity, range=Optional[str])

slots.glycominds_linearcode_representation = Slot(uri=CHEMROF.glycominds_linearcode_representation, name="glycominds_linearcode_representation", curie=CHEMROF.curie('glycominds_linearcode_representation'),
                   model_uri=CHEMROF.glycominds_linearcode_representation, domain=ChemicalEntity, range=Optional[str])

slots.kegg_chemical_function_representation = Slot(uri=CHEMROF.kegg_chemical_function_representation, name="kegg_chemical_function_representation", curie=CHEMROF.curie('kegg_chemical_function_representation'),
                   model_uri=CHEMROF.kegg_chemical_function_representation, domain=ChemicalEntity, range=Optional[str])

slots.glycoct_condensed = Slot(uri=CHEMROF.glycoct_condensed, name="glycoct_condensed", curie=CHEMROF.curie('glycoct_condensed'),
                   model_uri=CHEMROF.glycoct_condensed, domain=ChemicalEntity, range=Optional[str])

slots.hashed_chemical_formula = Slot(uri=CHEMROF.hashed_chemical_formula, name="hashed_chemical_formula", curie=CHEMROF.curie('hashed_chemical_formula'),
                   model_uri=CHEMROF.hashed_chemical_formula, domain=ChemicalEntity, range=Optional[str])

slots.chemical_formula = Slot(uri=CHEMROF.chemical_formula, name="chemical_formula", curie=CHEMROF.curie('chemical_formula'),
                   model_uri=CHEMROF.chemical_formula, domain=ChemicalEntity, range=Optional[str], mappings = [SCHEMA["hasRepresentation"], EDAM["data_0846"]])

slots.chebi_formula = Slot(uri=CHEMROF.chebi_formula, name="chebi_formula", curie=CHEMROF.curie('chebi_formula'),
                   model_uri=CHEMROF.chebi_formula, domain=ChemicalEntity, range=Optional[str])

slots.molecular_formula = Slot(uri=CHEMROF.molecular_formula, name="molecular_formula", curie=CHEMROF.curie('molecular_formula'),
                   model_uri=CHEMROF.molecular_formula, domain=ChemicalEntity, range=Optional[str], mappings = [CHEMINF["000042"]])

slots.empirical_formula = Slot(uri=CHEMROF.empirical_formula, name="empirical_formula", curie=CHEMROF.curie('empirical_formula'),
                   model_uri=CHEMROF.empirical_formula, domain=ChemicalEntity, range=Optional[str])

slots.generalized_empirical_formula = Slot(uri=CHEMROF.generalized_empirical_formula, name="generalized_empirical_formula", curie=CHEMROF.curie('generalized_empirical_formula'),
                   model_uri=CHEMROF.generalized_empirical_formula, domain=ChemicalEntity, range=Optional[str])

slots.smarts_string = Slot(uri=CHEMROF.smarts_string, name="smarts_string", curie=CHEMROF.curie('smarts_string'),
                   model_uri=CHEMROF.smarts_string, domain=ChemicalEntity, range=Optional[str])

slots.markush_string = Slot(uri=CHEMROF.markush_string, name="markush_string", curie=CHEMROF.curie('markush_string'),
                   model_uri=CHEMROF.markush_string, domain=ChemicalEntity, range=Optional[str])

slots.lychi_string = Slot(uri=CHEMROF.lychi_string, name="lychi_string", curie=CHEMROF.curie('lychi_string'),
                   model_uri=CHEMROF.lychi_string, domain=ChemicalEntity, range=Union[str, ChemicalEntityId])

slots.inchi_string = Slot(uri=CHEMROF.inchi_string, name="inchi_string", curie=CHEMROF.curie('inchi_string'),
                   model_uri=CHEMROF.inchi_string, domain=ChemicalEntity, range=Optional[str])

slots.inchi_key_string = Slot(uri=CHEMROF.inchi_key_string, name="inchi_key_string", curie=CHEMROF.curie('inchi_key_string'),
                   model_uri=CHEMROF.inchi_key_string, domain=ChemicalEntity, range=Optional[str])

slots.inchi2d_string = Slot(uri=CHEMROF.inchi2d_string, name="inchi2d_string", curie=CHEMROF.curie('inchi2d_string'),
                   model_uri=CHEMROF.inchi2d_string, domain=ChemicalEntity, range=Optional[str])

slots.inchi2d_key_string = Slot(uri=CHEMROF.inchi2d_key_string, name="inchi2d_key_string", curie=CHEMROF.curie('inchi2d_key_string'),
                   model_uri=CHEMROF.inchi2d_key_string, domain=ChemicalEntity, range=Optional[str])

slots.smiles_string = Slot(uri=CHEMROF.smiles_string, name="smiles_string", curie=CHEMROF.curie('smiles_string'),
                   model_uri=CHEMROF.smiles_string, domain=ChemicalEntity, range=Optional[str])

slots.curly_smiles_string = Slot(uri=CHEMROF.curly_smiles_string, name="curly_smiles_string", curie=CHEMROF.curie('curly_smiles_string'),
                   model_uri=CHEMROF.curly_smiles_string, domain=ChemicalEntity, range=Optional[str])

slots.isomeric_smiles_string = Slot(uri=CHEMROF.isomeric_smiles_string, name="isomeric_smiles_string", curie=CHEMROF.curie('isomeric_smiles_string'),
                   model_uri=CHEMROF.isomeric_smiles_string, domain=ChemicalEntity, range=Optional[str])

slots.extended_smiles_string = Slot(uri=CHEMROF.extended_smiles_string, name="extended_smiles_string", curie=CHEMROF.curie('extended_smiles_string'),
                   model_uri=CHEMROF.extended_smiles_string, domain=ChemicalEntity, range=Optional[str])

slots.canonical_smiles_string = Slot(uri=CHEMROF.canonical_smiles_string, name="canonical_smiles_string", curie=CHEMROF.curie('canonical_smiles_string'),
                   model_uri=CHEMROF.canonical_smiles_string, domain=ChemicalEntity, range=Optional[str])

slots.tucan_string = Slot(uri=CHEMROF.tucan_string, name="tucan_string", curie=CHEMROF.curie('tucan_string'),
                   model_uri=CHEMROF.tucan_string, domain=ChemicalEntity, range=Optional[str])

slots.selfies_string = Slot(uri=CHEMROF.selfies_string, name="selfies_string", curie=CHEMROF.curie('selfies_string'),
                   model_uri=CHEMROF.selfies_string, domain=ChemicalEntity, range=Union[str, ChemicalEntityId])

slots.has_mixfile_location = Slot(uri=CHEMROF.has_mixfile_location, name="has_mixfile_location", curie=CHEMROF.curie('has_mixfile_location'),
                   model_uri=CHEMROF.has_mixfile_location, domain=None, range=Optional[str])

slots.has_molfile_location = Slot(uri=CHEMROF.has_molfile_location, name="has_molfile_location", curie=CHEMROF.curie('has_molfile_location'),
                   model_uri=CHEMROF.has_molfile_location, domain=None, range=Optional[str])

slots.inchi_component = Slot(uri=CHEMROF.inchi_component, name="inchi_component", curie=CHEMROF.curie('inchi_component'),
                   model_uri=CHEMROF.inchi_component, domain=None, range=Optional[str])

slots.inchi_sublayer = Slot(uri=CHEMROF.inchi_sublayer, name="inchi_sublayer", curie=CHEMROF.curie('inchi_sublayer'),
                   model_uri=CHEMROF.inchi_sublayer, domain=None, range=Optional[str])

slots.inchi_version_string = Slot(uri=CHEMROF.inchi_version_string, name="inchi_version_string", curie=CHEMROF.curie('inchi_version_string'),
                   model_uri=CHEMROF.inchi_version_string, domain=None, range=str,
                   pattern=re.compile(r'^1[S]'))

slots.inchi_sublayer_in_main_layer = Slot(uri=CHEMROF.inchi_sublayer_in_main_layer, name="inchi_sublayer_in_main_layer", curie=CHEMROF.curie('inchi_sublayer_in_main_layer'),
                   model_uri=CHEMROF.inchi_sublayer_in_main_layer, domain=None, range=Optional[str])

slots.inchi_chemical_sublayer = Slot(uri=CHEMROF.inchi_chemical_sublayer, name="inchi_chemical_sublayer", curie=CHEMROF.curie('inchi_chemical_sublayer'),
                   model_uri=CHEMROF.inchi_chemical_sublayer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z0-9\.]+$'))

slots.inchi_atom_connections_sublayer = Slot(uri=CHEMROF.inchi_atom_connections_sublayer, name="inchi_atom_connections_sublayer", curie=CHEMROF.curie('inchi_atom_connections_sublayer'),
                   model_uri=CHEMROF.inchi_atom_connections_sublayer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^c.*'))

slots.inchi_hydrogen_connections_sublayer = Slot(uri=CHEMROF.inchi_hydrogen_connections_sublayer, name="inchi_hydrogen_connections_sublayer", curie=CHEMROF.curie('inchi_hydrogen_connections_sublayer'),
                   model_uri=CHEMROF.inchi_hydrogen_connections_sublayer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^h.*'))

slots.inchi_charge_sublayer = Slot(uri=CHEMROF.inchi_charge_sublayer, name="inchi_charge_sublayer", curie=CHEMROF.curie('inchi_charge_sublayer'),
                   model_uri=CHEMROF.inchi_charge_sublayer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^q.*'))

slots.inchi_proton_sublayer = Slot(uri=CHEMROF.inchi_proton_sublayer, name="inchi_proton_sublayer", curie=CHEMROF.curie('inchi_proton_sublayer'),
                   model_uri=CHEMROF.inchi_proton_sublayer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^p[\-]\d+'))

slots.inchi_stereochemical_double_bond_sublayer = Slot(uri=CHEMROF.inchi_stereochemical_double_bond_sublayer, name="inchi_stereochemical_double_bond_sublayer", curie=CHEMROF.curie('inchi_stereochemical_double_bond_sublayer'),
                   model_uri=CHEMROF.inchi_stereochemical_double_bond_sublayer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^b.*'))

slots.inchi_tetrahedral_stereochemical_sublayer = Slot(uri=CHEMROF.inchi_tetrahedral_stereochemical_sublayer, name="inchi_tetrahedral_stereochemical_sublayer", curie=CHEMROF.curie('inchi_tetrahedral_stereochemical_sublayer'),
                   model_uri=CHEMROF.inchi_tetrahedral_stereochemical_sublayer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[tm].*'))

slots.inchi_stereochemical_type_sublayer = Slot(uri=CHEMROF.inchi_stereochemical_type_sublayer, name="inchi_stereochemical_type_sublayer", curie=CHEMROF.curie('inchi_stereochemical_type_sublayer'),
                   model_uri=CHEMROF.inchi_stereochemical_type_sublayer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^s.*'))

slots.inchi_isotopic_layer = Slot(uri=CHEMROF.inchi_isotopic_layer, name="inchi_isotopic_layer", curie=CHEMROF.curie('inchi_isotopic_layer'),
                   model_uri=CHEMROF.inchi_isotopic_layer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[ih].*'))

slots.inchi_fixed_H_layer = Slot(uri=CHEMROF.inchi_fixed_H_layer, name="inchi_fixed_H_layer", curie=CHEMROF.curie('inchi_fixed_H_layer'),
                   model_uri=CHEMROF.inchi_fixed_H_layer, domain=None, range=Optional[str])

slots.inchi_reconnected_layer = Slot(uri=CHEMROF.inchi_reconnected_layer, name="inchi_reconnected_layer", curie=CHEMROF.curie('inchi_reconnected_layer'),
                   model_uri=CHEMROF.inchi_reconnected_layer, domain=None, range=Optional[str])

slots.atomically_connected_to = Slot(uri=CHEMROF.atomically_connected_to, name="atomically_connected_to", curie=CHEMROF.curie('atomically_connected_to'),
                   model_uri=CHEMROF.atomically_connected_to, domain=AtomOccurrence, range=Optional[Union[Union[str, AtomOccurrenceName], list[Union[str, AtomOccurrenceName]]]])

slots.is_organic = Slot(uri=CHEMROF.is_organic, name="is_organic", curie=CHEMROF.curie('is_organic'),
                   model_uri=CHEMROF.is_organic, domain=ChemicalEntity, range=Optional[Union[bool, Bool]])

slots.is_radical = Slot(uri=CHEMROF.is_radical, name="is_radical", curie=CHEMROF.curie('is_radical'),
                   model_uri=CHEMROF.is_radical, domain=ChemicalEntity, range=Optional[Union[bool, Bool]])

slots.next_in_homologous_series_from = Slot(uri=CHEMROF.next_in_homologous_series_from, name="next_in_homologous_series_from", curie=CHEMROF.curie('next_in_homologous_series_from'),
                   model_uri=CHEMROF.next_in_homologous_series_from, domain=Molecule, range=Optional[Union[str, MoleculeId]])

slots.isotopologue_of = Slot(uri=CHEMROF.isotopologue_of, name="isotopologue_of", curie=CHEMROF.curie('isotopologue_of'),
                   model_uri=CHEMROF.isotopologue_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.chemical_isomer_of = Slot(uri=CHEMROF.chemical_isomer_of, name="chemical_isomer_of", curie=CHEMROF.curie('chemical_isomer_of'),
                   model_uri=CHEMROF.chemical_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.structural_isomer_of = Slot(uri=CHEMROF.structural_isomer_of, name="structural_isomer_of", curie=CHEMROF.curie('structural_isomer_of'),
                   model_uri=CHEMROF.structural_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.isotopomer_of = Slot(uri=CHEMROF.isotopomer_of, name="isotopomer_of", curie=CHEMROF.curie('isotopomer_of'),
                   model_uri=CHEMROF.isotopomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.skeletal_isomer_of = Slot(uri=CHEMROF.skeletal_isomer_of, name="skeletal_isomer_of", curie=CHEMROF.curie('skeletal_isomer_of'),
                   model_uri=CHEMROF.skeletal_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.position_isomer_of = Slot(uri=CHEMROF.position_isomer_of, name="position_isomer_of", curie=CHEMROF.curie('position_isomer_of'),
                   model_uri=CHEMROF.position_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.functional_isomer_of = Slot(uri=CHEMROF.functional_isomer_of, name="functional_isomer_of", curie=CHEMROF.curie('functional_isomer_of'),
                   model_uri=CHEMROF.functional_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.tautomer_of = Slot(uri=CHEMROF.tautomer_of, name="tautomer_of", curie=CHEMROF.curie('tautomer_of'),
                   model_uri=CHEMROF.tautomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.stereoisomer_of = Slot(uri=CHEMROF.stereoisomer_of, name="stereoisomer_of", curie=CHEMROF.curie('stereoisomer_of'),
                   model_uri=CHEMROF.stereoisomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.diastereoisomers_of = Slot(uri=CHEMROF.diastereoisomers_of, name="diastereoisomers_of", curie=CHEMROF.curie('diastereoisomers_of'),
                   model_uri=CHEMROF.diastereoisomers_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.epimer_of = Slot(uri=CHEMROF.epimer_of, name="epimer_of", curie=CHEMROF.curie('epimer_of'),
                   model_uri=CHEMROF.epimer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.enantiomer_of = Slot(uri=CHEMROF.enantiomer_of, name="enantiomer_of", curie=CHEMROF.curie('enantiomer_of'),
                   model_uri=CHEMROF.enantiomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.variant_reaction_of = Slot(uri=CHEMROF.variant_reaction_of, name="variant_reaction_of", curie=CHEMROF.curie('variant_reaction_of'),
                   model_uri=CHEMROF.variant_reaction_of, domain=Reaction, range=Optional[Union[str, ReactionId]])

slots.reaction_has_bidirectional_form = Slot(uri=CHEMROF.reaction_has_bidirectional_form, name="reaction_has_bidirectional_form", curie=CHEMROF.curie('reaction_has_bidirectional_form'),
                   model_uri=CHEMROF.reaction_has_bidirectional_form, domain=Reaction, range=Optional[Union[str, ReactionId]])

slots.classification_relationship = Slot(uri=CHEMROF.classification_relationship, name="classification_relationship", curie=CHEMROF.curie('classification_relationship'),
                   model_uri=CHEMROF.classification_relationship, domain=None, range=Optional[str])

slots.owl_subclass_of = Slot(uri=CHEMROF.owl_subclass_of, name="owl_subclass_of", curie=CHEMROF.curie('owl_subclass_of'),
                   model_uri=CHEMROF.owl_subclass_of, domain=None, range=Optional[Union[dict, "OwlClass"]])

slots.subtype_of = Slot(uri=CHEMROF.subtype_of, name="subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.subtype_of, domain=None, range=Optional[Union[Union[dict, "OwlClass"], list[Union[dict, "OwlClass"]]]])

slots.has_subtype = Slot(uri=CHEMROF.has_subtype, name="has_subtype", curie=CHEMROF.curie('has_subtype'),
                   model_uri=CHEMROF.has_subtype, domain=None, range=Optional[str])

slots.has_major_microspecies_at_pH7_3 = Slot(uri=CHEMROF.has_major_microspecies_at_pH7_3, name="has_major_microspecies_at_pH7_3", curie=CHEMROF.curie('has_major_microspecies_at_pH7_3'),
                   model_uri=CHEMROF.has_major_microspecies_at_pH7_3, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.major_microspecies_at_pH7_3_of = Slot(uri=CHEMROF.major_microspecies_at_pH7_3_of, name="major_microspecies_at_pH7_3_of", curie=CHEMROF.curie('major_microspecies_at_pH7_3_of'),
                   model_uri=CHEMROF.major_microspecies_at_pH7_3_of, domain=ChemicalEntity, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.classified_by = Slot(uri=CHEMROF.classified_by, name="classified_by", curie=CHEMROF.curie('classified_by'),
                   model_uri=CHEMROF.classified_by, domain=None, range=Optional[Union[dict, "OwlClass"]])

slots.classifies = Slot(uri=CHEMROF.classifies, name="classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.classifies, domain=None, range=Optional[str])

slots.has_charge_state = Slot(uri=CHEMROF.has_charge_state, name="has_charge_state", curie=CHEMROF.curie('has_charge_state'),
                   model_uri=CHEMROF.has_charge_state, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.charge_agnostic_entity = Slot(uri=CHEMROF.charge_agnostic_entity, name="charge_agnostic_entity", curie=CHEMROF.curie('charge_agnostic_entity'),
                   model_uri=CHEMROF.charge_agnostic_entity, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.has_morphological_category = Slot(uri=CHEMROF.has_morphological_category, name="has_morphological_category", curie=CHEMROF.curie('has_morphological_category'),
                   model_uri=CHEMROF.has_morphological_category, domain=None, range=Optional[Union[str, "NanostructureMorphologyEnum"]])

slots.is_substitutent_group_from = Slot(uri=CHEMROF.is_substitutent_group_from, name="is_substitutent_group_from", curie=CHEMROF.curie('is_substitutent_group_from'),
                   model_uri=CHEMROF.is_substitutent_group_from, domain=None, range=Optional[Union[str, MoleculeId]])

slots.boiling_point_in_celcius = Slot(uri=CHEMROF.boiling_point_in_celcius, name="boiling_point_in_celcius", curie=CHEMROF.curie('boiling_point_in_celcius'),
                   model_uri=CHEMROF.boiling_point_in_celcius, domain=None, range=Optional[float])

slots.melting_point_in_celcius = Slot(uri=CHEMROF.melting_point_in_celcius, name="melting_point_in_celcius", curie=CHEMROF.curie('melting_point_in_celcius'),
                   model_uri=CHEMROF.melting_point_in_celcius, domain=None, range=Optional[float])

slots.standard_atomic_weight = Slot(uri=CHEMROF.standard_atomic_weight, name="standard_atomic_weight", curie=CHEMROF.curie('standard_atomic_weight'),
                   model_uri=CHEMROF.standard_atomic_weight, domain=None, range=Optional[float])

slots.mass = Slot(uri=CHEMROF.mass, name="mass", curie=CHEMROF.curie('mass'),
                   model_uri=CHEMROF.mass, domain=None, range=Optional[float])

slots.monoisotopic_mass = Slot(uri=CHEMROF.monoisotopic_mass, name="monoisotopic_mass", curie=CHEMROF.curie('monoisotopic_mass'),
                   model_uri=CHEMROF.monoisotopic_mass, domain=None, range=Optional[float])

slots.electron_configuration = Slot(uri=CHEMROF.electron_configuration, name="electron_configuration", curie=CHEMROF.curie('electron_configuration'),
                   model_uri=CHEMROF.electron_configuration, domain=None, range=Optional[str])

slots.has_stereocenter = Slot(uri=CHEMROF.has_stereocenter, name="has_stereocenter", curie=CHEMROF.curie('has_stereocenter'),
                   model_uri=CHEMROF.has_stereocenter, domain=None, range=Optional[Union[Union[dict, Stereocenter], list[Union[dict, Stereocenter]]]])

slots.subject_atom_occurrence = Slot(uri=CHEMROF.subject_atom_occurrence, name="subject_atom_occurrence", curie=CHEMROF.curie('subject_atom_occurrence'),
                   model_uri=CHEMROF.subject_atom_occurrence, domain=None, range=Optional[Union[str, AtomOccurrenceName]])

slots.object_atom_occurrence = Slot(uri=CHEMROF.object_atom_occurrence, name="object_atom_occurrence", curie=CHEMROF.curie('object_atom_occurrence'),
                   model_uri=CHEMROF.object_atom_occurrence, domain=None, range=Optional[Union[str, AtomOccurrenceName]])

slots.bond_type = Slot(uri=CHEMROF.bond_type, name="bond_type", curie=CHEMROF.curie('bond_type'),
                   model_uri=CHEMROF.bond_type, domain=None, range=Optional[Union[str, "BondTypeEnum"]])

slots.subatomic_particle_type = Slot(uri=CHEMROF.subatomic_particle_type, name="subatomic_particle_type", curie=CHEMROF.curie('subatomic_particle_type'),
                   model_uri=CHEMROF.subatomic_particle_type, domain=None, range=Optional[Union[str, "SubatomicParticleEnum"]])

slots.bond_length_in_angstroms = Slot(uri=CHEMROF.bond_length_in_angstroms, name="bond_length_in_angstroms", curie=CHEMROF.curie('bond_length_in_angstroms'),
                   model_uri=CHEMROF.bond_length_in_angstroms, domain=None, range=Optional[float])

slots.bond_angle = Slot(uri=CHEMROF.bond_angle, name="bond_angle", curie=CHEMROF.curie('bond_angle'),
                   model_uri=CHEMROF.bond_angle, domain=None, range=Optional[float])

slots.torsional_angle = Slot(uri=CHEMROF.torsional_angle, name="torsional_angle", curie=CHEMROF.curie('torsional_angle'),
                   model_uri=CHEMROF.torsional_angle, domain=None, range=Optional[float])

slots.occurrence_of = Slot(uri=CHEMROF.occurrence_of, name="occurrence_of", curie=CHEMROF.curie('occurrence_of'),
                   model_uri=CHEMROF.occurrence_of, domain=None, range=Union[str, AtomId])

slots.valence = Slot(uri=CHEMROF.valence, name="valence", curie=CHEMROF.curie('valence'),
                   model_uri=CHEMROF.valence, domain=None, range=Optional[int])

slots.oxidation_number = Slot(uri=CHEMROF.oxidation_number, name="oxidation_number", curie=CHEMROF.curie('oxidation_number'),
                   model_uri=CHEMROF.oxidation_number, domain=None, range=Optional[int])

slots.formal_charge = Slot(uri=CHEMROF.formal_charge, name="formal_charge", curie=CHEMROF.curie('formal_charge'),
                   model_uri=CHEMROF.formal_charge, domain=None, range=Optional[int])

slots.coordination_number = Slot(uri=CHEMROF.coordination_number, name="coordination_number", curie=CHEMROF.curie('coordination_number'),
                   model_uri=CHEMROF.coordination_number, domain=None, range=Optional[int])

slots.acidity = Slot(uri=CHEMROF.acidity, name="acidity", curie=CHEMROF.curie('acidity'),
                   model_uri=CHEMROF.acidity, domain=None, range=Optional[float])

slots.hard_or_soft = Slot(uri=CHEMROF.hard_or_soft, name="hard_or_soft", curie=CHEMROF.curie('hard_or_soft'),
                   model_uri=CHEMROF.hard_or_soft, domain=None, range=Optional[Union[str, "HardOrSoftEnum"]])

slots.bronsted_acid_base_role = Slot(uri=CHEMROF.bronsted_acid_base_role, name="bronsted_acid_base_role", curie=CHEMROF.curie('bronsted_acid_base_role'),
                   model_uri=CHEMROF.bronsted_acid_base_role, domain=None, range=Optional[Union[str, "BronstedAcidBaseRoleEnum"]])

slots.has_parent_alcohol = Slot(uri=CHEMROF.has_parent_alcohol, name="has_parent_alcohol", curie=CHEMROF.curie('has_parent_alcohol'),
                   model_uri=CHEMROF.has_parent_alcohol, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.has_parent_acid = Slot(uri=CHEMROF.has_parent_acid, name="has_parent_acid", curie=CHEMROF.curie('has_parent_acid'),
                   model_uri=CHEMROF.has_parent_acid, domain=None, range=Optional[Union[str, MoleculeByChargeStateId]])

slots.relative_configuration = Slot(uri=CHEMROF.relative_configuration, name="relative_configuration", curie=CHEMROF.curie('relative_configuration'),
                   model_uri=CHEMROF.relative_configuration, domain=None, range=Optional[str])

slots.optical_configuration = Slot(uri=CHEMROF.optical_configuration, name="optical_configuration", curie=CHEMROF.curie('optical_configuration'),
                   model_uri=CHEMROF.optical_configuration, domain=None, range=Optional[str])

slots.absolute_configuration = Slot(uri=CHEMROF.absolute_configuration, name="absolute_configuration", curie=CHEMROF.curie('absolute_configuration'),
                   model_uri=CHEMROF.absolute_configuration, domain=None, range=Optional[str])

slots.enantiomer_form_of = Slot(uri=CHEMROF.enantiomer_form_of, name="enantiomer_form_of", curie=CHEMROF.curie('enantiomer_form_of'),
                   model_uri=CHEMROF.enantiomer_form_of, domain=None, range=Optional[Union[str, MoleculeId]])

slots.has_left_enantiomer = Slot(uri=CHEMROF.has_left_enantiomer, name="has_left_enantiomer", curie=CHEMROF.curie('has_left_enantiomer'),
                   model_uri=CHEMROF.has_left_enantiomer, domain=None, range=Union[str, EnantiomerId])

slots.has_right_enantiomer = Slot(uri=CHEMROF.has_right_enantiomer, name="has_right_enantiomer", curie=CHEMROF.curie('has_right_enantiomer'),
                   model_uri=CHEMROF.has_right_enantiomer, domain=None, range=Union[str, EnantiomerId])

slots.chirality_agnostic_form = Slot(uri=CHEMROF.chirality_agnostic_form, name="chirality_agnostic_form", curie=CHEMROF.curie('chirality_agnostic_form'),
                   model_uri=CHEMROF.chirality_agnostic_form, domain=None, range=Optional[Union[str, MoleculeId]])

slots.has_bonding_structure = Slot(uri=CHEMROF.has_bonding_structure, name="has_bonding_structure", curie=CHEMROF.curie('has_bonding_structure'),
                   model_uri=CHEMROF.has_bonding_structure, domain=None, range=str)

slots.repetition_of = Slot(uri=CHEMROF.repetition_of, name="repetition_of", curie=CHEMROF.curie('repetition_of'),
                   model_uri=CHEMROF.repetition_of, domain=None, range=Optional[Union[str, MoleculeId]])

slots.degree_of_polymerization = Slot(uri=CHEMROF.degree_of_polymerization, name="degree_of_polymerization", curie=CHEMROF.curie('degree_of_polymerization'),
                   model_uri=CHEMROF.degree_of_polymerization, domain=None, range=Optional[int])

slots.left_participants = Slot(uri=CHEMROF.left_participants, name="left_participants", curie=CHEMROF.curie('left_participants'),
                   model_uri=CHEMROF.left_participants, domain=None, range=Optional[Union[Union[dict, ReactionParticipant], list[Union[dict, ReactionParticipant]]]])

slots.right_participants = Slot(uri=CHEMROF.right_participants, name="right_participants", curie=CHEMROF.curie('right_participants'),
                   model_uri=CHEMROF.right_participants, domain=None, range=Optional[Union[Union[dict, ReactionParticipant], list[Union[dict, ReactionParticipant]]]])

slots.direction = Slot(uri=CHEMROF.direction, name="direction", curie=CHEMROF.curie('direction'),
                   model_uri=CHEMROF.direction, domain=None, range=Optional[str])

slots.is_diastereoselective = Slot(uri=CHEMROF.is_diastereoselective, name="is_diastereoselective", curie=CHEMROF.curie('is_diastereoselective'),
                   model_uri=CHEMROF.is_diastereoselective, domain=None, range=Optional[Union[bool, Bool]])

slots.is_stereo = Slot(uri=CHEMROF.is_stereo, name="is_stereo", curie=CHEMROF.curie('is_stereo'),
                   model_uri=CHEMROF.is_stereo, domain=None, range=Optional[Union[bool, Bool]])

slots.is_balanced = Slot(uri=CHEMROF.is_balanced, name="is_balanced", curie=CHEMROF.curie('is_balanced'),
                   model_uri=CHEMROF.is_balanced, domain=None, range=Optional[Union[bool, Bool]])

slots.is_transport = Slot(uri=CHEMROF.is_transport, name="is_transport", curie=CHEMROF.curie('is_transport'),
                   model_uri=CHEMROF.is_transport, domain=None, range=Optional[Union[bool, Bool]])

slots.is_fully_characterized = Slot(uri=CHEMROF.is_fully_characterized, name="is_fully_characterized", curie=CHEMROF.curie('is_fully_characterized'),
                   model_uri=CHEMROF.is_fully_characterized, domain=None, range=Optional[Union[bool, Bool]])

slots.reaction_center = Slot(uri=CHEMROF.reaction_center, name="reaction_center", curie=CHEMROF.curie('reaction_center'),
                   model_uri=CHEMROF.reaction_center, domain=None, range=Optional[str])

slots.description = Slot(uri=CHEMROF.description, name="description", curie=CHEMROF.curie('description'),
                   model_uri=CHEMROF.description, domain=None, range=Optional[str])

slots.participant = Slot(uri=CHEMROF.participant, name="participant", curie=CHEMROF.curie('participant'),
                   model_uri=CHEMROF.participant, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.stoichiometry = Slot(uri=CHEMROF.stoichiometry, name="stoichiometry", curie=CHEMROF.curie('stoichiometry'),
                   model_uri=CHEMROF.stoichiometry, domain=None, range=Optional[int])

slots.has_role = Slot(uri=CHEMROF.has_role, name="has_role", curie=CHEMROF.curie('has_role'),
                   model_uri=CHEMROF.has_role, domain=None, range=Optional[Union[str, "IngredientRoleEnum"]])

slots.composed_of = Slot(uri=CHEMROF.composed_of, name="composed_of", curie=CHEMROF.curie('composed_of'),
                   model_uri=CHEMROF.composed_of, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.minimal_percentage = Slot(uri=CHEMROF.minimal_percentage, name="minimal_percentage", curie=CHEMROF.curie('minimal_percentage'),
                   model_uri=CHEMROF.minimal_percentage, domain=None, range=Optional[float])

slots.maximum_percentage = Slot(uri=CHEMROF.maximum_percentage, name="maximum_percentage", curie=CHEMROF.curie('maximum_percentage'),
                   model_uri=CHEMROF.maximum_percentage, domain=None, range=Optional[float])

slots.left_molecule = Slot(uri=CHEMROF.left_molecule, name="left_molecule", curie=CHEMROF.curie('left_molecule'),
                   model_uri=CHEMROF.left_molecule, domain=None, range=Optional[Union[str, MoleculeId]])

slots.right_molecule = Slot(uri=CHEMROF.right_molecule, name="right_molecule", curie=CHEMROF.curie('right_molecule'),
                   model_uri=CHEMROF.right_molecule, domain=None, range=Optional[Union[str, MoleculeId]])

slots.score = Slot(uri=CHEMROF.score, name="score", curie=CHEMROF.curie('score'),
                   model_uri=CHEMROF.score, domain=None, range=Optional[float])

slots.collection__entities = Slot(uri=CHEMROF.entities, name="collection__entities", curie=CHEMROF.curie('entities'),
                   model_uri=CHEMROF.collection__entities, domain=None, range=Optional[Union[dict[Union[str, DomainEntityId], Union[dict, DomainEntity]], list[Union[dict, DomainEntity]]]])

slots.naturalProduct__derived_from_organisms = Slot(uri=CHEMROF.derived_from_organisms, name="naturalProduct__derived_from_organisms", curie=CHEMROF.curie('derived_from_organisms'),
                   model_uri=CHEMROF.naturalProduct__derived_from_organisms, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.atomicBond__subject = Slot(uri=CHEMROF.subject, name="atomicBond__subject", curie=CHEMROF.curie('subject'),
                   model_uri=CHEMROF.atomicBond__subject, domain=None, range=Optional[Union[str, AtomOccurrenceName]])

slots.atomicBond__object = Slot(uri=CHEMROF.object, name="atomicBond__object", curie=CHEMROF.curie('object'),
                   model_uri=CHEMROF.atomicBond__object, domain=None, range=Optional[Union[str, AtomOccurrenceName]])

slots.atomicBond__bond_type = Slot(uri=CHEMROF.bond_type, name="atomicBond__bond_type", curie=CHEMROF.curie('bond_type'),
                   model_uri=CHEMROF.atomicBond__bond_type, domain=None, range=Optional[Union[str, "BondTypeEnum"]])

slots.atomicBond__bond_order = Slot(uri=CHEMROF.bond_order, name="atomicBond__bond_order", curie=CHEMROF.curie('bond_order'),
                   model_uri=CHEMROF.atomicBond__bond_order, domain=AtomicBond, range=Optional[int])

slots.atomicBond__bond_length = Slot(uri=CHEMROF.bond_length, name="atomicBond__bond_length", curie=CHEMROF.curie('bond_length'),
                   model_uri=CHEMROF.atomicBond__bond_length, domain=AtomicBond, range=Optional[float])

slots.atomicBond__bond_energy = Slot(uri=CHEMROF.bond_energy, name="atomicBond__bond_energy", curie=CHEMROF.curie('bond_energy'),
                   model_uri=CHEMROF.atomicBond__bond_energy, domain=None, range=Optional[float])

slots.atomicBond__bond_length_in_angstroms = Slot(uri=CHEMROF.bond_length_in_angstroms, name="atomicBond__bond_length_in_angstroms", curie=CHEMROF.curie('bond_length_in_angstroms'),
                   model_uri=CHEMROF.atomicBond__bond_length_in_angstroms, domain=None, range=Optional[float])

slots.atomicBond__bond_angle = Slot(uri=CHEMROF.bond_angle, name="atomicBond__bond_angle", curie=CHEMROF.curie('bond_angle'),
                   model_uri=CHEMROF.atomicBond__bond_angle, domain=None, range=Optional[float])

slots.atomicBond__torsional_angle = Slot(uri=CHEMROF.torsional_angle, name="atomicBond__torsional_angle", curie=CHEMROF.curie('torsional_angle'),
                   model_uri=CHEMROF.atomicBond__torsional_angle, domain=None, range=Optional[float])

slots.subatomicParticleOccurrence__occurrence_of = Slot(uri=CHEMROF.occurrence_of, name="subatomicParticleOccurrence__occurrence_of", curie=CHEMROF.curie('occurrence_of'),
                   model_uri=CHEMROF.subatomicParticleOccurrence__occurrence_of, domain=None, range=Union[str, SubatomicParticleId])

slots.subatomicParticleOccurrence__Count = Slot(uri=CHEMROF.Count, name="subatomicParticleOccurrence__Count", curie=CHEMROF.curie('Count'),
                   model_uri=CHEMROF.subatomicParticleOccurrence__Count, domain=None, range=Optional[int])

slots.atomOccurrence__name = Slot(uri=CHEMROF.name, name="atomOccurrence__name", curie=CHEMROF.curie('name'),
                   model_uri=CHEMROF.atomOccurrence__name, domain=None, range=URIRef)

slots.atomOccurrence__occurrence_of = Slot(uri=CHEMROF.occurrence_of, name="atomOccurrence__occurrence_of", curie=CHEMROF.curie('occurrence_of'),
                   model_uri=CHEMROF.atomOccurrence__occurrence_of, domain=None, range=Union[str, AtomId])

slots.atomOccurrence__valence = Slot(uri=CHEMROF.valence, name="atomOccurrence__valence", curie=CHEMROF.curie('valence'),
                   model_uri=CHEMROF.atomOccurrence__valence, domain=None, range=Optional[int])

slots.atomOccurrence__oxidation_number = Slot(uri=CHEMROF.oxidation_number, name="atomOccurrence__oxidation_number", curie=CHEMROF.curie('oxidation_number'),
                   model_uri=CHEMROF.atomOccurrence__oxidation_number, domain=None, range=Optional[int])

slots.atomOccurrence__formal_charge = Slot(uri=CHEMROF.formal_charge, name="atomOccurrence__formal_charge", curie=CHEMROF.curie('formal_charge'),
                   model_uri=CHEMROF.atomOccurrence__formal_charge, domain=None, range=Optional[int])

slots.atomOccurrence__coordination_number = Slot(uri=CHEMROF.coordination_number, name="atomOccurrence__coordination_number", curie=CHEMROF.curie('coordination_number'),
                   model_uri=CHEMROF.atomOccurrence__coordination_number, domain=None, range=Optional[int])

slots.ChemicalEntity_inchi_chemical_sublayer = Slot(uri=CHEMROF.inchi_chemical_sublayer, name="ChemicalEntity_inchi_chemical_sublayer", curie=CHEMROF.curie('inchi_chemical_sublayer'),
                   model_uri=CHEMROF.ChemicalEntity_inchi_chemical_sublayer, domain=ChemicalEntity, range=Optional[str],
                   pattern=re.compile(r'^[A-Z0-9\.]+$'))

slots.GroupingClass_subtype_of = Slot(uri=CHEMROF.subtype_of, name="GroupingClass_subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.GroupingClass_subtype_of, domain=GroupingClass, range=Optional[Union[Union[str, GroupingClassId], list[Union[str, GroupingClassId]]]])

slots.PhysicochemicalEntityGroupingClass_subtype_of = Slot(uri=CHEMROF.subtype_of, name="PhysicochemicalEntityGroupingClass_subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.PhysicochemicalEntityGroupingClass_subtype_of, domain=PhysicochemicalEntityGroupingClass, range=Optional[Union[Union[str, PhysicochemicalEntityGroupingClassId], list[Union[str, PhysicochemicalEntityGroupingClassId]]]])

slots.PhysicochemicalEntityGroupingClass_classifies = Slot(uri=CHEMROF.classifies, name="PhysicochemicalEntityGroupingClass_classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.PhysicochemicalEntityGroupingClass_classifies, domain=PhysicochemicalEntityGroupingClass, range=Optional[Union[str, PhysicochemicalEntityId]])

slots.ChemicalGroupingClass_subtype_of = Slot(uri=CHEMROF.subtype_of, name="ChemicalGroupingClass_subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.ChemicalGroupingClass_subtype_of, domain=ChemicalGroupingClass, range=Optional[Union[Union[str, ChemicalGroupingClassId], list[Union[str, ChemicalGroupingClassId]]]])

slots.ChemicalGroupingClass_classifies = Slot(uri=CHEMROF.classifies, name="ChemicalGroupingClass_classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.ChemicalGroupingClass_classifies, domain=ChemicalGroupingClass, range=Optional[Union[str, ChemicalEntityId]])

slots.ReactionGroupingClass_subtype_of = Slot(uri=CHEMROF.subtype_of, name="ReactionGroupingClass_subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.ReactionGroupingClass_subtype_of, domain=ReactionGroupingClass, range=Optional[Union[Union[str, ReactionGroupingClassId], list[Union[str, ReactionGroupingClassId]]]])

slots.ReactionGroupingClass_classifies = Slot(uri=CHEMROF.classifies, name="ReactionGroupingClass_classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.ReactionGroupingClass_classifies, domain=ReactionGroupingClass, range=Optional[Union[str, ReactionId]])

slots.MaterialGroupingClass_subtype_of = Slot(uri=CHEMROF.subtype_of, name="MaterialGroupingClass_subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.MaterialGroupingClass_subtype_of, domain=MaterialGroupingClass, range=Optional[Union[Union[str, MaterialGroupingClassId], list[Union[str, MaterialGroupingClassId]]]])

slots.MaterialGroupingClass_classifies = Slot(uri=CHEMROF.classifies, name="MaterialGroupingClass_classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.MaterialGroupingClass_classifies, domain=MaterialGroupingClass, range=Optional[Union[str, MaterialId]])

slots.ChemicalGroupingByCharge_subtype_of = Slot(uri=CHEMROF.subtype_of, name="ChemicalGroupingByCharge_subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.ChemicalGroupingByCharge_subtype_of, domain=ChemicalGroupingByCharge, range=Optional[Union[Union[str, MoleculeGroupingClassId], list[Union[str, MoleculeGroupingClassId]]]])

slots.ChemicalGroupingByCharge_has_charge_state = Slot(uri=CHEMROF.has_charge_state, name="ChemicalGroupingByCharge_has_charge_state", curie=CHEMROF.curie('has_charge_state'),
                   model_uri=CHEMROF.ChemicalGroupingByCharge_has_charge_state, domain=ChemicalGroupingByCharge, range=Optional[Union[str, URIorCURIE]])

slots.ChemicalGroupingByCharge_charge_agnostic_entity = Slot(uri=CHEMROF.charge_agnostic_entity, name="ChemicalGroupingByCharge_charge_agnostic_entity", curie=CHEMROF.curie('charge_agnostic_entity'),
                   model_uri=CHEMROF.ChemicalGroupingByCharge_charge_agnostic_entity, domain=ChemicalGroupingByCharge, range=Optional[Union[str, ChemicalEntityId]])

slots.MoleculeGroupingClass_subtype_of = Slot(uri=CHEMROF.subtype_of, name="MoleculeGroupingClass_subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.MoleculeGroupingClass_subtype_of, domain=MoleculeGroupingClass, range=Optional[Union[Union[str, MoleculeGroupingClassId], list[Union[str, MoleculeGroupingClassId]]]])

slots.MoleculeGroupingClass_classifies = Slot(uri=CHEMROF.classifies, name="MoleculeGroupingClass_classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.MoleculeGroupingClass_classifies, domain=MoleculeGroupingClass, range=Optional[Union[str, MoleculeId]])

slots.MolecularComponentGroupingClass_subtype_of = Slot(uri=CHEMROF.subtype_of, name="MolecularComponentGroupingClass_subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.MolecularComponentGroupingClass_subtype_of, domain=MolecularComponentGroupingClass, range=Optional[Union[Union[str, MolecularComponentGroupingClassId], list[Union[str, MolecularComponentGroupingClassId]]]])

slots.MolecularComponentGroupingClass_classifies = Slot(uri=CHEMROF.classifies, name="MolecularComponentGroupingClass_classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.MolecularComponentGroupingClass_classifies, domain=MolecularComponentGroupingClass, range=Optional[Union[str, MolecularComponentId]])

slots.MolecularDerivativeGroupingClass_name = Slot(uri=RDFS.label, name="MolecularDerivativeGroupingClass_name", curie=RDFS.curie('label'),
                   model_uri=CHEMROF.MolecularDerivativeGroupingClass_name, domain=MolecularDerivativeGroupingClass, range=Optional[str])

slots.MolecularDerivativeGroupingClass_classifies = Slot(uri=CHEMROF.classifies, name="MolecularDerivativeGroupingClass_classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.MolecularDerivativeGroupingClass_classifies, domain=MolecularDerivativeGroupingClass, range=Optional[Union[str, MoleculeId]])

slots.MoleculeGroupingClassDefinedByComponents_has_part = Slot(uri=BFO['0000051'], name="MoleculeGroupingClassDefinedByComponents_has_part", curie=BFO.curie('0000051'),
                   model_uri=CHEMROF.MoleculeGroupingClassDefinedByComponents_has_part, domain=MoleculeGroupingClassDefinedByComponents, range=Optional[Union[dict, "ChemicalEntityOrGrouping"]], mappings = [BFO["0000050"], SCHEMA["hasBioChemEntityPart"]])

slots.MoleculeGroupingClassDefinedByAdditionOfAGroup_has_group = Slot(uri=CHEMROF.has_group, name="MoleculeGroupingClassDefinedByAdditionOfAGroup_has_group", curie=CHEMROF.curie('has_group'),
                   model_uri=CHEMROF.MoleculeGroupingClassDefinedByAdditionOfAGroup_has_group, domain=MoleculeGroupingClassDefinedByAdditionOfAGroup, range=Optional[Union[Union[str, ChemicalGroupId], list[Union[str, ChemicalGroupId]]]])

slots.MoleculeGroupingClassDefinedByAdditionOfAGroup_derivative_of = Slot(uri=CHEMROF.derivative_of, name="MoleculeGroupingClassDefinedByAdditionOfAGroup_derivative_of", curie=CHEMROF.curie('derivative_of'),
                   model_uri=CHEMROF.MoleculeGroupingClassDefinedByAdditionOfAGroup_derivative_of, domain=MoleculeGroupingClassDefinedByAdditionOfAGroup, range=Optional[Union[str, PolyatomicEntityId]])

slots.ChemicalSaltGroupingClass_name = Slot(uri=RDFS.label, name="ChemicalSaltGroupingClass_name", curie=RDFS.curie('label'),
                   model_uri=CHEMROF.ChemicalSaltGroupingClass_name, domain=ChemicalSaltGroupingClass, range=Optional[str])

slots.ChemicalSaltGroupingClass_classifies = Slot(uri=CHEMROF.classifies, name="ChemicalSaltGroupingClass_classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.ChemicalSaltGroupingClass_classifies, domain=ChemicalSaltGroupingClass, range=Optional[Union[str, ChemicalSaltId]])

slots.ChemicalSaltByCation_name = Slot(uri=RDFS.label, name="ChemicalSaltByCation_name", curie=RDFS.curie('label'),
                   model_uri=CHEMROF.ChemicalSaltByCation_name, domain=ChemicalSaltByCation, range=Optional[str])

slots.ChemicalSaltByAnion_name = Slot(uri=RDFS.label, name="ChemicalSaltByAnion_name", curie=RDFS.curie('label'),
                   model_uri=CHEMROF.ChemicalSaltByAnion_name, domain=ChemicalSaltByAnion, range=Optional[str])

slots.AcidAnionGroupingClass_name = Slot(uri=RDFS.label, name="AcidAnionGroupingClass_name", curie=RDFS.curie('label'),
                   model_uri=CHEMROF.AcidAnionGroupingClass_name, domain=AcidAnionGroupingClass, range=Optional[str],
                   pattern=re.compile(r'ate$'))

slots.AtomGroupingClass_subtype_of = Slot(uri=CHEMROF.subtype_of, name="AtomGroupingClass_subtype_of", curie=CHEMROF.curie('subtype_of'),
                   model_uri=CHEMROF.AtomGroupingClass_subtype_of, domain=AtomGroupingClass, range=Optional[Union[Union[str, MoleculeGroupingClassId], list[Union[str, MoleculeGroupingClassId]]]])

slots.AtomGroupingClass_classifies = Slot(uri=CHEMROF.classifies, name="AtomGroupingClass_classifies", curie=CHEMROF.curie('classifies'),
                   model_uri=CHEMROF.AtomGroupingClass_classifies, domain=AtomGroupingClass, range=Optional[Union[str, AtomId]])

slots.Material_has_part = Slot(uri=BFO['0000051'], name="Material_has_part", curie=BFO.curie('0000051'),
                   model_uri=CHEMROF.Material_has_part, domain=Material, range=Optional[Union[str, ChemicalEntityId]], mappings = [BFO["0000050"], SCHEMA["hasBioChemEntityPart"]])

slots.Nanomaterial_has_morphological_category = Slot(uri=CHEMROF.has_morphological_category, name="Nanomaterial_has_morphological_category", curie=CHEMROF.curie('has_morphological_category'),
                   model_uri=CHEMROF.Nanomaterial_has_morphological_category, domain=Nanomaterial, range=Optional[Union[str, "NanostructureMorphologyEnum"]])

slots.AnionState_elemental_charge = Slot(uri=CHEMROF.elemental_charge, name="AnionState_elemental_charge", curie=CHEMROF.curie('elemental_charge'),
                   model_uri=CHEMROF.AnionState_elemental_charge, domain=None, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.CationState_elemental_charge = Slot(uri=CHEMROF.elemental_charge, name="CationState_elemental_charge", curie=CHEMROF.curie('elemental_charge'),
                   model_uri=CHEMROF.CationState_elemental_charge, domain=None, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.Uncharged_elemental_charge = Slot(uri=CHEMROF.elemental_charge, name="Uncharged_elemental_charge", curie=CHEMROF.curie('elemental_charge'),
                   model_uri=CHEMROF.Uncharged_elemental_charge, domain=None, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.PolyatomicEntity_inchi_atom_connections_sublayer = Slot(uri=CHEMROF.inchi_atom_connections_sublayer, name="PolyatomicEntity_inchi_atom_connections_sublayer", curie=CHEMROF.curie('inchi_atom_connections_sublayer'),
                   model_uri=CHEMROF.PolyatomicEntity_inchi_atom_connections_sublayer, domain=PolyatomicEntity, range=Optional[str],
                   pattern=re.compile(r'^c.*'))

slots.Macromolecule_has_submolecules = Slot(uri=CHEMROF.has_submolecules, name="Macromolecule_has_submolecules", curie=CHEMROF.curie('has_submolecules'),
                   model_uri=CHEMROF.Macromolecule_has_submolecules, domain=Macromolecule, range=Optional[Union[Union[str, MoleculeId], list[Union[str, MoleculeId]]]])

slots.Copolymer_polymer_of = Slot(uri=CHEMROF.polymer_of, name="Copolymer_polymer_of", curie=CHEMROF.curie('polymer_of'),
                   model_uri=CHEMROF.Copolymer_polymer_of, domain=Copolymer, range=Optional[Union[Union[str, MacromoleculeId], list[Union[str, MacromoleculeId]]]])

slots.Homopolymer_polymer_of = Slot(uri=CHEMROF.polymer_of, name="Homopolymer_polymer_of", curie=CHEMROF.curie('polymer_of'),
                   model_uri=CHEMROF.Homopolymer_polymer_of, domain=Homopolymer, range=Optional[Union[str, MacromoleculeId]])

slots.Molecule_has_atom_occurrences = Slot(uri=CHEMROF.has_atom_occurrences, name="Molecule_has_atom_occurrences", curie=CHEMROF.curie('has_atom_occurrences'),
                   model_uri=CHEMROF.Molecule_has_atom_occurrences, domain=Molecule, range=Optional[Union[dict[Union[str, AtomOccurrenceName], Union[dict, "AtomOccurrence"]], list[Union[dict, "AtomOccurrence"]]]])

slots.Molecule_has_bonds = Slot(uri=CHEMROF.has_bonds, name="Molecule_has_bonds", curie=CHEMROF.curie('has_bonds'),
                   model_uri=CHEMROF.Molecule_has_bonds, domain=Molecule, range=Optional[Union[Union[dict, "AtomicBond"], list[Union[dict, "AtomicBond"]]]])

slots.Molecule_has_part = Slot(uri=BFO['0000051'], name="Molecule_has_part", curie=BFO.curie('0000051'),
                   model_uri=CHEMROF.Molecule_has_part, domain=Molecule, range=Optional[str], mappings = [BFO["0000050"], SCHEMA["hasBioChemEntityPart"]])

slots.AminoAcidSequenceInterval_has_sequence_representation = Slot(uri=CHEMROF.has_sequence_representation, name="AminoAcidSequenceInterval_has_sequence_representation", curie=CHEMROF.curie('has_sequence_representation'),
                   model_uri=CHEMROF.AminoAcidSequenceInterval_has_sequence_representation, domain=AminoAcidSequenceInterval, range=Optional[str])

slots.NucleotideSequenceInterval_has_sequence_representation = Slot(uri=CHEMROF.has_sequence_representation, name="NucleotideSequenceInterval_has_sequence_representation", curie=CHEMROF.curie('has_sequence_representation'),
                   model_uri=CHEMROF.NucleotideSequenceInterval_has_sequence_representation, domain=NucleotideSequenceInterval, range=Optional[str])

slots.FunctionalGroup_is_substitutent_group_from = Slot(uri=CHEMROF.is_substitutent_group_from, name="FunctionalGroup_is_substitutent_group_from", curie=CHEMROF.curie('is_substitutent_group_from'),
                   model_uri=CHEMROF.FunctionalGroup_is_substitutent_group_from, domain=FunctionalGroup, range=Optional[Union[str, MoleculeId]])

slots.MoleculeByChargeState_acidity = Slot(uri=CHEMROF.acidity, name="MoleculeByChargeState_acidity", curie=CHEMROF.curie('acidity'),
                   model_uri=CHEMROF.MoleculeByChargeState_acidity, domain=MoleculeByChargeState, range=Optional[float])

slots.MoleculeByChargeState_hard_or_soft = Slot(uri=CHEMROF.hard_or_soft, name="MoleculeByChargeState_hard_or_soft", curie=CHEMROF.curie('hard_or_soft'),
                   model_uri=CHEMROF.MoleculeByChargeState_hard_or_soft, domain=MoleculeByChargeState, range=Optional[Union[str, "HardOrSoftEnum"]])

slots.MoleculeByChargeState_acid_form_of = Slot(uri=CHEMROF.acid_form_of, name="MoleculeByChargeState_acid_form_of", curie=CHEMROF.curie('acid_form_of'),
                   model_uri=CHEMROF.MoleculeByChargeState_acid_form_of, domain=MoleculeByChargeState, range=Optional[Union[Union[str, MoleculeByChargeStateId], list[Union[str, MoleculeByChargeStateId]]]])

slots.Atom_has_part = Slot(uri=BFO['0000051'], name="Atom_has_part", curie=BFO.curie('0000051'),
                   model_uri=CHEMROF.Atom_has_part, domain=Atom, range=Optional[Union[str, SubatomicParticleId]], mappings = [BFO["0000050"], SCHEMA["hasBioChemEntityPart"]])

slots.ChemicalElement_symbol = Slot(uri=BO.symbol, name="ChemicalElement_symbol", curie=BO.curie('symbol'),
                   model_uri=CHEMROF.ChemicalElement_symbol, domain=ChemicalElement, range=Optional[str],
                   pattern=re.compile(r'^[A-Z][a-z]*'))

slots.ChemicalElement_in_periodic_table_group = Slot(uri=CHEMROF.in_periodic_table_group, name="ChemicalElement_in_periodic_table_group", curie=CHEMROF.curie('in_periodic_table_group'),
                   model_uri=CHEMROF.ChemicalElement_in_periodic_table_group, domain=ChemicalElement, range=Optional[int])

slots.ChemicalElement_in_periodic_table_block = Slot(uri=CHEMROF.in_periodic_table_block, name="ChemicalElement_in_periodic_table_block", curie=CHEMROF.curie('in_periodic_table_block'),
                   model_uri=CHEMROF.ChemicalElement_in_periodic_table_block, domain=ChemicalElement, range=Optional[Union[str, "PeriodicTableBlockEnum"]])

slots.ChemicalElement_boiling_point_in_celcius = Slot(uri=CHEMROF.boiling_point_in_celcius, name="ChemicalElement_boiling_point_in_celcius", curie=CHEMROF.curie('boiling_point_in_celcius'),
                   model_uri=CHEMROF.ChemicalElement_boiling_point_in_celcius, domain=ChemicalElement, range=Optional[float])

slots.ChemicalElement_melting_point_in_celcius = Slot(uri=CHEMROF.melting_point_in_celcius, name="ChemicalElement_melting_point_in_celcius", curie=CHEMROF.curie('melting_point_in_celcius'),
                   model_uri=CHEMROF.ChemicalElement_melting_point_in_celcius, domain=ChemicalElement, range=Optional[float])

slots.ChemicalElement_standard_atomic_weight = Slot(uri=CHEMROF.standard_atomic_weight, name="ChemicalElement_standard_atomic_weight", curie=CHEMROF.curie('standard_atomic_weight'),
                   model_uri=CHEMROF.ChemicalElement_standard_atomic_weight, domain=ChemicalElement, range=Optional[float])

slots.ChemicalElement_mass = Slot(uri=CHEMROF.mass, name="ChemicalElement_mass", curie=CHEMROF.curie('mass'),
                   model_uri=CHEMROF.ChemicalElement_mass, domain=ChemicalElement, range=Optional[float])

slots.ChemicalElement_monoisotopic_mass = Slot(uri=CHEMROF.monoisotopic_mass, name="ChemicalElement_monoisotopic_mass", curie=CHEMROF.curie('monoisotopic_mass'),
                   model_uri=CHEMROF.ChemicalElement_monoisotopic_mass, domain=ChemicalElement, range=Optional[float])

slots.ChemicalElement_electron_configuration = Slot(uri=CHEMROF.electron_configuration, name="ChemicalElement_electron_configuration", curie=CHEMROF.curie('electron_configuration'),
                   model_uri=CHEMROF.ChemicalElement_electron_configuration, domain=ChemicalElement, range=Optional[str])

slots.ChemicalElement_has_stereocenter = Slot(uri=CHEMROF.has_stereocenter, name="ChemicalElement_has_stereocenter", curie=CHEMROF.curie('has_stereocenter'),
                   model_uri=CHEMROF.ChemicalElement_has_stereocenter, domain=ChemicalElement, range=Optional[Union[Union[dict, "Stereocenter"], list[Union[dict, "Stereocenter"]]]])

slots.ChemicalElement_has_major_microspecies_at_pH7_3 = Slot(uri=CHEMROF.has_major_microspecies_at_pH7_3, name="ChemicalElement_has_major_microspecies_at_pH7_3", curie=CHEMROF.curie('has_major_microspecies_at_pH7_3'),
                   model_uri=CHEMROF.ChemicalElement_has_major_microspecies_at_pH7_3, domain=ChemicalElement, range=Optional[Union[str, ChemicalElementId]])

slots.AtomIonicForm_elemental_charge = Slot(uri=CHEMROF.elemental_charge, name="AtomIonicForm_elemental_charge", curie=CHEMROF.curie('elemental_charge'),
                   model_uri=CHEMROF.AtomIonicForm_elemental_charge, domain=AtomIonicForm, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.AtomAnion_elemental_charge = Slot(uri=CHEMROF.elemental_charge, name="AtomAnion_elemental_charge", curie=CHEMROF.curie('elemental_charge'),
                   model_uri=CHEMROF.AtomAnion_elemental_charge, domain=AtomAnion, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.AtomCation_elemental_charge = Slot(uri=CHEMROF.elemental_charge, name="AtomCation_elemental_charge", curie=CHEMROF.curie('elemental_charge'),
                   model_uri=CHEMROF.AtomCation_elemental_charge, domain=AtomCation, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.StandardInchiObject_inchi_version_string = Slot(uri=CHEMROF.inchi_version_string, name="StandardInchiObject_inchi_version_string", curie=CHEMROF.curie('inchi_version_string'),
                   model_uri=CHEMROF.StandardInchiObject_inchi_version_string, domain=StandardInchiObject, range=str,
                   pattern=re.compile(r'^1S$'))

slots.ChemicalSalt_elemental_charge = Slot(uri=CHEMROF.elemental_charge, name="ChemicalSalt_elemental_charge", curie=CHEMROF.curie('elemental_charge'),
                   model_uri=CHEMROF.ChemicalSalt_elemental_charge, domain=ChemicalSalt, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.ChemicalSalt_has_cationic_component = Slot(uri=CHEMROF.has_cationic_component, name="ChemicalSalt_has_cationic_component", curie=CHEMROF.curie('has_cationic_component'),
                   model_uri=CHEMROF.ChemicalSalt_has_cationic_component, domain=ChemicalSalt, range=Optional[Union[dict, CationState]])

slots.ChemicalSalt_has_anionic_component = Slot(uri=CHEMROF.has_anionic_component, name="ChemicalSalt_has_anionic_component", curie=CHEMROF.curie('has_anionic_component'),
                   model_uri=CHEMROF.ChemicalSalt_has_anionic_component, domain=ChemicalSalt, range=Optional[Union[dict, AnionState]])

slots.Ester_has_parent_alcohol = Slot(uri=CHEMROF.has_parent_alcohol, name="Ester_has_parent_alcohol", curie=CHEMROF.curie('has_parent_alcohol'),
                   model_uri=CHEMROF.Ester_has_parent_alcohol, domain=Ester, range=Optional[Union[str, ChemicalEntityId]])

slots.Ester_has_parent_acid = Slot(uri=CHEMROF.has_parent_acid, name="Ester_has_parent_acid", curie=CHEMROF.curie('has_parent_acid'),
                   model_uri=CHEMROF.Ester_has_parent_acid, domain=Ester, range=Optional[Union[str, MoleculeByChargeStateId]])

slots.Stereoisomer_isomeric_smiles_string = Slot(uri=CHEMROF.isomeric_smiles_string, name="Stereoisomer_isomeric_smiles_string", curie=CHEMROF.curie('isomeric_smiles_string'),
                   model_uri=CHEMROF.Stereoisomer_isomeric_smiles_string, domain=Stereoisomer, range=Optional[str])

slots.Enantiomer_relative_configuration = Slot(uri=CHEMROF.relative_configuration, name="Enantiomer_relative_configuration", curie=CHEMROF.curie('relative_configuration'),
                   model_uri=CHEMROF.Enantiomer_relative_configuration, domain=Enantiomer, range=Optional[str])

slots.Enantiomer_optical_configuration = Slot(uri=CHEMROF.optical_configuration, name="Enantiomer_optical_configuration", curie=CHEMROF.curie('optical_configuration'),
                   model_uri=CHEMROF.Enantiomer_optical_configuration, domain=Enantiomer, range=Optional[str])

slots.Enantiomer_absolute_configuration = Slot(uri=CHEMROF.absolute_configuration, name="Enantiomer_absolute_configuration", curie=CHEMROF.curie('absolute_configuration'),
                   model_uri=CHEMROF.Enantiomer_absolute_configuration, domain=Enantiomer, range=Optional[str])

slots.Enantiomer_enantiomer_form_of = Slot(uri=CHEMROF.enantiomer_form_of, name="Enantiomer_enantiomer_form_of", curie=CHEMROF.curie('enantiomer_form_of'),
                   model_uri=CHEMROF.Enantiomer_enantiomer_form_of, domain=Enantiomer, range=Optional[Union[str, MoleculeId]])

slots.Enantiomer_inchi_tetrahedral_stereochemical_sublayer = Slot(uri=CHEMROF.inchi_tetrahedral_stereochemical_sublayer, name="Enantiomer_inchi_tetrahedral_stereochemical_sublayer", curie=CHEMROF.curie('inchi_tetrahedral_stereochemical_sublayer'),
                   model_uri=CHEMROF.Enantiomer_inchi_tetrahedral_stereochemical_sublayer, domain=Enantiomer, range=str,
                   pattern=re.compile(r'^[tm].*'))

slots.Enantiomer_inchi_stereochemical_type_sublayer = Slot(uri=CHEMROF.inchi_stereochemical_type_sublayer, name="Enantiomer_inchi_stereochemical_type_sublayer", curie=CHEMROF.curie('inchi_stereochemical_type_sublayer'),
                   model_uri=CHEMROF.Enantiomer_inchi_stereochemical_type_sublayer, domain=Enantiomer, range=str,
                   pattern=re.compile(r'^s.*'))

slots.RacemicMixture_has_left_enantiomer = Slot(uri=CHEMROF.has_left_enantiomer, name="RacemicMixture_has_left_enantiomer", curie=CHEMROF.curie('has_left_enantiomer'),
                   model_uri=CHEMROF.RacemicMixture_has_left_enantiomer, domain=RacemicMixture, range=Union[str, EnantiomerId])

slots.RacemicMixture_has_right_enantiomer = Slot(uri=CHEMROF.has_right_enantiomer, name="RacemicMixture_has_right_enantiomer", curie=CHEMROF.curie('has_right_enantiomer'),
                   model_uri=CHEMROF.RacemicMixture_has_right_enantiomer, domain=RacemicMixture, range=Union[str, EnantiomerId])

slots.RacemicMixture_chirality_agnostic_form = Slot(uri=CHEMROF.chirality_agnostic_form, name="RacemicMixture_chirality_agnostic_form", curie=CHEMROF.curie('chirality_agnostic_form'),
                   model_uri=CHEMROF.RacemicMixture_chirality_agnostic_form, domain=RacemicMixture, range=Optional[Union[str, MoleculeId]])

slots.RacemicMixture_IUPAC_name = Slot(uri=CHEMROF.IUPAC_name, name="RacemicMixture_IUPAC_name", curie=CHEMROF.curie('IUPAC_name'),
                   model_uri=CHEMROF.RacemicMixture_IUPAC_name, domain=RacemicMixture, range=Optional[str],
                   pattern=re.compile(r'^rac-'))

slots.Allotrope_allotropic_analog_of = Slot(uri=CHEMROF.allotropic_analog_of, name="Allotrope_allotropic_analog_of", curie=CHEMROF.curie('allotropic_analog_of'),
                   model_uri=CHEMROF.Allotrope_allotropic_analog_of, domain=Allotrope, range=Union[str, ChemicalElementId])

slots.Allotrope_has_bonding_structure = Slot(uri=CHEMROF.has_bonding_structure, name="Allotrope_has_bonding_structure", curie=CHEMROF.curie('has_bonding_structure'),
                   model_uri=CHEMROF.Allotrope_has_bonding_structure, domain=Allotrope, range=str)

slots.PolymerRepeatUnit_repetition_of = Slot(uri=CHEMROF.repetition_of, name="PolymerRepeatUnit_repetition_of", curie=CHEMROF.curie('repetition_of'),
                   model_uri=CHEMROF.PolymerRepeatUnit_repetition_of, domain=PolymerRepeatUnit, range=Optional[Union[str, MoleculeId]])

slots.PolymerRepeatUnit_degree_of_polymerization = Slot(uri=CHEMROF.degree_of_polymerization, name="PolymerRepeatUnit_degree_of_polymerization", curie=CHEMROF.curie('degree_of_polymerization'),
                   model_uri=CHEMROF.PolymerRepeatUnit_degree_of_polymerization, domain=PolymerRepeatUnit, range=Optional[int])

slots.PolymerRepeatUnit_mass = Slot(uri=CHEMROF.mass, name="PolymerRepeatUnit_mass", curie=CHEMROF.curie('mass'),
                   model_uri=CHEMROF.PolymerRepeatUnit_mass, domain=PolymerRepeatUnit, range=Optional[float])

slots.Reaction_left_participants = Slot(uri=CHEMROF.left_participants, name="Reaction_left_participants", curie=CHEMROF.curie('left_participants'),
                   model_uri=CHEMROF.Reaction_left_participants, domain=Reaction, range=Optional[Union[Union[dict, "ReactionParticipant"], list[Union[dict, "ReactionParticipant"]]]])

slots.Reaction_right_participants = Slot(uri=CHEMROF.right_participants, name="Reaction_right_participants", curie=CHEMROF.curie('right_participants'),
                   model_uri=CHEMROF.Reaction_right_participants, domain=Reaction, range=Optional[Union[Union[dict, "ReactionParticipant"], list[Union[dict, "ReactionParticipant"]]]])

slots.Reaction_direction = Slot(uri=CHEMROF.direction, name="Reaction_direction", curie=CHEMROF.curie('direction'),
                   model_uri=CHEMROF.Reaction_direction, domain=Reaction, range=Optional[str])

slots.Reaction_is_diastereoselective = Slot(uri=CHEMROF.is_diastereoselective, name="Reaction_is_diastereoselective", curie=CHEMROF.curie('is_diastereoselective'),
                   model_uri=CHEMROF.Reaction_is_diastereoselective, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.Reaction_is_stereo = Slot(uri=CHEMROF.is_stereo, name="Reaction_is_stereo", curie=CHEMROF.curie('is_stereo'),
                   model_uri=CHEMROF.Reaction_is_stereo, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.Reaction_is_balanced = Slot(uri=CHEMROF.is_balanced, name="Reaction_is_balanced", curie=CHEMROF.curie('is_balanced'),
                   model_uri=CHEMROF.Reaction_is_balanced, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.Reaction_is_transport = Slot(uri=CHEMROF.is_transport, name="Reaction_is_transport", curie=CHEMROF.curie('is_transport'),
                   model_uri=CHEMROF.Reaction_is_transport, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.Reaction_is_fully_characterized = Slot(uri=CHEMROF.is_fully_characterized, name="Reaction_is_fully_characterized", curie=CHEMROF.curie('is_fully_characterized'),
                   model_uri=CHEMROF.Reaction_is_fully_characterized, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.Reaction_reaction_center = Slot(uri=CHEMROF.reaction_center, name="Reaction_reaction_center", curie=CHEMROF.curie('reaction_center'),
                   model_uri=CHEMROF.Reaction_reaction_center, domain=Reaction, range=Optional[str])

slots.Reaction_description = Slot(uri=CHEMROF.description, name="Reaction_description", curie=CHEMROF.curie('description'),
                   model_uri=CHEMROF.Reaction_description, domain=Reaction, range=Optional[str])

slots.ReactionParticipant_participant = Slot(uri=CHEMROF.participant, name="ReactionParticipant_participant", curie=CHEMROF.curie('participant'),
                   model_uri=CHEMROF.ReactionParticipant_participant, domain=ReactionParticipant, range=Optional[Union[str, ChemicalEntityId]])

slots.ReactionParticipant_stoichiometry = Slot(uri=CHEMROF.stoichiometry, name="ReactionParticipant_stoichiometry", curie=CHEMROF.curie('stoichiometry'),
                   model_uri=CHEMROF.ReactionParticipant_stoichiometry, domain=ReactionParticipant, range=Optional[int])

slots.ProportionalPart_has_role = Slot(uri=CHEMROF.has_role, name="ProportionalPart_has_role", curie=CHEMROF.curie('has_role'),
                   model_uri=CHEMROF.ProportionalPart_has_role, domain=ProportionalPart, range=Optional[Union[str, "IngredientRoleEnum"]])

slots.ProportionalPart_composed_of = Slot(uri=CHEMROF.composed_of, name="ProportionalPart_composed_of", curie=CHEMROF.curie('composed_of'),
                   model_uri=CHEMROF.ProportionalPart_composed_of, domain=ProportionalPart, range=Optional[Union[str, ChemicalEntityId]])

slots.ProportionalPart_minimal_percentage = Slot(uri=CHEMROF.minimal_percentage, name="ProportionalPart_minimal_percentage", curie=CHEMROF.curie('minimal_percentage'),
                   model_uri=CHEMROF.ProportionalPart_minimal_percentage, domain=ProportionalPart, range=Optional[float])

slots.ProportionalPart_maximum_percentage = Slot(uri=CHEMROF.maximum_percentage, name="ProportionalPart_maximum_percentage", curie=CHEMROF.curie('maximum_percentage'),
                   model_uri=CHEMROF.ProportionalPart_maximum_percentage, domain=ProportionalPart, range=Optional[float])

slots.MoleculePairwiseSimilarity_left_molecule = Slot(uri=CHEMROF.left_molecule, name="MoleculePairwiseSimilarity_left_molecule", curie=CHEMROF.curie('left_molecule'),
                   model_uri=CHEMROF.MoleculePairwiseSimilarity_left_molecule, domain=MoleculePairwiseSimilarity, range=Optional[Union[str, MoleculeId]])

slots.MoleculePairwiseSimilarity_right_molecule = Slot(uri=CHEMROF.right_molecule, name="MoleculePairwiseSimilarity_right_molecule", curie=CHEMROF.curie('right_molecule'),
                   model_uri=CHEMROF.MoleculePairwiseSimilarity_right_molecule, domain=MoleculePairwiseSimilarity, range=Optional[Union[str, MoleculeId]])

slots.MoleculePairwiseSimilarity_score = Slot(uri=CHEMROF.score, name="MoleculePairwiseSimilarity_score", curie=CHEMROF.curie('score'),
                   model_uri=CHEMROF.MoleculePairwiseSimilarity_score, domain=MoleculePairwiseSimilarity, range=Optional[float])

slots.TanimotoSimilarity_score = Slot(uri=CHEMROF.score, name="TanimotoSimilarity_score", curie=CHEMROF.curie('score'),
                   model_uri=CHEMROF.TanimotoSimilarity_score, domain=TanimotoSimilarity, range=Optional[float])
