from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n0 1\n2 0\n"),
        edge("4\n0 1 2 3\n4 0 5 6\n7 1 0 2\n3 4 5 0\n"),
        edge("4\n0 1 1 1\n1 0 1 1\n1 1 0 1\n1 1 1 0\n"),
        edge("6\n0 1 2 3 4 5\n1 0 2 3 4 5\n1 2 0 3 4 5\n1 2 3 0 4 5\n1 2 3 4 0 5\n1 2 3 4 5 0\n"),
        edge("6\n0 5 4 3 2 1\n1 0 5 4 3 2\n2 1 0 5 4 3\n3 2 1 0 5 4\n4 3 2 1 0 5\n5 4 3 2 1 0\n"),
        stress("8\n0 1 2 3 4 5 6 7\n7 0 1 2 3 4 5 6\n6 7 0 1 2 3 4 5\n5 6 7 0 1 2 3 4\n4 5 6 7 0 1 2 3\n3 4 5 6 7 0 1 2\n2 3 4 5 6 7 0 1\n1 2 3 4 5 6 7 0\n"),
    ]
