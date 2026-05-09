from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 10\n10\n5\n", "5\n"),
        edge("3 60\n30 10 20\n3 0 4\n", "7\n"),
        edge("3 10\n6 7 8\n0 5 6\n", "5\n"),
        edge("5 100\n30 40 50 60 70\n3 4 5 6 7\n", "10\n"),
        edge("3 1\n1 1 1\n0 0 0\n", "0\n"),
        edge("4 15\n5 5 5 5\n1 2 3 4\n", "6\n"),
    ]
