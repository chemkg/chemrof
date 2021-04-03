# Auto generated from chem.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-02 17:32
# Schema: chemont
#
# id: chemont
# description: A data model describing metaclasses for chemical ontology classes
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from linkml.utils.metamodelcore import Bool
from linkml_model.types import Boolean, Float, Integer, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CHEMINF = CurieNamespace('CHEMINF', 'http://semanticscience.org/resource/CHEMINF_')
COB = CurieNamespace('COB', 'http://purl.obolibrary.org/obo/COB_')
DRUGBANK = CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/')
EC = CurieNamespace('EC', 'http://example.org/UNKNOWN/EC/')
GO = CurieNamespace('GO', 'http://identifiers.org/go/')
HMDB = CurieNamespace('HMDB', 'http://identifiers.org/hmdb/')
INCHI = CurieNamespace('INCHI', 'http://identifiers.org/inchi/')
INCHIKEY = CurieNamespace('INCHIKEY', 'http://identifiers.org/inchikey/')
KEGG = CurieNamespace('KEGG', 'http://identifiers.org/kegg/')
KEGG_GLYCAN = CurieNamespace('KEGG_GLYCAN', 'http://identifiers.org/kegg.glycan/')
KEGG_REACTION = CurieNamespace('KEGG_REACTION', 'http://identifiers.org/kegg.reaction/')
LANL_ELEMENT = CurieNamespace('LANL_ELEMENT', 'https://periodic.lanl.gov/')
MESH = CurieNamespace('MESH', 'http://identifiers.org/mesh/')
METACYC = CurieNamespace('MetaCyc', 'http://example.org/UNKNOWN/MetaCyc/')
METANETX = CurieNamespace('MetaNetX', 'http://example.org/UNKNOWN/MetaNetX/')
PR = CurieNamespace('PR', 'http://identifiers.org/pr/')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
PUBCHEM_ELEMENT = CurieNamespace('PUBCHEM_ELEMENT', 'https://pubchem.ncbi.nlm.nih.gov/element/')
REACT = CurieNamespace('REACT', 'http://example.org/UNKNOWN/REACT/')
RHEA = CurieNamespace('RHEA', 'http://identifiers.org/rhea/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RETRORULES = CurieNamespace('RetroRules', 'http://example.org/UNKNOWN/RetroRules/')
SEED = CurieNamespace('SEED', 'http://identifiers.org/seed/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
UNII = CurieNamespace('UNII', 'http://identifiers.org/unii/')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://example.org/UNKNOWN/UniProtKB/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
BIOPTOP = CurieNamespace('bioptop', 'http://purl.org/biotop/biotop.owl#')
CHEMONT = CurieNamespace('chemont', 'https://w3id.org/chemont/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EDAM = CurieNamespace('edam', 'http://identifiers.org/edam/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
WD = CurieNamespace('wd', 'http://www.wikidata.org/entity/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CHEMONT


# Types
class PeriodicTableGroup(int):
    type_class_uri = XSD.int
    type_class_curie = "xsd:int"
    type_name = "periodic table group"
    type_model_uri = CHEMONT.PeriodicTableGroup


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


class SequenceString(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "sequence string"
    type_model_uri = CHEMONT.SequenceString


class AminoAcidSequenceString(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "amino acid sequence string"
    type_model_uri = CHEMONT.AminoAcidSequenceString


class DNASequenceString(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "DNA sequence string"
    type_model_uri = CHEMONT.DNASequenceString


# Class references
class ChemicalEntityId(extended_str):
    pass


class SubatomicParticleId(ChemicalEntityId):
    pass


class NucleonId(SubatomicParticleId):
    pass


class NeutronId(NucleonId):
    pass


class ProtonId(NucleonId):
    pass


class ElectronId(SubatomicParticleId):
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


class PolyatomicIonId(MoleculeId):
    pass


class MolecularCationId(PolyatomicIonId):
    pass


class MolecularAnionId(PolyatomicIonId):
    pass


class UnchargedMoleculeId(MoleculeId):
    pass


class AtomId(ChemicalEntityId):
    pass


class ChemicalElementId(AtomId):
    pass


class IsotopeId(AtomId):
    pass


class NuclideId(AtomId):
    pass


class RadionuclideId(NuclideId):
    pass


class AtomIonicFormId(AtomId):
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


class BronstedAcidId(MoleculeId):
    pass


class AcidBaseId(MolecularAnionId):
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


@dataclass
class OwlClass(YAMLRoot):
    """
    instances of this class mixin are OWL Classes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "owl class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.OwlClass

    owl_subclass_of: Optional[Union[dict, "OwlClass"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**self.owl_subclass_of)

        super().__post_init__(**kwargs)


@dataclass
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

    subtype_of: Optional[Union[Union[dict, "GroupingClass"], List[Union[dict, "GroupingClass"]]]] = empty_list()
    classifies: Optional[Union[str, ChemicalEntityId]] = None
    owl_subclass_of: Optional[Union[dict, OwlClass]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype_of is None:
            self.subtype_of = []
        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of]
        self.subtype_of = [v if isinstance(v, GroupingClass) else GroupingClass(**v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, ChemicalEntityId):
            self.classifies = ChemicalEntityId(self.classifies)

        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**self.owl_subclass_of)

        super().__post_init__(**kwargs)


@dataclass
class MoleculeGroupingClass(GroupingClass):
    """
    A grouping class that classifies molecules. Example: carbohydrate, monosaccharide, amino acid, polyacrylamide
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MoleculeGroupingClass
    class_class_curie: ClassVar[str] = "chemont:MoleculeGroupingClass"
    class_name: ClassVar[str] = "molecule grouping class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MoleculeGroupingClass

    subtype_of: Optional[Union[Union[dict, "MoleculeGroupingClass"], List[Union[dict, "MoleculeGroupingClass"]]]] = empty_list()
    classifies: Optional[Union[str, MoleculeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype_of is None:
            self.subtype_of = []
        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of]
        self.subtype_of = [v if isinstance(v, MoleculeGroupingClass) else MoleculeGroupingClass(**v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, MoleculeId):
            self.classifies = MoleculeId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass
class MolecularComponentGroupingClass(GroupingClass):
    """
    A grouping class that classifies molecular components. Example: inorganic anion group
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularComponentGroupingClass
    class_class_curie: ClassVar[str] = "chemont:MolecularComponentGroupingClass"
    class_name: ClassVar[str] = "molecular component grouping class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularComponentGroupingClass

    subtype_of: Optional[Union[Union[dict, "MolecularComponentGroupingClass"], List[Union[dict, "MolecularComponentGroupingClass"]]]] = empty_list()
    classifies: Optional[Union[str, MolecularComponentId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype_of is None:
            self.subtype_of = []
        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of]
        self.subtype_of = [v if isinstance(v, MolecularComponentGroupingClass) else MolecularComponentGroupingClass(**v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, MolecularComponentId):
            self.classifies = MolecularComponentId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass
class MolecularDerivativeGroupingClass(MoleculeGroupingClass):
    """
    A grouping class defined as a derivative of another molecule or molecular grouping class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularDerivativeGroupingClass
    class_class_curie: ClassVar[str] = "chemont:MolecularDerivativeGroupingClass"
    class_name: ClassVar[str] = "molecular derivative grouping class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularDerivativeGroupingClass

    derivative_of: Optional[Union[str, ChemicalEntityId]] = None
    name: Optional[str] = None
    classifies: Optional[Union[str, MoleculeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.derivative_of is not None and not isinstance(self.derivative_of, ChemicalEntityId):
            self.derivative_of = ChemicalEntityId(self.derivative_of)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.classifies is not None and not isinstance(self.classifies, MoleculeId):
            self.classifies = MoleculeId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass
class MoleculeGroupingClassDefinedByComponents(MoleculeGroupingClass):
    """
    A grouping class defined as an exhaustive list of components
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MoleculeGroupingClassDefinedByComponents
    class_class_curie: ClassVar[str] = "chemont:MoleculeGroupingClassDefinedByComponents"
    class_name: ClassVar[str] = "molecule grouping class defined by components"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MoleculeGroupingClassDefinedByComponents

    has_part: Optional[Union[dict, "ChemicalEntityOrGrouping"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_part is not None and not isinstance(self.has_part, ChemicalEntityOrGrouping):
            self.has_part = ChemicalEntityOrGrouping()

        super().__post_init__(**kwargs)


@dataclass
class MoleculeGroupingClassDefinedByAdditionOfAGroup(MoleculeGroupingClass):
    """
    A grouping class defined in terms of a derivative of a molecule and the addition of a group
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MoleculeGroupingClassDefinedByAdditionOfAGroup
    class_class_curie: ClassVar[str] = "chemont:MoleculeGroupingClassDefinedByAdditionOfAGroup"
    class_name: ClassVar[str] = "molecule grouping class defined by addition of a group"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MoleculeGroupingClassDefinedByAdditionOfAGroup

    has_group: Optional[Union[Union[str, ChemicalGroupId], List[Union[str, ChemicalGroupId]]]] = empty_list()
    derivative_of: Optional[Union[str, PolyatomicEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_group is None:
            self.has_group = []
        if not isinstance(self.has_group, list):
            self.has_group = [self.has_group]
        self.has_group = [v if isinstance(v, ChemicalGroupId) else ChemicalGroupId(v) for v in self.has_group]

        if self.derivative_of is not None and not isinstance(self.derivative_of, PolyatomicEntityId):
            self.derivative_of = PolyatomicEntityId(self.derivative_of)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalSaltGroupingClass(MoleculeGroupingClass):
    """
    A grouping class for a chemical salt
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalSaltGroupingClass
    class_class_curie: ClassVar[str] = "chemont:ChemicalSaltGroupingClass"
    class_name: ClassVar[str] = "chemical salt grouping class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalSaltGroupingClass

    has_anionic_component: Optional[str] = None
    has_cationic_component: Optional[str] = None
    name: Optional[str] = None
    classifies: Optional[Union[str, ChemicalSaltId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_anionic_component is not None and not isinstance(self.has_anionic_component, str):
            self.has_anionic_component = str(self.has_anionic_component)

        if self.has_cationic_component is not None and not isinstance(self.has_cationic_component, str):
            self.has_cationic_component = str(self.has_cationic_component)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.classifies is not None and not isinstance(self.classifies, ChemicalSaltId):
            self.classifies = ChemicalSaltId(self.classifies)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalSaltByCation(ChemicalSaltGroupingClass):
    """
    A grouping class for a chemical salt named by cation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalSaltByCation
    class_class_curie: ClassVar[str] = "chemont:ChemicalSaltByCation"
    class_name: ClassVar[str] = "chemical salt by cation"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalSaltByCation

    has_cationic_component: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_cationic_component is not None and not isinstance(self.has_cationic_component, str):
            self.has_cationic_component = str(self.has_cationic_component)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalSaltByAnion(ChemicalSaltGroupingClass):
    """
    A grouping class for a chemical salt named by anion
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalSaltByAnion
    class_class_curie: ClassVar[str] = "chemont:ChemicalSaltByAnion"
    class_name: ClassVar[str] = "chemical salt by anion"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalSaltByAnion

    has_anionic_component: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_anionic_component is not None and not isinstance(self.has_anionic_component, str):
            self.has_anionic_component = str(self.has_anionic_component)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


class GeneralizedMolecularStructureClass(MoleculeGroupingClass):
    """
    A molecule grouping class that can be written using a chemical formula using variables (e.g. n), or arithmetic
    expressions uing variables (e.g. 2n+2), plus optionally constraints on those variables (e.g. n>3). An example is
    alkane; CnH2n+2, which groups specific molecules such as methane
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.GeneralizedMolecularStructureClass
    class_class_curie: ClassVar[str] = "chemont:GeneralizedMolecularStructureClass"
    class_name: ClassVar[str] = "generalized molecular structure class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.GeneralizedMolecularStructureClass


@dataclass
class GroupingClassForAcidsOrBases(MoleculeGroupingClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.GroupingClassForAcidsOrBases
    class_class_curie: ClassVar[str] = "chemont:GroupingClassForAcidsOrBases"
    class_name: ClassVar[str] = "grouping class for acids or bases"
    class_model_uri: ClassVar[URIRef] = CHEMONT.GroupingClassForAcidsOrBases

    conjugate_base_of: Optional[Union[str, ChemicalEntityId]] = None
    conjugate_acid_of: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.conjugate_base_of is not None and not isinstance(self.conjugate_base_of, ChemicalEntityId):
            self.conjugate_base_of = ChemicalEntityId(self.conjugate_base_of)

        if self.conjugate_acid_of is not None and not isinstance(self.conjugate_acid_of, ChemicalEntityId):
            self.conjugate_acid_of = ChemicalEntityId(self.conjugate_acid_of)

        super().__post_init__(**kwargs)


@dataclass
class AcidAnionGroupingClass(GroupingClassForAcidsOrBases):
    """
    A molecule grouping class that groups the different ion forms of the base of an acid
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AcidAnionGroupingClass
    class_class_curie: ClassVar[str] = "chemont:AcidAnionGroupingClass"
    class_name: ClassVar[str] = "acid anion grouping class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AcidAnionGroupingClass

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


class GeneralAcidBaseGroupingClass(GroupingClassForAcidsOrBases):
    """
    A molecule grouping class that can groups an acid together with all its conjugate bases. physiological
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.GeneralAcidBaseGroupingClass
    class_class_curie: ClassVar[str] = "chemont:GeneralAcidBaseGroupingClass"
    class_name: ClassVar[str] = "general acid base grouping class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.GeneralAcidBaseGroupingClass


@dataclass
class AcidBaseConflationClass(GroupingClassForAcidsOrBases):
    """
    A molecule grouping class that can groups an acid together with all its conjugate bases. physiological
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AcidBaseConflationClass
    class_class_curie: ClassVar[str] = "chemont:AcidBaseConflationClass"
    class_name: ClassVar[str] = "acid base conflation class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AcidBaseConflationClass

    has_physiological_base: Optional[Union[str, AcidBaseId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_physiological_base is not None and not isinstance(self.has_physiological_base, AcidBaseId):
            self.has_physiological_base = AcidBaseId(self.has_physiological_base)

        super().__post_init__(**kwargs)


@dataclass
class AtomGroupingClass(GroupingClass):
    """
    A grouping class that classifies atoms. For example, metal atom
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingClass
    class_class_curie: ClassVar[str] = "chemont:AtomGroupingClass"
    class_name: ClassVar[str] = "atom grouping class"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingClass

    subtype_of: Optional[Union[Union[dict, MoleculeGroupingClass], List[Union[dict, MoleculeGroupingClass]]]] = empty_list()
    classifies: Optional[Union[str, AtomId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype_of is None:
            self.subtype_of = []
        if not isinstance(self.subtype_of, list):
            self.subtype_of = [self.subtype_of]
        self.subtype_of = [v if isinstance(v, MoleculeGroupingClass) else MoleculeGroupingClass(**v) for v in self.subtype_of]

        if self.classifies is not None and not isinstance(self.classifies, AtomId):
            self.classifies = AtomId(self.classifies)

        super().__post_init__(**kwargs)


class AtomGroupingByPeriodicTablePlacement(AtomGroupingClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingByPeriodicTablePlacement
    class_class_curie: ClassVar[str] = "chemont:AtomGroupingByPeriodicTablePlacement"
    class_name: ClassVar[str] = "atom grouping by periodic table placement"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingByPeriodicTablePlacement


@dataclass
class AtomGroupingByPeriodicTableGroup(AtomGroupingByPeriodicTablePlacement):
    """
    Example: p-block atom
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingByPeriodicTableGroup
    class_class_curie: ClassVar[str] = "chemont:AtomGroupingByPeriodicTableGroup"
    class_name: ClassVar[str] = "atom grouping by periodic table group"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingByPeriodicTableGroup

    in_periodic_table_group: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.in_periodic_table_group is not None and not isinstance(self.in_periodic_table_group, int):
            self.in_periodic_table_group = int(self.in_periodic_table_group)

        super().__post_init__(**kwargs)


@dataclass
class AtomGroupingByPeriodicTableBlock(AtomGroupingByPeriodicTablePlacement):
    """
    Example: group 13 atom
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingByPeriodicTableBlock
    class_class_curie: ClassVar[str] = "chemont:AtomGroupingByPeriodicTableBlock"
    class_name: ClassVar[str] = "atom grouping by periodic table block"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingByPeriodicTableBlock

    in_periodic_table_block: Optional[Union[dict, "PeriodicTableBlock"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.in_periodic_table_block is not None and not isinstance(self.in_periodic_table_block, PeriodicTableBlock):
            self.in_periodic_table_block = PeriodicTableBlock(**self.in_periodic_table_block)

        super().__post_init__(**kwargs)


class AtomGroupingByProperty(AtomGroupingClass):
    """
    Example: metal atom
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingByProperty
    class_class_curie: ClassVar[str] = "chemont:AtomGroupingByProperty"
    class_name: ClassVar[str] = "atom grouping by property"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomGroupingByProperty


@dataclass
class Material(YAMLRoot):
    """
    A substance composed of one or more chemical entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Material
    class_class_curie: ClassVar[str] = "chemont:Material"
    class_name: ClassVar[str] = "material"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Material

    has_part: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_part is not None and not isinstance(self.has_part, ChemicalEntityId):
            self.has_part = ChemicalEntityId(self.has_part)

        super().__post_init__(**kwargs)


@dataclass
class Nanostructure(Material):
    """
    A nanostructure is a structure of intermediate size between microscopic and molecular structures. Nanostructural
    detail is microstructure at nanoscale.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Nanostructure
    class_class_curie: ClassVar[str] = "chemont:Nanostructure"
    class_name: ClassVar[str] = "nanostructure"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Nanostructure

    has_morphological_category: Optional[Union[str, "NanostructureMorphologyEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_morphological_category is not None and not isinstance(self.has_morphological_category, NanostructureMorphologyEnum):
            self.has_morphological_category = NanostructureMorphologyEnum(self.has_morphological_category)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntity(YAMLRoot):
    """
    An entity that can be described using using chemical properties.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalEntity
    class_class_curie: ClassVar[str] = "chemont:ChemicalEntity"
    class_name: ClassVar[str] = "chemical entity"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    name: Optional[str] = None
    is_radical: Optional[Union[bool, Bool]] = None
    has_standard_inchi_object: Optional[Union[dict, "StandardInchiObject"]] = None
    has_characteristic: Optional[Union[dict, "ChemicalCharacteristic"]] = None
    owl_subclass_of: Optional[Union[dict, OwlClass]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.is_radical is not None and not isinstance(self.is_radical, Bool):
            self.is_radical = Bool(self.is_radical)

        if self.has_standard_inchi_object is not None and not isinstance(self.has_standard_inchi_object, StandardInchiObject):
            self.has_standard_inchi_object = StandardInchiObject(**self.has_standard_inchi_object)

        if self.has_characteristic is not None and not isinstance(self.has_characteristic, ChemicalCharacteristic):
            self.has_characteristic = ChemicalCharacteristic()

        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**self.owl_subclass_of)

        super().__post_init__(**kwargs)


@dataclass
class SubatomicParticle(ChemicalEntity):
    """
    A chemical entity below the granularity of an atom.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.SubatomicParticle
    class_class_curie: ClassVar[str] = "chemont:SubatomicParticle"
    class_name: ClassVar[str] = "subatomic particle"
    class_model_uri: ClassVar[URIRef] = CHEMONT.SubatomicParticle

    id: Union[str, SubatomicParticleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SubatomicParticleId):
            self.id = SubatomicParticleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Nucleon(SubatomicParticle):
    """
    A neutron or proton
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Nucleon
    class_class_curie: ClassVar[str] = "chemont:Nucleon"
    class_name: ClassVar[str] = "nucleon"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Nucleon

    id: Union[str, NucleonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NucleonId):
            self.id = NucleonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Neutron(Nucleon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Neutron
    class_class_curie: ClassVar[str] = "chemont:Neutron"
    class_name: ClassVar[str] = "neutron"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Neutron

    id: Union[str, NeutronId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NeutronId):
            self.id = NeutronId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Proton(Nucleon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Proton
    class_class_curie: ClassVar[str] = "chemont:Proton"
    class_name: ClassVar[str] = "proton"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Proton

    id: Union[str, ProtonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProtonId):
            self.id = ProtonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Electron(SubatomicParticle):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Electron
    class_class_curie: ClassVar[str] = "chemont:Electron"
    class_name: ClassVar[str] = "electron"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Electron

    id: Union[str, ElectronId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ElectronId):
            self.id = ElectronId(self.id)

        super().__post_init__(**kwargs)


class ChemicalEntityOrGrouping(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalEntityOrGrouping
    class_class_curie: ClassVar[str] = "chemont:ChemicalEntityOrGrouping"
    class_name: ClassVar[str] = "chemical entity or grouping"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalEntityOrGrouping


class IsPartOrWhole(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.IsPartOrWhole
    class_class_curie: ClassVar[str] = "chemont:IsPartOrWhole"
    class_name: ClassVar[str] = "is part or whole"
    class_model_uri: ClassVar[URIRef] = CHEMONT.IsPartOrWhole


class IsPart(IsPartOrWhole):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.IsPart
    class_class_curie: ClassVar[str] = "chemont:IsPart"
    class_name: ClassVar[str] = "is part"
    class_model_uri: ClassVar[URIRef] = CHEMONT.IsPart


class IsWhole(IsPartOrWhole):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.IsWhole
    class_class_curie: ClassVar[str] = "chemont:IsWhole"
    class_name: ClassVar[str] = "is whole"
    class_model_uri: ClassVar[URIRef] = CHEMONT.IsWhole


class Connectivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Connectivity
    class_class_curie: ClassVar[str] = "chemont:Connectivity"
    class_name: ClassVar[str] = "connectivity"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Connectivity


class FullyCovalentlyBonded(Connectivity):
    """
    All pairs of atoms in this entity are transitively connected via covalent bonds
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.FullyCovalentlyBonded
    class_class_curie: ClassVar[str] = "chemont:FullyCovalentlyBonded"
    class_name: ClassVar[str] = "fully covalently bonded"
    class_model_uri: ClassVar[URIRef] = CHEMONT.FullyCovalentlyBonded


class WeaklyBonded(Connectivity):
    """
    Not covalently bonded
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.WeaklyBonded
    class_class_curie: ClassVar[str] = "chemont:WeaklyBonded"
    class_name: ClassVar[str] = "weakly bonded"
    class_model_uri: ClassVar[URIRef] = CHEMONT.WeaklyBonded


class State(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.State
    class_class_curie: ClassVar[str] = "chemont:State"
    class_name: ClassVar[str] = "state"
    class_model_uri: ClassVar[URIRef] = CHEMONT.State


@dataclass
class ChargeState(State):
    """
    Applies to entities that have a charge state, which may be positive, negative, or neutral
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChargeState
    class_class_curie: ClassVar[str] = "chemont:ChargeState"
    class_name: ClassVar[str] = "charge state"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChargeState

    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


@dataclass
class Uncharged(ChargeState):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Uncharged
    class_class_curie: ClassVar[str] = "chemont:Uncharged"
    class_name: ClassVar[str] = "uncharged"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Uncharged

    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


class Charged(ChargeState):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Charged
    class_class_curie: ClassVar[str] = "chemont:Charged"
    class_name: ClassVar[str] = "charged"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Charged


@dataclass
class AnionState(Charged):
    """
    This mixin is applied on an entity (atom or molecule) that is negatively charged
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AnionState
    class_class_curie: ClassVar[str] = "chemont:AnionState"
    class_name: ClassVar[str] = "anion state"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AnionState

    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


@dataclass
class CationState(Charged):
    """
    This mixin is applied on an entity (atom or molecule) that is positively charged
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.CationState
    class_class_curie: ClassVar[str] = "chemont:CationState"
    class_name: ClassVar[str] = "cation state"
    class_model_uri: ClassVar[URIRef] = CHEMONT.CationState

    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


@dataclass
class PolyatomicEntity(ChemicalEntity):
    """
    Any chemical entity consisting of more than one atom.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.PolyatomicEntity
    class_class_curie: ClassVar[str] = "chemont:PolyatomicEntity"
    class_name: ClassVar[str] = "polyatomic entity"
    class_model_uri: ClassVar[URIRef] = CHEMONT.PolyatomicEntity

    id: Union[str, PolyatomicEntityId] = None

@dataclass
class MolecularComponent(PolyatomicEntity):
    """
    A proper part of a molecule that is larger than an atom
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularComponent
    class_class_curie: ClassVar[str] = "chemont:MolecularComponent"
    class_name: ClassVar[str] = "molecular component"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularComponent

    id: Union[str, MolecularComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MolecularComponentId):
            self.id = MolecularComponentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PolymerPart(MolecularComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.PolymerPart
    class_class_curie: ClassVar[str] = "chemont:PolymerPart"
    class_name: ClassVar[str] = "polymer part"
    class_model_uri: ClassVar[URIRef] = CHEMONT.PolymerPart

    id: Union[str, PolymerPartId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PolymerPartId):
            self.id = PolymerPartId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Monomer(PolymerPart):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Monomer
    class_class_curie: ClassVar[str] = "chemont:Monomer"
    class_name: ClassVar[str] = "monomer"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Monomer

    id: Union[str, MonomerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MonomerId):
            self.id = MonomerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MolecularSubsequence(PolymerPart):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularSubsequence
    class_class_curie: ClassVar[str] = "chemont:MolecularSubsequence"
    class_name: ClassVar[str] = "molecular subsequence"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularSubsequence

    id: Union[str, MolecularSubsequenceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MolecularSubsequenceId):
            self.id = MolecularSubsequenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalGroup(MolecularComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalGroup
    class_class_curie: ClassVar[str] = "chemont:ChemicalGroup"
    class_name: ClassVar[str] = "chemical group"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalGroup

    id: Union[str, ChemicalGroupId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalGroupId):
            self.id = ChemicalGroupId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalMixture(PolyatomicEntity):
    """
    A polyatomic entity that consists of two or more parts that are weakly bound, may be of known or unknown
    stoichiometry
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalMixture
    class_class_curie: ClassVar[str] = "chemont:ChemicalMixture"
    class_name: ClassVar[str] = "chemical mixture"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalMixture

    id: Union[str, ChemicalMixtureId] = None

@dataclass
class PreciseChemicalMixture(ChemicalMixture):
    """
    A polyatomic entity that consists of two or more parts that are weakly bound, and of known stoichiometry
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.PreciseChemicalMixture
    class_class_curie: ClassVar[str] = "chemont:PreciseChemicalMixture"
    class_name: ClassVar[str] = "precise chemical mixture"
    class_model_uri: ClassVar[URIRef] = CHEMONT.PreciseChemicalMixture

    id: Union[str, PreciseChemicalMixtureId] = None

@dataclass
class MolecularComplex(PreciseChemicalMixture):
    """
    A molecular complex is a chemical complex composed of at least one weakly interacting molecule.[SIO] Examples:
    chromosome, double-standed DNA, protein-containing macromolecular complex
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularComplex
    class_class_curie: ClassVar[str] = "chemont:MolecularComplex"
    class_name: ClassVar[str] = "molecular complex"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularComplex

    id: Union[str, MolecularComplexId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MolecularComplexId):
            self.id = MolecularComplexId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SupramolecularPolymer(MolecularComplex):
    """
    polymeric arrays of monomeric units that are connected by reversible and highly directional secondary
    interactions–that is, non-covalent bonds
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.SupramolecularPolymer
    class_class_curie: ClassVar[str] = "chemont:SupramolecularPolymer"
    class_name: ClassVar[str] = "supramolecular polymer"
    class_model_uri: ClassVar[URIRef] = CHEMONT.SupramolecularPolymer

    id: Union[str, SupramolecularPolymerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SupramolecularPolymerId):
            self.id = SupramolecularPolymerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ImpreciseChemicalMixture(ChemicalMixture):
    """
    A macroscopic polyatomic entity that consists of multiple chemical entities where the stoichiometry is not
    specified and the spatial arrangement of the ingredients is not defined. Examples include coal, tea tree oil,
    toothpaste
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ImpreciseChemicalMixture
    class_class_curie: ClassVar[str] = "chemont:ImpreciseChemicalMixture"
    class_name: ClassVar[str] = "imprecise chemical mixture"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ImpreciseChemicalMixture

    id: Union[str, ImpreciseChemicalMixtureId] = None
    has_proportional_parts: Optional[Union[Union[dict, "ProportionalPart"], List[Union[dict, "ProportionalPart"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ImpreciseChemicalMixtureId):
            self.id = ImpreciseChemicalMixtureId(self.id)

        if self.has_proportional_parts is None:
            self.has_proportional_parts = []
        if not isinstance(self.has_proportional_parts, list):
            self.has_proportional_parts = [self.has_proportional_parts]
        self.has_proportional_parts = [v if isinstance(v, ProportionalPart) else ProportionalPart(**v) for v in self.has_proportional_parts]

        super().__post_init__(**kwargs)


@dataclass
class Molecule(PolyatomicEntity):
    """
    A chemical entity that consists of two or more atoms where all atoms are connected via covalent bonds.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Molecule
    class_class_curie: ClassVar[str] = "chemont:Molecule"
    class_name: ClassVar[str] = "molecule"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Molecule

    id: Union[str, MoleculeId] = None
    has_atom_occurrences: Optional[Union[Union[dict, "AtomOccurrence"], List[Union[dict, "AtomOccurrence"]]]] = empty_list()
    has_bonds: Optional[Union[Union[dict, "AtomicBond"], List[Union[dict, "AtomicBond"]]]] = empty_list()
    has_submolecules: Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]] = empty_list()
    has_atoms: Optional[Union[Union[str, AtomId], List[Union[str, AtomId]]]] = empty_list()
    is_organic: Optional[Union[bool, Bool]] = None
    has_part: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_atom_occurrences is None:
            self.has_atom_occurrences = []
        if not isinstance(self.has_atom_occurrences, list):
            self.has_atom_occurrences = [self.has_atom_occurrences]
        self._normalize_inlined_slot(slot_name="has_atom_occurrences", slot_type=AtomOccurrence, key_name="occurrence of", inlined_as_list=True, keyed=False)

        if self.has_bonds is None:
            self.has_bonds = []
        if not isinstance(self.has_bonds, list):
            self.has_bonds = [self.has_bonds]
        self.has_bonds = [v if isinstance(v, AtomicBond) else AtomicBond(**v) for v in self.has_bonds]

        if self.has_submolecules is None:
            self.has_submolecules = []
        if not isinstance(self.has_submolecules, list):
            self.has_submolecules = [self.has_submolecules]
        self.has_submolecules = [v if isinstance(v, MoleculeId) else MoleculeId(v) for v in self.has_submolecules]

        if self.has_atoms is None:
            self.has_atoms = []
        if not isinstance(self.has_atoms, list):
            self.has_atoms = [self.has_atoms]
        self.has_atoms = [v if isinstance(v, AtomId) else AtomId(v) for v in self.has_atoms]

        if self.is_organic is not None and not isinstance(self.is_organic, Bool):
            self.is_organic = Bool(self.is_organic)

        if self.has_part is not None and not isinstance(self.has_part, str):
            self.has_part = str(self.has_part)

        super().__post_init__(**kwargs)


@dataclass
class SmallMolecule(Molecule):
    """
    A molecule characterized by availability in small-molecule databases
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.SmallMolecule
    class_class_curie: ClassVar[str] = "chemont:SmallMolecule"
    class_name: ClassVar[str] = "small molecule"
    class_model_uri: ClassVar[URIRef] = CHEMONT.SmallMolecule

    id: Union[str, SmallMoleculeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SmallMoleculeId):
            self.id = SmallMoleculeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Macromolecule(Molecule):
    """
    A large molecule, such as a polymer, lipid, or macrocycle
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Macromolecule
    class_class_curie: ClassVar[str] = "chemont:Macromolecule"
    class_name: ClassVar[str] = "macromolecule"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Macromolecule

    id: Union[str, MacromoleculeId] = None
    has_submolecules: Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacromoleculeId):
            self.id = MacromoleculeId(self.id)

        if self.has_submolecules is None:
            self.has_submolecules = []
        if not isinstance(self.has_submolecules, list):
            self.has_submolecules = [self.has_submolecules]
        self.has_submolecules = [v if isinstance(v, MoleculeId) else MoleculeId(v) for v in self.has_submolecules]

        super().__post_init__(**kwargs)


@dataclass
class Peptide(Macromolecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Peptide
    class_class_curie: ClassVar[str] = "chemont:Peptide"
    class_name: ClassVar[str] = "peptide"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Peptide

    id: Union[str, PeptideId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PeptideId):
            self.id = PeptideId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Protein(Macromolecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Protein
    class_class_curie: ClassVar[str] = "chemont:Protein"
    class_name: ClassVar[str] = "protein"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Protein

    id: Union[str, ProteinId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Glycan(Macromolecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Glycan
    class_class_curie: ClassVar[str] = "chemont:Glycan"
    class_name: ClassVar[str] = "glycan"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Glycan

    id: Union[str, GlycanId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GlycanId):
            self.id = GlycanId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MonomolecularPolymer(Macromolecule):
    """
    A macromolecule composed of repeating subunits. Examples: cellulose
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MonomolecularPolymer
    class_class_curie: ClassVar[str] = "chemont:MonomolecularPolymer"
    class_name: ClassVar[str] = "monomolecular polymer"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MonomolecularPolymer

    id: Union[str, MonomolecularPolymerId] = None
    polymer_of: Optional[Union[str, MacromoleculeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MonomolecularPolymerId):
            self.id = MonomolecularPolymerId(self.id)

        if self.polymer_of is not None and not isinstance(self.polymer_of, MacromoleculeId):
            self.polymer_of = MacromoleculeId(self.polymer_of)

        super().__post_init__(**kwargs)


@dataclass
class Copolymer(MonomolecularPolymer):
    """
    a polymer derived from more than one species of monomer
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Copolymer
    class_class_curie: ClassVar[str] = "chemont:Copolymer"
    class_name: ClassVar[str] = "copolymer"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Copolymer

    id: Union[str, CopolymerId] = None
    has_part: Optional[Union[Union[str, MacromoleculeId], List[Union[str, MacromoleculeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CopolymerId):
            self.id = CopolymerId(self.id)

        if self.has_part is None:
            self.has_part = []
        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part]
        self.has_part = [v if isinstance(v, MacromoleculeId) else MacromoleculeId(v) for v in self.has_part]

        super().__post_init__(**kwargs)


@dataclass
class NaturalProduct(Molecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.NaturalProduct
    class_class_curie: ClassVar[str] = "chemont:NaturalProduct"
    class_name: ClassVar[str] = "natural product"
    class_model_uri: ClassVar[URIRef] = CHEMONT.NaturalProduct

    id: Union[str, NaturalProductId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NaturalProductId):
            self.id = NaturalProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Moiety(MolecularComponent):
    """
    a named part of a molecule. In some instances moieties may be composed of yet smaller moieties and functional
    groups
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Moiety
    class_class_curie: ClassVar[str] = "chemont:Moiety"
    class_name: ClassVar[str] = "moiety"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Moiety

    id: Union[str, MoietyId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MoietyId):
            self.id = MoietyId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SequenceInterval(MolecularComponent):
    """
    a chain of connected monomers in a linear polymer - for example, a sub-region of an amino acid or nucleotide
    sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.SequenceInterval
    class_class_curie: ClassVar[str] = "chemont:SequenceInterval"
    class_name: ClassVar[str] = "sequence interval"
    class_model_uri: ClassVar[URIRef] = CHEMONT.SequenceInterval

    id: Union[str, SequenceIntervalId] = None
    has_sequence_representation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_sequence_representation is not None and not isinstance(self.has_sequence_representation, str):
            self.has_sequence_representation = str(self.has_sequence_representation)

        super().__post_init__(**kwargs)


@dataclass
class AminoAcidSequenceInterval(SequenceInterval):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AminoAcidSequenceInterval
    class_class_curie: ClassVar[str] = "chemont:AminoAcidSequenceInterval"
    class_name: ClassVar[str] = "amino acid sequence interval"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AminoAcidSequenceInterval

    id: Union[str, AminoAcidSequenceIntervalId] = None
    has_sequence_representation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AminoAcidSequenceIntervalId):
            self.id = AminoAcidSequenceIntervalId(self.id)

        if self.has_sequence_representation is not None and not isinstance(self.has_sequence_representation, str):
            self.has_sequence_representation = str(self.has_sequence_representation)

        super().__post_init__(**kwargs)


@dataclass
class NucleotideSequenceInterval(SequenceInterval):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.NucleotideSequenceInterval
    class_class_curie: ClassVar[str] = "chemont:NucleotideSequenceInterval"
    class_name: ClassVar[str] = "nucleotide sequence interval"
    class_model_uri: ClassVar[URIRef] = CHEMONT.NucleotideSequenceInterval

    id: Union[str, NucleotideSequenceIntervalId] = None
    has_sequence_representation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NucleotideSequenceIntervalId):
            self.id = NucleotideSequenceIntervalId(self.id)

        if self.has_sequence_representation is not None and not isinstance(self.has_sequence_representation, str):
            self.has_sequence_representation = str(self.has_sequence_representation)

        super().__post_init__(**kwargs)


@dataclass
class DNASequenceInterval(NucleotideSequenceInterval):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.DNASequenceInterval
    class_class_curie: ClassVar[str] = "chemont:DNASequenceInterval"
    class_name: ClassVar[str] = "DNA sequence interval"
    class_model_uri: ClassVar[URIRef] = CHEMONT.DNASequenceInterval

    id: Union[str, DNASequenceIntervalId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DNASequenceIntervalId):
            self.id = DNASequenceIntervalId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RNASequenceInterval(NucleotideSequenceInterval):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.RNASequenceInterval
    class_class_curie: ClassVar[str] = "chemont:RNASequenceInterval"
    class_name: ClassVar[str] = "RNA sequence interval"
    class_model_uri: ClassVar[URIRef] = CHEMONT.RNASequenceInterval

    id: Union[str, RNASequenceIntervalId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RNASequenceIntervalId):
            self.id = RNASequenceIntervalId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FunctionalGroup(MolecularComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.FunctionalGroup
    class_class_curie: ClassVar[str] = "chemont:FunctionalGroup"
    class_name: ClassVar[str] = "functional group"
    class_model_uri: ClassVar[URIRef] = CHEMONT.FunctionalGroup

    id: Union[str, FunctionalGroupId] = None
    is_substitutent_group_from: Optional[Union[str, MoleculeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FunctionalGroupId):
            self.id = FunctionalGroupId(self.id)

        if self.is_substitutent_group_from is not None and not isinstance(self.is_substitutent_group_from, MoleculeId):
            self.is_substitutent_group_from = MoleculeId(self.is_substitutent_group_from)

        super().__post_init__(**kwargs)


@dataclass
class MolecularSpecies(Molecule):
    """
    A molecule in which the units are identical. Example: methyl
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularSpecies
    class_class_curie: ClassVar[str] = "chemont:MolecularSpecies"
    class_name: ClassVar[str] = "molecular species"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularSpecies

    id: Union[str, MolecularSpeciesId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MolecularSpeciesId):
            self.id = MolecularSpeciesId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NonSpeciesMolecule(Molecule):
    """
    A molecule in which the units are not identical. TODO: move this higher
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.NonSpeciesMolecule
    class_class_curie: ClassVar[str] = "chemont:NonSpeciesMolecule"
    class_name: ClassVar[str] = "non species molecule"
    class_model_uri: ClassVar[URIRef] = CHEMONT.NonSpeciesMolecule

    id: Union[str, NonSpeciesMoleculeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NonSpeciesMoleculeId):
            self.id = NonSpeciesMoleculeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PolyatomicIon(Molecule):
    """
    A molecule that has a charge. For example, nitrate is a molecular and ionic species; its formula is (NO3-).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.PolyatomicIon
    class_class_curie: ClassVar[str] = "chemont:PolyatomicIon"
    class_name: ClassVar[str] = "polyatomic ion"
    class_model_uri: ClassVar[URIRef] = CHEMONT.PolyatomicIon

    id: Union[str, PolyatomicIonId] = None
    conjugate_base_of: Optional[Union[str, ChemicalEntityId]] = None
    conjugate_acid_of: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PolyatomicIonId):
            self.id = PolyatomicIonId(self.id)

        if self.conjugate_base_of is not None and not isinstance(self.conjugate_base_of, ChemicalEntityId):
            self.conjugate_base_of = ChemicalEntityId(self.conjugate_base_of)

        if self.conjugate_acid_of is not None and not isinstance(self.conjugate_acid_of, ChemicalEntityId):
            self.conjugate_acid_of = ChemicalEntityId(self.conjugate_acid_of)

        super().__post_init__(**kwargs)


@dataclass
class MolecularCation(PolyatomicIon):
    """
    A polyatomic ion that is positive
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularCation
    class_class_curie: ClassVar[str] = "chemont:MolecularCation"
    class_name: ClassVar[str] = "molecular cation"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularCation

    id: Union[str, MolecularCationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MolecularCationId):
            self.id = MolecularCationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MolecularAnion(PolyatomicIon):
    """
    A polyatomic ion that is negative
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MolecularAnion
    class_class_curie: ClassVar[str] = "chemont:MolecularAnion"
    class_name: ClassVar[str] = "molecular anion"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MolecularAnion

    id: Union[str, MolecularAnionId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MolecularAnionId):
            self.id = MolecularAnionId(self.id)

        super().__post_init__(**kwargs)


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

    id: Union[str, UnchargedMoleculeId] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, UnchargedMoleculeId):
            self.id = UnchargedMoleculeId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


@dataclass
class Atom(ChemicalEntity):
    """
    A chemical entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Atom
    class_class_curie: ClassVar[str] = "chemont:Atom"
    class_name: ClassVar[str] = "atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Atom

    id: Union[str, AtomId] = None
    atomic_number: Optional[int] = None
    symbol: Optional[str] = None
    name: Optional[str] = None
    has_part: Optional[Union[str, SubatomicParticleId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.atomic_number is not None and not isinstance(self.atomic_number, int):
            self.atomic_number = int(self.atomic_number)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.has_part is not None and not isinstance(self.has_part, SubatomicParticleId):
            self.has_part = SubatomicParticleId(self.has_part)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalElement(Atom):
    """
    generic form of an atom, with unspecified neutron or charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalElement
    class_class_curie: ClassVar[str] = "chemont:ChemicalElement"
    class_name: ClassVar[str] = "chemical element"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalElement

    id: Union[str, ChemicalElementId] = None
    symbol: Optional[str] = None
    in_periodic_table_group: Optional[int] = None
    in_periodic_table_block: Optional[Union[dict, "PeriodicTableBlock"]] = None
    boiling_point_in_celcius: Optional[float] = None
    melting_point_in_celcius: Optional[float] = None
    standard_atomic_weight: Optional[float] = None
    electron_configuration: Optional[str] = None
    has_stereocenter: Optional[Union[Union[dict, "Stereocenter"], List[Union[dict, "Stereocenter"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalElementId):
            self.id = ChemicalElementId(self.id)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.in_periodic_table_group is not None and not isinstance(self.in_periodic_table_group, int):
            self.in_periodic_table_group = int(self.in_periodic_table_group)

        if self.in_periodic_table_block is not None and not isinstance(self.in_periodic_table_block, PeriodicTableBlock):
            self.in_periodic_table_block = PeriodicTableBlock(**self.in_periodic_table_block)

        if self.boiling_point_in_celcius is not None and not isinstance(self.boiling_point_in_celcius, float):
            self.boiling_point_in_celcius = float(self.boiling_point_in_celcius)

        if self.melting_point_in_celcius is not None and not isinstance(self.melting_point_in_celcius, float):
            self.melting_point_in_celcius = float(self.melting_point_in_celcius)

        if self.standard_atomic_weight is not None and not isinstance(self.standard_atomic_weight, float):
            self.standard_atomic_weight = float(self.standard_atomic_weight)

        if self.electron_configuration is not None and not isinstance(self.electron_configuration, str):
            self.electron_configuration = str(self.electron_configuration)

        if self.has_stereocenter is None:
            self.has_stereocenter = []
        if not isinstance(self.has_stereocenter, list):
            self.has_stereocenter = [self.has_stereocenter]
        self.has_stereocenter = [v if isinstance(v, Stereocenter) else Stereocenter(**v) for v in self.has_stereocenter]

        super().__post_init__(**kwargs)


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

    id: Union[str, IsotopeId] = None
    neutron_number: Optional[int] = None
    isotope_of: Optional[Union[str, IsotopeId]] = None
    half_life: Optional[int] = None
    decay_product: Optional[Union[str, IsotopeId]] = None
    decay_mode: Optional[str] = None
    decay_energy: Optional[str] = None
    mode_of_formation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, IsotopeId):
            self.id = IsotopeId(self.id)

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

    id: Union[str, NuclideId] = None
    energy_level: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NuclideId):
            self.id = NuclideId(self.id)

        if self.energy_level is not None and not isinstance(self.energy_level, str):
            self.energy_level = str(self.energy_level)

        super().__post_init__(**kwargs)


@dataclass
class Radionuclide(Nuclide):
    """
    an atom that has excess nuclear energy, making it unstable
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Radionuclide
    class_class_curie: ClassVar[str] = "chemont:Radionuclide"
    class_name: ClassVar[str] = "radionuclide"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Radionuclide

    id: Union[str, RadionuclideId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RadionuclideId):
            self.id = RadionuclideId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AtomIonicForm(Atom):
    """
    an atom type in which charge state is specified. Example: Chloride is an atom ionic species; its formula is Cl−.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomIonicForm
    class_class_curie: ClassVar[str] = "chemont:AtomIonicForm"
    class_name: ClassVar[str] = "atom ionic form"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomIonicForm

    id: Union[str, AtomIonicFormId] = None
    elemental_charge: Optional[int] = None
    elemental_change: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        if self.elemental_change is not None and not isinstance(self.elemental_change, str):
            self.elemental_change = str(self.elemental_change)

        super().__post_init__(**kwargs)


@dataclass
class UnchargedAtom(AtomIonicForm):
    """
    An atom type that has no charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.UnchargedAtom
    class_class_curie: ClassVar[str] = "chemont:UnchargedAtom"
    class_name: ClassVar[str] = "uncharged atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.UnchargedAtom

    id: Union[str, UnchargedAtomId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, UnchargedAtomId):
            self.id = UnchargedAtomId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MonoatomicIon(AtomIonicForm):
    """
    An atom type that has a charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MonoatomicIon
    class_class_curie: ClassVar[str] = "chemont:MonoatomicIon"
    class_name: ClassVar[str] = "monoatomic ion"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MonoatomicIon

    id: Union[str, MonoatomicIonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MonoatomicIonId):
            self.id = MonoatomicIonId(self.id)

        super().__post_init__(**kwargs)


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

    id: Union[str, AtomAnionId] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AtomAnionId):
            self.id = AtomAnionId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


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

    id: Union[str, AtomCationId] = None
    elemental_charge: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AtomCationId):
            self.id = AtomCationId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        super().__post_init__(**kwargs)


@dataclass
class FullySpecifiedAtom(Atom):
    """
    An atom type that has atomic number, charge, and neutron number stated
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.FullySpecifiedAtom
    class_class_curie: ClassVar[str] = "chemont:FullySpecifiedAtom"
    class_name: ClassVar[str] = "fully specified atom"
    class_model_uri: ClassVar[URIRef] = CHEMONT.FullySpecifiedAtom

    id: Union[str, FullySpecifiedAtomId] = None
    elemental_charge: Optional[int] = None
    neutron_number: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FullySpecifiedAtomId):
            self.id = FullySpecifiedAtomId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        if self.neutron_number is not None and not isinstance(self.neutron_number, int):
            self.neutron_number = int(self.neutron_number)

        super().__post_init__(**kwargs)


class InformationalChemicalEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.InformationalChemicalEntity
    class_class_curie: ClassVar[str] = "chemont:InformationalChemicalEntity"
    class_name: ClassVar[str] = "informational chemical entity"
    class_model_uri: ClassVar[URIRef] = CHEMONT.InformationalChemicalEntity


class PeriodicTablePlacement(InformationalChemicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.PeriodicTablePlacement
    class_class_curie: ClassVar[str] = "chemont:PeriodicTablePlacement"
    class_name: ClassVar[str] = "periodic table placement"
    class_model_uri: ClassVar[URIRef] = CHEMONT.PeriodicTablePlacement


@dataclass
class PeriodicTableBlock(PeriodicTablePlacement):
    """
    A block of the periodic table is a set of elements unified by the orbitals their valence electrons or vacancies
    lie in
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.PeriodicTableBlock
    class_class_curie: ClassVar[str] = "chemont:PeriodicTableBlock"
    class_name: ClassVar[str] = "periodic table block"
    class_model_uri: ClassVar[URIRef] = CHEMONT.PeriodicTableBlock

    type: Optional[Union[str, "PeriodicTableBlockEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, PeriodicTableBlockEnum):
            self.type = PeriodicTableBlockEnum(self.type)

        super().__post_init__(**kwargs)


class InchiObject(InformationalChemicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.InchiObject
    class_class_curie: ClassVar[str] = "chemont:InchiObject"
    class_name: ClassVar[str] = "inchi object"
    class_model_uri: ClassVar[URIRef] = CHEMONT.InchiObject


@dataclass
class StandardInchiObject(InchiObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.StandardInchiObject
    class_class_curie: ClassVar[str] = "chemont:StandardInchiObject"
    class_name: ClassVar[str] = "standard inchi object"
    class_model_uri: ClassVar[URIRef] = CHEMONT.StandardInchiObject

    inchi_version_string: str = None
    inchi_chemical_sublayer: str = None
    inchi_atom_connections_sublayer: Optional[str] = None
    inchi_hydrogen_connections_sublayer: Optional[str] = None
    inchi_charge_sublayer: Optional[str] = None
    inchi_proton_sublayer: Optional[str] = None
    inchi_stereochemical_double_bond_sublayer: Optional[str] = None
    inchi_tetrahedral_stereochemical_sublayer: Optional[str] = None
    inchi_stereochemical_type_sublayer: Optional[str] = None
    inchi_isotopic_layer: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.inchi_version_string is None:
            raise ValueError("inchi_version_string must be supplied")
        if not isinstance(self.inchi_version_string, str):
            self.inchi_version_string = str(self.inchi_version_string)

        if self.inchi_chemical_sublayer is None:
            raise ValueError("inchi_chemical_sublayer must be supplied")
        if not isinstance(self.inchi_chemical_sublayer, str):
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


@dataclass
class RelationalChemicalEntity(YAMLRoot):
    """
    A reified relationship
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.RelationalChemicalEntity
    class_class_curie: ClassVar[str] = "chemont:RelationalChemicalEntity"
    class_name: ClassVar[str] = "relational chemical entity"
    class_model_uri: ClassVar[URIRef] = CHEMONT.RelationalChemicalEntity

    owl_subclass_of: Optional[Union[dict, OwlClass]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**self.owl_subclass_of)

        super().__post_init__(**kwargs)


class ChemicalCharacteristic(YAMLRoot):
    """
    A property of a chemical entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalCharacteristic
    class_class_curie: ClassVar[str] = "chemont:ChemicalCharacteristic"
    class_name: ClassVar[str] = "chemical characteristic"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalCharacteristic


@dataclass
class Location(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Location
    class_class_curie: ClassVar[str] = "chemont:Location"
    class_name: ClassVar[str] = "location"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Location

    owl_subclass_of: Optional[Union[dict, OwlClass]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**self.owl_subclass_of)

        super().__post_init__(**kwargs)


@dataclass
class Stereocenter(Location):
    """
    a particular instance of a stereogenic element that is geometrically a point, bearing different substituents, such
    that interchanging any two substituents leads to a stereoisomer
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Stereocenter
    class_class_curie: ClassVar[str] = "chemont:Stereocenter"
    class_name: ClassVar[str] = "stereocenter"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Stereocenter

    owl_subclass_of: Optional[Union[dict, OwlClass]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**self.owl_subclass_of)

        super().__post_init__(**kwargs)


class ChiralityCenter(Stereocenter):
    """
    a stereocenter consisting of an atom holding a set of ligands (atoms or groups of atoms) in a spatial arrangement
    which is not superimposable on its mirror image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChiralityCenter
    class_class_curie: ClassVar[str] = "chemont:ChiralityCenter"
    class_name: ClassVar[str] = "chirality center"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChiralityCenter


@dataclass
class AtomicBond(RelationalChemicalEntity):
    """
    A connection between two atoms. Note this is the reified form of 'atomically connected to'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomicBond
    class_class_curie: ClassVar[str] = "chemont:AtomicBond"
    class_name: ClassVar[str] = "atomic bond"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomicBond

    owl_subclass_of: Optional[Union[dict, OwlClass]] = None
    has_atom_occurrences: Optional[Union[Union[dict, "AtomOccurrence"], List[Union[dict, "AtomOccurrence"]]]] = empty_list()
    bond_order: Optional[int] = None
    bond_type: Optional[Union[str, "BondTypeEnum"]] = None
    bond_length_in_angstroms: Optional[float] = None
    bond_angle: Optional[float] = None
    torsional_angle: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**self.owl_subclass_of)

        if self.has_atom_occurrences is None:
            self.has_atom_occurrences = []
        if not isinstance(self.has_atom_occurrences, list):
            self.has_atom_occurrences = [self.has_atom_occurrences]
        self._normalize_inlined_slot(slot_name="has_atom_occurrences", slot_type=AtomOccurrence, key_name="occurrence of", inlined_as_list=True, keyed=False)

        if self.bond_order is not None and not isinstance(self.bond_order, int):
            self.bond_order = int(self.bond_order)

        if self.bond_type is not None and not isinstance(self.bond_type, BondTypeEnum):
            self.bond_type = BondTypeEnum(self.bond_type)

        if self.bond_length_in_angstroms is not None and not isinstance(self.bond_length_in_angstroms, float):
            self.bond_length_in_angstroms = float(self.bond_length_in_angstroms)

        if self.bond_angle is not None and not isinstance(self.bond_angle, float):
            self.bond_angle = float(self.bond_angle)

        if self.torsional_angle is not None and not isinstance(self.torsional_angle, float):
            self.torsional_angle = float(self.torsional_angle)

        super().__post_init__(**kwargs)


@dataclass
class AtomOccurrence(RelationalChemicalEntity):
    """
    An occurrence of an atom in the context of a particular molecule. For example, one of two occurrences of oxygen in
    nitrate
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AtomOccurrence
    class_class_curie: ClassVar[str] = "chemont:AtomOccurrence"
    class_name: ClassVar[str] = "atom occurrence"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AtomOccurrence

    occurrence_of: Union[str, AtomId] = None
    owl_subclass_of: Optional[Union[dict, OwlClass]] = None
    valence: Optional[int] = None
    oxidation_number: Optional[int] = None
    formal_charge: Optional[int] = None
    coordination_number: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.occurrence_of is None:
            raise ValueError("occurrence_of must be supplied")
        if not isinstance(self.occurrence_of, AtomId):
            self.occurrence_of = AtomId(self.occurrence_of)

        if self.owl_subclass_of is not None and not isinstance(self.owl_subclass_of, OwlClass):
            self.owl_subclass_of = OwlClass(**self.owl_subclass_of)

        if self.valence is not None and not isinstance(self.valence, int):
            self.valence = int(self.valence)

        if self.oxidation_number is not None and not isinstance(self.oxidation_number, int):
            self.oxidation_number = int(self.oxidation_number)

        if self.formal_charge is not None and not isinstance(self.formal_charge, int):
            self.formal_charge = int(self.formal_charge)

        if self.coordination_number is not None and not isinstance(self.coordination_number, int):
            self.coordination_number = int(self.coordination_number)

        super().__post_init__(**kwargs)


@dataclass
class BronstedAcid(Molecule):
    """
    A molecule capable of donating a hydron to an acceptor. Example: citric acid
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.BronstedAcid
    class_class_curie: ClassVar[str] = "chemont:BronstedAcid"
    class_name: ClassVar[str] = "Bronsted acid"
    class_model_uri: ClassVar[URIRef] = CHEMONT.BronstedAcid

    id: Union[str, BronstedAcidId] = None
    acidity: Optional[float] = None
    hard_or_soft: Optional[Union[str, "HardOrSoftEnum"]] = None
    acid_form_of: Optional[Union[Union[str, AcidBaseId], List[Union[str, AcidBaseId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BronstedAcidId):
            self.id = BronstedAcidId(self.id)

        if self.acidity is not None and not isinstance(self.acidity, float):
            self.acidity = float(self.acidity)

        if self.hard_or_soft is not None and not isinstance(self.hard_or_soft, HardOrSoftEnum):
            self.hard_or_soft = HardOrSoftEnum(self.hard_or_soft)

        if self.acid_form_of is None:
            self.acid_form_of = []
        if not isinstance(self.acid_form_of, list):
            self.acid_form_of = [self.acid_form_of]
        self.acid_form_of = [v if isinstance(v, AcidBaseId) else AcidBaseId(v) for v in self.acid_form_of]

        super().__post_init__(**kwargs)


@dataclass
class AcidBase(MolecularAnion):
    """
    A conugate base of an acid with charge specified. Example: citrate(3-)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.AcidBase
    class_class_curie: ClassVar[str] = "chemont:AcidBase"
    class_name: ClassVar[str] = "acid base"
    class_model_uri: ClassVar[URIRef] = CHEMONT.AcidBase

    id: Union[str, AcidBaseId] = None
    has_acid_form: Optional[Union[str, BronstedAcidId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AcidBaseId):
            self.id = AcidBaseId(self.id)

        if self.has_acid_form is not None and not isinstance(self.has_acid_form, BronstedAcidId):
            self.has_acid_form = BronstedAcidId(self.has_acid_form)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalSalt(PreciseChemicalMixture):
    """
    a chemical compound consisting of an ionic assembly of cations and anions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ChemicalSalt
    class_class_curie: ClassVar[str] = "chemont:ChemicalSalt"
    class_name: ClassVar[str] = "chemical salt"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ChemicalSalt

    id: Union[str, ChemicalSaltId] = None
    elemental_charge: Optional[int] = None
    has_cationic_component: Optional[Union[dict, CationState]] = None
    has_anionic_component: Optional[Union[dict, AnionState]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalSaltId):
            self.id = ChemicalSaltId(self.id)

        if self.elemental_charge is not None and not isinstance(self.elemental_charge, int):
            self.elemental_charge = int(self.elemental_charge)

        if self.has_cationic_component is not None and not isinstance(self.has_cationic_component, CationState):
            self.has_cationic_component = CationState(**self.has_cationic_component)

        if self.has_anionic_component is not None and not isinstance(self.has_anionic_component, AnionState):
            self.has_anionic_component = AnionState(**self.has_anionic_component)

        super().__post_init__(**kwargs)


@dataclass
class Ester(Molecule):
    """
    An ester is a chemical compound derived from an acid (organic or inorganic) in which at least one –OH hydroxyl
    group is replaced by an –O– alkyl (alkoxy) group
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Ester
    class_class_curie: ClassVar[str] = "chemont:Ester"
    class_name: ClassVar[str] = "ester"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Ester

    id: Union[str, EsterId] = None
    has_parent_alcohol: Optional[Union[str, ChemicalEntityId]] = None
    has_parent_acid: Optional[Union[str, BronstedAcidId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EsterId):
            self.id = EsterId(self.id)

        if self.has_parent_alcohol is not None and not isinstance(self.has_parent_alcohol, ChemicalEntityId):
            self.has_parent_alcohol = ChemicalEntityId(self.has_parent_alcohol)

        if self.has_parent_acid is not None and not isinstance(self.has_parent_acid, BronstedAcidId):
            self.has_parent_acid = BronstedAcidId(self.has_parent_acid)

        super().__post_init__(**kwargs)


@dataclass
class Stereoisomer(Molecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Stereoisomer
    class_class_curie: ClassVar[str] = "chemont:Stereoisomer"
    class_name: ClassVar[str] = "stereoisomer"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Stereoisomer

    id: Union[str, StereoisomerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, StereoisomerId):
            self.id = StereoisomerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Enantiomer(Stereoisomer):
    """
    one of two stereoisomers of a chiral molecule that are mirror images. Example: R-thalidomide
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Enantiomer
    class_class_curie: ClassVar[str] = "chemont:Enantiomer"
    class_name: ClassVar[str] = "enantiomer"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Enantiomer

    id: Union[str, EnantiomerId] = None
    relative_configuration: Optional[str] = None
    optical_configuration: Optional[str] = None
    absolute_configuration: Optional[str] = None
    enantiomer_form_of: Optional[Union[str, MoleculeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnantiomerId):
            self.id = EnantiomerId(self.id)

        if self.relative_configuration is not None and not isinstance(self.relative_configuration, str):
            self.relative_configuration = str(self.relative_configuration)

        if self.optical_configuration is not None and not isinstance(self.optical_configuration, str):
            self.optical_configuration = str(self.optical_configuration)

        if self.absolute_configuration is not None and not isinstance(self.absolute_configuration, str):
            self.absolute_configuration = str(self.absolute_configuration)

        if self.enantiomer_form_of is not None and not isinstance(self.enantiomer_form_of, MoleculeId):
            self.enantiomer_form_of = MoleculeId(self.enantiomer_form_of)

        super().__post_init__(**kwargs)


@dataclass
class RacemicMixture(PreciseChemicalMixture):
    """
    a chemical compound that has equal amounts of left- and right-handed enantiomers of a chiral molecule. An example
    is Thalidomide
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.RacemicMixture
    class_class_curie: ClassVar[str] = "chemont:RacemicMixture"
    class_name: ClassVar[str] = "racemic mixture"
    class_model_uri: ClassVar[URIRef] = CHEMONT.RacemicMixture

    id: Union[str, RacemicMixtureId] = None
    has_left_enantiomer: Union[str, EnantiomerId] = None
    has_right_enantiomer: Union[str, EnantiomerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RacemicMixtureId):
            self.id = RacemicMixtureId(self.id)

        if self.has_left_enantiomer is None:
            raise ValueError("has_left_enantiomer must be supplied")
        if not isinstance(self.has_left_enantiomer, EnantiomerId):
            self.has_left_enantiomer = EnantiomerId(self.has_left_enantiomer)

        if self.has_right_enantiomer is None:
            raise ValueError("has_right_enantiomer must be supplied")
        if not isinstance(self.has_right_enantiomer, EnantiomerId):
            self.has_right_enantiomer = EnantiomerId(self.has_right_enantiomer)

        super().__post_init__(**kwargs)


@dataclass
class Allotrope(Molecule):
    """
    A molecule consisting of atoms of the same element
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Allotrope
    class_class_curie: ClassVar[str] = "chemont:Allotrope"
    class_name: ClassVar[str] = "allotrope"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Allotrope

    id: Union[str, AllotropeId] = None
    allotropic_analog_of: Union[str, ChemicalElementId] = None
    has_bonding_structure: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AllotropeId):
            self.id = AllotropeId(self.id)

        if self.allotropic_analog_of is None:
            raise ValueError("allotropic_analog_of must be supplied")
        if not isinstance(self.allotropic_analog_of, ChemicalElementId):
            self.allotropic_analog_of = ChemicalElementId(self.allotropic_analog_of)

        if self.has_bonding_structure is None:
            raise ValueError("has_bonding_structure must be supplied")
        if not isinstance(self.has_bonding_structure, str):
            self.has_bonding_structure = str(self.has_bonding_structure)

        super().__post_init__(**kwargs)


@dataclass
class Reaction(YAMLRoot):
    """
    reaction
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Reaction
    class_class_curie: ClassVar[str] = "chemont:Reaction"
    class_name: ClassVar[str] = "reaction"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Reaction

    left_participants: Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]] = empty_list()
    right_participants: Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]] = empty_list()
    direction: Optional[str] = None
    smarts_string: Optional[str] = None
    is_diastereoselective: Optional[Union[bool, Bool]] = None
    is_stereo: Optional[Union[bool, Bool]] = None
    is_balanced: Optional[Union[bool, Bool]] = None
    is_transport: Optional[Union[bool, Bool]] = None
    is_fully_characterized: Optional[Union[bool, Bool]] = None
    reaction_center: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.left_participants is None:
            self.left_participants = []
        if not isinstance(self.left_participants, list):
            self.left_participants = [self.left_participants]
        self.left_participants = [v if isinstance(v, ReactionParticipant) else ReactionParticipant(**v) for v in self.left_participants]

        if self.right_participants is None:
            self.right_participants = []
        if not isinstance(self.right_participants, list):
            self.right_participants = [self.right_participants]
        self.right_participants = [v if isinstance(v, ReactionParticipant) else ReactionParticipant(**v) for v in self.right_participants]

        if self.direction is not None and not isinstance(self.direction, str):
            self.direction = str(self.direction)

        if self.smarts_string is not None and not isinstance(self.smarts_string, str):
            self.smarts_string = str(self.smarts_string)

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

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class IsomeraseReaction(Reaction):
    """
    A reaction that converts a molecule from one isomer to another. TODO: create rules for this
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.IsomeraseReaction
    class_class_curie: ClassVar[str] = "chemont:IsomeraseReaction"
    class_name: ClassVar[str] = "isomerase reaction"
    class_model_uri: ClassVar[URIRef] = CHEMONT.IsomeraseReaction


@dataclass
class ReactionParticipant(RelationalChemicalEntity):
    """
    Instances of this link a reaction to a chemical entity participant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ReactionParticipant
    class_class_curie: ClassVar[str] = "chemont:ReactionParticipant"
    class_name: ClassVar[str] = "reaction participant"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ReactionParticipant

    participant: Optional[Union[str, ChemicalEntityId]] = None
    stoichiometry: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.participant is not None and not isinstance(self.participant, ChemicalEntityId):
            self.participant = ChemicalEntityId(self.participant)

        if self.stoichiometry is not None and not isinstance(self.stoichiometry, int):
            self.stoichiometry = int(self.stoichiometry)

        super().__post_init__(**kwargs)


@dataclass
class ProportionalPart(RelationalChemicalEntity):
    """
    A part of a complex mixture that is of uniform composition
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.ProportionalPart
    class_class_curie: ClassVar[str] = "chemont:ProportionalPart"
    class_name: ClassVar[str] = "proportional part"
    class_model_uri: ClassVar[URIRef] = CHEMONT.ProportionalPart

    has_role: Optional[Union[str, "IngredientRoleEnum"]] = None
    composed_of: Optional[Union[str, ChemicalEntityId]] = None
    minimal_percentage: Optional[float] = None
    maximum_percentage: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_role is not None and not isinstance(self.has_role, IngredientRoleEnum):
            self.has_role = IngredientRoleEnum(self.has_role)

        if self.composed_of is not None and not isinstance(self.composed_of, ChemicalEntityId):
            self.composed_of = ChemicalEntityId(self.composed_of)

        if self.minimal_percentage is not None and not isinstance(self.minimal_percentage, float):
            self.minimal_percentage = float(self.minimal_percentage)

        if self.maximum_percentage is not None and not isinstance(self.maximum_percentage, float):
            self.maximum_percentage = float(self.maximum_percentage)

        super().__post_init__(**kwargs)


class Measure(RelationalChemicalEntity):
    """
    todo
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.Measure
    class_class_curie: ClassVar[str] = "chemont:Measure"
    class_name: ClassVar[str] = "measure"
    class_model_uri: ClassVar[URIRef] = CHEMONT.Measure


@dataclass
class MoleculePairwiseSimilarity(Measure):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.MoleculePairwiseSimilarity
    class_class_curie: ClassVar[str] = "chemont:MoleculePairwiseSimilarity"
    class_name: ClassVar[str] = "molecule pairwise similarity"
    class_model_uri: ClassVar[URIRef] = CHEMONT.MoleculePairwiseSimilarity

    left_molecule: Optional[Union[str, MoleculeId]] = None
    right_molecule: Optional[Union[str, MoleculeId]] = None
    score: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.left_molecule is not None and not isinstance(self.left_molecule, MoleculeId):
            self.left_molecule = MoleculeId(self.left_molecule)

        if self.right_molecule is not None and not isinstance(self.right_molecule, MoleculeId):
            self.right_molecule = MoleculeId(self.right_molecule)

        if self.score is not None and not isinstance(self.score, str):
            self.score = str(self.score)

        super().__post_init__(**kwargs)


@dataclass
class TanimotoSimilarity(MoleculePairwiseSimilarity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMONT.TanimotoSimilarity
    class_class_curie: ClassVar[str] = "chemont:TanimotoSimilarity"
    class_name: ClassVar[str] = "tanimoto similarity"
    class_model_uri: ClassVar[URIRef] = CHEMONT.TanimotoSimilarity

    score: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.score is not None and not isinstance(self.score, float):
            self.score = float(self.score)

        super().__post_init__(**kwargs)


# Enumerations
class NanostructureMorphologyEnum(EnumDefinitionImpl):

    nanotube = PermissibleValue(text="nanotube",
                                       meaning=CHEBI["50796"])
    nanoparticle = PermissibleValue(text="nanoparticle",
                                               meaning=CHEBI["50803"])
    nanorod = PermissibleValue(text="nanorod",
                                     meaning=CHEBI["50805"])
    nanotubosome = PermissibleValue(text="nanotubosome",
                                               meaning=CHEBI["50806"])
    nanofibre = PermissibleValue(text="nanofibre",
                                         meaning=CHEBI["52518"])
    nanocrystal = PermissibleValue(text="nanocrystal",
                                             meaning=CHEBI["52529"])
    nanoribbon = PermissibleValue(text="nanoribbon",
                                           meaning=CHEBI["52530"])
    nanosheet = PermissibleValue(text="nanosheet",
                                         meaning=CHEBI["52531"])
    nanowire = PermissibleValue(text="nanowire",
                                       meaning=CHEBI["52593"])

    _defn = EnumDefinition(
        name="NanostructureMorphologyEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "quantum dot",
                PermissibleValue(text="quantum dot",
                                 meaning=CHEBI["50853"]) )

class PeriodicTableBlockEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="PeriodicTableBlockEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "s-block",
                PermissibleValue(text="s-block") )
        setattr(cls, "p-block",
                PermissibleValue(text="p-block") )
        setattr(cls, "d-block",
                PermissibleValue(text="d-block") )
        setattr(cls, "f-block",
                PermissibleValue(text="f-block") )
        setattr(cls, "g-block",
                PermissibleValue(text="g-block") )

class IngredientRoleEnum(EnumDefinitionImpl):

    excipient = PermissibleValue(text="excipient")
    solvent = PermissibleValue(text="solvent")

    _defn = EnumDefinition(
        name="IngredientRoleEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "active ingredient",
                PermissibleValue(text="active ingredient") )
        setattr(cls, "inactive ingredient",
                PermissibleValue(text="inactive ingredient") )

class BondTypeEnum(EnumDefinitionImpl):

    covalent = PermissibleValue(text="covalent",
                                       description="A covalent bond is a chemical bond that involves the sharing of pairs of electrons between atoms. This sharing results in a stable balance of attractive and repulsive forces between those atoms.")
    ionic = PermissibleValue(text="ionic")
    polycentric = PermissibleValue(text="polycentric")

    _defn = EnumDefinition(
        name="BondTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "metal-metal",
                PermissibleValue(text="metal-metal") )
        setattr(cls, "salt bridge",
                PermissibleValue(text="salt bridge") )

class HardOrSoftEnum(EnumDefinitionImpl):

    hard = PermissibleValue(text="hard")
    soft = PermissibleValue(text="soft")
    borderline = PermissibleValue(text="borderline")

    _defn = EnumDefinition(
        name="HardOrSoftEnum",
    )

# Slots
class slots:
    pass

slots.chemical_to_chemical_relationship = Slot(uri=CHEMONT.chemical_to_chemical_relationship, name="chemical to chemical relationship", curie=CHEMONT.curie('chemical_to_chemical_relationship'),
                   model_uri=CHEMONT.chemical_to_chemical_relationship, domain=None, range=Optional[str])

slots.chemical_property = Slot(uri=CHEMONT.chemical_property, name="chemical property", curie=CHEMONT.curie('chemical_property'),
                   model_uri=CHEMONT.chemical_property, domain=None, range=Optional[str])

slots.information_property = Slot(uri=CHEMONT.information_property, name="information property", curie=CHEMONT.curie('information_property'),
                   model_uri=CHEMONT.information_property, domain=None, range=Optional[str])

slots.in_periodic_table_group = Slot(uri=CHEMONT.in_periodic_table_group, name="in periodic table group", curie=CHEMONT.curie('in_periodic_table_group'),
                   model_uri=CHEMONT.in_periodic_table_group, domain=None, range=Optional[int])

slots.in_periodic_table_block = Slot(uri=CHEMONT.in_periodic_table_block, name="in periodic table block", curie=CHEMONT.curie('in_periodic_table_block'),
                   model_uri=CHEMONT.in_periodic_table_block, domain=None, range=Optional[Union[dict, PeriodicTableBlock]])

slots.id = Slot(uri=CHEMONT.id, name="id", curie=CHEMONT.curie('id'),
                   model_uri=CHEMONT.id, domain=None, range=URIRef, mappings = [SCHEMA.identifier])

slots.name = Slot(uri=CHEMONT.name, name="name", curie=CHEMONT.curie('name'),
                   model_uri=CHEMONT.name, domain=None, range=Optional[str])

slots.symbol = Slot(uri=CHEMONT.symbol, name="symbol", curie=CHEMONT.curie('symbol'),
                   model_uri=CHEMONT.symbol, domain=None, range=Optional[str])

slots.property_of_atom = Slot(uri=CHEMONT.property_of_atom, name="property of atom", curie=CHEMONT.curie('property_of_atom'),
                   model_uri=CHEMONT.property_of_atom, domain=Atom, range=Optional[str])

slots.subatomic_particle_count = Slot(uri=CHEMONT.subatomic_particle_count, name="subatomic particle count", curie=CHEMONT.curie('subatomic_particle_count'),
                   model_uri=CHEMONT.subatomic_particle_count, domain=Atom, range=Optional[str])

slots.atomic_number = Slot(uri=CHEMONT.atomic_number, name="atomic number", curie=CHEMONT.curie('atomic_number'),
                   model_uri=CHEMONT.atomic_number, domain=Atom, range=Optional[int], mappings = [CHEMINF["000079"]])

slots.neutron_number = Slot(uri=CHEMONT.neutron_number, name="neutron number", curie=CHEMONT.curie('neutron_number'),
                   model_uri=CHEMONT.neutron_number, domain=Atom, range=Optional[int], mappings = [CHEMINF["000078"]])

slots.nucleon_number = Slot(uri=CHEMONT.nucleon_number, name="nucleon number", curie=CHEMONT.curie('nucleon_number'),
                   model_uri=CHEMONT.nucleon_number, domain=Atom, range=Optional[int])

slots.elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="elemental charge", curie=CHEMONT.curie('elemental_charge'),
                   model_uri=CHEMONT.elemental_charge, domain=ChemicalEntity, range=Optional[int], mappings = [CHEMINF["000120"]])

slots.alternate_form_of = Slot(uri=CHEMONT.alternate_form_of, name="alternate form of", curie=CHEMONT.curie('alternate_form_of'),
                   model_uri=CHEMONT.alternate_form_of, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.allotropic_analog_of = Slot(uri=CHEMONT.allotropic_analog_of, name="allotropic analog of", curie=CHEMONT.curie('allotropic_analog_of'),
                   model_uri=CHEMONT.allotropic_analog_of, domain=Allotrope, range=Optional[Union[str, AllotropeId]])

slots.isotope_of = Slot(uri=CHEMONT.isotope_of, name="isotope of", curie=CHEMONT.curie('isotope_of'),
                   model_uri=CHEMONT.isotope_of, domain=Isotope, range=Optional[Union[str, IsotopeId]])

slots.isotone_of = Slot(uri=CHEMONT.isotone_of, name="isotone of", curie=CHEMONT.curie('isotone_of'),
                   model_uri=CHEMONT.isotone_of, domain=Isotope, range=Optional[Union[str, IsotopeId]])

slots.nuclear_isomer_of = Slot(uri=CHEMONT.nuclear_isomer_of, name="nuclear isomer of", curie=CHEMONT.curie('nuclear_isomer_of'),
                   model_uri=CHEMONT.nuclear_isomer_of, domain=Isotope, range=Optional[Union[str, IsotopeId]])

slots.isobar_of = Slot(uri=CHEMONT.isobar_of, name="isobar of", curie=CHEMONT.curie('isobar_of'),
                   model_uri=CHEMONT.isobar_of, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.derivative_of = Slot(uri=CHEMONT.derivative_of, name="derivative of", curie=CHEMONT.curie('derivative_of'),
                   model_uri=CHEMONT.derivative_of, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.has_derivative = Slot(uri=CHEMONT.has_derivative, name="has derivative", curie=CHEMONT.curie('has_derivative'),
                   model_uri=CHEMONT.has_derivative, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.conjugate_base_of = Slot(uri=CHEMONT.conjugate_base_of, name="conjugate base of", curie=CHEMONT.curie('conjugate_base_of'),
                   model_uri=CHEMONT.conjugate_base_of, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.conjugate_acid_of = Slot(uri=CHEMONT.conjugate_acid_of, name="conjugate acid of", curie=CHEMONT.curie('conjugate_acid_of'),
                   model_uri=CHEMONT.conjugate_acid_of, domain=ChemicalEntity, range=Optional[Union[str, ChemicalEntityId]])

slots.acid_form_of = Slot(uri=CHEMONT.acid_form_of, name="acid form of", curie=CHEMONT.curie('acid_form_of'),
                   model_uri=CHEMONT.acid_form_of, domain=BronstedAcid, range=Optional[Union[Union[str, AcidBaseId], List[Union[str, AcidBaseId]]]])

slots.has_physiological_base = Slot(uri=CHEMONT.has_physiological_base, name="has physiological base", curie=CHEMONT.curie('has_physiological_base'),
                   model_uri=CHEMONT.has_physiological_base, domain=BronstedAcid, range=Optional[Union[str, AcidBaseId]])

slots.has_acid_form = Slot(uri=CHEMONT.has_acid_form, name="has acid form", curie=CHEMONT.curie('has_acid_form'),
                   model_uri=CHEMONT.has_acid_form, domain=AcidBase, range=Optional[Union[str, BronstedAcidId]])

slots.has_characteristic = Slot(uri=CHEMONT.has_characteristic, name="has characteristic", curie=CHEMONT.curie('has_characteristic'),
                   model_uri=CHEMONT.has_characteristic, domain=None, range=Optional[Union[dict, ChemicalCharacteristic]])

slots.has_part = Slot(uri=CHEMONT.has_part, name="has part", curie=CHEMONT.curie('has_part'),
                   model_uri=CHEMONT.has_part, domain=None, range=Optional[str], mappings = [BFO["0000050"], SCHEMA.hasBioChemEntityPart])

slots.has_atoms = Slot(uri=CHEMONT.has_atoms, name="has atoms", curie=CHEMONT.curie('has_atoms'),
                   model_uri=CHEMONT.has_atoms, domain=Molecule, range=Optional[Union[Union[str, AtomId], List[Union[str, AtomId]]]])

slots.has_submolecules = Slot(uri=CHEMONT.has_submolecules, name="has submolecules", curie=CHEMONT.curie('has_submolecules'),
                   model_uri=CHEMONT.has_submolecules, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.has_ionic_component = Slot(uri=CHEMONT.has_ionic_component, name="has ionic component", curie=CHEMONT.curie('has_ionic_component'),
                   model_uri=CHEMONT.has_ionic_component, domain=None, range=Optional[str])

slots.has_cationic_component = Slot(uri=CHEMONT.has_cationic_component, name="has cationic component", curie=CHEMONT.curie('has_cationic_component'),
                   model_uri=CHEMONT.has_cationic_component, domain=None, range=Optional[str])

slots.has_anionic_component = Slot(uri=CHEMONT.has_anionic_component, name="has anionic component", curie=CHEMONT.curie('has_anionic_component'),
                   model_uri=CHEMONT.has_anionic_component, domain=None, range=Optional[str])

slots.has_group = Slot(uri=CHEMONT.has_group, name="has group", curie=CHEMONT.curie('has_group'),
                   model_uri=CHEMONT.has_group, domain=Atom, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.has_proportional_parts = Slot(uri=CHEMONT.has_proportional_parts, name="has proportional parts", curie=CHEMONT.curie('has_proportional_parts'),
                   model_uri=CHEMONT.has_proportional_parts, domain=ImpreciseChemicalMixture, range=Optional[Union[Union[dict, "ProportionalPart"], List[Union[dict, "ProportionalPart"]]]])

slots.energy_level = Slot(uri=CHEMONT.energy_level, name="energy level", curie=CHEMONT.curie('energy_level'),
                   model_uri=CHEMONT.energy_level, domain=None, range=Optional[str])

slots.has_atom_occurrences = Slot(uri=CHEMONT.has_atom_occurrences, name="has atom occurrences", curie=CHEMONT.curie('has_atom_occurrences'),
                   model_uri=CHEMONT.has_atom_occurrences, domain=None, range=Optional[Union[Union[dict, AtomOccurrence], List[Union[dict, AtomOccurrence]]]])

slots.has_bonds = Slot(uri=CHEMONT.has_bonds, name="has bonds", curie=CHEMONT.curie('has_bonds'),
                   model_uri=CHEMONT.has_bonds, domain=Molecule, range=Optional[Union[Union[dict, "AtomicBond"], List[Union[dict, "AtomicBond"]]]])

slots.half_life = Slot(uri=CHEMONT.half_life, name="half life", curie=CHEMONT.curie('half_life'),
                   model_uri=CHEMONT.half_life, domain=Isotope, range=Optional[int])

slots.decay_mode = Slot(uri=CHEMONT.decay_mode, name="decay mode", curie=CHEMONT.curie('decay_mode'),
                   model_uri=CHEMONT.decay_mode, domain=Isotope, range=Optional[str])

slots.decay_product = Slot(uri=CHEMONT.decay_product, name="decay product", curie=CHEMONT.curie('decay_product'),
                   model_uri=CHEMONT.decay_product, domain=Isotope, range=Optional[Union[str, IsotopeId]])

slots.decay_energy = Slot(uri=CHEMONT.decay_energy, name="decay energy", curie=CHEMONT.curie('decay_energy'),
                   model_uri=CHEMONT.decay_energy, domain=Isotope, range=Optional[str])

slots.mode_of_formation = Slot(uri=CHEMONT.mode_of_formation, name="mode of formation", curie=CHEMONT.curie('mode_of_formation'),
                   model_uri=CHEMONT.mode_of_formation, domain=Isotope, range=Optional[str])

slots.thermophysical_property = Slot(uri=CHEMONT.thermophysical_property, name="thermophysical property", curie=CHEMONT.curie('thermophysical_property'),
                   model_uri=CHEMONT.thermophysical_property, domain=None, range=Optional[str])

slots.molar_value = Slot(uri=CHEMONT.molar_value, name="molar value", curie=CHEMONT.curie('molar_value'),
                   model_uri=CHEMONT.molar_value, domain=None, range=Optional[str])

slots.molar_cohesive_energy = Slot(uri=CHEMONT.molar_cohesive_energy, name="molar cohesive energy", curie=CHEMONT.curie('molar_cohesive_energy'),
                   model_uri=CHEMONT.molar_cohesive_energy, domain=None, range=Optional[str])

slots.has_cyclic_structure = Slot(uri=CHEMONT.has_cyclic_structure, name="has cyclic structure", curie=CHEMONT.curie('has_cyclic_structure'),
                   model_uri=CHEMONT.has_cyclic_structure, domain=Molecule, range=Optional[Union[bool, Bool]], mappings = [CHEMINF["000067"]])

slots.has_sequence_representation = Slot(uri=CHEMONT.has_sequence_representation, name="has sequence representation", curie=CHEMONT.curie('has_sequence_representation'),
                   model_uri=CHEMONT.has_sequence_representation, domain=None, range=Optional[str])

slots.chemical_formula = Slot(uri=CHEMONT.chemical_formula, name="chemical formula", curie=CHEMONT.curie('chemical_formula'),
                   model_uri=CHEMONT.chemical_formula, domain=ChemicalEntity, range=Optional[str], mappings = [SCHEMA.hasRepresentation, EDAM.data_0846])

slots.molecular_formula = Slot(uri=CHEMONT.molecular_formula, name="molecular formula", curie=CHEMONT.curie('molecular_formula'),
                   model_uri=CHEMONT.molecular_formula, domain=ChemicalEntity, range=Optional[str], mappings = [CHEMINF["000042"]])

slots.empirical_formula = Slot(uri=CHEMONT.empirical_formula, name="empirical formula", curie=CHEMONT.curie('empirical_formula'),
                   model_uri=CHEMONT.empirical_formula, domain=ChemicalEntity, range=Optional[str])

slots.generalized_empirical_formula = Slot(uri=CHEMONT.generalized_empirical_formula, name="generalized empirical formula", curie=CHEMONT.curie('generalized_empirical_formula'),
                   model_uri=CHEMONT.generalized_empirical_formula, domain=ChemicalEntity, range=Optional[str])

slots.smarts_string = Slot(uri=CHEMONT.smarts_string, name="smarts string", curie=CHEMONT.curie('smarts_string'),
                   model_uri=CHEMONT.smarts_string, domain=ChemicalEntity, range=Optional[str])

slots.lychi_string = Slot(uri=CHEMONT.lychi_string, name="lychi string", curie=CHEMONT.curie('lychi_string'),
                   model_uri=CHEMONT.lychi_string, domain=ChemicalEntity, range=Union[str, ChemicalEntityId])

slots.inchi_string = Slot(uri=CHEMONT.inchi_string, name="inchi string", curie=CHEMONT.curie('inchi_string'),
                   model_uri=CHEMONT.inchi_string, domain=ChemicalEntity, range=Union[str, ChemicalEntityId])

slots.inchi_key_string = Slot(uri=CHEMONT.inchi_key_string, name="inchi key string", curie=CHEMONT.curie('inchi_key_string'),
                   model_uri=CHEMONT.inchi_key_string, domain=ChemicalEntity, range=Optional[str])

slots.smiles_string = Slot(uri=CHEMONT.smiles_string, name="smiles string", curie=CHEMONT.curie('smiles_string'),
                   model_uri=CHEMONT.smiles_string, domain=ChemicalEntity, range=Union[Union[str, ChemicalEntityId], List[Union[str, ChemicalEntityId]]])

slots.curly_smiles_string = Slot(uri=CHEMONT.curly_smiles_string, name="curly smiles string", curie=CHEMONT.curie('curly_smiles_string'),
                   model_uri=CHEMONT.curly_smiles_string, domain=ChemicalEntity, range=Optional[str])

slots.isomeric_smiles_string = Slot(uri=CHEMONT.isomeric_smiles_string, name="isomeric smiles string", curie=CHEMONT.curie('isomeric_smiles_string'),
                   model_uri=CHEMONT.isomeric_smiles_string, domain=ChemicalEntity, range=Union[Union[str, ChemicalEntityId], List[Union[str, ChemicalEntityId]]])

slots.extended_smiles_string = Slot(uri=CHEMONT.extended_smiles_string, name="extended smiles string", curie=CHEMONT.curie('extended_smiles_string'),
                   model_uri=CHEMONT.extended_smiles_string, domain=ChemicalEntity, range=Union[Union[str, ChemicalEntityId], List[Union[str, ChemicalEntityId]]])

slots.canonical_smiles_string = Slot(uri=CHEMONT.canonical_smiles_string, name="canonical smiles string", curie=CHEMONT.curie('canonical_smiles_string'),
                   model_uri=CHEMONT.canonical_smiles_string, domain=ChemicalEntity, range=Union[str, ChemicalEntityId])

slots.has_standard_inchi_object = Slot(uri=CHEMONT.has_standard_inchi_object, name="has standard inchi object", curie=CHEMONT.curie('has_standard_inchi_object'),
                   model_uri=CHEMONT.has_standard_inchi_object, domain=None, range=Optional[Union[dict, StandardInchiObject]])

slots.inchi_component = Slot(uri=CHEMONT.inchi_component, name="inchi component", curie=CHEMONT.curie('inchi_component'),
                   model_uri=CHEMONT.inchi_component, domain=None, range=Optional[str])

slots.inchi_sublayer = Slot(uri=CHEMONT.inchi_sublayer, name="inchi sublayer", curie=CHEMONT.curie('inchi_sublayer'),
                   model_uri=CHEMONT.inchi_sublayer, domain=InchiObject, range=Optional[str])

slots.inchi_version_string = Slot(uri=CHEMONT.inchi_version_string, name="inchi version string", curie=CHEMONT.curie('inchi_version_string'),
                   model_uri=CHEMONT.inchi_version_string, domain=None, range=str,
                   pattern=re.compile(r'^1[S]'))

slots.inchi_chemical_sublayer = Slot(uri=CHEMONT.inchi_chemical_sublayer, name="inchi chemical sublayer", curie=CHEMONT.curie('inchi_chemical_sublayer'),
                   model_uri=CHEMONT.inchi_chemical_sublayer, domain=InchiObject, range=str,
                   pattern=re.compile(r'^[A-Z0-9\.]+$'))

slots.inchi_atom_connections_sublayer = Slot(uri=CHEMONT.inchi_atom_connections_sublayer, name="inchi atom connections sublayer", curie=CHEMONT.curie('inchi_atom_connections_sublayer'),
                   model_uri=CHEMONT.inchi_atom_connections_sublayer, domain=InchiObject, range=Optional[str],
                   pattern=re.compile(r'^c.*'))

slots.inchi_hydrogen_connections_sublayer = Slot(uri=CHEMONT.inchi_hydrogen_connections_sublayer, name="inchi hydrogen connections sublayer", curie=CHEMONT.curie('inchi_hydrogen_connections_sublayer'),
                   model_uri=CHEMONT.inchi_hydrogen_connections_sublayer, domain=InchiObject, range=Optional[str],
                   pattern=re.compile(r'^h.*'))

slots.inchi_charge_sublayer = Slot(uri=CHEMONT.inchi_charge_sublayer, name="inchi charge sublayer", curie=CHEMONT.curie('inchi_charge_sublayer'),
                   model_uri=CHEMONT.inchi_charge_sublayer, domain=InchiObject, range=Optional[str],
                   pattern=re.compile(r'^q.*'))

slots.inchi_proton_sublayer = Slot(uri=CHEMONT.inchi_proton_sublayer, name="inchi proton sublayer", curie=CHEMONT.curie('inchi_proton_sublayer'),
                   model_uri=CHEMONT.inchi_proton_sublayer, domain=InchiObject, range=Optional[str],
                   pattern=re.compile(r'^p[\-]\d+'))

slots.inchi_stereochemical_double_bond_sublayer = Slot(uri=CHEMONT.inchi_stereochemical_double_bond_sublayer, name="inchi stereochemical double bond sublayer", curie=CHEMONT.curie('inchi_stereochemical_double_bond_sublayer'),
                   model_uri=CHEMONT.inchi_stereochemical_double_bond_sublayer, domain=InchiObject, range=Optional[str],
                   pattern=re.compile(r'^b.*'))

slots.inchi_tetrahedral_stereochemical_sublayer = Slot(uri=CHEMONT.inchi_tetrahedral_stereochemical_sublayer, name="inchi tetrahedral stereochemical sublayer", curie=CHEMONT.curie('inchi_tetrahedral_stereochemical_sublayer'),
                   model_uri=CHEMONT.inchi_tetrahedral_stereochemical_sublayer, domain=InchiObject, range=Optional[str],
                   pattern=re.compile(r'^[tm].*'))

slots.inchi_stereochemical_type_sublayer = Slot(uri=CHEMONT.inchi_stereochemical_type_sublayer, name="inchi stereochemical type sublayer", curie=CHEMONT.curie('inchi_stereochemical_type_sublayer'),
                   model_uri=CHEMONT.inchi_stereochemical_type_sublayer, domain=InchiObject, range=Optional[str],
                   pattern=re.compile(r'^s.*'))

slots.inchi_isotopic_layer = Slot(uri=CHEMONT.inchi_isotopic_layer, name="inchi isotopic layer", curie=CHEMONT.curie('inchi_isotopic_layer'),
                   model_uri=CHEMONT.inchi_isotopic_layer, domain=InchiObject, range=Optional[str],
                   pattern=re.compile(r'^[ih].*'))

slots.inchi_fixed_H_layer = Slot(uri=CHEMONT.inchi_fixed_H_layer, name="inchi fixed H layer", curie=CHEMONT.curie('inchi_fixed_H_layer'),
                   model_uri=CHEMONT.inchi_fixed_H_layer, domain=InchiObject, range=Optional[str])

slots.inchi_reconnected_layer = Slot(uri=CHEMONT.inchi_reconnected_layer, name="inchi reconnected layer", curie=CHEMONT.curie('inchi_reconnected_layer'),
                   model_uri=CHEMONT.inchi_reconnected_layer, domain=InchiObject, range=Optional[str])

slots.atomically_connected_to = Slot(uri=CHEMONT.atomically_connected_to, name="atomically connected to", curie=CHEMONT.curie('atomically_connected_to'),
                   model_uri=CHEMONT.atomically_connected_to, domain=AtomOccurrence, range=Optional[Union[Union[dict, "AtomOccurrence"], List[Union[dict, "AtomOccurrence"]]]])

slots.is_organic = Slot(uri=CHEMONT.is_organic, name="is organic", curie=CHEMONT.curie('is_organic'),
                   model_uri=CHEMONT.is_organic, domain=ChemicalEntity, range=Optional[Union[bool, Bool]])

slots.is_radical = Slot(uri=CHEMONT.is_radical, name="is radical", curie=CHEMONT.curie('is_radical'),
                   model_uri=CHEMONT.is_radical, domain=ChemicalEntity, range=Optional[Union[bool, Bool]])

slots.next_in_homologous_series_from = Slot(uri=CHEMONT.next_in_homologous_series_from, name="next in homologous series from", curie=CHEMONT.curie('next_in_homologous_series_from'),
                   model_uri=CHEMONT.next_in_homologous_series_from, domain=Molecule, range=Optional[Union[str, MoleculeId]])

slots.chemical_isomer_of = Slot(uri=CHEMONT.chemical_isomer_of, name="chemical isomer of", curie=CHEMONT.curie('chemical_isomer_of'),
                   model_uri=CHEMONT.chemical_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.structural_isomer_of = Slot(uri=CHEMONT.structural_isomer_of, name="structural isomer of", curie=CHEMONT.curie('structural_isomer_of'),
                   model_uri=CHEMONT.structural_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.skeletal_isomer_of = Slot(uri=CHEMONT.skeletal_isomer_of, name="skeletal isomer of", curie=CHEMONT.curie('skeletal_isomer_of'),
                   model_uri=CHEMONT.skeletal_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.position_isomer_of = Slot(uri=CHEMONT.position_isomer_of, name="position isomer of", curie=CHEMONT.curie('position_isomer_of'),
                   model_uri=CHEMONT.position_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.functional_isomer_of = Slot(uri=CHEMONT.functional_isomer_of, name="functional isomer of", curie=CHEMONT.curie('functional_isomer_of'),
                   model_uri=CHEMONT.functional_isomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.tautomer_of = Slot(uri=CHEMONT.tautomer_of, name="tautomer of", curie=CHEMONT.curie('tautomer_of'),
                   model_uri=CHEMONT.tautomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.stereoisomer_of = Slot(uri=CHEMONT.stereoisomer_of, name="stereoisomer of", curie=CHEMONT.curie('stereoisomer_of'),
                   model_uri=CHEMONT.stereoisomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.diastereoisomers_of = Slot(uri=CHEMONT.diastereoisomers_of, name="diastereoisomers of", curie=CHEMONT.curie('diastereoisomers_of'),
                   model_uri=CHEMONT.diastereoisomers_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.epimer_of = Slot(uri=CHEMONT.epimer_of, name="epimer of", curie=CHEMONT.curie('epimer_of'),
                   model_uri=CHEMONT.epimer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.enantiomer_of = Slot(uri=CHEMONT.enantiomer_of, name="enantiomer of", curie=CHEMONT.curie('enantiomer_of'),
                   model_uri=CHEMONT.enantiomer_of, domain=Molecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.bond_order = Slot(uri=CHEMONT.bond_order, name="bond order", curie=CHEMONT.curie('bond_order'),
                   model_uri=CHEMONT.bond_order, domain=AtomicBond, range=Optional[int])

slots.bond_length = Slot(uri=CHEMONT.bond_length, name="bond length", curie=CHEMONT.curie('bond_length'),
                   model_uri=CHEMONT.bond_length, domain=AtomicBond, range=Optional[float])

slots.bond_energy = Slot(uri=CHEMONT.bond_energy, name="bond energy", curie=CHEMONT.curie('bond_energy'),
                   model_uri=CHEMONT.bond_energy, domain=AtomicBond, range=Optional[float])

slots.owl_subclass_of = Slot(uri=CHEMONT.owl_subclass_of, name="owl subclass of", curie=CHEMONT.curie('owl_subclass_of'),
                   model_uri=CHEMONT.owl_subclass_of, domain=None, range=Optional[Union[dict, "OwlClass"]])

slots.subtype_of = Slot(uri=CHEMONT.subtype_of, name="subtype of", curie=CHEMONT.curie('subtype_of'),
                   model_uri=CHEMONT.subtype_of, domain=None, range=Optional[Union[Union[dict, "OwlClass"], List[Union[dict, "OwlClass"]]]])

slots.has_subtype = Slot(uri=CHEMONT.has_subtype, name="has subtype", curie=CHEMONT.curie('has_subtype'),
                   model_uri=CHEMONT.has_subtype, domain=None, range=Optional[str])

slots.classified_by = Slot(uri=CHEMONT.classified_by, name="classified by", curie=CHEMONT.curie('classified_by'),
                   model_uri=CHEMONT.classified_by, domain=None, range=Optional[Union[dict, "OwlClass"]])

slots.classifies = Slot(uri=CHEMONT.classifies, name="classifies", curie=CHEMONT.curie('classifies'),
                   model_uri=CHEMONT.classifies, domain=None, range=Optional[str])

slots.has_morphological_category = Slot(uri=CHEMONT.has_morphological_category, name="has morphological category", curie=CHEMONT.curie('has_morphological_category'),
                   model_uri=CHEMONT.has_morphological_category, domain=None, range=Optional[Union[str, "NanostructureMorphologyEnum"]])

slots.polymer_of = Slot(uri=CHEMONT.polymer_of, name="polymer of", curie=CHEMONT.curie('polymer_of'),
                   model_uri=CHEMONT.polymer_of, domain=None, range=Optional[Union[str, MacromoleculeId]])

slots.is_substitutent_group_from = Slot(uri=CHEMONT.is_substitutent_group_from, name="is substitutent group from", curie=CHEMONT.curie('is_substitutent_group_from'),
                   model_uri=CHEMONT.is_substitutent_group_from, domain=None, range=Optional[Union[str, MoleculeId]])

slots.boiling_point_in_celcius = Slot(uri=CHEMONT.boiling_point_in_celcius, name="boiling point in celcius", curie=CHEMONT.curie('boiling_point_in_celcius'),
                   model_uri=CHEMONT.boiling_point_in_celcius, domain=None, range=Optional[float])

slots.melting_point_in_celcius = Slot(uri=CHEMONT.melting_point_in_celcius, name="melting point in celcius", curie=CHEMONT.curie('melting_point_in_celcius'),
                   model_uri=CHEMONT.melting_point_in_celcius, domain=None, range=Optional[float])

slots.standard_atomic_weight = Slot(uri=CHEMONT.standard_atomic_weight, name="standard atomic weight", curie=CHEMONT.curie('standard_atomic_weight'),
                   model_uri=CHEMONT.standard_atomic_weight, domain=None, range=Optional[float])

slots.electron_configuration = Slot(uri=CHEMONT.electron_configuration, name="electron configuration", curie=CHEMONT.curie('electron_configuration'),
                   model_uri=CHEMONT.electron_configuration, domain=None, range=Optional[str])

slots.has_stereocenter = Slot(uri=CHEMONT.has_stereocenter, name="has stereocenter", curie=CHEMONT.curie('has_stereocenter'),
                   model_uri=CHEMONT.has_stereocenter, domain=None, range=Optional[Union[Union[dict, Stereocenter], List[Union[dict, Stereocenter]]]])

slots.elemental_change = Slot(uri=CHEMONT.elemental_change, name="elemental change", curie=CHEMONT.curie('elemental_change'),
                   model_uri=CHEMONT.elemental_change, domain=None, range=Optional[str])

slots.type = Slot(uri=CHEMONT.type, name="type", curie=CHEMONT.curie('type'),
                   model_uri=CHEMONT.type, domain=None, range=Optional[Union[str, "PeriodicTableBlockEnum"]])

slots.bond_type = Slot(uri=CHEMONT.bond_type, name="bond type", curie=CHEMONT.curie('bond_type'),
                   model_uri=CHEMONT.bond_type, domain=None, range=Optional[Union[str, "BondTypeEnum"]])

slots.bond_length_in_angstroms = Slot(uri=CHEMONT.bond_length_in_angstroms, name="bond length in angstroms", curie=CHEMONT.curie('bond_length_in_angstroms'),
                   model_uri=CHEMONT.bond_length_in_angstroms, domain=None, range=Optional[float])

slots.bond_angle = Slot(uri=CHEMONT.bond_angle, name="bond angle", curie=CHEMONT.curie('bond_angle'),
                   model_uri=CHEMONT.bond_angle, domain=None, range=Optional[float])

slots.torsional_angle = Slot(uri=CHEMONT.torsional_angle, name="torsional angle", curie=CHEMONT.curie('torsional_angle'),
                   model_uri=CHEMONT.torsional_angle, domain=None, range=Optional[float])

slots.occurrence_of = Slot(uri=CHEMONT.occurrence_of, name="occurrence of", curie=CHEMONT.curie('occurrence_of'),
                   model_uri=CHEMONT.occurrence_of, domain=None, range=Union[str, AtomId])

slots.valence = Slot(uri=CHEMONT.valence, name="valence", curie=CHEMONT.curie('valence'),
                   model_uri=CHEMONT.valence, domain=None, range=Optional[int])

slots.oxidation_number = Slot(uri=CHEMONT.oxidation_number, name="oxidation number", curie=CHEMONT.curie('oxidation_number'),
                   model_uri=CHEMONT.oxidation_number, domain=None, range=Optional[int])

slots.formal_charge = Slot(uri=CHEMONT.formal_charge, name="formal charge", curie=CHEMONT.curie('formal_charge'),
                   model_uri=CHEMONT.formal_charge, domain=None, range=Optional[int])

slots.coordination_number = Slot(uri=CHEMONT.coordination_number, name="coordination number", curie=CHEMONT.curie('coordination_number'),
                   model_uri=CHEMONT.coordination_number, domain=None, range=Optional[int])

slots.acidity = Slot(uri=CHEMONT.acidity, name="acidity", curie=CHEMONT.curie('acidity'),
                   model_uri=CHEMONT.acidity, domain=None, range=Optional[float])

slots.hard_or_soft = Slot(uri=CHEMONT.hard_or_soft, name="hard or soft", curie=CHEMONT.curie('hard_or_soft'),
                   model_uri=CHEMONT.hard_or_soft, domain=None, range=Optional[Union[str, "HardOrSoftEnum"]])

slots.has_parent_alcohol = Slot(uri=CHEMONT.has_parent_alcohol, name="has parent alcohol", curie=CHEMONT.curie('has_parent_alcohol'),
                   model_uri=CHEMONT.has_parent_alcohol, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.has_parent_acid = Slot(uri=CHEMONT.has_parent_acid, name="has parent acid", curie=CHEMONT.curie('has_parent_acid'),
                   model_uri=CHEMONT.has_parent_acid, domain=None, range=Optional[Union[str, BronstedAcidId]])

slots.relative_configuration = Slot(uri=CHEMONT.relative_configuration, name="relative configuration", curie=CHEMONT.curie('relative_configuration'),
                   model_uri=CHEMONT.relative_configuration, domain=None, range=Optional[str])

slots.optical_configuration = Slot(uri=CHEMONT.optical_configuration, name="optical configuration", curie=CHEMONT.curie('optical_configuration'),
                   model_uri=CHEMONT.optical_configuration, domain=None, range=Optional[str])

slots.absolute_configuration = Slot(uri=CHEMONT.absolute_configuration, name="absolute configuration", curie=CHEMONT.curie('absolute_configuration'),
                   model_uri=CHEMONT.absolute_configuration, domain=None, range=Optional[str])

slots.enantiomer_form_of = Slot(uri=CHEMONT.enantiomer_form_of, name="enantiomer form of", curie=CHEMONT.curie('enantiomer_form_of'),
                   model_uri=CHEMONT.enantiomer_form_of, domain=None, range=Optional[Union[str, MoleculeId]])

slots.has_left_enantiomer = Slot(uri=CHEMONT.has_left_enantiomer, name="has left enantiomer", curie=CHEMONT.curie('has_left_enantiomer'),
                   model_uri=CHEMONT.has_left_enantiomer, domain=None, range=Union[str, EnantiomerId])

slots.has_right_enantiomer = Slot(uri=CHEMONT.has_right_enantiomer, name="has right enantiomer", curie=CHEMONT.curie('has_right_enantiomer'),
                   model_uri=CHEMONT.has_right_enantiomer, domain=None, range=Union[str, EnantiomerId])

slots.has_bonding_structure = Slot(uri=CHEMONT.has_bonding_structure, name="has bonding structure", curie=CHEMONT.curie('has_bonding_structure'),
                   model_uri=CHEMONT.has_bonding_structure, domain=None, range=str)

slots.left_participants = Slot(uri=CHEMONT.left_participants, name="left participants", curie=CHEMONT.curie('left_participants'),
                   model_uri=CHEMONT.left_participants, domain=None, range=Optional[Union[Union[dict, ReactionParticipant], List[Union[dict, ReactionParticipant]]]])

slots.right_participants = Slot(uri=CHEMONT.right_participants, name="right participants", curie=CHEMONT.curie('right_participants'),
                   model_uri=CHEMONT.right_participants, domain=None, range=Optional[Union[Union[dict, ReactionParticipant], List[Union[dict, ReactionParticipant]]]])

slots.direction = Slot(uri=CHEMONT.direction, name="direction", curie=CHEMONT.curie('direction'),
                   model_uri=CHEMONT.direction, domain=None, range=Optional[str])

slots.is_diastereoselective = Slot(uri=CHEMONT.is_diastereoselective, name="is diastereoselective", curie=CHEMONT.curie('is_diastereoselective'),
                   model_uri=CHEMONT.is_diastereoselective, domain=None, range=Optional[Union[bool, Bool]])

slots.is_stereo = Slot(uri=CHEMONT.is_stereo, name="is stereo", curie=CHEMONT.curie('is_stereo'),
                   model_uri=CHEMONT.is_stereo, domain=None, range=Optional[Union[bool, Bool]])

slots.is_balanced = Slot(uri=CHEMONT.is_balanced, name="is balanced", curie=CHEMONT.curie('is_balanced'),
                   model_uri=CHEMONT.is_balanced, domain=None, range=Optional[Union[bool, Bool]])

slots.is_transport = Slot(uri=CHEMONT.is_transport, name="is transport", curie=CHEMONT.curie('is_transport'),
                   model_uri=CHEMONT.is_transport, domain=None, range=Optional[Union[bool, Bool]])

slots.is_fully_characterized = Slot(uri=CHEMONT.is_fully_characterized, name="is fully characterized", curie=CHEMONT.curie('is_fully_characterized'),
                   model_uri=CHEMONT.is_fully_characterized, domain=None, range=Optional[Union[bool, Bool]])

slots.reaction_center = Slot(uri=CHEMONT.reaction_center, name="reaction center", curie=CHEMONT.curie('reaction_center'),
                   model_uri=CHEMONT.reaction_center, domain=None, range=Optional[str])

slots.description = Slot(uri=CHEMONT.description, name="description", curie=CHEMONT.curie('description'),
                   model_uri=CHEMONT.description, domain=None, range=Optional[str])

slots.participant = Slot(uri=CHEMONT.participant, name="participant", curie=CHEMONT.curie('participant'),
                   model_uri=CHEMONT.participant, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.stoichiometry = Slot(uri=CHEMONT.stoichiometry, name="stoichiometry", curie=CHEMONT.curie('stoichiometry'),
                   model_uri=CHEMONT.stoichiometry, domain=None, range=Optional[int])

slots.has_role = Slot(uri=CHEMONT.has_role, name="has role", curie=CHEMONT.curie('has_role'),
                   model_uri=CHEMONT.has_role, domain=None, range=Optional[Union[str, "IngredientRoleEnum"]])

slots.composed_of = Slot(uri=CHEMONT.composed_of, name="composed of", curie=CHEMONT.curie('composed_of'),
                   model_uri=CHEMONT.composed_of, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.minimal_percentage = Slot(uri=CHEMONT.minimal_percentage, name="minimal percentage", curie=CHEMONT.curie('minimal_percentage'),
                   model_uri=CHEMONT.minimal_percentage, domain=None, range=Optional[float])

slots.maximum_percentage = Slot(uri=CHEMONT.maximum_percentage, name="maximum percentage", curie=CHEMONT.curie('maximum_percentage'),
                   model_uri=CHEMONT.maximum_percentage, domain=None, range=Optional[float])

slots.left_molecule = Slot(uri=CHEMONT.left_molecule, name="left molecule", curie=CHEMONT.curie('left_molecule'),
                   model_uri=CHEMONT.left_molecule, domain=None, range=Optional[Union[str, MoleculeId]])

slots.right_molecule = Slot(uri=CHEMONT.right_molecule, name="right molecule", curie=CHEMONT.curie('right_molecule'),
                   model_uri=CHEMONT.right_molecule, domain=None, range=Optional[Union[str, MoleculeId]])

slots.score = Slot(uri=CHEMONT.score, name="score", curie=CHEMONT.curie('score'),
                   model_uri=CHEMONT.score, domain=None, range=Optional[str])

slots.grouping_class_subtype_of = Slot(uri=CHEMONT.subtype_of, name="grouping class_subtype of", curie=CHEMONT.curie('subtype_of'),
                   model_uri=CHEMONT.grouping_class_subtype_of, domain=GroupingClass, range=Optional[Union[Union[dict, "GroupingClass"], List[Union[dict, "GroupingClass"]]]])

slots.grouping_class_classifies = Slot(uri=CHEMONT.classifies, name="grouping class_classifies", curie=CHEMONT.curie('classifies'),
                   model_uri=CHEMONT.grouping_class_classifies, domain=GroupingClass, range=Optional[Union[str, ChemicalEntityId]])

slots.molecule_grouping_class_subtype_of = Slot(uri=CHEMONT.subtype_of, name="molecule grouping class_subtype of", curie=CHEMONT.curie('subtype_of'),
                   model_uri=CHEMONT.molecule_grouping_class_subtype_of, domain=MoleculeGroupingClass, range=Optional[Union[Union[dict, "MoleculeGroupingClass"], List[Union[dict, "MoleculeGroupingClass"]]]])

slots.molecule_grouping_class_classifies = Slot(uri=CHEMONT.classifies, name="molecule grouping class_classifies", curie=CHEMONT.curie('classifies'),
                   model_uri=CHEMONT.molecule_grouping_class_classifies, domain=MoleculeGroupingClass, range=Optional[Union[str, MoleculeId]])

slots.molecular_component_grouping_class_subtype_of = Slot(uri=CHEMONT.subtype_of, name="molecular component grouping class_subtype of", curie=CHEMONT.curie('subtype_of'),
                   model_uri=CHEMONT.molecular_component_grouping_class_subtype_of, domain=MolecularComponentGroupingClass, range=Optional[Union[Union[dict, "MolecularComponentGroupingClass"], List[Union[dict, "MolecularComponentGroupingClass"]]]])

slots.molecular_component_grouping_class_classifies = Slot(uri=CHEMONT.classifies, name="molecular component grouping class_classifies", curie=CHEMONT.curie('classifies'),
                   model_uri=CHEMONT.molecular_component_grouping_class_classifies, domain=MolecularComponentGroupingClass, range=Optional[Union[str, MolecularComponentId]])

slots.molecular_derivative_grouping_class_name = Slot(uri=CHEMONT.name, name="molecular derivative grouping class_name", curie=CHEMONT.curie('name'),
                   model_uri=CHEMONT.molecular_derivative_grouping_class_name, domain=MolecularDerivativeGroupingClass, range=Optional[str])

slots.molecular_derivative_grouping_class_classifies = Slot(uri=CHEMONT.classifies, name="molecular derivative grouping class_classifies", curie=CHEMONT.curie('classifies'),
                   model_uri=CHEMONT.molecular_derivative_grouping_class_classifies, domain=MolecularDerivativeGroupingClass, range=Optional[Union[str, MoleculeId]])

slots.molecule_grouping_class_defined_by_components_has_part = Slot(uri=CHEMONT.has_part, name="molecule grouping class defined by components_has part", curie=CHEMONT.curie('has_part'),
                   model_uri=CHEMONT.molecule_grouping_class_defined_by_components_has_part, domain=MoleculeGroupingClassDefinedByComponents, range=Optional[Union[dict, "ChemicalEntityOrGrouping"]])

slots.molecule_grouping_class_defined_by_addition_of_a_group_has_group = Slot(uri=CHEMONT.has_group, name="molecule grouping class defined by addition of a group_has group", curie=CHEMONT.curie('has_group'),
                   model_uri=CHEMONT.molecule_grouping_class_defined_by_addition_of_a_group_has_group, domain=MoleculeGroupingClassDefinedByAdditionOfAGroup, range=Optional[Union[Union[str, ChemicalGroupId], List[Union[str, ChemicalGroupId]]]])

slots.molecule_grouping_class_defined_by_addition_of_a_group_derivative_of = Slot(uri=CHEMONT.derivative_of, name="molecule grouping class defined by addition of a group_derivative of", curie=CHEMONT.curie('derivative_of'),
                   model_uri=CHEMONT.molecule_grouping_class_defined_by_addition_of_a_group_derivative_of, domain=MoleculeGroupingClassDefinedByAdditionOfAGroup, range=Optional[Union[str, PolyatomicEntityId]])

slots.chemical_salt_grouping_class_name = Slot(uri=CHEMONT.name, name="chemical salt grouping class_name", curie=CHEMONT.curie('name'),
                   model_uri=CHEMONT.chemical_salt_grouping_class_name, domain=ChemicalSaltGroupingClass, range=Optional[str])

slots.chemical_salt_grouping_class_classifies = Slot(uri=CHEMONT.classifies, name="chemical salt grouping class_classifies", curie=CHEMONT.curie('classifies'),
                   model_uri=CHEMONT.chemical_salt_grouping_class_classifies, domain=ChemicalSaltGroupingClass, range=Optional[Union[str, ChemicalSaltId]])

slots.chemical_salt_by_cation_name = Slot(uri=CHEMONT.name, name="chemical salt by cation_name", curie=CHEMONT.curie('name'),
                   model_uri=CHEMONT.chemical_salt_by_cation_name, domain=ChemicalSaltByCation, range=Optional[str])

slots.chemical_salt_by_anion_name = Slot(uri=CHEMONT.name, name="chemical salt by anion_name", curie=CHEMONT.curie('name'),
                   model_uri=CHEMONT.chemical_salt_by_anion_name, domain=ChemicalSaltByAnion, range=Optional[str])

slots.acid_anion_grouping_class_name = Slot(uri=CHEMONT.name, name="acid anion grouping class_name", curie=CHEMONT.curie('name'),
                   model_uri=CHEMONT.acid_anion_grouping_class_name, domain=AcidAnionGroupingClass, range=Optional[str],
                   pattern=re.compile(r'ate$'))

slots.acid_base_conflation_class_has_physiological_base = Slot(uri=CHEMONT.has_physiological_base, name="acid base conflation class_has physiological base", curie=CHEMONT.curie('has_physiological_base'),
                   model_uri=CHEMONT.acid_base_conflation_class_has_physiological_base, domain=AcidBaseConflationClass, range=Optional[Union[str, AcidBaseId]])

slots.atom_grouping_class_subtype_of = Slot(uri=CHEMONT.subtype_of, name="atom grouping class_subtype of", curie=CHEMONT.curie('subtype_of'),
                   model_uri=CHEMONT.atom_grouping_class_subtype_of, domain=AtomGroupingClass, range=Optional[Union[Union[dict, MoleculeGroupingClass], List[Union[dict, MoleculeGroupingClass]]]])

slots.atom_grouping_class_classifies = Slot(uri=CHEMONT.classifies, name="atom grouping class_classifies", curie=CHEMONT.curie('classifies'),
                   model_uri=CHEMONT.atom_grouping_class_classifies, domain=AtomGroupingClass, range=Optional[Union[str, AtomId]])

slots.material_has_part = Slot(uri=CHEMONT.has_part, name="material_has part", curie=CHEMONT.curie('has_part'),
                   model_uri=CHEMONT.material_has_part, domain=Material, range=Optional[Union[str, ChemicalEntityId]])

slots.nanostructure_has_morphological_category = Slot(uri=CHEMONT.has_morphological_category, name="nanostructure_has morphological category", curie=CHEMONT.curie('has_morphological_category'),
                   model_uri=CHEMONT.nanostructure_has_morphological_category, domain=Nanostructure, range=Optional[Union[str, "NanostructureMorphologyEnum"]])

slots.anion_state_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="anion state_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                   model_uri=CHEMONT.anion_state_elemental_charge, domain=None, range=Optional[int])

slots.cation_state_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="cation state_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                   model_uri=CHEMONT.cation_state_elemental_charge, domain=None, range=Optional[int])

slots.uncharged_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="uncharged_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                   model_uri=CHEMONT.uncharged_elemental_charge, domain=None, range=Optional[int])

slots.macromolecule_has_submolecules = Slot(uri=CHEMONT.has_submolecules, name="macromolecule_has submolecules", curie=CHEMONT.curie('has_submolecules'),
                   model_uri=CHEMONT.macromolecule_has_submolecules, domain=Macromolecule, range=Optional[Union[Union[str, MoleculeId], List[Union[str, MoleculeId]]]])

slots.monomolecular_polymer_polymer_of = Slot(uri=CHEMONT.polymer_of, name="monomolecular polymer_polymer of", curie=CHEMONT.curie('polymer_of'),
                   model_uri=CHEMONT.monomolecular_polymer_polymer_of, domain=MonomolecularPolymer, range=Optional[Union[str, MacromoleculeId]])

slots.copolymer_has_part = Slot(uri=CHEMONT.has_part, name="copolymer_has part", curie=CHEMONT.curie('has_part'),
                   model_uri=CHEMONT.copolymer_has_part, domain=Copolymer, range=Optional[Union[Union[str, MacromoleculeId], List[Union[str, MacromoleculeId]]]])

slots.molecule_has_atom_occurrences = Slot(uri=CHEMONT.has_atom_occurrences, name="molecule_has atom occurrences", curie=CHEMONT.curie('has_atom_occurrences'),
                   model_uri=CHEMONT.molecule_has_atom_occurrences, domain=Molecule, range=Optional[Union[Union[dict, "AtomOccurrence"], List[Union[dict, "AtomOccurrence"]]]])

slots.molecule_has_bonds = Slot(uri=CHEMONT.has_bonds, name="molecule_has bonds", curie=CHEMONT.curie('has_bonds'),
                   model_uri=CHEMONT.molecule_has_bonds, domain=Molecule, range=Optional[Union[Union[dict, "AtomicBond"], List[Union[dict, "AtomicBond"]]]])

slots.molecule_has_part = Slot(uri=CHEMONT.has_part, name="molecule_has part", curie=CHEMONT.curie('has_part'),
                   model_uri=CHEMONT.molecule_has_part, domain=Molecule, range=Optional[str])

slots.amino_acid_sequence_interval_has_sequence_representation = Slot(uri=CHEMONT.has_sequence_representation, name="amino acid sequence interval_has sequence representation", curie=CHEMONT.curie('has_sequence_representation'),
                   model_uri=CHEMONT.amino_acid_sequence_interval_has_sequence_representation, domain=AminoAcidSequenceInterval, range=Optional[str])

slots.nucleotide_sequence_interval_has_sequence_representation = Slot(uri=CHEMONT.has_sequence_representation, name="nucleotide sequence interval_has sequence representation", curie=CHEMONT.curie('has_sequence_representation'),
                   model_uri=CHEMONT.nucleotide_sequence_interval_has_sequence_representation, domain=NucleotideSequenceInterval, range=Optional[str])

slots.functional_group_is_substitutent_group_from = Slot(uri=CHEMONT.is_substitutent_group_from, name="functional group_is substitutent group from", curie=CHEMONT.curie('is_substitutent_group_from'),
                   model_uri=CHEMONT.functional_group_is_substitutent_group_from, domain=FunctionalGroup, range=Optional[Union[str, MoleculeId]])

slots.atom_has_part = Slot(uri=CHEMONT.has_part, name="atom_has part", curie=CHEMONT.curie('has_part'),
                   model_uri=CHEMONT.atom_has_part, domain=Atom, range=Optional[Union[str, SubatomicParticleId]])

slots.chemical_element_symbol = Slot(uri=CHEMONT.symbol, name="chemical element_symbol", curie=CHEMONT.curie('symbol'),
                   model_uri=CHEMONT.chemical_element_symbol, domain=ChemicalElement, range=Optional[str],
                   pattern=re.compile(r'^[A-Z][a-z]*'))

slots.chemical_element_in_periodic_table_group = Slot(uri=CHEMONT.in_periodic_table_group, name="chemical element_in periodic table group", curie=CHEMONT.curie('in_periodic_table_group'),
                   model_uri=CHEMONT.chemical_element_in_periodic_table_group, domain=ChemicalElement, range=Optional[int])

slots.chemical_element_in_periodic_table_block = Slot(uri=CHEMONT.in_periodic_table_block, name="chemical element_in periodic table block", curie=CHEMONT.curie('in_periodic_table_block'),
                   model_uri=CHEMONT.chemical_element_in_periodic_table_block, domain=ChemicalElement, range=Optional[Union[dict, "PeriodicTableBlock"]])

slots.chemical_element_boiling_point_in_celcius = Slot(uri=CHEMONT.boiling_point_in_celcius, name="chemical element_boiling point in celcius", curie=CHEMONT.curie('boiling_point_in_celcius'),
                   model_uri=CHEMONT.chemical_element_boiling_point_in_celcius, domain=ChemicalElement, range=Optional[float])

slots.chemical_element_melting_point_in_celcius = Slot(uri=CHEMONT.melting_point_in_celcius, name="chemical element_melting point in celcius", curie=CHEMONT.curie('melting_point_in_celcius'),
                   model_uri=CHEMONT.chemical_element_melting_point_in_celcius, domain=ChemicalElement, range=Optional[float])

slots.chemical_element_standard_atomic_weight = Slot(uri=CHEMONT.standard_atomic_weight, name="chemical element_standard atomic weight", curie=CHEMONT.curie('standard_atomic_weight'),
                   model_uri=CHEMONT.chemical_element_standard_atomic_weight, domain=ChemicalElement, range=Optional[float])

slots.chemical_element_electron_configuration = Slot(uri=CHEMONT.electron_configuration, name="chemical element_electron configuration", curie=CHEMONT.curie('electron_configuration'),
                   model_uri=CHEMONT.chemical_element_electron_configuration, domain=ChemicalElement, range=Optional[str])

slots.chemical_element_has_stereocenter = Slot(uri=CHEMONT.has_stereocenter, name="chemical element_has stereocenter", curie=CHEMONT.curie('has_stereocenter'),
                   model_uri=CHEMONT.chemical_element_has_stereocenter, domain=ChemicalElement, range=Optional[Union[Union[dict, "Stereocenter"], List[Union[dict, "Stereocenter"]]]])

slots.atom_ionic_form_elemental_change = Slot(uri=CHEMONT.elemental_change, name="atom ionic form_elemental change", curie=CHEMONT.curie('elemental_change'),
                   model_uri=CHEMONT.atom_ionic_form_elemental_change, domain=AtomIonicForm, range=Optional[str])

slots.atom_anion_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="atom anion_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                   model_uri=CHEMONT.atom_anion_elemental_charge, domain=AtomAnion, range=Optional[int])

slots.atom_cation_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="atom cation_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                   model_uri=CHEMONT.atom_cation_elemental_charge, domain=AtomCation, range=Optional[int])

slots.periodic_table_block_type = Slot(uri=CHEMONT.type, name="periodic table block_type", curie=CHEMONT.curie('type'),
                   model_uri=CHEMONT.periodic_table_block_type, domain=PeriodicTableBlock, range=Optional[Union[str, "PeriodicTableBlockEnum"]])

slots.standard_inchi_object_inchi_version_string = Slot(uri=CHEMONT.inchi_version_string, name="standard inchi object_inchi version string", curie=CHEMONT.curie('inchi_version_string'),
                   model_uri=CHEMONT.standard_inchi_object_inchi_version_string, domain=StandardInchiObject, range=str,
                   pattern=re.compile(r'^1S$'))

slots.atomic_bond_has_atom_occurrences = Slot(uri=CHEMONT.has_atom_occurrences, name="atomic bond_has atom occurrences", curie=CHEMONT.curie('has_atom_occurrences'),
                   model_uri=CHEMONT.atomic_bond_has_atom_occurrences, domain=AtomicBond, range=Optional[Union[Union[dict, "AtomOccurrence"], List[Union[dict, "AtomOccurrence"]]]])

slots.atomic_bond_bond_type = Slot(uri=CHEMONT.bond_type, name="atomic bond_bond type", curie=CHEMONT.curie('bond_type'),
                   model_uri=CHEMONT.atomic_bond_bond_type, domain=AtomicBond, range=Optional[Union[str, "BondTypeEnum"]])

slots.atomic_bond_bond_length_in_angstroms = Slot(uri=CHEMONT.bond_length_in_angstroms, name="atomic bond_bond length in angstroms", curie=CHEMONT.curie('bond_length_in_angstroms'),
                   model_uri=CHEMONT.atomic_bond_bond_length_in_angstroms, domain=AtomicBond, range=Optional[float])

slots.atomic_bond_bond_angle = Slot(uri=CHEMONT.bond_angle, name="atomic bond_bond angle", curie=CHEMONT.curie('bond_angle'),
                   model_uri=CHEMONT.atomic_bond_bond_angle, domain=AtomicBond, range=Optional[float])

slots.atomic_bond_torsional_angle = Slot(uri=CHEMONT.torsional_angle, name="atomic bond_torsional angle", curie=CHEMONT.curie('torsional_angle'),
                   model_uri=CHEMONT.atomic_bond_torsional_angle, domain=AtomicBond, range=Optional[float])

slots.atom_occurrence_occurrence_of = Slot(uri=CHEMONT.occurrence_of, name="atom occurrence_occurrence of", curie=CHEMONT.curie('occurrence_of'),
                   model_uri=CHEMONT.atom_occurrence_occurrence_of, domain=AtomOccurrence, range=Union[str, AtomId])

slots.atom_occurrence_valence = Slot(uri=CHEMONT.valence, name="atom occurrence_valence", curie=CHEMONT.curie('valence'),
                   model_uri=CHEMONT.atom_occurrence_valence, domain=AtomOccurrence, range=Optional[int])

slots.atom_occurrence_oxidation_number = Slot(uri=CHEMONT.oxidation_number, name="atom occurrence_oxidation number", curie=CHEMONT.curie('oxidation_number'),
                   model_uri=CHEMONT.atom_occurrence_oxidation_number, domain=AtomOccurrence, range=Optional[int])

slots.atom_occurrence_formal_charge = Slot(uri=CHEMONT.formal_charge, name="atom occurrence_formal charge", curie=CHEMONT.curie('formal_charge'),
                   model_uri=CHEMONT.atom_occurrence_formal_charge, domain=AtomOccurrence, range=Optional[int])

slots.atom_occurrence_coordination_number = Slot(uri=CHEMONT.coordination_number, name="atom occurrence_coordination number", curie=CHEMONT.curie('coordination_number'),
                   model_uri=CHEMONT.atom_occurrence_coordination_number, domain=AtomOccurrence, range=Optional[int])

slots.Bronsted_acid_acidity = Slot(uri=CHEMONT.acidity, name="Bronsted acid_acidity", curie=CHEMONT.curie('acidity'),
                   model_uri=CHEMONT.Bronsted_acid_acidity, domain=BronstedAcid, range=Optional[float])

slots.Bronsted_acid_hard_or_soft = Slot(uri=CHEMONT.hard_or_soft, name="Bronsted acid_hard or soft", curie=CHEMONT.curie('hard_or_soft'),
                   model_uri=CHEMONT.Bronsted_acid_hard_or_soft, domain=BronstedAcid, range=Optional[Union[str, "HardOrSoftEnum"]])

slots.Bronsted_acid_acid_form_of = Slot(uri=CHEMONT.acid_form_of, name="Bronsted acid_acid form of", curie=CHEMONT.curie('acid_form_of'),
                   model_uri=CHEMONT.Bronsted_acid_acid_form_of, domain=BronstedAcid, range=Optional[Union[Union[str, AcidBaseId], List[Union[str, AcidBaseId]]]])

slots.acid_base_has_acid_form = Slot(uri=CHEMONT.has_acid_form, name="acid base_has acid form", curie=CHEMONT.curie('has_acid_form'),
                   model_uri=CHEMONT.acid_base_has_acid_form, domain=AcidBase, range=Optional[Union[str, BronstedAcidId]])

slots.chemical_salt_elemental_charge = Slot(uri=CHEMONT.elemental_charge, name="chemical salt_elemental charge", curie=CHEMONT.curie('elemental_charge'),
                   model_uri=CHEMONT.chemical_salt_elemental_charge, domain=ChemicalSalt, range=Optional[int])

slots.chemical_salt_has_cationic_component = Slot(uri=CHEMONT.has_cationic_component, name="chemical salt_has cationic component", curie=CHEMONT.curie('has_cationic_component'),
                   model_uri=CHEMONT.chemical_salt_has_cationic_component, domain=ChemicalSalt, range=Optional[Union[dict, CationState]])

slots.chemical_salt_has_anionic_component = Slot(uri=CHEMONT.has_anionic_component, name="chemical salt_has anionic component", curie=CHEMONT.curie('has_anionic_component'),
                   model_uri=CHEMONT.chemical_salt_has_anionic_component, domain=ChemicalSalt, range=Optional[Union[dict, AnionState]])

slots.ester_has_parent_alcohol = Slot(uri=CHEMONT.has_parent_alcohol, name="ester_has parent alcohol", curie=CHEMONT.curie('has_parent_alcohol'),
                   model_uri=CHEMONT.ester_has_parent_alcohol, domain=Ester, range=Optional[Union[str, ChemicalEntityId]])

slots.ester_has_parent_acid = Slot(uri=CHEMONT.has_parent_acid, name="ester_has parent acid", curie=CHEMONT.curie('has_parent_acid'),
                   model_uri=CHEMONT.ester_has_parent_acid, domain=Ester, range=Optional[Union[str, BronstedAcidId]])

slots.enantiomer_relative_configuration = Slot(uri=CHEMONT.relative_configuration, name="enantiomer_relative configuration", curie=CHEMONT.curie('relative_configuration'),
                   model_uri=CHEMONT.enantiomer_relative_configuration, domain=Enantiomer, range=Optional[str])

slots.enantiomer_optical_configuration = Slot(uri=CHEMONT.optical_configuration, name="enantiomer_optical configuration", curie=CHEMONT.curie('optical_configuration'),
                   model_uri=CHEMONT.enantiomer_optical_configuration, domain=Enantiomer, range=Optional[str])

slots.enantiomer_absolute_configuration = Slot(uri=CHEMONT.absolute_configuration, name="enantiomer_absolute configuration", curie=CHEMONT.curie('absolute_configuration'),
                   model_uri=CHEMONT.enantiomer_absolute_configuration, domain=Enantiomer, range=Optional[str])

slots.enantiomer_enantiomer_form_of = Slot(uri=CHEMONT.enantiomer_form_of, name="enantiomer_enantiomer form of", curie=CHEMONT.curie('enantiomer_form_of'),
                   model_uri=CHEMONT.enantiomer_enantiomer_form_of, domain=Enantiomer, range=Optional[Union[str, MoleculeId]])

slots.racemic_mixture_has_left_enantiomer = Slot(uri=CHEMONT.has_left_enantiomer, name="racemic mixture_has left enantiomer", curie=CHEMONT.curie('has_left_enantiomer'),
                   model_uri=CHEMONT.racemic_mixture_has_left_enantiomer, domain=RacemicMixture, range=Union[str, EnantiomerId])

slots.racemic_mixture_has_right_enantiomer = Slot(uri=CHEMONT.has_right_enantiomer, name="racemic mixture_has right enantiomer", curie=CHEMONT.curie('has_right_enantiomer'),
                   model_uri=CHEMONT.racemic_mixture_has_right_enantiomer, domain=RacemicMixture, range=Union[str, EnantiomerId])

slots.allotrope_allotropic_analog_of = Slot(uri=CHEMONT.allotropic_analog_of, name="allotrope_allotropic analog of", curie=CHEMONT.curie('allotropic_analog_of'),
                   model_uri=CHEMONT.allotrope_allotropic_analog_of, domain=Allotrope, range=Union[str, ChemicalElementId])

slots.allotrope_has_bonding_structure = Slot(uri=CHEMONT.has_bonding_structure, name="allotrope_has bonding structure", curie=CHEMONT.curie('has_bonding_structure'),
                   model_uri=CHEMONT.allotrope_has_bonding_structure, domain=Allotrope, range=str)

slots.reaction_left_participants = Slot(uri=CHEMONT.left_participants, name="reaction_left participants", curie=CHEMONT.curie('left_participants'),
                   model_uri=CHEMONT.reaction_left_participants, domain=Reaction, range=Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]])

slots.reaction_right_participants = Slot(uri=CHEMONT.right_participants, name="reaction_right participants", curie=CHEMONT.curie('right_participants'),
                   model_uri=CHEMONT.reaction_right_participants, domain=Reaction, range=Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]])

slots.reaction_direction = Slot(uri=CHEMONT.direction, name="reaction_direction", curie=CHEMONT.curie('direction'),
                   model_uri=CHEMONT.reaction_direction, domain=Reaction, range=Optional[str])

slots.reaction_smarts_string = Slot(uri=CHEMONT.smarts_string, name="reaction_smarts string", curie=CHEMONT.curie('smarts_string'),
                   model_uri=CHEMONT.reaction_smarts_string, domain=Reaction, range=Optional[str])

slots.reaction_is_diastereoselective = Slot(uri=CHEMONT.is_diastereoselective, name="reaction_is diastereoselective", curie=CHEMONT.curie('is_diastereoselective'),
                   model_uri=CHEMONT.reaction_is_diastereoselective, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_stereo = Slot(uri=CHEMONT.is_stereo, name="reaction_is stereo", curie=CHEMONT.curie('is_stereo'),
                   model_uri=CHEMONT.reaction_is_stereo, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_balanced = Slot(uri=CHEMONT.is_balanced, name="reaction_is balanced", curie=CHEMONT.curie('is_balanced'),
                   model_uri=CHEMONT.reaction_is_balanced, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_transport = Slot(uri=CHEMONT.is_transport, name="reaction_is transport", curie=CHEMONT.curie('is_transport'),
                   model_uri=CHEMONT.reaction_is_transport, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_fully_characterized = Slot(uri=CHEMONT.is_fully_characterized, name="reaction_is fully characterized", curie=CHEMONT.curie('is_fully_characterized'),
                   model_uri=CHEMONT.reaction_is_fully_characterized, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_reaction_center = Slot(uri=CHEMONT.reaction_center, name="reaction_reaction center", curie=CHEMONT.curie('reaction_center'),
                   model_uri=CHEMONT.reaction_reaction_center, domain=Reaction, range=Optional[str])

slots.reaction_description = Slot(uri=CHEMONT.description, name="reaction_description", curie=CHEMONT.curie('description'),
                   model_uri=CHEMONT.reaction_description, domain=Reaction, range=Optional[str])

slots.reaction_participant_participant = Slot(uri=CHEMONT.participant, name="reaction participant_participant", curie=CHEMONT.curie('participant'),
                   model_uri=CHEMONT.reaction_participant_participant, domain=ReactionParticipant, range=Optional[Union[str, ChemicalEntityId]])

slots.reaction_participant_stoichiometry = Slot(uri=CHEMONT.stoichiometry, name="reaction participant_stoichiometry", curie=CHEMONT.curie('stoichiometry'),
                   model_uri=CHEMONT.reaction_participant_stoichiometry, domain=ReactionParticipant, range=Optional[int])

slots.proportional_part_has_role = Slot(uri=CHEMONT.has_role, name="proportional part_has role", curie=CHEMONT.curie('has_role'),
                   model_uri=CHEMONT.proportional_part_has_role, domain=ProportionalPart, range=Optional[Union[str, "IngredientRoleEnum"]])

slots.proportional_part_composed_of = Slot(uri=CHEMONT.composed_of, name="proportional part_composed of", curie=CHEMONT.curie('composed_of'),
                   model_uri=CHEMONT.proportional_part_composed_of, domain=ProportionalPart, range=Optional[Union[str, ChemicalEntityId]])

slots.proportional_part_minimal_percentage = Slot(uri=CHEMONT.minimal_percentage, name="proportional part_minimal percentage", curie=CHEMONT.curie('minimal_percentage'),
                   model_uri=CHEMONT.proportional_part_minimal_percentage, domain=ProportionalPart, range=Optional[float])

slots.proportional_part_maximum_percentage = Slot(uri=CHEMONT.maximum_percentage, name="proportional part_maximum percentage", curie=CHEMONT.curie('maximum_percentage'),
                   model_uri=CHEMONT.proportional_part_maximum_percentage, domain=ProportionalPart, range=Optional[float])

slots.molecule_pairwise_similarity_left_molecule = Slot(uri=CHEMONT.left_molecule, name="molecule pairwise similarity_left molecule", curie=CHEMONT.curie('left_molecule'),
                   model_uri=CHEMONT.molecule_pairwise_similarity_left_molecule, domain=MoleculePairwiseSimilarity, range=Optional[Union[str, MoleculeId]])

slots.molecule_pairwise_similarity_right_molecule = Slot(uri=CHEMONT.right_molecule, name="molecule pairwise similarity_right molecule", curie=CHEMONT.curie('right_molecule'),
                   model_uri=CHEMONT.molecule_pairwise_similarity_right_molecule, domain=MoleculePairwiseSimilarity, range=Optional[Union[str, MoleculeId]])

slots.molecule_pairwise_similarity_score = Slot(uri=CHEMONT.score, name="molecule pairwise similarity_score", curie=CHEMONT.curie('score'),
                   model_uri=CHEMONT.molecule_pairwise_similarity_score, domain=MoleculePairwiseSimilarity, range=Optional[str])

slots.tanimoto_similarity_score = Slot(uri=CHEMONT.score, name="tanimoto similarity_score", curie=CHEMONT.curie('score'),
                   model_uri=CHEMONT.tanimoto_similarity_score, domain=TanimotoSimilarity, range=Optional[float])
