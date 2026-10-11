#!/bin/sh
# One hill-climbing check: working-tree rules (p_chemrof) vs the last accepted
# copy (p_baseline). Accept only if Rhea dev and IUPAC dev show no significant
# regression and at least one shows a gain beyond noise (see README).
export PYTHONPATH=../../src
for s in train dev; do
  echo "== Rhea $s"; uv run --frozen python evalr.py p_chemrof --split $s --compare p_baseline | grep -E "paired|rows"
done
for s in train dev; do
  echo "== IUPAC $s"; uv run --frozen python iupac_eval.py compare p_chemrof p_baseline --split $s | tail -2
done
