from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n1\n1 1\n", "0\n"),
        edge("3\n1 2 3\n2\n1 3\n2 3\n", "0\n0\n"),
        edge("3\n3 2 1\n2\n1 3\n1 2\n", "2\n1\n"),
        edge("5\n1 3 2 4 3\n3\n1 5\n2 4\n3 5\n", "2\n1\n1\n"),
        edge("5\n5 5 5 5 5\n2\n1 5\n2 4\n", "0\n0\n"),
        stress("8\n1 5 3 4 2 6 6 1\n4\n1 8\n2 5\n4 8\n6 7\n", "3\n2\n2\n0\n"),
    ]
