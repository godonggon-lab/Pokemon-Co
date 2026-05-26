from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2\n0\n"),
        edge("2 2\n1\n0 0 1 0\n"),
        stress("4 3\n3\n0 0 1 0\n1 1 1 2\n2 2 3 2\n"),
    ]
