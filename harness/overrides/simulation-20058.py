from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1 2\n3 4\n0\n"),
        edge("1 2\n1 0\n0 1\n1 0\n"),
        edge("2 1\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n1\n"),
        edge("2 2\n0 0 0 0\n0 5 5 0\n0 5 5 0\n0 0 0 0\n1 2\n"),
        edge("3 2\n1 1 1 1 1 1 1 1\n1 0 0 0 0 0 0 1\n1 0 5 5 5 5 0 1\n1 0 5 0 0 5 0 1\n1 0 5 5 5 5 0 1\n1 0 0 0 0 0 0 1\n1 1 1 1 1 1 1 1\n0 0 0 0 0 0 0 0\n1 2\n"),
        stress("3 3\n1 2 3 4 5 6 7 8\n8 7 6 5 4 3 2 1\n1 1 1 1 1 1 1 1\n2 2 2 2 2 2 2 2\n3 3 3 3 3 3 3 3\n4 4 4 4 4 4 4 4\n5 5 5 5 5 5 5 5\n6 6 6 6 6 6 6 6\n1 2 3\n"),
    ]
