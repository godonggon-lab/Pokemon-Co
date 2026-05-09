from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n"),
        edge("3\n1 2 3\n"),
        edge("3\n3 2 1\n"),
        edge("5\n3 1 4 3 2\n"),
        edge("6\n10 10 10 10 10 10\n"),
        stress("10\n10 9 8 7 6 5 4 3 2 1\n"),
    ]
