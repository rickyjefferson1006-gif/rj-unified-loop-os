#!/usr/bin/env bash
# RJ Unified Loop OS — make all scripts executable
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
chmod +x "$SCRIPT_DIR/run.sh" "$SCRIPT_DIR/run-autocode.sh" "$SCRIPT_DIR/install.sh" "$SCRIPT_DIR/loop-dashboard.sh"
echo "All scripts executable"
