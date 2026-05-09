from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n", "1\n"),
        edge("1 4\n0\n", "6\n"),
        edge("2 3\n0 10\n", "3\n"),
        edge("2 5\n0 2\n", "7\n"),
        edge("3 6\n-2 0 2\n", "8\n"),
        stress("5 10\n-10 -5 0 5 10\n", "10\n"),
    ]
