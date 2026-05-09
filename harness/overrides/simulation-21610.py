from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n1 0\n0 1\n1 1\n"),
        edge("3 2\n0 0 0\n0 0 0\n0 0 0\n1 1\n3 2\n"),
        edge("4 1\n1 2 3 4\n4 3 2 1\n1 1 1 1\n0 0 0 0\n8 1\n"),
        edge("5 3\n0 1 0 1 0\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1\n0 1 0 1 0\n1 3\n5 2\n7 1\n"),
        edge("6 4\n1 1 1 1 1 1\n2 2 2 2 2 2\n3 3 3 3 3 3\n4 4 4 4 4 4\n5 5 5 5 5 5\n6 6 6 6 6 6\n2 1\n4 2\n6 3\n8 4\n"),
        stress("8 5\n1 0 2 0 3 0 4 0\n0 4 0 3 0 2 0 1\n1 1 1 1 1 1 1 1\n2 2 2 2 2 2 2 2\n3 3 3 3 3 3 3 3\n4 4 4 4 4 4 4 4\n5 5 5 5 5 5 5 5\n6 6 6 6 6 6 6 6\n1 1\n2 2\n3 3\n4 4\n5 5\n"),
    ]
