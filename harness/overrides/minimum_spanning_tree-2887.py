from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n0 0 0\n10 20 30\n"),
        edge("3\n0 0 0\n1 100 100\n100 1 100\n"),
        edge("4\n0 0 0\n5 5 5\n10 0 10\n0 10 10\n"),
        edge("5\n11 -15 -15\n14 -5 -15\n-1 -1 -5\n10 -4 -1\n19 -4 19\n"),
        edge("6\n0 0 0\n1 2 3\n2 4 6\n3 6 9\n10 10 10\n11 12 13\n"),
        stress("8\n0 0 0\n3 8 2\n6 1 4\n9 9 9\n12 3 7\n15 14 1\n18 5 6\n21 20 2\n"),
    ]
