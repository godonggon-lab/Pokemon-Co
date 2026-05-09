from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n", "1\n"),
        edge("2\n1 1\n", "1 2\n"),
        edge("3\n1 1 1\n", "1 2 3\n"),
        edge("3\n-1 -1 -1\n", "1 3 2\n"),
        edge("5\n3 2 1 -3 -1\n", "1 4 5 3 2\n"),
        stress("6\n1 -1 2 -2 3 -3\n", "1 2 6 3 5 4\n"),
    ]
