from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n7\n"),
        edge("1 3\n3 2 1\n"),
        edge("3 1\n3\n2\n1\n"),
        edge("2 2\n4 3\n2 1\n"),
        edge("3 3\n9 6 3\n8 5 2\n7 4 1\n"),
        stress("5 5\n25 24 23 22 21\n20 19 18 17 16\n15 14 13 12 11\n10 9 8 7 6\n5 4 3 2 1\n"),
    ]
