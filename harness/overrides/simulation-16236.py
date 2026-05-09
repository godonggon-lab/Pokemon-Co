from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n9 0\n0 1\n", "2\n"),
        edge("3\n0 0 0\n0 9 1\n0 0 0\n", "1\n"),
        edge("3\n1 0 0\n0 9 0\n0 0 1\n", "6\n"),
        edge("4\n0 0 0 0\n0 9 3 0\n0 1 0 0\n0 0 1 0\n", "3\n"),
        edge("5\n0 0 0 0 0\n0 9 1 0 0\n0 0 0 0 0\n0 0 1 0 0\n0 0 0 1 0\n", "5\n"),
        stress("6\n5 4 3 2 3 4\n4 3 2 3 4 5\n3 2 9 5 6 6\n2 1 2 3 4 5\n3 2 1 6 5 4\n6 6 6 6 6 6\n", "60\n"),
    ]
