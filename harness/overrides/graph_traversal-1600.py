from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("0\n1 1\n0\n"), edge("1\n3 3\n0 1 0\n1 1 1\n0 1 0\n"), stress("2\n5 4\n0 0 0 0 0\n1 1 1 1 0\n0 0 0 0 0\n0 1 1 1 0\n")]
