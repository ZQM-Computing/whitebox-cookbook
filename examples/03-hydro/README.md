# 03 — Hydro: fill, flow, watershed

Run the classic depression-fill → flow-direction → accumulation →
watershed chain on the same synthetic plane DEM as pattern 02, with
every expected value derived by hand first.

## Inputs

`gen_dem.py` writes `dem.asc`: a 10x10 plane, elevation = column index
(0..9), cellsize 30 m. `gen_outlet.py` writes the point shapefile required
by Watershed at the center of row 5, column 9 (synthetic x=285, y=135).
All flow runs east off the grid edge. Rows and columns are 0-based.

## Run

```bash
bash run.sh  # optional output directory: bash run.sh /path/to/output
```

## Expected output

All four outputs are 10x10, matching `dem.asc`:

- `dem_filled.asc`: identical to `dem.asc` (checked by
  `check_fill.py`). A plane has no depressions, so filling must be a
  no-op. Any difference means the input grid was not the plane.
- `d8pntr.tif`: flow-direction grid; every cell points east.
- `d8acc.tif`: flow-accumulation grid; values increase eastward along
  each row, maximum 10 in the east column if the tool counts the cell
  itself, 9 otherwise. The self-count convention is **to confirm at
  validation** — do not assert one value until it is.
- `basin.tif`: watershed from the outlet at row 5, column 9 (middle
  row, east edge). Expected basin = row 5 only: 10 cells. Every other
  row drains off the edge at its own east cell, not through this
  outlet.

## Failure behavior

- `check_fill.py` exits nonzero on any grid difference — regenerate
  the DEM, do not adjust the filled grid to match.
- The runner generates `outlet.shp`, `.shx`, and `.dbf` from a deterministic
  synthetic point and tests its binary structure/coordinates in CI. Whether
  the installed WhiteboxTools 2.4.0 Watershed tool accepts this vector input
  and the chosen parameter spelling remains a live-runtime gate.

## Versions and evidence

- Tool: WhiteboxTools 2.4.0 (fleet-verified on all three Windows
  nodes; Node-1 extract dir `C:\WhiteboxTools`).
- Evidence level: design-only (gate 1 target). Tool names
  (FillDepressions, D8Pointer, D8FlowAccum, Watershed) are standard
  WhiteboxTools tools; the parameter names (`--dem`, `--pntr`,
  `--d8_pntr`, `--pour_pts`, `--output`) and the accumulation
  self-count convention are **to confirm at validation** against the
  fleet binary's `--help` output.
