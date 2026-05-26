from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 1 10\n0 0 0\n0 0 0\n0 0 0\n1 1\n1 2 3 3\n"),
        edge("4 2 20\n0 0 0 0\n0 1 0 0\n0 0 0 0\n0 0 0 0\n1 1\n1 2 3 4\n4 4 3 1\n"),
        stress("5 3 30\n0 0 0 0 0\n0 1 1 1 0\n0 0 0 0 0\n0 1 0 1 0\n0 0 0 0 0\n3 3\n1 1 5 5\n5 1 1 5\n3 1 3 5\n"),
    ]
