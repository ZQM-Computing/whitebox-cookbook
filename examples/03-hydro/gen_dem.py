"""Generate the synthetic 10x10 east-sloping plane DEM (see 02-terrain).

Elevation equals the column index (0..9), cellsize 30 m. A plane has no
depressions, so FillDepressions must leave it unchanged, and all flow
runs east off the grid edge. Rows and columns below are 0-based.

Usage: python3 gen_dem.py dem.asc
"""
import sys

NCOLS, NROWS = 10, 10


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
