from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 0\n5\n", "1\n"),
        edge("1\n2 0\n1 2\n", "2\n"),
        edge("1\n2 1\n1 2\n", "1\n"),
        edge("1\n4 2\n1 2 3 4\n", "2\n"),
        edge("2\n3 0\n2 1 2\n3 2\n1 1 9\n", "1\n1\n"),
        stress("1\n6 3\n1 1 9 1 1 1\n", "2\n"),
    ]
