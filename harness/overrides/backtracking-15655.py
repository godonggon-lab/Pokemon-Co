from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n42\n"),
        edge("2 1\n2 1\n"),
        edge("3 2\n4 2 9\n"),
        edge("4 3\n10 1 7 3\n"),
        edge("5 5\n5 4 3 2 1\n"),
        stress("8 4\n8 1 7 2 6 3 5 4\n"),
    ]
