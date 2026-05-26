from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 2 1\n1 0 0\n0 2 0\n0 0 0\n"),
        edge("4 3 2\n1 0 2 0\n0 0 0 0\n2 0 0 2\n0 0 0 0\n"),
        stress("5 4 3\n1 0 2 0 0\n0 0 0 2 0\n2 0 0 0 0\n0 2 0 0 2\n0 0 0 0 0\n"),
    ]
