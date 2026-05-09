from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n", "0\n0\n"),
        edge("3 3\n0 0 0\n0 1 0\n0 0 0\n", "1\n1\n"),
        edge("4 4\n0 0 0 0\n0 1 1 0\n0 1 1 0\n0 0 0 0\n", "1\n4\n"),
        edge("5 5\n0 0 0 0 0\n0 1 1 1 0\n0 1 1 1 0\n0 1 1 1 0\n0 0 0 0 0\n", "2\n1\n"),
        edge("5 5\n0 0 0 0 0\n0 1 1 1 0\n0 1 0 1 0\n0 1 1 1 0\n0 0 0 0 0\n", "1\n8\n"),
        edge("6 6\n0 0 0 0 0 0\n0 1 1 1 1 0\n0 1 1 1 1 0\n0 1 1 1 1 0\n0 1 1 1 1 0\n0 0 0 0 0 0\n", "2\n4\n"),
    ]
