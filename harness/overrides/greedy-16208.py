from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10\n"),
        edge("2\n1 2\n"),
        edge("3\n1 2 3\n"),
        edge("4\n4 3 2 1\n"),
        edge("5\n5 5 5 5 5\n"),
        stress("8\n1 3 5 7 9 11 13 15\n"),
    ]
