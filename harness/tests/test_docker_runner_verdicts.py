from __future__ import annotations

import shutil
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from harness.judge_core import DockerRunner


def docker_available() -> bool:
    if shutil.which("docker") is None:
        return False
    return subprocess.run(["docker", "info"], capture_output=True).returncode == 0


@unittest.skipUnless(docker_available(), "Docker daemon is not available")
class DockerRunnerVerdictTests(unittest.TestCase):
    def setUp(self):
        self.runner = DockerRunner()

    def test_cpp_compile_error(self):
        result = self.runner.run(
            "cpp",
            "int main( { return 0; }\n",
            "",
            time_limit_s=1.0,
            memory_mb=128,
        )
        self.assertTrue(result.compile_error, msg=result)

    def test_python_runtime_error(self):
        result = self.runner.run(
            "python",
            "raise RuntimeError('boom')\n",
            "",
            time_limit_s=1.0,
            memory_mb=128,
        )
        self.assertFalse(result.ok, msg=result)
        self.assertFalse(result.compile_error, msg=result)
        self.assertFalse(result.timed_out, msg=result)

    def test_python_time_limit(self):
        result = self.runner.run(
            "python",
            "while True:\n    pass\n",
            "",
            time_limit_s=1.0,
            memory_mb=128,
        )
        self.assertTrue(result.timed_out, msg=result)

    def test_python_memory_limit(self):
        result = self.runner.run(
            "python",
            "x = bytearray(512 * 1024 * 1024)\nprint(len(x))\n",
            "",
            time_limit_s=3.0,
            memory_mb=64,
        )
        self.assertFalse(result.ok, msg=result)
        self.assertTrue(result.oom_killed or "MemoryError" in result.stderr, msg=result)

    def test_output_limit(self):
        result = self.runner.run(
            "python",
            "print('x' * 2048)\n",
            "",
            time_limit_s=1.0,
            memory_mb=128,
            max_output_bytes=64,
        )
        self.assertTrue(result.output_exceeded, msg=result)


if __name__ == "__main__":
    unittest.main()
