from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n1 1 2\n"),
        edge("3\n1 1 0\n"),
        edge("4\n1 2 3 0\n"),
        edge("5\n8 3 2 4 7\n"),
        edge("6\n1 1 1 1 1 3\n"),
        stress("11\n1 2 3 4 5 6 7 8 9 10 11\n"),
    ]
