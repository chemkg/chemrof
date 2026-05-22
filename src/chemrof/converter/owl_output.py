"""Convert chemrof dicts to OWL ontology via linkml-owl.

Each chemical entity is adapted to a minimal LinkML instance, then handed to
``linkml_owl.dumpers.OWLDumper``. The OWL interpretation is defined by
annotations in ``chemrof.yaml``.

>>> from chemrof.converter.convert import ChemConverter
>>> obj = ChemConverter().convert("CCO")
>>> owl = dicts_to_owl([obj])
>>> "CCO" in owl
True
>>> "SubClassOf" in owl
True
"""

from __future__ import annotations

import logging
from contextlib import contextmanager
from functools import lru_cache
from pathlib import Path

from linkml_owl.dumpers.owl_dumper import OWLDumper
from linkml_runtime.utils.schemaview import SchemaView

_SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "chemrof.yaml"


@lru_cache(maxsize=1)
def _get_schemaview() -> SchemaView:
    return SchemaView(str(_SCHEMA_PATH))


@lru_cache(maxsize=None)
def _instance_class(class_name: str):
    """Create a tiny object class that looks like a LinkML runtime class."""

    return type(class_name, (), {"class_name": class_name})


def _raw_id(value) -> str | None:
    """Extract a CURIE/ID string from a scalar or inlined object."""
    if isinstance(value, dict):
        return value.get("id")
    return str(value) if value is not None else None


def _class_name(obj: dict) -> str:
    """Return the LinkML class name for a converter object."""
    typ = obj.get("type")
    if typ:
        return str(typ).split(":")[-1]
    return "SmallMolecule"


def _is_empty(value) -> bool:
    return value is None or value == [] or value == {}


def _normalize_value(value):
    """Normalize inlined references to identifiers before linkml-owl sees them."""
    if isinstance(value, list):
        return [_normalize_value(v) for v in value if not _is_empty(v)]
    if isinstance(value, dict):
        raw_id = _raw_id(value)
        if raw_id:
            return raw_id
    return value


def _to_linkml_instance(obj: dict):
    """Adapt a converter dict to the minimal object protocol used by OWLDumper."""
    sv = _get_schemaview()
    class_name = _class_name(obj)
    slot_names = {slot.name for slot in sv.class_induced_slots(class_name)}
    instance = _instance_class(class_name)()
    for key, value in obj.items():
        if key == "type" or key not in slot_names or _is_empty(value):
            continue
        setattr(instance, key, _normalize_value(value))
    return instance


@contextmanager
def _suppress_namespace_warnings():
    """Avoid leaking LinkML namespace remapping warnings into CLI OWL output."""
    logger = logging.getLogger("linkml_runtime.Namespaces")
    old_level = logger.level
    logger.setLevel(logging.ERROR)
    try:
        yield
    finally:
        logger.setLevel(old_level)


def dicts_to_owl(objs: list[dict], output_type: str = "ofn") -> str:
    """Convert chemrof dicts to an OWL ontology string.

    Uses linkml-owl OWLDumper with schema annotations to produce OWL axioms,
    including ChemOnt ``classified_by`` values as ``SubClassOf`` axioms.

    Args:
        objs: List of chemrof dicts from the converter.
        output_type: ``"ofn"`` (OWL Functional Syntax) or ``"owl"`` (RDF/XML).

    Returns:
        OWL string in the requested format.
    """
    sv = _get_schemaview()
    elements = [_to_linkml_instance(obj) for obj in objs]
    dumper = OWLDumper()
    with _suppress_namespace_warnings():
        return dumper.dumps(elements, schemaview=sv, output_type=output_type)
