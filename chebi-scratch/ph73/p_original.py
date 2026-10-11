"""The rule set as first committed (355d3cf) (frozen copy in data/baseline/), for --compare."""
import importlib.util

_spec = importlib.util.spec_from_file_location('protonation_original', 'data/baseline/protonation_original.py')
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
predict = _mod.predict_major_microspecies
