from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0 0 0\n0 0 0\n0 0 0\n"),
        edge("1 1 0\n2 2 0\n0 0 0\n"),
        stress("1 2 1\n2 1 0\n0 0 2\n"),
    ]
