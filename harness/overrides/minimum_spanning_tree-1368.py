from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n0\n"),
        edge("2\n5\n5\n0 1\n1 0\n"),
        edge("3\n10\n10\n1\n0 2 3\n2 0 4\n3 4 0\n"),
        edge("3\n1\n100\n100\n0 50 50\n50 0 1\n50 1 0\n"),
        edge("4\n8\n6\n7\n10\n0 3 4 100\n3 0 2 5\n4 2 0 1\n100 5 1 0\n"),
        stress("5\n20\n15\n30\n25\n10\n0 5 9 8 7\n5 0 6 20 4\n9 6 0 3 11\n8 20 3 0 2\n7 4 11 2 0\n"),
    ]
