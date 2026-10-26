import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
EXAMPLE = ROOT / "examples" / "01-cli-basics"


class WhiteboxExampleContractTests(unittest.TestCase):
    def test_example_documents_invocation_and_runtime_boundary(self):
        readme = (EXAMPLE / "README.md").read_text(encoding="utf-8")
        self.assertIn("inspect-cli.sh", readme)
        self.assertIn("does not install WhiteboxTools", readme)

    def test_script_captures_version_and_tool_inventory(self):
        script = (EXAMPLE / "inspect-cli.sh").read_text(encoding="utf-8")
        self.assertIn('"${WHITEBOX_TOOLS_BIN:-whitebox_tools}"', script)
        self.assertIn('"$bin" --version', script)
        self.assertIn('"$bin" --listtools', script)
        self.assertIn('set -euo pipefail', script)


if __name__ == "__main__":
    unittest.main()
