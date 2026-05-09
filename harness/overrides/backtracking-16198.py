from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n1 2 3\n"),
        edge("4\n1 2 3 4\n"),
        edge("4\n10 1 10 1\n"),
        edge("5\n2 2 2 2 2\n"),
        edge("6\n1 9 2 8 3 7\n"),
        stress("10\n1 2 3 4 5 6 7 8 9 10\n"),
    ]
