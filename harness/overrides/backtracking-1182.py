from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n"),
        edge("1 0\n1\n"),
        edge("3 0\n-1 0 1\n"),
        edge("5 0\n-7 -3 -2 5 8\n"),
        edge("6 3\n1 2 3 4 -1 -2\n"),
        stress("10 5\n1 1 1 1 1 2 2 2 -1 -2\n"),
    ]
