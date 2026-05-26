from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1 -1\n"),
        edge("6\n20 1 15 8 4 10\n"),
        stress("8\n-100 100 -50 50 -25 25 0 75\n"),
    ]
