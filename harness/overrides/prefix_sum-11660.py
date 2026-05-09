from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n5\n1 1 1 1\n", "5\n"),
        edge("2 3\n1 2\n3 4\n1 1 1 1\n1 1 2 2\n2 1 2 2\n", "1\n10\n7\n"),
        edge("3 3\n1 2 3\n4 5 6\n7 8 9\n1 1 3 3\n2 2 3 3\n1 2 2 3\n", "45\n28\n16\n"),
        edge("3 2\n0 0 0\n0 10 0\n0 0 0\n2 2 2 2\n1 1 3 3\n", "10\n10\n"),
        edge("4 2\n1 1 1 1\n1 1 1 1\n1 1 1 1\n1 1 1 1\n1 1 4 4\n2 2 3 3\n", "16\n4\n"),
        stress("4 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n1 1 4 4\n1 1 1 4\n4 1 4 4\n2 2 3 3\n", "136\n10\n58\n34\n"),
    ]
