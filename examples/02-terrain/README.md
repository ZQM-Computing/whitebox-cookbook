# 02 — Terrain: slope, hillshade, roughness

Derive the three basic terrain surfaces from one synthetic DEM, and
check each against an expectation computed by hand before running.

## Inputs

`gen_dem.py` writes `dem.asc`: a 10x10 ESRI ASCII grid whose elevation
equals the column index (0..9), cellsize 30 m. It is a perfect
east-sloping plane — no real terrain, no real place.

## Run

```bash
bash run.sh  # optional output directory: bash run.sh /path/to/output
```

## Expected output

All three outputs are written to `build/` by default (or the directory passed as the first argument) and should be 10x10, matching `dem.asc`:

- `slope.tif`: interior cells ≈ 1.91 degrees. Derivation: eastward
  gradient 1/30, slope = atan(1/30) = 1.909 degrees. Edge cells may
  differ (truncated neighbourhood) — assert the interior only.
- `hillshade.tif`: values in the 0–255 range, dimensions matching the
  input. No per-cell value is asserted: the default azimuth/altitude
  are **to confirm at validation**.
- `roughness.tif`: near-constant across the interior (a perfect plane
  has no local relief), dimensions matching the input. The exact
  roughness statistic definition is **to confirm at validation**.

## Failure behavior

- Missing `dem.asc` (generator not run): the Slope step errors on the
  missing input instead of producing an empty raster — run the
  generator first.
- Wrong grid shape in `dem.asc`: outputs will not be 10x10 and the
  dimension check fails — regenerate from `gen_dem.py`, do not
  hand-edit the grid.

## Versions and evidence

- Tool: WhiteboxTools 2.4.0 (fleet-verified on all three Windows
  nodes; Node-1 extract dir `C:\WhiteboxTools`).
- Evidence level: design-only (gate 1 target). Tool names (Slope,
  Hillshade, Roughness) are standard WhiteboxTools tools; the
  `--dem`/`--output` flag spellings, the degrees default for Slope,
  and the `.asc` input support are **to confirm at validation**
  against the fleet binary's `--help` output.
