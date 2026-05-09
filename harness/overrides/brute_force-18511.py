from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("10 1\n1\n"),
        edge("100 2\n1 9\n"),
        edge("657 3\n1 5 7\n"),
        edge("999 3\n3 6 9\n"),
        edge("1234 4\n1 2 3 4\n"),
        stress("98765 5\n1 3 5 7 9\n"),
    ]
