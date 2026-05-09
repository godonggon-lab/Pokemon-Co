from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n5\n", "5\n"),
        edge("1 1\n-5\n", "-5\n"),
        edge("1 3\n1 -2 3\n", "3\n"),
        edge("2 2\n1 2\n3 4\n", "10\n"),
        edge("2 2\n-1 -2\n-3 -4\n", "-1\n"),
        stress("3 3\n1 -2 3\n-4 5 -6\n7 -8 9\n", "9\n"),
    ]
