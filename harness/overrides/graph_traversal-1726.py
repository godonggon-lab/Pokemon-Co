from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n1 1 1\n1 1 1\n"),
        edge("1 5\n0 0 0 0 0\n1 1 1\n1 5 1\n"),
        edge("5 1\n0\n0\n0\n0\n0\n1 1 3\n5 1 3\n"),
        edge("3 3\n0 0 0\n0 1 0\n0 0 0\n1 1 1\n3 3 3\n"),
        edge("4 5\n0 0 0 0 0\n1 1 0 1 0\n0 0 0 1 0\n0 1 0 0 0\n1 1 1\n4 5 1\n"),
        stress("5 5\n0 0 0 0 0\n0 1 1 1 0\n0 0 0 1 0\n0 1 0 0 0\n0 0 0 1 0\n1 1 1\n5 5 2\n"),
    ]
