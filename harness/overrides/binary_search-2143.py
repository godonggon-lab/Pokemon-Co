from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n1\n1\n1\n2\n", "1\n"),
        edge("0\n2\n1 -1\n2\n1 -1\n", "3\n"),
        edge("5\n4\n1 3 1 2\n3\n1 3 2\n", "7\n"),
        edge("4\n2\n2 2\n2\n2 2\n", "4\n"),
        edge("10\n3\n1 2 3\n2\n4 5\n", "3\n"),
        stress("7\n4\n1 1 1 1\n3\n3 3 3\n", "11\n"),
    ]
