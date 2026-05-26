from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("4\n0 10 15 20\n5 0 9 10\n6 13 0 12\n8 8 9 0\n"),
        edge("3\n0 1 0\n1 0 2\n3 4 0\n"),
        stress("5\n0 7 3 0 2\n4 0 6 5 0\n8 1 0 9 7\n6 4 2 0 3\n5 8 1 6 0\n"),
    ]
