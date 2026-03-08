#!/bin/bash
# Reproduce all figures from workflow scripts.
# Run from project root.
# Setup: install uv (https://docs.astral.sh/uv/) OR create venv and install deps:
#   python3 -m venv .venv && .venv/bin/pip install pandas matplotlib seaborn scikit-learn
set -e
cd "$(dirname "$0")"
PYTHON="${PYTHON:-python}"
if command -v uv &>/dev/null; then
  RUN="uv run python"
else
  RUN="${RUN:-.venv/bin/python}"
  if [ ! -x "$RUN" ]; then RUN=python3; fi
fi
echo "Running visualization pipeline (using: $RUN)..."
$RUN workflow/viz_1d_data.py
$RUN workflow/viz_2d_data.py
$RUN workflow/viz_1d_multi_method.py
$RUN workflow/viz_digits.py
echo "Done. Figures in figs/"
