from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n1\n"),
        edge("1 1\n1\n2\n"),
        edge("3 3\n1 2 3\n2 3 4\n"),
        edge("5 4\n1 2 3 4 5\n6 7 8 9\n"),
        edge("5 5\n-1 0 1 2 3\n0 2 4 6 8\n"),
        stress("10 10\n1 2 3 4 5 6 7 8 9 10\n5 6 7 8 9 10 11 12 13 14\n"),
    ]
