from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 0\n", "0\n"),
        edge("2\n1 0\n1 1\n", "1\n"),
        edge("4\n1 0\n2 1\n1 1\n2 0\n", "2\n"),
        edge("5\n1 0\n1 0\n1 1\n1 1\n1 0\n", "2\n"),
        edge("6\n1 0\n2 0\n3 0\n1 1\n2 1\n3 1\n", "3\n"),
        stress("8\n1 0\n2 1\n1 1\n2 0\n1 0\n2 1\n3 0\n3 1\n", "5\n"),
    ]
