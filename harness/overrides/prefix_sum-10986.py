from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n5\n", "1\n"),
        edge("1 2\n1\n", "0\n"),
        edge("3 3\n1 2 3\n", "3\n"),
        edge("5 3\n1 2 3 1 2\n", "7\n"),
        edge("5 5\n5 5 5 5 5\n", "15\n"),
        stress("10 4\n1 2 3 4 5 6 7 8 9 10\n", "10\n"),
    ]
