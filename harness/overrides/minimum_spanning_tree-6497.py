from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0\n0 0\n"),
        edge("2 1\n0 1 5\n0 0\n"),
        edge("3 3\n0 1 1\n1 2 2\n0 2 5\n0 0\n"),
        edge("4 5\n0 1 3\n1 2 4\n2 3 5\n0 3 10\n0 2 2\n0 0\n"),
        edge("3 3\n0 1 1\n1 2 2\n0 2 3\n4 5\n0 1 1\n1 2 1\n2 3 1\n3 0 1\n0 2 10\n0 0\n"),
        stress("5 7\n0 1 4\n0 2 2\n1 2 1\n1 3 7\n2 3 3\n2 4 8\n3 4 5\n0 0\n"),
    ]
