from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 1\n1 2 4 6 7\n"),
        edge("4 2\n1 3 5 7\n"),
        stress("10 3\n1 2 4 5 6 8 10 11 12 14\n"),
    ]
