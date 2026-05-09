from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n", "5\n"),
        edge("1\n-5\n", "-5\n"),
        edge("3\n1 2 3\n", "6\n"),
        edge("3\n-1 -2 -3\n", "-1\n"),
        edge("10\n10 -4 3 1 5 6 -35 12 21 -1\n", "33\n"),
        stress("8\n-2 1 -3 4 -1 2 1 -5\n", "6\n"),
    ]
