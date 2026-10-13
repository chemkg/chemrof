"""ChEBI enricher: resolve atoms, monoatomic ions and isotopes to CHEBI ids.

Resolution is offline, from the bundled table of ChEBI atomic species (see
``chemrof.converter.species``). Entities that are not single atoms are left
untouched; looking those up by InChIKey would need a live ChEBI/OLS query.

>>> from chemrof.converter.convert import ChemConverter
>>> obj = ChemConverter(enrichers=[ChebiEnricher()]).convert("[Fe+3]")
>>> obj["id"], obj["name"]
('CHEBI:29034', 'iron(3+)')
"""

from __future__ import annotations

import logging

from chemrof.converter.enrichers.base import EnrichmentContext
from chemrof.converter.species import lookup

logger = logging.getLogger(__name__)


class ChebiEnricher:
    """Sets ``id`` (and ``name``) of single-atom entities from ChEBI.

    The original InChIKey-based id is replaced; because other entities may refer
    to it (a salt to its ions), callers that enrich several linked entities
    should run :func:`chemrof.converter.enrichers.base.rewrite_references`
    afterwards -- the ``chemrof convert`` CLI does.
    """

    name = "chebi"

    def enrich(self, obj: dict, context: EnrichmentContext) -> dict:
        z = obj.get("atomic_number")
        if z is None:
            logger.debug("ChebiEnricher: %s is not a single atom, skipping", obj.get("id"))
            return obj

        neutrons = obj.get("neutron_number")
        mass_number = None if neutrons is None else z + neutrons
        species = lookup(z, obj.get("elemental_charge", 0), mass_number)
        if species is None:
            logger.debug("ChebiEnricher: no ChEBI class for %s", obj.get("id"))
            return obj

        obj["id"] = species.chebi_id
        obj["name"] = species.name
        return obj
