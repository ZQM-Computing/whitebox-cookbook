#!/usr/bin/env bash
# 02-terrain: slope, hillshade, and roughness from the synthetic plane DEM.
# Set WHITEBOX_TOOLS to the full binary path if it is not on PATH.
set -euo pipefail
WBT="${WHITEBOX_TOOLS:-whitebox_tools}"
python3 gen_dem.py dem.asc
"$WBT" --run=Slope --dem=dem.asc --output=slope.tif
"$WBT" --run=Hillshade --dem=dem.asc --output=hillshade.tif
"$WBT" --run=Roughness --dem=dem.asc --output=roughness.tif
echo "Outputs: slope.tif hillshade.tif roughness.tif (each 10x10, matching dem.asc)"
