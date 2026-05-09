from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n"),
        edge("5 1\n3\n"),
        edge("10 3\n1 2 3\n"),
        edge("10 3\n2 9 5\n"),
        edge("10 10\n10 9 8 7 6 5 4 3 2 1\n"),
        stress("32 6\n27 16 30 11 6 23\n"),
    ]
