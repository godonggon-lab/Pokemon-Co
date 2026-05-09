from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n42\n"),
        edge("2 2\n2 1\n"),
        edge("3 2\n4 2 9\n"),
        edge("4 3\n10 1 7 3\n"),
        edge("5 1\n5 4 3 2 1\n"),
        stress("7 3\n7 1 6 2 5 3 4\n"),
    ]
