from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n"),
        edge("3 3\n3 0 3\n"),
        edge("4 4\n0 1 2 3\n"),
        edge("4 4\n3 0 0 3\n"),
        edge("5 8\n0 1 0 2 1 0 1 3\n"),
        stress("10 10\n10 0 9 0 8 0 7 0 6 10\n"),
    ]
