# 04 — LiDAR tools: info, filtering, gridding

Work a 12-point synthetic LAS file through LiDAR info and gridding.
The file is generated in pure Python, so the pattern needs no real
survey and no real place.

## Inputs

`gen_las.py` writes `sample.las` into the selected output directory: LAS 1.2, point format 0, 12 points —
8 ground points (classification 2) on the plane z = 100.0 and 4
unclassified points (classification 1) at z = 105.0. `check_las.py`
verifies the header and the class counts before any WhiteboxTools
command runs.

## Run

```bash
bash run.sh  # optional output directory: bash run.sh /path/to/output
```

## Expected output

- `check_las.py`: `LAS check: 12 points, classes {2: 8, 1: 4} — OK`.
- `LidarInfo`: reports 12 points (the count above, not a new number).
- `lidar_dem.tif` in the selected output directory: a gridded DEM from the point cloud. Its grid
  spacing and extent depend on the gridding parameters, which are
  **to confirm at validation** — the pattern asserts the file exists
  and the input counts, not a grid shape.
- Filtering by class is demonstrated by the class-count check itself:
  the input separates cleanly into ground (2) and unclassified (1),
  which is the predicate a class-filtered gridding pass would use.
  The class-filtered gridding command form is **to confirm at
  validation**.

## Failure behavior

- `check_las.py` exits nonzero on any header or class mismatch —
  regenerate `sample.las`, do not hand-edit the binary.
- Non-LAS input to `LidarInfo`: the tool errors instead of reporting
  a count — confirm the input is the generated `.las` file.

## Versions and evidence

- Tool: WhiteboxTools 2.4.0 (fleet-verified on all three Windows
  nodes; Node-1 extract dir `C:\WhiteboxTools`).
- Evidence level: design-only (gate 1 target). Tool names (LidarInfo,
  LidarTinGridding) are standard WhiteboxTools tools; the `--input` /
  `--output` flag spellings and the gridding parameters are **to
  confirm at validation** against the fleet binary's `--help` output.
  The LAS generator and checker are pure stdlib and were executed
  during drafting (header size, record layout, and class counts all
  re-parsed by the checker).
