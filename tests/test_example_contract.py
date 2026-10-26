import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
EXAMPLE = ROOT / "examples" / "01-cli-basics"


class WhiteboxExampleContractTests(unittest.TestCase):
    def test_example_documents_invocation_and_runtime_boundary(self):
        readme = (EXAMPLE / "README.md").read_text(encoding="utf-8")
        self.assertIn("inspect-cli.sh", readme)
        self.assertIn("does not install WhiteboxTools", readme)

    def test_all_example_shell_scripts_fail_fast_and_resolve_output_directories(self):
        scripts = sorted((ROOT / "examples").rglob("*.sh"))
        self.assertGreaterEqual(len(scripts), 4)
        for script_path in scripts:
            with self.subTest(script=script_path.relative_to(ROOT)):
                script = script_path.read_text(encoding="utf-8")
                self.assertIn("set -euo pipefail", script)
        for relative in (
            "examples/02-terrain/run.sh",
            "examples/03-hydro/run.sh",
            "examples/04-lidar-tools/run.sh",
        ):
            script = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn('DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"', script)
            self.assertIn('OUT_DIR="${1:-$DIR/build}"', script)

    def test_hydrology_runner_generates_the_missing_outlet_fixture(self):
        script = (ROOT / "examples/03-hydro/run.sh").read_text(encoding="utf-8")
        self.assertIn('python3 "$DIR/gen_outlet.py" "$OUT_DIR/outlet"', script)
        self.assertIn('--pour_pts="$OUT_DIR/outlet.shp"', script)
        readme = (ROOT / "examples/03-hydro/README.md").read_text(encoding="utf-8")
        self.assertIn("gen_outlet.py", readme)

    def test_outlet_shapefile_has_valid_headers_and_expected_point(self):
        generator = ROOT / "examples/03-hydro/gen_outlet.py"
        with tempfile.TemporaryDirectory() as temp:
            prefix = Path(temp) / "outlet"
            subprocess.run([sys.executable, str(generator), str(prefix)], check=True, capture_output=True, text=True)
            shp = prefix.with_suffix(".shp").read_bytes()
            shx = prefix.with_suffix(".shx").read_bytes()
            dbf = prefix.with_suffix(".dbf").read_bytes()
        self.assertEqual(struct.unpack_from(">i", shp, 0)[0], 9994)
        self.assertEqual(struct.unpack_from(">i", shp, 24)[0], len(shp) // 2)
        self.assertEqual(struct.unpack_from("<ii", shp, 28), (1000, 1))
        self.assertEqual(struct.unpack_from(">ii", shp, 100), (1, 10))
        shape_type, x, y = struct.unpack_from("<idd", shp, 108)
        self.assertEqual(shape_type, 1)
        self.assertEqual((x, y), (285.0, 135.0))
        self.assertEqual(struct.unpack_from(">ii", shx, 100), (50, 10))
        self.assertEqual(len(dbf), 71)
        self.assertEqual(dbf[32 + 32], 13)

    def test_synthetic_las_generator_passes_its_binary_contract(self):
        generator = ROOT / "examples/04-lidar-tools/gen_las.py"
        checker = ROOT / "examples/04-lidar-tools/check_las.py"
        with tempfile.TemporaryDirectory() as temp:
            las = Path(temp) / "synthetic.las"
            subprocess.run([sys.executable, str(generator), str(las)], check=True, capture_output=True, text=True)
            result = subprocess.run([sys.executable, str(checker), str(las)], check=True, capture_output=True, text=True)
        self.assertIn("12 points", result.stdout)
        self.assertIn("classes", result.stdout)


    def test_all_runners_share_the_binary_override_and_cli_basics_only_requests_help(self):
        for relative in (
            "examples/01-cli-basics/run.sh",
            "examples/02-terrain/run.sh",
            "examples/03-hydro/run.sh",
            "examples/04-lidar-tools/run.sh",
        ):
            script = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn('WBT="${WHITEBOX_TOOLS_BIN:-whitebox_tools}"', script)
        cli = (EXAMPLE / "run.sh").read_text(encoding="utf-8")
        self.assertIn('"$WBT" --toolhelp=Slope', cli)
        self.assertNotIn('--run=Slope --help', cli)

    def test_script_captures_version_and_tool_inventory(self):
        script = (EXAMPLE / "inspect-cli.sh").read_text(encoding="utf-8")
        self.assertIn('"${WHITEBOX_TOOLS_BIN:-whitebox_tools}"', script)
        self.assertIn('"$bin" --version', script)
        self.assertIn('"$bin" --listtools', script)
        self.assertIn('set -euo pipefail', script)


if __name__ == "__main__":
    unittest.main()
