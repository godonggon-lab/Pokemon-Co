from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3 1\n1 2 3\n4 5 6\n"),
        edge("4 3 2\n-1 3 5 7\n2 -4 6\n"),
        stress("5 4 3\n1 -2 3 -4 5\n10 20 -30 40\n"),
    ]
