from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n7\n", "0\n"),
        edge("2\n1 2\n", "2\n"),
        edge("3\n1 2 3\n", "11\n"),
        edge("5\n1 1 1 1 1\n", "10\n"),
        edge("5\n0 1 2 3 4\n", "35\n"),
        stress("100\n" + " ".join(str(i) for i in range(1, 101)) + "\n", "12582075\n"),
    ]
