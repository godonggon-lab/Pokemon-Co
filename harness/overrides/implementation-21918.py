from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n1 1 1\n"),
        edge("3 2\n0 1 0\n2 1 3\n3 2 2\n"),
        edge("5 4\n1 0 1 0 1\n1 3 0\n2 1 5\n3 2 4\n4 1 3\n"),
        edge("6 5\n0 0 0 0 0 0\n4 1 6\n2 2 5\n1 4 1\n3 3 6\n2 1 6\n"),
        edge("8 6\n1 1 1 1 1 1 1 1\n3 1 8\n4 2 7\n2 1 4\n1 8 0\n2 5 8\n4 1 1\n"),
        stress("10 8\n0 1 0 1 0 1 0 1 0 1\n2 1 10\n3 1 5\n4 6 10\n1 5 1\n2 4 7\n3 2 9\n4 1 10\n1 10 0\n"),
    ]
