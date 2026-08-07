#!/usr/bin/env bash
# =============================================================================
# RJ Unified Loop OS — Install & Verify
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║       RJ UNIFIED LOOP OS v2.0 — Installer              ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Check Python
echo "[1/5] Checking Python..."
PYTHON=$(which python3 || which python || echo "")
if [[ -z "$PYTHON" ]]; then
  echo "  ERROR: Python 3 not found. Install Python 3.12+ and retry."
  exit 1
fi
PYVER=$($PYTHON --version 2>&1)
echo "  OK: $PYVER"

# Check directory structure
echo "[2/5] Verifying directory structure..."
REQUIRED_DIRS=("engine" "engine/schemas" "engine/templates" "autocode" "config" "agents" "prompts" "scripts" "tests")
MISSING=0
for d in "${REQUIRED_DIRS[@]}"; do
  if [[ ! -d "$PROJECT_ROOT/$d" ]]; then
    echo "  MISSING: $d"
    MISSING=1
  fi
done
if [[ $MISSING -eq 1 ]]; then
  echo "  ERROR: Required directories missing. Re-extract the project."
  exit 1
fi
echo "  OK: All directories present"

# Check core files
echo "[3/5] Verifying core engine files..."
REQUIRED_FILES=("engine/loop_os.py" "engine/research_build.py" "engine/experience_build.py" "engine/loop-catalog.json")
for f in "${REQUIRED_FILES[@]}"; do
  if [[ ! -f "$PROJECT_ROOT/$f" ]]; then
    echo "  MISSING: $f"
    MISSING=1
  fi
done
if [[ $MISSING -eq 1 ]]; then
  echo "  ERROR: Core engine files missing."
  exit 1
fi
echo "  OK: All core files present"

# Check config
echo "[4/5] Checking configuration..."
if [[ ! -f "$PROJECT_ROOT/config/loop-policy.json" ]]; then
  echo "  WARNING: config/loop-policy.json not found"
fi
if [[ ! -f "$PROJECT_ROOT/.env" ]]; then
  echo "  NOTE: No .env file found. Copy config/.env.example to .env and fill in your keys."
fi
echo "  OK: Config checked"

# Verify catalog loads
echo "[5/5] Verifying loop catalog..."
$PYTHON "$PROJECT_ROOT/engine/loop_os.py" list \
  --project "$PROJECT_ROOT" \
  --catalog "$PROJECT_ROOT/engine/loop-catalog.json" \
  --policy "$PROJECT_ROOT/config/loop-policy.json" > /dev/null 2>&1 && echo "  OK: Loop catalog loads successfully" || echo "  WARNING: Catalog validation may have issues"

echo ""
echo "════════════════════════════════════════════════════════════"
echo "  INSTALL COMPLETE"
echo ""
echo "  Next steps:"
echo "    1. cp config/.env.example .env   (fill in your API keys)"
echo "    2. ./scripts/run.sh --list       (see all loops)"
echo "    3. ./scripts/run.sh --loop <id>  (run a loop)"
echo "════════════════════════════════════════════════════════════"
