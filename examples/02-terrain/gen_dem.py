"""Generate a synthetic 10x10 ESRI ASCII DEM: a perfect east-sloping plane.

Elevation equals the column index (0..9), cellsize 30 m, so the eastward
gradient is exactly 1/30 and the interior slope is atan(1/30) = 1.909
degrees. No real terrain, no real place: the grid is pure arithmetic.

Usage: python3 gen_dem.py dem.asc
"""
import sys

NCOLS, NROWS = 10, 10
CELLSIZE = 30.0


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "dem.asc"
    with open(path, "w", encoding="ascii") as f:
        f.write("ncols 10\nnrows 10\nxllcorner 0.0\n")
        f.write("yllcorner 0.0\ncellsize 30.0\nNODATA_value -9999\n")
        for _row in range(NROWS):
            f.write(" ".join(str(col) for col in range(NCOLS)) + "\n")
    print(f"Wrote {path}: 10x10 plane, elevation = column index")


if __name__ == "__main__":
    main()
