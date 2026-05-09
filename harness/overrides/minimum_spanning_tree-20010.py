from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n0 1 5\n", "5\n5\n"),
        edge("3 3\n0 1 1\n1 2 2\n0 2 5\n", "3\n3\n"),
        edge("4 5\n0 1 1\n1 2 2\n2 3 3\n0 3 10\n1 3 4\n", "6\n6\n"),
        edge("4 3\n0 1 5\n1 2 5\n2 3 5\n", "15\n15\n"),
        edge("5 7\n0 1 2\n0 2 3\n1 2 1\n1 3 4\n2 4 5\n3 4 6\n0 4 10\n", "12\n10\n"),
        stress("6 9\n0 1 3\n0 2 1\n1 2 2\n1 3 4\n2 3 6\n2 4 5\n3 4 7\n3 5 8\n4 5 9\n", "20\n19\n"),
    ]
