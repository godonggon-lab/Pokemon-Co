from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n"),
        edge("3 1\n2 3 4\n"),
        edge("3 3\n1 2 3\n"),
        edge("5 5\n10 1 2 3 4\n"),
        edge("6 2\n1 1 1 10 10 10\n"),
        stress("10 1\n1 2 3 4 5 6 7 8 9 10\n"),
    ]
