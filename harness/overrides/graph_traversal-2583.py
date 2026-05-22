from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1 0\n"), edge("5 7 3\n0 2 4 4\n1 1 2 5\n4 0 6 2\n"), edge("3 3 1\n0 0 3 3\n"), stress("10 10 2\n0 0 5 5\n5 5 10 10\n")]
