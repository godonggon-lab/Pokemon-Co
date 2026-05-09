from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 0\n", "1\n"),
        edge("2 2 0\n", "2\n"),
        edge("3 3 0\n", "6\n"),
        edge("3 3 5\n", "4\n"),
        edge("4 4 6\n", "12\n"),
        stress("5 5 13\n", "36\n"),
    ]
