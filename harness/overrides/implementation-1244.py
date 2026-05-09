from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n1\n1 1\n", "1\n"),
        edge("8\n0 1 0 1 0 0 0 1\n2\n1 3\n2 3\n", "1 0 0 0 1 1 0 1\n"),
        edge("5\n1 1 1 1 1\n1\n2 3\n", "0 0 0 0 0\n"),
        edge("10\n0 0 0 0 0 0 0 0 0 0\n3\n1 2\n1 5\n2 6\n", "0 1 0 1 1 0 0 1 0 0\n"),
        edge("21\n0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0\n2\n1 1\n2 11\n", "0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1\n0\n"),
        stress("25\n1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1\n3\n1 3\n2 13\n1 5\n", "1 0 0 0 0 1 1 0 0 1 1 1 0 0 1 0 1 1 1 1\n0 0 1 1 0\n"),
    ]
