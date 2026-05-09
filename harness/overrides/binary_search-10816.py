from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n3\n5 4 6\n"),
        edge("5\n4 1 5 2 3\n5\n1 3 7 9 5\n"),
        edge("5\n1 1 1 2 2\n4\n1 2 3 0\n"),
        edge("6\n-1 -1 0 0 0 1\n5\n-1 0 1 2 -2\n"),
        edge("10\n1 2 2 3 3 3 4 4 4 4\n4\n1 2 3 4\n"),
        stress("12\n5 5 5 5 1 1 2 2 2 3 4 4\n6\n1 2 3 4 5 6\n"),
    ]
