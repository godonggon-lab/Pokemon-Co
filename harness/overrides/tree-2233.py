from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n01\n1 2\n"),
        edge("3\n001101\n2 5\n"),
        stress("5\n0001101101\n3 8\n"),
    ]
