from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0 0 0 0\n"),
        edge("3\n3 3 0 1\n4 2 1 2\n4 2 2 1\n"),
        stress("4\n50 50 0 3\n50 50 1 2\n10 10 2 4\n20 20 3 1\n"),
    ]
