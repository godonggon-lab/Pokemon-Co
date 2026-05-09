from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n-1 2\n", "-1 2\n"),
        edge("5\n-2 4 -99 -1 98\n", "-99 98\n"),
        edge("3\n1 2 3\n", "1 2\n"),
        edge("3\n-5 -2 -1\n", "-2 -1\n"),
        edge("6\n-10 -4 -1 2 7 20\n", "-1 2\n"),
        stress("10\n-100 -50 -20 -7 -3 2 5 9 40 90\n", "-3 2\n"),
    ]
