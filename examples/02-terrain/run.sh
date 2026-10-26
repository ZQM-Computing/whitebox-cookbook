#!/usr/bin/env bash
# 02-terrain: slope, hillshade, and roughness from the synthetic plane DEM.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WBT="${WHITEBOX_TOOLS_BIN:-whitebox_tools}"
OUT_DIR="${1:-$DIR/build}"
mkdir -p "$OUT_DIR"

python3 "$DIR/gen_dem.py" "$OUT_DIR/dem.asc"
"$WBT" --run=Slope --dem="$OUT_DIR/dem.asc" --output="$OUT_DIR/slope.tif"
"$WBT" --run=Hillshade --dem="$OUT_DIR/dem.asc" --output="$OUT_DIR/hillshade.tif"
"$WBT" --run=Roughness --dem="$OUT_DIR/dem.asc" --output="$OUT_DIR/roughness.tif"
echo "Outputs written to $OUT_DIR: slope.tif hillshade.tif roughness.tif"
