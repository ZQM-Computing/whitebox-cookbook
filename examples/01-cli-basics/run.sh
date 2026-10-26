#!/usr/bin/env bash
# 01-cli-basics: version, tool list, and one tool's help.
# Set WHITEBOX_TOOLS to the full binary path if it is not on PATH
# (fleet Node-1 extract dir: C:\WhiteboxTools).
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WBT="${WHITEBOX_TOOLS:-whitebox_tools}"
bash "$DIR/inspect-cli.sh" "$DIR/build/whitebox-tools.txt"
"$WBT" --help
"$WBT" --run=Slope --help
