from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3\n0 0 0\n0 1 0\n0 0 0\n", "0\n"),
        edge("5 5\n0 0 0 0 0\n0 2 2 2 0\n0 2 2 2 0\n0 2 2 2 0\n0 0 0 0 0\n", "0\n"),
        edge("5 5\n0 0 0 0 0\n0 2 0 2 0\n0 0 0 0 0\n0 2 0 2 0\n0 0 0 0 0\n", "0\n"),
        edge("5 5\n0 0 0 0 0\n0 3 3 3 0\n0 3 0 3 0\n0 3 3 3 0\n0 0 0 0 0\n", "0\n"),
        edge("5 7\n0 0 0 0 0 0 0\n0 4 4 4 4 4 0\n0 4 0 0 0 4 0\n0 4 4 4 4 4 0\n0 0 0 0 0 0 0\n", "0\n"),
        stress("5 7\n0 0 0 0 0 0 0\n0 5 5 1 5 5 0\n0 5 1 1 1 5 0\n0 5 5 1 5 5 0\n0 0 0 0 0 0 0\n", "2\n"),
    ]
