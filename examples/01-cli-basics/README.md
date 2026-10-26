# Inspect the WhiteboxTools CLI

This pattern verifies that the WhiteboxTools executable is reachable, captures its version, and saves the available-tool listing. It does not run terrain or LiDAR processing; those examples must validate their input datasets and output artifacts separately.

## Prerequisites

- WhiteboxTools 2.4.0 or compatible
- Bash and the WhiteboxTools executable on `PATH`, or set `WHITEBOX_TOOLS_BIN` to its full path

## Run

```bash
bash examples/01-cli-basics/inspect-cli.sh build/whitebox-tools.txt
```

The output records the version and tool list. Review it when troubleshooting differences between hosts; do not assume every installation exposes identical tools or parameters.

## Validation boundary

CI checks the script and documentation contract, plus Bash syntax. It does not install WhiteboxTools or certify the installed runtime; execute this pattern on the target machine for that.
