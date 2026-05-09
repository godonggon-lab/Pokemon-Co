from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 0 0 4\n0\n1 2 3 4\n"),
        edge("2 2 0 0 4\n0 2\n3 0\n1 4 2 3\n"),
        edge("3 3 1 1 6\n0 0 0\n0 5 0\n0 0 0\n1 1 4 4 2 3\n"),
        edge("3 4 0 0 8\n0 2 0 4\n5 0 6 0\n0 7 0 8\n1 1 1 4 4 2 2 3\n"),
        edge("4 4 2 2 10\n0 0 0 0\n0 1 2 0\n0 3 4 0\n0 0 0 0\n1 2 3 4 1 2 3 4 1 2\n"),
        stress("5 5 2 2 12\n0 0 1 0 0\n0 2 0 3 0\n4 0 5 0 6\n0 7 0 8 0\n0 0 9 0 0\n1 1 4 4 2 2 3 3 1 4 2 3\n"),
    ]
