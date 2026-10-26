# WhiteboxTools Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **WhiteboxTools cookbook** for terrain, hydrology, and LiDAR analysis from the command line. Patterns are drawn from the ZQM fleet's WhiteboxTools 2.4.0 installs on all three Windows nodes. It is intended for Geospatial engineers who want a fast, dependency-light CLI for terrain work. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public. First pattern pass written (design-only, gate 1 target — none runtime-validated on the fleet yet).

**What this repository is:** WhiteboxTools patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Geospatial engineers who want a fast, dependency-light CLI for terrain work.

## Prerequisites

- WhiteboxTools 2.4.0 (fleet record: Node-1 extract dir `C:\WhiteboxTools`; confirm the path on Node-3/Node-4 at validation)
- A DEM and, for the LiDAR pass, a sample LAS file (both generated synthetically by the patterns)
- Bash (on fleet Windows nodes, the same commands run in PowerShell with the fleet binary path)

## Patterns

| # | Example | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 01 | [examples/01-cli-basics](examples/01-cli-basics) | Running WhiteboxTools commands and reading tool help | Written (design-only) |
| 02 | [examples/02-terrain](examples/02-terrain) | Slope, hillshade, and roughness from a DEM | Written (design-only) |
| 03 | [examples/03-hydro](examples/03-hydro) | Depression filling, flow direction, and watershed extraction | Written (design-only) |
| 04 | [examples/04-lidar-tools](examples/04-lidar-tools) | LiDAR point-cloud tools: filtering, gridding, and ground classification | Written (design-only) |

## Repository layout

```text
whitebox-cookbook/
├── examples/
│   ├── 01-cli-basics/
│   ├── 02-terrain/
│   ├── 03-hydro/
│   └── 04-lidar-tools/
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: all four table rows (this pass, design-only)
- Validation pass (gate 3): run each pattern against the fleet WhiteboxTools 2.4.0 binary; confirm CLI flag spellings, tool parameter names, and all stated expected values

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [grass-cookbook](https://github.com/ZQM-Computing/grass-cookbook) — Geoscientific analysis, terrain, and watershed modeling
- [pdal-cookbook](https://github.com/ZQM-Computing/pdal-cookbook) — Point-cloud pipelines, translation, and pgPointCloud ingest
- [saga-cookbook](https://github.com/ZQM-Computing/saga-cookbook) — Terrain analysis and geoscientific modeling from the command line
