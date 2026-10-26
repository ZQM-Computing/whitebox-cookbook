#!/usr/bin/env python3
"""Create a one-point ESRI Shapefile outlet for the synthetic 10x10 DEM.

The DEM has a 30 m cell size and no assigned CRS. The point is the center
of row 5, column 9 (0-based from the north-west), at synthetic coordinates
x=285, y=135. Writes .shp/.shx/.dbf using only the Python standard library.
"""
import struct
import sys
from pathlib import Path

X, Y = 285.0, 135.0


def shp_header(file_length_words: int) -> bytes:
    return (
        struct.pack(">7i", 9994, 0, 0, 0, 0, 0, file_length_words)
        + struct.pack("<2i", 1000, 1)
        + struct.pack("<4d", X, Y, X, Y)
        + struct.pack("<4d", 0.0, 0.0, 0.0, 0.0)
    )


def write_shapefile(prefix: Path) -> None:
    prefix.parent.mkdir(parents=True, exist_ok=True)
    point = struct.pack("<idd", 1, X, Y)
    record_header = struct.pack(">2i", 1, len(point) // 2)
    (prefix.with_suffix(".shp")).write_bytes(shp_header(50 + (len(record_header) + len(point)) // 2) + record_header + point)

    index_record = struct.pack(">2i", 50, len(point) // 2)
    (prefix.with_suffix(".shx")).write_bytes(shp_header(50 + len(index_record) // 2) + index_record)

    # dBASE III table: one numeric ID field, one record.
    header_length, record_length = 65, 5
    dbf_header = struct.pack("<BBBBIHH20x", 3, 126, 10, 26, 1, header_length, record_length)
    field = b"ID\x00\x00\x00\x00\x00\x00\x00\x00\x00N" + b"\x00\x00\x00\x00" + bytes((4, 0)) + b"\x00" * 14
    if len(field) != 32:
        raise AssertionError(f"DBF field descriptor must be 32 bytes, got {len(field)}")
    (prefix.with_suffix(".dbf")).write_bytes(dbf_header + field + b"\r" + b" " + b"   1" + b"\x1a")


def main() -> None:
    prefix = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("outlet")
    write_shapefile(prefix)
    print(f"Wrote {prefix}.shp/.shx/.dbf at synthetic point ({X}, {Y})")


if __name__ == "__main__":
    main()
