"""Convert Maud kinetic-model TOML files into chemrof-compliant dicts.

`Maud <https://github.com/biosustain/Maud>`_ describes Bayesian kinetic models
of metabolism as TOML. This module maps the *structural* kinetic model onto
chemrof classes:

- ``[[metabolite]]``  -> ``SmallMolecule`` (a concrete ``ChemicalEntity``),
  keyed by InChIKey where available.
- ``[[reaction]]``    -> ``Reaction`` with ``left_participants`` /
  ``right_participants`` (``ReactionParticipant``), ``reaction_mechanism`` and
  ``direction``.
- ``[[allostery]]``   -> ``Reaction.has_allosteric_regulation``
  (``AllostericRegulation``).
- ``[[competitive_inhibition]]`` -> ``Reaction.has_competitive_inhibition``
  (``CompetitiveInhibition``).

The entities are returned inside a ``Collection`` (the chemrof tree-root
container).

Out of scope for this *structural* mapping: experiment data (measured
fluxes/concentrations, knockouts) and Bayesian priors (kcat/km/ki/dgf
distributions). These belong to the fluxomics modelling/experiment layer rather
than to the chemical reaction network.

>>> model = {
...     "metabolite": [
...         {"id": "met-L", "name": "methionine", "inchi_key": "FFEARJCKVFRZRR-BYPYZUCNSA-N"},
...         {"id": "amet", "name": "adenosyl methionine", "inchi_key": "MEFKEPWMEQBLKI-AIRLBKTGSA-O"},
...         {"id": "atp", "name": "ATP", "inchi_key": "ZKHQWZAMYRWXGA-KQYNXXCUSA-J"},
...         {"id": "pi", "name": "phosphate"},
...         {"id": "ppi", "name": "pyrophosphate"},
...     ],
...     "metabolite_in_compartment": [
...         {"metabolite_id": m, "compartment_id": "c"}
...         for m in ["met-L", "amet", "atp", "pi", "ppi"]
...     ],
...     "reaction": [
...         {
...             "id": "METAT", "name": "Methionine adenosyltransferase",
...             "mechanism": "irreversible_michaelis_menten",
...             "stoichiometry": {"met-L_c": -1.0, "atp_c": -1.0,
...                               "pi_c": 1.0, "ppi_c": 1.0, "amet_c": 1.0},
...         }
...     ],
...     "enzyme_reaction": [{"enzyme_id": "MAT1", "reaction_id": "METAT"}],
...     "competitive_inhibition": [
...         {"enzyme_id": "MAT1", "reaction_id": "METAT",
...          "metabolite_id": "amet", "compartment_id": "c"}
...     ],
... }
>>> coll = MaudConverter().convert_model(model)
>>> coll["entities"][0]["type"]
'chemrof:SmallMolecule'
>>> coll["entities"][0]["id"]
'INCHIKEY:FFEARJCKVFRZRR-BYPYZUCNSA-N'
>>> rxn = [e for e in coll["entities"] if e["type"] == "RXNO:0000000"][0]
>>> rxn["reaction_mechanism"]
'irreversible_michaelis_menten'
>>> sorted(p["participant"] for p in rxn["left_participants"])
['INCHIKEY:FFEARJCKVFRZRR-BYPYZUCNSA-N', 'INCHIKEY:ZKHQWZAMYRWXGA-KQYNXXCUSA-J']
>>> rxn["has_competitive_inhibition"][0]["effector"]
'INCHIKEY:MEFKEPWMEQBLKI-AIRLBKTGSA-O'
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import toml

_TYPE_PREFIX = "chemrof:"

# chemrof type designators (the `type` slot uses each class's class_uri where one
# is defined, otherwise the chemrof CURIE). Reaction carries class_uri
# RXNO:0000000; SmallMolecule has no explicit class_uri.
_SMALL_MOLECULE_TYPE = f"{_TYPE_PREFIX}SmallMolecule"
_REACTION_TYPE = "RXNO:0000000"

# Maud mechanism strings that map onto chemrof ReactionMechanismEnum values.
_MECHANISMS = {
    "reversible_michaelis_menten",
    "irreversible_michaelis_menten",
    "mass_action",
    "drain",
}

# Mechanisms that imply a bidirectional reaction.
_REVERSIBLE_MECHANISMS = {"reversible_michaelis_menten", "mass_action"}


class MaudConverter:
    """Convert a parsed Maud kinetic model into chemrof-compliant dicts."""

    def convert_file(self, path: str | Path) -> dict[str, Any]:
        """Read a Maud TOML file and convert it.

        Accepts either a kinetic-model file (containing ``[[reaction]]``) or a
        Maud ``config.toml`` that references one via ``kinetic_model_file``; in
        the latter case the referenced file is resolved relative to the config.
        """
        path = Path(path)
        data = toml.load(path)
        if "reaction" not in data and "kinetic_model_file" in data:
            data = toml.load(path.parent / data["kinetic_model_file"])
        return self.convert_model(data)

    def convert_model(self, model: dict[str, Any]) -> dict[str, Any]:
        """Convert an already-parsed Maud kinetic model dict to a Collection."""
        metabolite_id = self._metabolite_id_map(model)
        mic_to_metabolite = self._mic_to_metabolite_map(model)
        enzyme_to_reaction = {
            er["enzyme_id"]: er["reaction_id"]
            for er in model.get("enzyme_reaction", [])
        }

        entities: list[dict[str, Any]] = [
            self._metabolite_entity(m, metabolite_id)
            for m in model.get("metabolite", [])
        ]

        reactions: dict[str, dict[str, Any]] = {}
        for rxn in model.get("reaction", []):
            entity = self._reaction_entity(rxn, metabolite_id, mic_to_metabolite)
            reactions[rxn["id"]] = entity
            entities.append(entity)

        self._attach_regulation(
            model, reactions, enzyme_to_reaction, metabolite_id
        )

        return {"entities": entities}

    # -- helpers ---------------------------------------------------------

    def _metabolite_id_map(self, model: dict[str, Any]) -> dict[str, str]:
        """Map each Maud metabolite id to a chemrof entity id (InChIKey-based)."""
        out: dict[str, str] = {}
        for m in model.get("metabolite", []):
            key = m.get("inchi_key")
            out[m["id"]] = (
                f"INCHIKEY:{key}" if key else f"maud.metabolite:{m['id']}"
            )
        return out

    def _mic_to_metabolite_map(self, model: dict[str, Any]) -> dict[str, str]:
        """Map ``metabolite-in-compartment`` ids (e.g. ``met-L_c``) to metabolite ids."""
        out: dict[str, str] = {}
        for mic in model.get("metabolite_in_compartment", []):
            mic_id = f"{mic['metabolite_id']}_{mic['compartment_id']}"
            out[mic_id] = mic["metabolite_id"]
        return out

    def _resolve_participant(
        self,
        mic_id: str,
        metabolite_id: dict[str, str],
        mic_to_metabolite: dict[str, str],
    ) -> str:
        """Resolve a stoichiometry key to a chemrof metabolite id."""
        met = mic_to_metabolite.get(mic_id)
        if met is None:
            # Fall back to stripping a trailing _<compartment> suffix.
            met = mic_id.rsplit("_", 1)[0]
        return metabolite_id.get(met, f"maud.metabolite:{met}")

    def _metabolite_entity(
        self, m: dict[str, Any], metabolite_id: dict[str, str]
    ) -> dict[str, Any]:
        entity: dict[str, Any] = {
            "id": metabolite_id[m["id"]],
            "type": _SMALL_MOLECULE_TYPE,
        }
        if m.get("name"):
            entity["name"] = m["name"]
        if m.get("inchi_key"):
            entity["inchi_key_string"] = m["inchi_key"]
        return entity

    def _reaction_entity(
        self,
        rxn: dict[str, Any],
        metabolite_id: dict[str, str],
        mic_to_metabolite: dict[str, str],
    ) -> dict[str, Any]:
        left: list[dict[str, Any]] = []
        right: list[dict[str, Any]] = []
        for mic_id, coeff in rxn.get("stoichiometry", {}).items():
            participant = {
                "participant": self._resolve_participant(
                    mic_id, metabolite_id, mic_to_metabolite
                ),
                "stoichiometry": abs(float(coeff)),
            }
            (left if coeff < 0 else right).append(participant)

        entity: dict[str, Any] = {
            "id": f"maud.reaction:{rxn['id']}",
            "type": _REACTION_TYPE,
        }
        if rxn.get("name"):
            entity["name"] = rxn["name"]

        mechanism = rxn.get("mechanism")
        if mechanism in _MECHANISMS:
            entity["reaction_mechanism"] = mechanism
        entity["direction"] = (
            "bidirectional" if mechanism in _REVERSIBLE_MECHANISMS else "l->r"
        )
        if left:
            entity["left_participants"] = left
        if right:
            entity["right_participants"] = right
        return entity

    def _attach_regulation(
        self,
        model: dict[str, Any],
        reactions: dict[str, dict[str, Any]],
        enzyme_to_reaction: dict[str, str],
        metabolite_id: dict[str, str],
    ) -> None:
        for allo in model.get("allostery", []):
            rid = enzyme_to_reaction.get(allo["enzyme_id"])
            rxn = reactions.get(rid)
            if rxn is None:
                continue
            reg = {
                "effector": metabolite_id.get(
                    allo["metabolite_id"],
                    f"maud.metabolite:{allo['metabolite_id']}",
                ),
                "regulated_enzyme": allo["enzyme_id"],
                "modification_type": allo["modification_type"],
            }
            rxn.setdefault("has_allosteric_regulation", []).append(reg)

        for ci in model.get("competitive_inhibition", []):
            rid = ci.get("reaction_id") or enzyme_to_reaction.get(ci["enzyme_id"])
            rxn = reactions.get(rid)
            if rxn is None:
                continue
            reg = {
                "effector": metabolite_id.get(
                    ci["metabolite_id"], f"maud.metabolite:{ci['metabolite_id']}"
                ),
                "regulated_enzyme": ci["enzyme_id"],
            }
            rxn.setdefault("has_competitive_inhibition", []).append(reg)


def convert_maud_file(path: str | Path) -> dict[str, Any]:
    """Convenience wrapper: convert a Maud TOML file to a chemrof Collection dict."""
    return MaudConverter().convert_file(path)
