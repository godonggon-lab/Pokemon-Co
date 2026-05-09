from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n"),
        edge("1\n2\n"),
        edge("4\n1 3 5 7\n"),
        edge("5\n2 4 6 8 10\n"),
        edge("6\n997 991 1 0 3 4\n"),
        stress("10\n2 3 5 7 11 13 17 19 23 29\n"),
    ]
