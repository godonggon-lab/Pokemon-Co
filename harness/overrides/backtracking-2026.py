from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 0\n"),
        edge("2 3 1\n1 2\n"),
        edge("3 3 3\n1 2\n1 3\n2 3\n"),
        edge("3 4 2\n1 2\n3 4\n"),
        edge("3 5 6\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n"),
        stress("4 6 9\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n3 5\n4 5\n5 6\n"),
    ]
