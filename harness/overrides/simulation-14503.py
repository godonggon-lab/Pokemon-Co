from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3\n1 1 0\n1 1 1\n1 0 1\n1 1 1\n", "1\n"),
        edge("3 3\n1 1 0\n1 1 1\n1 0 1\n1 1 1\n", "1\n"),
        edge("3 4\n1 1 0\n1 1 1 1\n1 0 0 1\n1 1 1 1\n", "2\n"),
        edge("4 4\n1 1 1\n1 1 1 1\n1 0 0 1\n1 0 0 1\n1 1 1 1\n", "4\n"),
        edge("4 5\n1 1 1\n1 1 1 1 1\n1 0 0 0 1\n1 0 1 0 1\n1 1 1 1 1\n", "5\n"),
        stress("5 5\n2 2 0\n1 1 1 1 1\n1 0 0 0 1\n1 0 0 0 1\n1 0 0 0 1\n1 1 1 1 1\n", "9\n"),
    ]
