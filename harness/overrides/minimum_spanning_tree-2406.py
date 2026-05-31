from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 0\n0 0 0\n0 0 5\n0 5 0\n"),
        edge("4 1\n2 3\n0 0 0 0\n0 0 4 6\n0 4 0 2\n0 6 2 0\n"),
        stress("5 1\n2 3\n0 0 0 0 0\n0 0 3 8 9\n0 3 0 2 7\n0 8 2 0 1\n0 9 7 1 0\n"),
    ]
