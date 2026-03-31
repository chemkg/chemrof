"""Convert chemrof dicts to OWL ontology axioms.

Each chemical entity becomes an OWL Class that is a SubClassOf its
chemrof type, with annotation assertions for the data properties.

>>> from chemrof.converter.smiles import SmilesConverter
>>> converter = SmilesConverter()
>>> obj = converter.convert("CCO")
>>> owl = dicts_to_owl([obj])
>>> "LFQSCWFLJHTTHZ" in owl
True
>>> "SubClassOf" in owl
True
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import pyhornedowl
from pyhornedowl import model
from linkml_runtime.utils.schemaview import SchemaView

_SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "chemrof.yaml"

_CHEMROF_NS = "https://w3id.org/chemrof/"
_RDFS_LABEL = "http://www.w3.org/2000/01/rdf-schema#label"

# Slots to emit as OWL annotation assertions.
_ANNOTATION_SLOTS = [
    "smiles_string",
    "inchi_string",
    "inchi_chemical_sublayer",
    "inchi_atom_connections_sublayer",
    "inchi_hydrogen_connections_sublayer",
    "inchi_charge_sublayer",
    "inchi_proton_sublayer",
    "inchi_stereochemical_double_bond_sublayer",
    "inchi_tetrahedral_stereochemical_sublayer",
    "inchi_stereochemical_type_sublayer",
    "inchi_isotopic_layer",
    "empirical_formula",
    "molecular_mass",
    "elemental_charge",
    "has_element",
    "is_organic",
    "is_radical",
]


@lru_cache(maxsize=1)
def _get_schemaview() -> SchemaView:
    return SchemaView(str(_SCHEMA_PATH))


def _resolve_id(raw_id: str) -> str:
    """Turn a chemrof ID like ``INCHIKEY:ABCDE...`` into a full IRI."""
    sv = _get_schemaview()
    for pfx in sv.schema.prefixes.values():
        prefix_str = pfx.prefix_prefix + ":"
        if raw_id.startswith(prefix_str):
            return pfx.prefix_reference + raw_id[len(prefix_str):]
    return _CHEMROF_NS + raw_id


def _resolve_slot(slot_name: str) -> str:
    """Turn a slot name into its full IRI via the schema."""
    sv = _get_schemaview()
    slot = sv.get_slot(slot_name)
    if slot and slot.slot_uri:
        uri = sv.get_uri(slot, expand=True)
        if uri:
            return str(uri)
    return _CHEMROF_NS + slot_name


def _ann_assertion(subject_iri: str, prop_iri: str, value: str) -> model.AnnotationAssertion:
    """Build an AnnotationAssertion axiom."""
    prop = model.AnnotationProperty(model.IRI.parse(prop_iri))
    ann = model.Annotation(prop, model.SimpleLiteral(value))
    return model.AnnotationAssertion(
        subject=model.IRI.parse(subject_iri),
        ann=ann,
    )


def dicts_to_owl(objs: list[dict], output_type: str = "ofn") -> str:
    """Convert chemrof dicts to an OWL ontology string.

    Each entity is emitted as an OWL Class with:
    - ``SubClassOf`` to its chemrof type (e.g. ``chemrof:SmallMolecule``)
    - ``rdfs:label`` from the ``name`` field
    - Annotation assertions for structural properties

    Args:
        objs: List of chemrof dicts (from SmilesConverter.convert()).
        output_type: Serialization format -- ``"ofn"`` (OWL Functional
            Syntax, default) or ``"owl"`` (RDF/XML).

    Returns:
        OWL string in the requested format.
    """
    ont = pyhornedowl.PyIndexedOntology()

    sv = _get_schemaview()
    for pfx in sv.schema.prefixes.values():
        ont.add_prefix_mapping(pfx.prefix_prefix, pfx.prefix_reference)

    for obj in objs:
        _add_entity(ont, obj)

    return ont.save_to_string(output_type)


def _add_entity(ont: pyhornedowl.PyIndexedOntology, obj: dict) -> None:
    """Add one chemrof dict as OWL axioms."""
    raw_id = obj.get("id", "")
    entity_iri = _resolve_id(raw_id)
    type_name = obj.get("type", "chemrof:SmallMolecule").replace("chemrof:", "")
    type_iri = _CHEMROF_NS + type_name

    # Declaration + SubClassOf
    ont.add_axiom(model.DeclareClass(model.Class(model.IRI.parse(entity_iri))))
    ont.add_axiom(model.DeclareClass(model.Class(model.IRI.parse(type_iri))))
    ont.add_axiom(model.SubClassOf(
        sub=model.Class(model.IRI.parse(entity_iri)),
        sup=model.Class(model.IRI.parse(type_iri)),
    ))

    # rdfs:label
    name = obj.get("name")
    if name:
        ont.add_axiom(_ann_assertion(entity_iri, _RDFS_LABEL, name))

    # Data property annotations
    for slot_name in _ANNOTATION_SLOTS:
        val = obj.get(slot_name)
        if val is not None:
            prop_iri = _resolve_slot(slot_name)
            ont.add_axiom(_ann_assertion(entity_iri, prop_iri, str(val)))
