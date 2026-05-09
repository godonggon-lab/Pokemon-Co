from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n5\n", "-5 \n"),
        edge("3 1\n1 2 3\n4 5 6\n7 8 9\n", "-1 -2 -3 \n-4 -5 -6 \n-7 -8 -9 \n"),
        edge("3 3\n1 1 1\n1 1 1\n1 1 1\n", "0 0 0 \n0 -1 0 \n0 0 0 \n"),
        edge("5 3\n1 2 3 2 1\n2 3 4 3 2\n3 4 5 4 3\n2 3 4 3 2\n1 2 3 2 1\n", "0 0 0 0 0 \n0 -1 -1 -1 0 \n0 -1 0 0 -1 \n0 -1 0 0 -1 \n0 0 -1 -1 1 \n"),
        edge("5 5\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1\n", "0 0 0 0 0 \n0 0 0 0 0 \n0 0 -1 0 0 \n0 0 0 0 0 \n0 0 0 0 0 \n"),
        stress("7 3\n1 0 2 0 3 0 4\n0 5 0 6 0 7 0\n8 0 9 0 10 0 11\n0 12 0 13 0 14 0\n15 0 16 0 17 0 18\n0 19 0 20 0 21 0\n22 0 23 0 24 0 25\n", "0 0 0 0 0 0 0 \n0 -1 1 -2 1 -2 1 \n0 1 -6 7 -7 3 -3 \n0 -8 13 -14 7 -3 3 \n0 7 -19 19 -13 1 -2 \n0 -14 21 -21 7 0 0 \n0 7 -21 21 -14 0 0 \n"),
    ]
