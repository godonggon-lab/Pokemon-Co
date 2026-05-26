from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 0 0 0 0 5 0 5 0 0 0 5 0 0 5 0 5 0\n0 0 5 0 0 5 0 0 5 0 0 5 0 0 5 0 0 5\n1 4 0 2 2 1 2 0 3 2 0 3 1 3 1 2 1 2\n0 5 0 0 0 5 2 0 3 2 0 3 1 0 4 0 0 5\n"),
        stress("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n5 0 0 4 1 0 3 1 1 2 1 2 1 1 3 0 0 5\n5 0 0 5 0 0 5 0 0 5 0 0 5 0 0 5 0 0\n1 1 3 1 1 3 1 1 3 1 1 3 1 1 3 1 1 3\n"),
    ]
