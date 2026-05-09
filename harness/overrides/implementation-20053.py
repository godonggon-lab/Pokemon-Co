from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n0\n", "0 0\n"),
        edge("1\n5\n20 10 35 30 7\n", "7 35\n"),
        edge("2\n3\n-1 -2 -3\n4\n5 5 5 5\n", "-3 -1\n5 5\n"),
        edge("1\n6\n-1000000 1000000 0 42 -7 42\n", "-1000000 1000000\n"),
        edge("3\n2\n1 2\n2\n2 1\n3\n0 0 0\n", "1 2\n1 2\n0 0\n"),
        stress("1\n20\n" + " ".join(str(i) for i in range(-10, 10)) + "\n", "-10 9\n"),
    ]
