# 01 — CLI basics

Run WhiteboxTools, confirm the version, read the tool list, and read one
tool's help. This is the smoke test every later pattern assumes.

## Run

```bash
bash run.sh
```

On fleet Windows nodes, run the same three commands in PowerShell with
the fleet binary on PATH, or set `WHITEBOX_TOOLS` to the full binary
path (Node-1 documented extract dir: `C:\WhiteboxTools`).

## Expected output

- `--version` reports WhiteboxTools 2.4.0 (the fleet-recorded version;
  Node-1's `--version` run is the fleet evidence).
- `--help` lists the available tools.
- The per-tool help form prints Slope's parameters.

## Failure behavior

- Binary not on PATH: the script fails immediately with
  `whitebox_tools: command not found` (or the Windows equivalent) —
  fix PATH or set `WHITEBOX_TOOLS`, do not guess at a binary location.
- Unknown tool name: the tool errors instead of producing output;
  re-check the name against `--help`.

## Versions and evidence

- Tool: WhiteboxTools 2.4.0, fleet-verified on all three Windows nodes.
- Evidence level: design-only (gate 1 target). The `--version` form is
  fleet-proven; the `--help` and per-tool help spellings follow the
  documented 2.4.0 CLI and are **to confirm at validation** against the
  fleet binary's own `--help` output.
