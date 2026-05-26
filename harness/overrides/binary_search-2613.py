from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 2\n1 2 3 4 5\n"),
        edge("6 3\n5 5 5 5 5 5\n"),
        stress("8 4\n1 100 1 100 1 100 1 100\n"),
    ]
