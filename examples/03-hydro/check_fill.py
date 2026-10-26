"""Check that FillDepressions left the plane DEM unchanged.

Reads two ESRI ASCII grids and exits nonzero unless every cell matches.
A plane has no depressions, so the filled grid must equal the input.

Usage: python3 check_fill.py dem.asc dem_filled.asc
"""
import sys


def read_grid(path):
    with open(path, encoding="ascii") as f:
        header = [next(f).split() for _ in range(6)]
        rows = [[float(v) for v in line.split()] for line in f if line.strip()]
    return header, rows


def main() -> None:
    before_h, before = read_grid(sys.argv[1])
    after_h, after = read_grid(sys.argv[2])
    if before_h != after_h or before != after:
        raise SystemExit("Fill check FAILED: filled grid differs from input")
    print("Fill check: identical (no depressions, as designed)")


if __name__ == "__main__":
    main()
