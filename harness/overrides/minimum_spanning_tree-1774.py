from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 0\n0 0\n3 4\n", "5.00\n"),
        edge("2 1\n0 0\n3 4\n1 2\n", "0.00\n"),
        edge("3 0\n0 0\n3 0\n0 4\n", "7.00\n"),
        edge("3 1\n0 0\n3 0\n0 4\n1 2\n", "4.00\n"),
        edge("4 1\n0 0\n0 3\n4 0\n4 3\n1 2\n", "7.00\n"),
        stress("5 2\n0 0\n2 0\n2 2\n0 2\n5 5\n1 2\n3 4\n", "6.24\n"),
    ]
