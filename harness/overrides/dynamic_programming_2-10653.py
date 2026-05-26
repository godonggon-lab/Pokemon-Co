from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 0\n0 0\n1 1\n2 2\n"),
        edge("4 1\n0 0\n10 0\n10 10\n20 10\n"),
        stress("6 2\n0 0\n1 2\n4 2\n4 8\n9 8\n9 9\n"),
    ]
