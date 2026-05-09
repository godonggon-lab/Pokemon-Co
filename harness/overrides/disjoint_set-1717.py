from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1 1 1\n"),
        edge("3 4\n0 1 2\n1 1 2\n1 2 3\n0 2 3\n"),
        edge("5 6\n0 1 2\n0 3 4\n1 1 3\n0 2 3\n1 1 4\n1 4 5\n"),
        edge("7 8\n0 1 2\n0 2 3\n1 1 3\n1 1 4\n0 4 5\n0 5 6\n0 6 7\n1 4 7\n"),
        edge("10 7\n1 1 10\n0 1 10\n1 1 10\n0 2 9\n0 9 10\n1 2 1\n1 3 4\n"),
        stress("12 12\n0 1 2\n0 2 3\n0 4 5\n0 5 6\n1 1 6\n0 3 4\n1 1 6\n0 7 8\n0 8 9\n0 9 10\n0 10 11\n1 7 11\n"),
    ]
