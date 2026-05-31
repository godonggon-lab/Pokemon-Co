from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n0 0 10\n0 0 5\n0 0 2\n"),
        edge("4\n0 0 20\n-5 0 3\n5 0 3\n0 0 1\n"),
        stress("5\n0 0 30\n0 0 20\n0 0 10\n-20 0 5\n20 0 5\n"),
    ]
