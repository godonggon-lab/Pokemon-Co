from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n", "1\n"),
        edge("1\n1\n", "0\n"),
        edge("2\n0 1\n2 0\n", "2\n"),
        edge("3\n0 1 2\n1 2 0\n2 0 1\n", "5\n"),
        edge("3\n0 0 0\n0 0 0\n0 0 0\n", "1\n"),
        stress("4\n0 1 2 0\n1 2 0 1\n2 0 1 2\n0 1 2 0\n", "7\n"),
    ]
