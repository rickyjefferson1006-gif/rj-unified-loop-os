#!/usr/bin/env bash
# =============================================================================
# RJ Unified Loop OS — Autocode Generator Runner
# Usage: ./scripts/run-autocode.sh <template> [output_path]
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
AUTOCODE_DIR="$PROJECT_ROOT/autocode"

usage() {
  echo "Usage: run-autocode.sh <template> [output_path]"
  echo ""
  echo "Available templates:"
  for f in "$AUTOCODE_DIR"/*.md; do
    name=$(basename "$f" .md)
    echo "  $name"
  done
  echo ""
  echo "Examples:"
  echo "  ./scripts/run-autocode.sh blog ./output/blog-post.md"
  echo "  ./scripts/run-autocode.sh funnel ./output/landing-page.md"
  exit 0
}

[[ $# -eq 0 || "$1" == "-h" || "$1" == "--help" ]] && usage

TEMPLATE="$1"
TEMPLATE_PATH="$AUTOCODE_DIR/$TEMPLATE.md"

if [[ ! -f "$TEMPLATE_PATH" ]]; then
  echo "Error: Template '$TEMPLATE' not found in autocode/"
  echo "Run with no arguments to see available templates."
  exit 1
fi

OUTPUT="${2:-$PROJECT_ROOT/output/$TEMPLATE-output.md}"
mkdir -p "$(dirname "$OUTPUT")"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║         RJ AUTOCODE GENERATOR                           ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "  Template: $TEMPLATE"
echo "  Source:   $TEMPLATE_PATH"
echo "  Output:   $OUTPUT"
echo ""

echo "--- TEMPLATE PREVIEW (first 20 lines) ---"
head -20 "$TEMPLATE_PATH"
echo "..."
echo "--- END PREVIEW ---"
echo ""

echo "To use this template with an AI agent, run:"
echo "  vibe --prompt \"\$(cat $TEMPLATE_PATH)\" --output $OUTPUT"
echo ""
echo "Or manually copy the template and paste into your AI coding tool."
