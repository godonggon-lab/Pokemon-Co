from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 1 2 2\n"),
        edge("2\n-1 -1 1 1\n2 2 3 3\n"),
        stress("4\n-2 -2 2 2\n2 -1 4 1\n5 5 6 6\n-6 5 -5 6\n"),
    ]
