#!/usr/bin/env bash
# 03-hydro: fill, flow direction, accumulation, and watershed extraction.
# Outlet is the center of row 5, column 9 (0-based from the north-west).
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WBT="${WHITEBOX_TOOLS:-whitebox_tools}"
OUT_DIR="${1:-$DIR/build}"
mkdir -p "$OUT_DIR"

python3 "$DIR/gen_dem.py" "$OUT_DIR/dem.asc"
python3 "$DIR/gen_outlet.py" "$OUT_DIR/outlet"
"$WBT" --run=FillDepressions --dem="$OUT_DIR/dem.asc" --output="$OUT_DIR/dem_filled.asc"
python3 "$DIR/check_fill.py" "$OUT_DIR/dem.asc" "$OUT_DIR/dem_filled.asc"
"$WBT" --run=D8Pointer --dem="$OUT_DIR/dem_filled.asc" --output="$OUT_DIR/d8pntr.tif"
"$WBT" --run=D8FlowAccum --pntr="$OUT_DIR/d8pntr.tif" --output="$OUT_DIR/d8acc.tif"
"$WBT" --run=Watershed --d8_pntr="$OUT_DIR/d8pntr.tif" --pour_pts="$OUT_DIR/outlet.shp" --output="$OUT_DIR/basin.tif"
echo "Outputs written to $OUT_DIR: dem_filled.asc d8pntr.tif d8acc.tif basin.tif"
