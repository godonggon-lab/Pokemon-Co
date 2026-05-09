from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n5\n", "1\n5\n"),
        edge("1\n3\n1 5 2\n", "2\n1 2\n"),
        edge("1\n5\n5 4 3 2 1\n", "3\n5 4 3\n"),
        edge("1\n7\n1 2 3 4 5 6 7\n", "4\n1 2 3 4\n"),
        edge("2\n1\n-10\n3\n-1 -5 -3\n", "1\n-10\n2\n-1 -3\n"),
        stress("1\n21\n" + " ".join(str(i) for i in range(1, 22)) + "\n", "11\n1 2 3 4 5 6 7 8 9 10\n11\n"),
    ]
