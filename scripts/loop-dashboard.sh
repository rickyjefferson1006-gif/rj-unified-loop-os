#!/usr/bin/env bash
# =============================================================================
# RJ Unified Loop OS — Dashboard
# Shows all loop statuses across the project
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║           RJ UNIFIED LOOP OS — DASHBOARD                       ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

# Show catalog summary
echo "━━━ LOOP CATALOG ━━━"
python3 "$PROJECT_ROOT/engine/loop_os.py" list \
  --project "$PROJECT_ROOT" \
  --catalog "$PROJECT_ROOT/engine/loop-catalog.json" \
  --policy "$PROJECT_ROOT/config/loop-policy.json" 2>/dev/null | \
  python3 -c "
import json, sys
data = json.load(sys.stdin)
print(f'  Total loops: {len(data[\"loops\"])}')
for loop in data['loops']:
    print(f'  [{loop[\"risk\"].upper():8s}] {loop[\"id\"]:40s} {loop[\"cadence\"]}')
"

echo ""
echo "━━━ ACTIVE RUNS ━━━"
LOOP_OS_DIR="$PROJECT_ROOT/.loop-os"
if [[ -d "$LOOP_OS_DIR" ]]; then
  for loop_dir in "$LOOP_OS_DIR"/*/; do
    loop_name=$(basename "$loop_dir")
    run_count=$(ls "$loop_dir" 2>/dev/null | wc -l | tr -d ' ')
    echo "  $loop_name: $run_count run(s)"
    latest=$(ls -t "$loop_dir" 2>/dev/null | head -1)
    if [[ -n "$latest" && -f "$loop_dir/$latest/run.json" ]]; then
      status=$(python3 -c "import json; d=json.load(open('$loop_dir/$latest/run.json')); print(d.get('status','unknown'))" 2>/dev/null || echo "error")
      echo "    Latest: $latest → $status"
    fi
  done
else
  echo "  No runs yet. Initialize one with: ./scripts/run.sh --init --loop <id> --inputs <file>"
fi

echo ""
echo "━━━ QUICK COMMANDS ━━━"
echo "  List all loops:      ./scripts/run.sh --list"
echo "  Describe a loop:     ./scripts/run.sh --describe --loop <id>"
echo "  Run a loop:          ./scripts/run.sh --loop <id>"
echo "  Verify latest run:   ./scripts/run.sh --verify --loop <id>"
echo "  Run autocode:        ./scripts/run-autocode.sh <template>"
