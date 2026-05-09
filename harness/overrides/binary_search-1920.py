from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n3\n5\n4\n6\n", "1\n0\n0\n"),
        edge("5\n4 1 5 2 3\n5\n1 3 7 9 5\n", "1\n1\n0\n0\n1\n"),
        edge("3\n-1 0 1\n5\n-1\n0\n1\n2\n-2\n", "1\n1\n1\n0\n0\n"),
        edge("5\n1 1 1 1 1\n3\n1\n2\n0\n", "1\n0\n0\n"),
        edge("6\n10 20 30 40 50 60\n4\n5\n10\n60\n70\n", "0\n1\n1\n0\n"),
        stress("10\n1 4 9 16 25 36 49 64 81 100\n6\n1\n2\n49\n50\n100\n101\n", "1\n0\n1\n0\n1\n0\n"),
    ]
