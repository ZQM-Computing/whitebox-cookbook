#!/usr/bin/env bash
# 04-lidar-tools: validate a synthetic LAS file, inspect it, and grid it.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WBT="${WHITEBOX_TOOLS:-whitebox_tools}"
OUT_DIR="${1:-$DIR/build}"
mkdir -p "$OUT_DIR"

python3 "$DIR/gen_las.py" "$OUT_DIR/sample.las"
python3 "$DIR/check_las.py" "$OUT_DIR/sample.las"
"$WBT" --run=LidarInfo --input="$OUT_DIR/sample.las"
"$WBT" --run=LidarTinGridding --input="$OUT_DIR/sample.las" --output="$OUT_DIR/lidar_dem.tif"
echo "Outputs written to $OUT_DIR: sample.las lidar_dem.tif"
