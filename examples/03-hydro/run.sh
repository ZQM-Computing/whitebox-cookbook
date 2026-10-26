#!/usr/bin/env bash
# 03-hydro: fill, flow direction, flow accumulation, watershed extraction.
# Set WHITEBOX_TOOLS to the full binary path if it is not on PATH.
# Rows/columns in the notes are 0-based; the outlet is row 5, column 9
# (middle row, east edge).
set -euo pipefail
WBT="${WHITEBOX_TOOLS:-whitebox_tools}"
python3 gen_dem.py dem.asc
"$WBT" --run=FillDepressions --dem=dem.asc --output=dem_filled.asc
python3 check_fill.py dem.asc dem_filled.asc
"$WBT" --run=D8Pointer --dem=dem_filled.asc --output=d8pntr.asc
"$WBT" --run=D8FlowAccum --pntr=d8pntr.asc --output=d8acc.asc
"$WBT" --run=Watershed --d8_pntr=d8pntr.asc --pour_pts=outlet.shp --output=basin.asc
echo "Outputs: dem_filled.asc d8pntr.asc d8acc.asc basin.asc (each 10x10)"
