from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 2\n1 2 0\n0 1 2\n2 0 1\n1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2\n2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3\n"),
        edge("2 2\n1 2\n0 1\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n"),
        stress("4 3\n1 2 0 2\n0 1 2 0\n2 0 1 2\n0 2 0 1\n1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4\n4 3 2 1 4 3 2 1 4 3 2 1 4 3 2 1 4 3 2 1\n"),
    ]
