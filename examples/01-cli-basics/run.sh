#!/usr/bin/env bash
# 01-cli-basics: version, tool list, and one tool's help.
# Set WHITEBOX_TOOLS to the full binary path if it is not on PATH
# (fleet Node-1 extract dir: C:\WhiteboxTools).
set -euo pipefail
WBT="${WHITEBOX_TOOLS:-whitebox_tools}"
"$WBT" --version
"$WBT" --help
"$WBT" --run=Slope --help
