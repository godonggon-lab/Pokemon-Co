from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 1\n7\n"),
        edge("2 2 2\n1 2\n3 4\n"),
        stress("4 4 4\n1 -2 3 4\n-5 6 -7 8\n9 -10 11 -12\n13 14 -15 16\n"),
    ]
