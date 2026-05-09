from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n0 0 0\n0 0 10\n0 0 0\n", "10\n"),
        edge("3\n1 2 3\n4 5 6\n7 8 9\n", "40\n"),
        edge("5\n0 0 0 0 0\n0 0 0 0 0\n0 0 100 0 0\n0 0 0 0 0\n0 0 0 0 0\n", "0\n"),
        edge("5\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1\n", "24\n"),
        edge("5\n0 10 0 10 0\n10 0 10 0 10\n0 10 0 10 0\n10 0 10 0 10\n0 10 0 10 0\n", "101\n"),
        stress("7\n1 2 3 4 5 6 7\n8 9 10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31 32 33 34 35\n36 37 38 39 40 41 42\n43 44 45 46 47 48 49\n", "771\n"),
    ]
