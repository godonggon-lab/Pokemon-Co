from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n", "0\n"),
        edge("1 1\n1\n", "6\n"),
        edge("2 1\n1 1\n", "10\n"),
        edge("1 2\n1\n1\n", "10\n"),
        edge("2 2\n1 1\n1 1\n", "14\n"),
        edge("2 2\n1 0\n0 1\n", "10\n"),
    ]
