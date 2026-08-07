#!/usr/bin/env bash
# =============================================================================
# RJ Unified Loop OS — Run Script
# Usage: ./scripts/run.sh --loop <loop-id> [--project <path>] [--stage <stage>]
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ENGINE="$PROJECT_ROOT/engine"

PROJECT="$PROJECT_ROOT"
LOOP=""
STAGE="all"
INPUTS=""
POLICY=""

usage() {
  cat <<EOF
Usage: run.sh --loop <LOOP_ID> [options]

Options:
  --loop <id>      Loop ID from loop-catalog.json (required)
  --project <path> Project directory (default: $PROJECT_ROOT)
  --stage <name>   Run specific stage (default: all)
  --inputs <path>  Input JSON file for the loop
  --policy <path>  Policy file (default: config/loop-policy.json)
  --list           List all available loops
  --describe       Show loop details
  --verify         Verify latest run without executing
  --init           Initialize a new run only (requires --inputs)
  -h, --help       Show this help

Examples:
  ./scripts/run.sh --list
  ./scripts/run.sh --describe --loop credit-dispute-case
  ./scripts/run.sh --init --loop credit-dispute-case --inputs case.json
  ./scripts/run.sh --loop credit-dispute-case
  ./scripts/run.sh --verify --loop credit-dispute-case
EOF
  exit 0
}

[[ $# -eq 0 ]] && usage

while [[ $# -gt 0 ]]; do
  case "$1" in
    --loop) LOOP="$2"; shift 2 ;;
    --project) PROJECT="$2"; shift 2 ;;
    --stage) STAGE="$2"; shift 2 ;;
    --inputs) INPUTS="$2"; shift 2 ;;
    --policy) POLICY="$2"; shift 2 ;;
    --list) COMMAND="list"; shift ;;
    --describe) COMMAND="describe"; shift ;;
    --verify) COMMAND="verify"; shift ;;
    --init) COMMAND="init"; shift ;;
    -h|--help) usage ;;
    *) echo "Unknown option: $1"; usage ;;
  esac
done

# Default to running the loop if no explicit command
COMMAND="${COMMAND:-run}"

# Set default policy
POLICY="${POLICY:-$PROJECT_ROOT/config/loop-policy.json}"

cd "$PROJECT_ROOT"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║         RJ UNIFIED LOOP OS v2.0 — Loop Runner          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

ARGS=(
  --project "$PROJECT"
  --catalog "$ENGINE/loop-catalog.json"
  --policy "$POLICY"
)

case "$COMMAND" in
  list)
    python3 "$ENGINE/loop_os.py" list "${ARGS[@]}"
    ;;
  describe)
    [[ -z "$LOOP" ]] && echo "Error: --loop required for describe" && exit 1
    python3 "$ENGINE/loop_os.py" describe "${ARGS[@]}" --loop "$LOOP"
    ;;
  init)
    [[ -z "$LOOP" ]] && echo "Error: --loop required for init" && exit 1
    [[ -z "$INPUTS" ]] && echo "Error: --inputs required for init" && exit 1
    python3 "$ENGINE/loop_os.py" init "${ARGS[@]}" --loop "$LOOP" --inputs "$INPUTS"
    ;;
  verify)
    [[ -z "$LOOP" ]] && echo "Error: --loop required for verify" && exit 1
    python3 "$ENGINE/loop_os.py" verify "${ARGS[@]}" --loop "$LOOP"
    ;;
  run)
    [[ -z "$LOOP" ]] && echo "Error: --loop required" && exit 1
    python3 "$ENGINE/loop_os.py" run "${ARGS[@]}" --loop "$LOOP" --stage "$STAGE"
    ;;
esac
