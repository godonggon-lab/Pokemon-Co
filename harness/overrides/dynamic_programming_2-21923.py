from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n5\n"),
        edge("1 2\n1 2\n"),
        edge("2 1\n1\n2\n"),
        edge("2 2\n1 2\n3 4\n"),
        edge("3 3\n1 2 3\n4 5 6\n7 8 9\n"),
        stress("3 4\n1 -2 3 4\n5 6 -7 8\n9 10 11 -12\n"),
    ]
