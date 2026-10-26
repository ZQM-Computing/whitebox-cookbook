# 01 — CLI basics

Run WhiteboxTools, confirm the version, read the tool list, and read one
tool's help. This is the smoke test every later pattern assumes.

This pattern verifies that the WhiteboxTools executable is reachable,
captures its version, and saves the available-tool listing. It does not
run terrain or LiDAR processing; those examples must validate their
input datasets and output artifacts separately.

## Prerequisites

- WhiteboxTools 2.4.0 or compatible
- Bash and the WhiteboxTools executable on `PATH`, or set
  `WHITEBOX_TOOLS_BIN` to its full path (`run.sh` below accepts
  `WHITEBOX_TOOLS` instead)

## Run

```bash
bash run.sh
```

`run.sh` prints the version, the `--help` tool list, and Slope's
per-tool help.

```bash
bash examples/01-cli-basics/inspect-cli.sh build/whitebox-tools.txt
```

`inspect-cli.sh` records the version and tool list to
`build/whitebox-tools.txt`. Review it when troubleshooting differences
between hosts; do not assume every installation exposes identical tools
or parameters.

## Expected output

- `--version` reports WhiteboxTools 2.4.0 (the fleet-recorded version;
  Node-1's `--version` run is the fleet evidence).
- `--help` lists the available tools; `--listtools` (used by
  `inspect-cli.sh`) captures the same inventory to a file.
- The per-tool help form prints Slope's parameters.

## Failure behavior

- Binary not on PATH: the scripts fail immediately (`run.sh` with
  `command not found`; `inspect-cli.sh` with exit 127 and
  `ERROR: WhiteboxTools executable not found`) — fix PATH or set
  `WHITEBOX_TOOLS` / `WHITEBOX_TOOLS_BIN`, do not guess at a binary
  location.
- Unknown tool name: the tool errors instead of producing output;
  re-check the name against `--help`.

## Validation boundary

CI checks the script and documentation contract, plus Bash syntax. It
does not install WhiteboxTools or certify the installed runtime;
execute this pattern on the target machine for that.

## Versions and evidence

- Tool: WhiteboxTools 2.4.0 (fleet-verified on all three Windows
  nodes; Node-1 extract dir `C:\WhiteboxTools`).
- Evidence level: design-only (gate 1 target). The `--version` form is
  fleet-proven; the `--help`, `--listtools`, and per-tool help
  spellings follow the documented 2.4.0 CLI and are **to confirm at
  validation** against the fleet binary's own `--help` output.
