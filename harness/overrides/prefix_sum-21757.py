from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("4\n1 1 1 1\n", "1\n"),
        edge("5\n1 1 1 1 1\n", "0\n"),
        edge("8\n1 1 1 1 1 1 1 1\n", "1\n"),
        edge("5\n0 0 0 0 0\n", "4\n"),
        edge("6\n0 0 0 0 0 0\n", "10\n"),
        edge("6\n1 -1 1 -1 1 -1\n", "0\n"),
    ]
