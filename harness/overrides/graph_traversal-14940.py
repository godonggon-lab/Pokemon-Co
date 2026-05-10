from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n2\n", "0\n"),
        edge("1 2\n2 1\n", "0 1\n"),
        edge("2 2\n2 1\n1 1\n", "0 1\n1 2\n"),
        edge("3 3\n2 0 1\n0 0 1\n1 1 1\n", "0 0 -1\n0 0 -1\n-1 -1 -1\n"),
        edge("3 4\n1 1 1 1\n1 2 0 1\n1 1 1 1\n", "2 1 2 3\n1 0 0 4\n2 1 2 3\n"),
        stress("4 4\n2 1 0 1\n1 1 0 1\n0 1 1 1\n1 1 0 1\n", "0 1 0 7\n1 2 0 6\n0 3 4 5\n5 4 0 6\n"),
    ]
