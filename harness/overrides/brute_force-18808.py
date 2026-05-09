from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 1\n1 1\n1\n"),
        edge("2 2 1\n1 2\n1 1\n"),
        edge("3 3 2\n1 3\n1 1 1\n2 1\n1\n1\n"),
        edge("4 4 2\n2 2\n1 1\n1 1\n2 3\n1 0 1\n1 1 1\n"),
        edge("5 5 3\n2 3\n1 1 0\n0 1 1\n3 2\n1 0\n1 1\n0 1\n1 4\n1 1 1 1\n"),
        stress("6 6 4\n2 2\n1 1\n1 1\n2 3\n1 0 1\n1 1 1\n3 1\n1\n1\n1\n1 5\n1 1 1 1 1\n"),
    ]
