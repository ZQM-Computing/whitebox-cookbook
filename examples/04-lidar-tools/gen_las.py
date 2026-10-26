"""Generate a minimal synthetic LAS 1.2 file (12 points, pure stdlib).

Point format 0, 20-byte records, scale 0.01, offsets 0. Eight ground
points (classification 2) sit on the plane z = 100.0; four unclassified
points (classification 1) sit at z = 105.0. No real survey, no real
place: coordinates are small synthetic integers.

Usage: python3 gen_las.py sample.las
"""
import struct
import sys

HEADER_FMT = "<4sHH16sBB32s32sHHHIIBH I5I3d3d6d".replace(" ", "")
RECORD_FMT = "<iiiHBBbBH"
HEADER_SIZE = 227
RECORD_LEN = 20


def pad(text, size):
    raw = text.encode("ascii")
    return raw + b"\x00" * (size - len(raw))


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.las"
    ground = [(x * 10.0, (i % 2) * 10.0, 100.0, 2) for i, x in enumerate(range(8))]
    air = [(x * 10.0, 5.0, 105.0, 1) for x in range(4)]
    points = ground + air
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]
    by_return = [len(points), 0, 0, 0, 0]
    header = struct.pack(
        HEADER_FMT,
        b"LASF", 0, 0, b"\x00" * 16, 1, 2,
        pad("WhiteboxTools cookbook", 32), pad("gen_las.py", 32),
        1, 2026, HEADER_SIZE, HEADER_SIZE, 0, 0, RECORD_LEN,
        len(points), *by_return,
        0.01, 0.01, 0.01, 0.0, 0.0, 0.0,
        max(xs), min(xs), max(ys), min(ys), max(zs), min(zs),
    )
    assert len(header) == HEADER_SIZE, len(header)
    with open(path, "wb") as f:
        f.write(header)
        for x, y, z, cls in points:
            f.write(struct.pack(
                RECORD_FMT,
                int(round(x / 0.01)), int(round(y / 0.01)), int(round(z / 0.01)),
                0, 0x21, cls, 0, 0, 0,
            ))
    print(f"Wrote {path}: 12 points (8 ground class 2, 4 class 1)")


if __name__ == "__main__":
    main()
