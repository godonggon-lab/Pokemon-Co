from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n1 2 5\n"),
        edge("3 1\n1 2 5\n"),
        edge("3 3\n1 2 1\n2 3 2\n1 3 5\n"),
        edge("4 5\n1 2 3\n2 3 4\n3 4 5\n1 4 10\n1 3 2\n"),
        edge("4 2\n1 2 1\n3 4 2\n"),
        stress("5 7\n1 2 4\n1 3 2\n2 3 1\n2 4 7\n3 4 3\n3 5 8\n4 5 5\n"),
    ]
