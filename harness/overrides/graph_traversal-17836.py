from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2 2\n0 0\n0 0\n", "2\n"),
        edge("2 2 1\n0 0\n0 0\n", "Fail\n"),
        edge("3 3 4\n0 1 0\n0 1 0\n0 2 0\n", "4\n"),
        edge("3 3 3\n0 1 0\n0 1 0\n0 2 0\n", "Fail\n"),
        edge("4 4 6\n0 0 1 1\n1 0 1 0\n1 0 2 0\n1 1 1 0\n", "6\n"),
        stress("5 5 8\n0 1 1 1 1\n0 0 0 0 1\n1 1 1 0 1\n2 0 0 0 1\n1 1 1 0 0\n", "8\n"),
    ]
