from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1 4\n4\n3 2 5 6\n"),
        edge("1\n7\n3\n7 14 1\n"),
        stress("5\n1 3 9 27 81\n6\n1 2 4 40 121 122\n"),
    ]
