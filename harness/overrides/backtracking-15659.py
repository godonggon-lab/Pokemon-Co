from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n5 6\n0 0 1 0\n"),
        edge("4\n1 2 3 4\n1 1 1 0\n"),
        stress("6\n3 8 2 5 7 4\n2 1 1 1\n"),
    ]
