from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5\n1 2 3 4 5\n"),
        edge("5\n5 4 3 2 1\n"),
        stress("8\n3 7 1 6 2 5 4 8\n"),
    ]
