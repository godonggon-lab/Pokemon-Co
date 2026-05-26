from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 5\n1 2 3 4 5\n"),
        edge("6 7\n2 2 2 2 2 2\n"),
        stress("8 10\n5 1 3 7 2 6 4 8\n"),
    ]
