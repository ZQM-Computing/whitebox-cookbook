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

**Status:** Active, public — seeding. Pattern passes land in follow-up work from fleet-verified setups; the tables below list what is planned, not what is already written.

**What this repository is:** WhiteboxTools patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Geospatial engineers who want a fast, dependency-light CLI for terrain work.

## Prerequisites

- WhiteboxTools 2.4.0
- A DEM and, for the LiDAR pass, a sample LAS file
- Bash

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-cli-basics` | Running WhiteboxTools commands and reading tool help |
| 02 | `02-terrain` | Slope, hillshade, and roughness from a DEM |
| 03 | `03-hydro` | Depression filling, flow direction, and watershed extraction |
| 04 | `04-lidar-tools` | LiDAR point-cloud tools: filtering, gridding, and ground classification |

## Repository layout

```text
whitebox-cookbook/
├── examples/          # pattern passes, landing in follow-up work
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [grass-cookbook](https://github.com/ZQM-Computing/grass-cookbook) — Geoscientific analysis, terrain, and watershed modeling
- [pdal-cookbook](https://github.com/ZQM-Computing/pdal-cookbook) — Point-cloud pipelines, translation, and pgPointCloud ingest
- [saga-cookbook](https://github.com/ZQM-Computing/saga-cookbook) — Terrain analysis and geoscientific modeling from the command line
