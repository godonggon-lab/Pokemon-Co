from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n5 6\n0 0 1 0\n"),
        edge("6\n1 2 3 4 5 6\n2 1 1 1\n"),
        stress("8\n-3 4 -5 6 -7 8 -9 10\n2 2 2 1\n"),
    ]
