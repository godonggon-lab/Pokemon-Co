from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n5 6\n1 0 0 0\n"),
        edge("2\n5 6\n0 1 0 0\n"),
        edge("3\n3 4 5\n1 1 0 0\n"),
        edge("3\n7 3 2\n0 0 1 1\n"),
        edge("4\n1 2 3 4\n1 1 1 0\n"),
        stress("6\n10 20 30 40 50 60\n2 1 1 1\n"),
    ]
