from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nleo\n"),
        edge("2\nleo\nkiki\nleo\n"),
        edge("3\nalice\nbob\nalice\nalice\nbob\n"),
        edge("4\nmislav\nstanko\nmislav\nana\nstanko\nana\nmislav\n"),
        edge("5\na\na\nb\nb\nc\na\nb\nb\nc\n"),
        stress("6\nrunner1\nrunner2\nrunner3\nrunner2\nrunner4\nrunner5\nrunner1\nrunner2\nrunner3\nrunner4\nrunner5\n"),
    ]
