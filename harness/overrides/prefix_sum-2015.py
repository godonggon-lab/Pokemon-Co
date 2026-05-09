from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 5\n5\n"),
        edge("1 5\n1\n"),
        edge("3 3\n1 2 3\n"),
        edge("4 0\n1 -1 1 -1\n"),
        edge("5 5\n1 2 3 2 5\n"),
        stress("10 3\n1 2 -1 3 0 3 -3 1 2 1\n"),
    ]
