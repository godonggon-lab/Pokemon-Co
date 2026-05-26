from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 10\n5 10 8 20\n"),
        edge("3 10\n5 10 3 8\n4 7 2 4\n4 9 3 5\n"),
        stress("4 15\n5 10 3 6\n4 7 8 20\n6 12 4 8\n3 5 5 9\n"),
    ]
