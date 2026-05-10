from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1 1\n1 0\n", "2\n"),
        edge("3\n1 1 1\n1 1 1\n1 1 0\n", "6\n"),
        edge("3\n2 1 1\n1 1 1\n1 1 0\n", "2\n"),
        edge("4\n2 3 3 1\n1 2 1 3\n1 2 3 1\n3 1 1 0\n", "3\n"),
        edge("4\n3 1 1 1\n1 1 1 1\n1 1 1 1\n1 1 1 0\n", "2\n"),
        stress("4\n2 2 2 2\n2 2 2 2\n2 2 2 2\n2 2 2 0\n", "0\n"),
    ]
