from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0 10\n"),
        edge("1 10\n10\n"),
        edge("3 10\n1 2 3\n"),
        edge("3 10\n10 10 10\n"),
        edge("5 10\n6 4 5 5 1\n"),
        stress("8 15\n5 5 5 5 5 5 5 5\n"),
    ]
