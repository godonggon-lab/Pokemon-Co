from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1 1\n", "1\n"),
        edge("10 1\n3 5\n", "6\n"),
        edge("10 2\n3 5\n1 1\n", "6\n"),
        edge("12 2\n5 5\n7 8\n", "12\n"),
        edge("20 3\n3 5\n8 12\n20 30\n", "12\n"),
        stress("100 3\n10 10\n15 20\n40 60\n", "70\n"),
    ]
