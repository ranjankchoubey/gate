#!/bin/bash
# Local build: parse → generate HTML + PDF + QR
set -e

cd "$(dirname "$0")"

# Activate venv automatically
if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
fi

echo "=== Validating question bank ==="
python3 scripts/parse.py

echo ""
echo "=== Generating practice sets ==="
python3 scripts/generate.py

echo ""
echo "=== Done ==="
echo "Open: docs/gate-da-prob-stats/lecture/01-counting-combinatorics/index.html"
