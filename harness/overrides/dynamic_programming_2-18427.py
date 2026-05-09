from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 1\n1\n"),
        edge("1 3 5\n1 2 3\n"),
        edge("2 2 3\n1 2\n1 3\n"),
        edge("3 3 5\n1 2 3\n2 3 4\n1 4 5\n"),
        edge("4 4 10\n1 5\n2 4 6\n3 7\n1 2 8\n"),
        stress("5 5 12\n1 2 3\n2 5 7\n1 4 6\n3 6 9\n2 8 10\n"),
    ]
