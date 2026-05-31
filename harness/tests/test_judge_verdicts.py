from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from harness.judge_core import RunResult, judge


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


if __name__ == "__main__":
    unittest.main()
