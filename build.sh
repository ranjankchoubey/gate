#!/bin/bash
# Local build: parse → generate HTML + PDF + QR
set -e

cd "$(dirname "$0")"

echo "=== Validating question bank ==="
python3 scripts/parse.py

echo ""
echo "=== Generating practice sets ==="
python3 scripts/generate.py

echo ""
echo "=== Done ==="
echo "Open: docs/discrete-math/lecture/counting-basics/index.html"
