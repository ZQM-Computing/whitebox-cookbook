#!/usr/bin/env bash
set -euo pipefail

output_path="${1:-build/whitebox-tools.txt}"
bin="${WHITEBOX_TOOLS_BIN:-whitebox_tools}"
if ! command -v "$bin" >/dev/null 2>&1 && [[ ! -x "$bin" ]]; then
  echo "ERROR: WhiteboxTools executable not found: $bin" >&2
  echo "Set WHITEBOX_TOOLS_BIN or add whitebox_tools to PATH." >&2
  exit 127
fi

mkdir -p "$(dirname "$output_path")"
{
  echo "## WhiteboxTools version"
  "$bin" --version
  echo
  echo "## Available tools"
  "$bin" --listtools
} >"$output_path" 2>&1

if [[ ! -s "$output_path" ]]; then
  echo "ERROR: WhiteboxTools produced no version/tool output" >&2
  exit 1
fi
printf 'Captured WhiteboxTools version and tool list to %s\n' "$output_path"
