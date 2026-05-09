from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0\n", "0\n"),
        edge("2 1\n1 2 5\n", "5\n"),
        edge("3 3\n1 2 1\n2 3 2\n1 3 3\n", "3\n"),
        edge("4 5\n1 2 1\n2 3 2\n3 4 3\n1 4 10\n2 4 4\n", "6\n"),
        edge("5 7\n1 2 4\n1 3 2\n2 3 1\n2 4 7\n3 4 3\n3 5 8\n4 5 5\n", "11\n"),
        stress("6 9\n1 2 3\n1 3 1\n2 3 2\n2 4 4\n3 4 6\n3 5 5\n4 5 7\n4 6 8\n5 6 9\n", "20\n"),
    ]
