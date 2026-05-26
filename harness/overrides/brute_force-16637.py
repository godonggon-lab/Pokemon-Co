from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n7\n"),
        edge("9\n3+8*7-9*2\n"),
        stress("11\n1-2*3+4*5-6\n"),
    ]
