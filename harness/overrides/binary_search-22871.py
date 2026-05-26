from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1 3\n"),
        edge("5\n1 4 2 7 3\n"),
        stress("7\n10 1 9 2 8 3 7\n"),
    ]
