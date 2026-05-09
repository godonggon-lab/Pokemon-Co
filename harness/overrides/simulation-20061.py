from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 0 0\n", "0\n2\n"),
        edge("2\n2 0 0\n3 0 0\n", "0\n8\n"),
        edge("4\n1 0 0\n1 0 1\n1 0 2\n1 0 3\n", "1\n4\n"),
        edge("5\n2 0 0\n2 1 0\n3 0 0\n3 0 1\n1 2 2\n", "0\n18\n"),
        edge("8\n1 0 0\n2 0 1\n3 0 2\n1 1 1\n2 2 0\n3 0 3\n1 3 3\n1 0 0\n", "3\n6\n"),
        stress("10\n1 0 0\n1 0 1\n1 0 2\n1 0 3\n2 1 0\n2 2 1\n3 0 0\n3 0 1\n1 2 2\n1 3 3\n", "1\n18\n"),
    ]
