"""Audit every rule of a protonation module's RuleSet against the experimental data.

    python audit_rules.py [chemrof.converter.protonation | chemrof.converter.protonation_cleanroom]
"""
import importlib, sys
from audit_exp import load, audit

name = sys.argv[1] if len(sys.argv) > 1 else 'chemrof.converter.protonation'
mod = importlib.import_module(name)
rules = getattr(mod, 'CLEANROOM_RULES', None) or mod.DEFAULT_RULES
d = load()
print('single-site molecules:', len(d))
groups = [('ACID ' + n, s) for n, s, _ in rules.acids]
groups += [('AMINE (generic)', rules.amine)]
groups += [('WEAK AMINE', s) for s in rules.weak_amines]
groups += [('AMIDINE-type', s) for s in rules.amidines]
groups += [(k, s) for k, s in (('CYCLIC DIKETONE', rules.cyclic_diketone), ('TROPOLONE', rules.tropolone),
                               ('IMINO ACID', rules.imino_acid)) if s]
for label, s in groups:
    print('##', label)
    print(audit(d, s))
