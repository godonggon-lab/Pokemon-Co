from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0\n", "1\n"),
        edge("4 0\n", "1 2 3 4\n"),
        edge("3 2\n1 2\n2 3\n", "3\n"),
        edge("4 2\n1 2\n3 2\n", "2\n"),
        edge("5 4\n1 5\n2 5\n3 5\n4 5\n", "5\n"),
        stress("8 8\n1 2\n2 3\n3 4\n4 5\n6 5\n7 5\n8 5\n1 5\n", "5\n"),
    ]
