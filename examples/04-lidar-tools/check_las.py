"""Verify the synthetic LAS file from gen_las.py (pure stdlib).

Asserts the LAS 1.2 header (signature, version, 227-byte header, point
format 0, 20-byte records, 12 points) and the class counts (8 ground,
4 unclassified). Exits nonzero on any mismatch.

Usage: python3 check_las.py sample.las
"""
import struct
import sys

HEADER_FMT = "<4sHH16sBB32s32sHHHIIBH I5I3d3d6d".replace(" ", "")
RECORD_FMT = "<iiiHBBbBH"


def main() -> None:
    path = sys.argv[1]
    with open(path, "rb") as f:
        raw = f.read()
    header = struct.unpack(HEADER_FMT, raw[:227])
    (sig, _src, _enc, _guid, major, minor, _sys, _soft,
     _day, _year, hsize, offset, _vlr, pfmt, reclen, count) = header[:16]
    assert sig == b"LASF", sig
    assert (major, minor) == (1, 2), (major, minor)
    assert hsize == 227 and offset == 227, (hsize, offset)
    assert pfmt == 0 and reclen == 20, (pfmt, reclen)
    assert count == 12, count
    records = raw[offset:offset + count * reclen]
    assert len(records) == count * reclen
    classes = {}
    for i in range(count):
        rec = struct.unpack_from(RECORD_FMT, records, i * reclen)
        classes[rec[5]] = classes.get(rec[5], 0) + 1
    assert classes == {2: 8, 1: 4}, classes
    print(f"LAS check: 12 points, classes {classes} — OK")


if __name__ == "__main__":
    main()
