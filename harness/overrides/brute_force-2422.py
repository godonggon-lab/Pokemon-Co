from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 0\n", "1\n"),
        edge("5 0\n", "10\n"),
        edge("5 1\n1 2\n", "7\n"),
        edge("5 3\n1 2\n3 4\n1 5\n", "2\n"),
        edge("6 5\n1 2\n2 3\n3 4\n4 5\n5 6\n", "4\n"),
        stress("8 6\n1 2\n1 3\n2 3\n4 5\n5 6\n6 7\n", "24\n"),
    ]
