from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3 1 1\n2 1 2\n1 1 1\n0 1 0\n"),
        edge("4 4 1 2\n2 1 1 2\n1 0 1 1\n1 1 1 1\n2 1 0 2\n"),
        stress("5 5 2 2\n2 1 1 1 2\n1 0 1 0 1\n1 1 2 1 1\n1 0 1 0 1\n2 1 1 1 2\n"),
    ]
