from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from harness.limits import resolve_limits


class JudgeLimitsTests(unittest.TestCase):
    def test_statement_limits_are_safe_for_docker_compile(self):
        limits = resolve_limits("dynamic_programming_2-1005")

        self.assertGreaterEqual(limits.time_limit_ms, 1000)
        self.assertEqual(limits.memory_limit_mb, 256)
        self.assertEqual(limits.raw_memory_limit_mb, 1)

    def test_requested_limits_are_clamped(self):
        limits = resolve_limits("unknown-999999", {
            "timeLimitMs": 100,
            "memoryLimitMb": 64,
            "maxOutputBytes": 512,
        })

        self.assertEqual(limits.time_limit_ms, 1000)
        self.assertEqual(limits.memory_limit_mb, 256)
        self.assertEqual(limits.max_output_bytes, 512)

    def test_unknown_problem_uses_fallbacks(self):
        limits = resolve_limits("unknown-999999")

        self.assertEqual(limits.time_limit_ms, 2000)
        self.assertEqual(limits.memory_limit_mb, 256)
        self.assertEqual(limits.source, "fallback")


if __name__ == "__main__":
    unittest.main()
