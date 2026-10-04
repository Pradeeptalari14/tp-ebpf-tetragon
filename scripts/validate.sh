#!/usr/bin/env bash
set -euo pipefail
echo "Validating Tetragon policies..."
grep -q "kind: TracingPolicy" tracingpolicy-k8s.yaml
python3 -m py_compile tetragon_siem_bridge.py
echo "✓ Validation clean."
