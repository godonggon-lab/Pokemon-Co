from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 0 0\n"),
        edge("3\n1 0 0\n2 1 1\n3 2 2\n"),
        stress("5\n1 0 0\n1 0 1\n2 1 1\n3 2 2\n1 3 3\n"),
    ]
