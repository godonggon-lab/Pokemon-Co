from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n0\n1\n"),
        edge("2\n2\n0 1\n1 0\n1 2\n"),
        edge("3\n3\n0 1 0\n1 0 1\n0 1 0\n1 2 3\n"),
        edge("3\n2\n0 1 0\n1 0 0\n0 0 0\n1 3\n"),
        edge("5\n4\n0 1 0 0 0\n1 0 1 0 0\n0 1 0 1 0\n0 0 1 0 1\n0 0 0 1 0\n1 3 5 2\n"),
        stress("6\n5\n0 1 0 0 0 0\n1 0 1 0 0 0\n0 1 0 0 0 0\n0 0 0 0 1 0\n0 0 0 1 0 1\n0 0 0 0 1 0\n1 2 3 2 1\n"),
    ]
