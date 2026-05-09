from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n1 2 5\n", "0\n"),
        edge("3 3\n1 2 1\n2 3 2\n1 3 3\n", "1\n"),
        edge("4 5\n1 2 1\n2 3 2\n3 4 3\n1 4 10\n2 4 4\n", "3\n"),
        edge("5 6\n1 2 3\n1 3 4\n2 3 2\n2 4 6\n3 5 5\n4 5 1\n", "6\n"),
        edge("7 12\n1 2 3\n1 3 2\n3 2 1\n2 5 2\n3 4 4\n7 3 6\n5 1 5\n1 6 2\n6 4 1\n6 5 3\n4 5 3\n6 7 4\n", "8\n"),
        stress("6 9\n1 2 1\n1 3 5\n2 3 2\n2 4 4\n3 4 3\n3 5 8\n4 5 7\n4 6 6\n5 6 9\n", "12\n"),
    ]
