from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 2\n1 2 3\n"),
        edge("4 3\n4 6 8 10\n"),
        stress("6 3\n2 5 7 11 13 17\n"),
    ]
