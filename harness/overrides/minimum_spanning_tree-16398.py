from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n", "0\n"),
        edge("2\n0 5\n5 0\n", "5\n"),
        edge("3\n0 1 3\n1 0 2\n3 2 0\n", "3\n"),
        edge("4\n0 1 4 10\n1 0 2 5\n4 2 0 3\n10 5 3 0\n", "6\n"),
        edge("4\n0 10 10 1\n10 0 2 2\n10 2 0 3\n1 2 3 0\n", "5\n"),
        stress("5\n0 3 4 8 9\n3 0 2 6 7\n4 2 0 5 1\n8 6 5 0 2\n9 7 1 2 0\n", "8\n"),
    ]
