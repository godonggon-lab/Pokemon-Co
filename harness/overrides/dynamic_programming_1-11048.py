from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n5\n", "5\n"),
        edge("1 3\n1 2 3\n", "6\n"),
        edge("3 1\n1\n2\n3\n", "6\n"),
        edge("2 2\n1 2\n3 4\n", "8\n"),
        edge("3 3\n1 2 3\n4 5 6\n7 8 9\n", "29\n"),
        stress("4 4\n1 0 0 0\n0 10 0 0\n0 0 10 0\n0 0 0 1\n", "22\n"),
    ]
