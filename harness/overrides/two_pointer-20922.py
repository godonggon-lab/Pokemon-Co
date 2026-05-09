from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n", "1\n"),
        edge("3 1\n1 2 3\n", "3\n"),
        edge("3 1\n1 1 1\n", "1\n"),
        edge("5 2\n1 1 1 2 2\n", "4\n"),
        edge("9 2\n3 2 5 5 6 4 4 5 7\n", "7\n"),
        stress("12 3\n1 2 1 2 1 2 3 3 3 4 4 4\n", "12\n"),
    ]
