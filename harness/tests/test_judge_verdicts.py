from __future__ import annotations

import sys
import unittest
import importlib.util
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from harness.judge_core import RunResult, judge

ROOT = Path(__file__).resolve().parents[2]


class StaticRunner:
    def __init__(self, result: RunResult):
        self.result = result

    def run(self, *_args, **_kwargs) -> RunResult:
        return self.result


class JudgeVerdictTests(unittest.TestCase):
    def test_tle_bubbles_up_to_judge_status(self):
        result = judge(
            problem_slug="dynamic_programming_1-1003",
            category_slug="dynamic_programming_1",
            user_lang="python",
            user_code="while True: pass",
            oracle_lang="python",
            oracle_code="print(0)",
            user_runner=StaticRunner(RunResult(False, "", "", 1000, True, False)),
            oracle_runner=StaticRunner(RunResult(True, "0\n", "", 1, False, False)),
            case_count=1,
            time_limit_s=1.0,
            memory_limit_mb=256,
        )

        self.assertEqual(result["status"], "TLE")

    def test_ole_bubbles_up_to_judge_status(self):
        result = judge(
            problem_slug="dynamic_programming_1-1003",
            category_slug="dynamic_programming_1",
            user_lang="python",
            user_code="print('x' * 999999)",
            oracle_lang="python",
            oracle_code="print(0)",
            user_runner=StaticRunner(RunResult(False, "x" * 128, "", 1, False, False, output_exceeded=True)),
            oracle_runner=StaticRunner(RunResult(True, "0\n", "", 1, False, False)),
            case_count=1,
            time_limit_s=1.0,
            memory_limit_mb=256,
            max_output_bytes=64,
        )

        self.assertEqual(result["status"], "OLE")

    def test_replace_samples_override_skips_boj_samples(self):
        override_path = ROOT / "harness" / "overrides" / "brute_force-4690.py"
        spec = importlib.util.spec_from_file_location("override_4690", override_path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        expected = module._solve()

        result = judge(
            problem_slug="brute_force-4690",
            category_slug="brute_force",
            user_lang="python",
            user_code="",
            oracle_lang="python",
            oracle_code="",
            user_runner=StaticRunner(RunResult(True, expected, "", 1, False, False)),
            oracle_runner=StaticRunner(RunResult(True, expected, "", 1, False, False)),
            case_count=1,
            time_limit_s=1.0,
            memory_limit_mb=256,
        )

        self.assertEqual(result["status"], "AC")
        self.assertEqual(result["total"], 1)


if __name__ == "__main__":
    unittest.main()
