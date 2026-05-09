from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0\n"),
        edge("3 0\n"),
        edge("3 2\n1 2\n2 3\n"),
        edge("5 2\n1 2\n4 5\n"),
        edge("6 5\n1 2\n2 3\n3 1\n4 5\n5 6\n"),
        stress("8 6\n1 2\n2 3\n4 5\n5 6\n6 4\n7 8\n"),
    ]
