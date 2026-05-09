from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n2 5\n1 4\n", "1\n"),
        edge("1\n3 10\n1 2 3\n", "1\n"),
        edge("1\n4 5\n1 2 3 4\n", "2\n"),
        edge("1\n5 0\n-5 -1 1 2 10\n", "1\n"),
        edge("2\n2 5\n1 4\n4 5\n1 2 3 4\n", "1\n2\n"),
        stress("1\n6 8\n1 2 3 5 6 10\n", "2\n"),
    ]
