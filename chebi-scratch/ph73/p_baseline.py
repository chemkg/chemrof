"""The last accepted rule set (frozen copy in data/baseline/), for --compare."""
import importlib.util

_spec = importlib.util.spec_from_file_location('protonation_baseline', 'data/baseline/protonation_baseline.py')
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
predict = _mod.predict_major_microspecies
