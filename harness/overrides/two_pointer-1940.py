from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n3\n1 2\n"),
        edge("2\n10\n1 2\n"),
        edge("5\n5\n1 2 3 4 5\n"),
        edge("6\n7\n1 6 2 5 3 4\n"),
        edge("8\n10\n1 1 9 9 5 5 4 6\n"),
        stress("20\n21\n1 20 2 19 3 18 4 17 5 16 6 15 7 14 8 13 9 12 10 11\n"),
    ]
