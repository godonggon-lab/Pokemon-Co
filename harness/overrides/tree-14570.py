from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n-1 -1\n10\n"),
        edge("3\n2 3\n-1 -1\n-1 -1\n5\n"),
        stress("5\n2 3\n4 5\n-1 -1\n-1 -1\n-1 -1\n9\n"),
    ]
