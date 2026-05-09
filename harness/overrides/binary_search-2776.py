from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n5\n3\n5\n4\n6\n"),
        edge("1\n5\n4 1 5 2 3\n5\n1 3 7 9 5\n"),
        edge("1\n3\n-1 0 1\n5\n-1 0 1 2 -2\n"),
        edge("2\n3\n1 2 3\n3\n1 4 2\n4\n10 20 30 40\n4\n10 15 30 50\n"),
        edge("1\n5\n1 1 1 2 2\n4\n1 2 3 0\n"),
        stress("1\n10\n1 4 9 16 25 36 49 64 81 100\n6\n1 2 49 50 100 101\n"),
    ]
