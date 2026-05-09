from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3 1\n0 0 0\n-1 10 0\n-1 0 0\n", "8\n"),
        edge("4 4 1\n0 0 0 0\n-1 0 5 0\n-1 0 0 0\n0 0 0 0\n", "5\n"),
        edge("5 5 2\n0 0 5 0 0\n-1 0 0 0 0\n-1 0 10 0 0\n0 0 0 0 0\n0 0 0 0 0\n", "14\n"),
        edge("6 6 3\n0 0 0 0 0 0\n-1 0 0 30 0 0\n-1 0 0 0 0 0\n0 0 0 0 20 0\n0 10 0 0 0 0\n0 0 0 0 0 0\n", "57\n"),
        edge("7 7 4\n0 0 0 0 0 0 0\n-1 10 0 0 0 0 0\n-1 0 0 0 20 0 0\n0 0 0 0 0 0 0\n0 0 30 0 0 0 0\n0 0 0 0 0 40 0\n0 0 0 0 0 0 0\n", "97\n"),
        stress("7 8 5\n0 0 0 0 0 0 0 9\n0 0 0 0 3 0 0 8\n-1 0 5 0 0 0 22 0\n-1 8 0 0 0 0 0 0\n0 0 0 0 0 10 43 0\n0 0 5 0 15 0 0 0\n0 0 40 0 0 0 20 0\n", "172\n"),
    ]
