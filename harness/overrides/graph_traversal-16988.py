from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2\n0 2\n0 0\n"),
        edge("3 3\n1 2 0\n0 0 0\n0 2 1\n"),
        stress("5 5\n1 2 0 0 1\n0 2 0 2 0\n0 0 0 0 0\n1 0 2 0 1\n0 0 0 2 0\n"),
    ]
