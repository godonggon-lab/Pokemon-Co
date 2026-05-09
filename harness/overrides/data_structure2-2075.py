from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n", "5\n"),
        edge("2\n1 2\n3 4\n", "3\n"),
        edge("3\n1 2 3\n4 5 6\n7 8 9\n", "7\n"),
        edge("3\n9 8 7\n6 5 4\n3 2 1\n", "7\n"),
        edge("4\n1 1 1 1\n2 2 2 2\n3 3 3 3\n4 4 4 4\n", "4\n"),
        stress("5\n1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25\n", "21\n"),
    ]
