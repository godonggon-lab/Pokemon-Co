from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n0 1\n1 0\n", "0\n"),
        edge("4\n0 1 2 3\n1 0 4 5\n2 4 0 6\n3 5 6 0\n", "2\n"),
        edge("4\n0 1 1 1\n1 0 1 1\n1 1 0 10\n1 1 10 0\n", "0\n"),
        edge("4\n0 5 4 5\n4 0 5 4\n5 4 0 5\n4 5 4 0\n", "0\n"),
        edge("6\n0 1 2 3 4 5\n1 0 2 3 4 5\n2 2 0 3 4 5\n3 3 3 0 4 5\n4 4 4 4 0 5\n5 5 5 5 5 0\n", "0\n"),
        stress("6\n0 1 2 3 4 5\n6 0 7 8 9 10\n11 12 0 13 14 15\n16 17 18 0 19 20\n21 22 23 24 0 25\n26 27 28 29 30 0\n", "12\n"),
    ]
