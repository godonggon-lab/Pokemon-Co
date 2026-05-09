from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n5\n1 1\n"),
        edge("3 3\n1 2 3\n1 1\n1 3\n2 3\n"),
        edge("5 3\n5 4 3 2 1\n1 5\n2 4\n3 3\n"),
        edge("4 2\n-1 -2 -3 -4\n1 4\n2 3\n"),
        edge("6 3\n1 1 1 1 1 1\n1 6\n3 5\n6 6\n"),
        stress("10 5\n1 2 3 4 5 6 7 8 9 10\n1 10\n1 1\n10 10\n3 7\n4 9\n"),
    ]
