from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0 1 0 1 2\n", "1 2\n"),
        edge("1 1 3 1 -1 1\n", "2 1\n"),
        edge("2 3 13 1 -1 -1\n", "2 3\n"),
        edge("1 2 5 3 4 11\n", "1 2\n"),
        edge("5 7 31 3 2 12\n", "2 3\n"),
        stress("-1 1 0 1 1 4\n", "2 2\n"),
    ]
