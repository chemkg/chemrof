"""Convert chemrof dicts to OWL ontology via linkml-data2owl.

Uses the OWLDumper from linkml-owl with the annotated chemrof schema
to generate proper OWL axioms including EquivalentClasses for types
that have owl.template annotations (MonoatomicIon, Enantiomer,
RacemicMixture).

>>> from chemrof.converter.convert import ChemConverter
>>> obj = ChemConverter().convert("CCO")
>>> owl = dicts_to_owl([obj])
>>> "CCO" in owl
True
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView
from linkml_owl.dumpers.owl_dumper import OWLDumper

import chemrof.schema.chemrof as chemrof_module

_SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "chemrof.yaml"

# Map converter entity type names to generated Python classes
_CLASS_MAP = {
    "SmallMolecule": chemrof_module.SmallMolecule,
    "AtomCation": chemrof_module.AtomCation,
    "AtomAnion": chemrof_module.AtomAnion,
    "MonoatomicIon": chemrof_module.MonoatomicIon,
    "MolecularCation": chemrof_module.MolecularCation,
    "MolecularAnion": chemrof_module.MolecularAnion,
    "UnchargedAtom": chemrof_module.UnchargedAtom,
    "Enantiomer": chemrof_module.Enantiomer,
    "RacemicMixture": chemrof_module.RacemicMixture,
}


@lru_cache(maxsize=1)
def _get_schemaview() -> SchemaView:
    return SchemaView(str(_SCHEMA_PATH))


def _dict_to_instance(obj: dict):
    """Convert a chemrof dict to a linkml runtime instance."""
    import dataclasses

    type_name = obj.get("type", "chemrof:SmallMolecule").replace("chemrof:", "")
    cls = _CLASS_MAP.get(type_name)
    if cls is None:
        cls = chemrof_module.SmallMolecule

    sv = _get_schemaview()
    valid_slots = {s.name for s in sv.class_induced_slots(type_name)}
    field_names = {f.name for f in dataclasses.fields(cls)}

    # Build kwargs for all fields the class accepts
    kwargs = {}
    for key, value in obj.items():
        if key == "type":
            continue
        if key in field_names and key in valid_slots:
            kwargs[key] = value
        elif key in ("id", "name") and key in field_names:
            kwargs[key] = value

    return cls(**kwargs)


def dicts_to_owl(objs: list[dict], output_type: str = "ofn") -> str:
    """Convert chemrof dicts to an OWL ontology string.

    Uses linkml-owl OWLDumper with schema annotations to produce
    EquivalentClasses axioms for annotated types and SubClassOf +
    AnnotationAssertions for others.

    Args:
        objs: List of chemrof dicts (from ChemConverter).
        output_type: ``"ofn"`` (OWL Functional Syntax) or ``"owl"`` (RDF/XML).

    Returns:
        OWL string in the requested format.
    """
    sv = _get_schemaview()
    dumper = OWLDumper()
    dumper.schemaview = sv

    instances = [_dict_to_instance(obj) for obj in objs]
    ont = dumper.to_ontology_document(instances, sv.schema)
    return ont.save_to_string(output_type)
