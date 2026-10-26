#!/usr/bin/env bash
# 04-lidar-tools: LiDAR info and gridding from the synthetic LAS file.
# Set WHITEBOX_TOOLS to the full binary path if it is not on PATH.
set -euo pipefail
WBT="${WHITEBOX_TOOLS:-whitebox_tools}"
python3 gen_las.py sample.las
python3 check_las.py sample.las
"$WBT" --run=LidarInfo --input=sample.las
"$WBT" --run=LidarTinGridding --input=sample.las --output=lidar_dem.tif
echo "Outputs: sample.las (12 points), lidar_dem.tif"
