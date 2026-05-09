from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10\n", "10\n"),
        edge("2\n1 2\n", "3\n"),
        edge("3\n1 2 3\n", "3\n"),
        edge("4\n1 2 3 4\n", "5\n"),
        edge("5\n10 20 30 40 50\n", "50\n"),
        stress("6\n1 100 2 99 3 98\n", "101\n"),
    ]
