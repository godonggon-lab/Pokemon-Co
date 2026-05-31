from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5\n1 3 4 2 5\n"),
        edge("6\n1 2 3 4 5 6\n"),
        stress("8\n1 3 2 4 3 5 4 6\n"),
    ]
