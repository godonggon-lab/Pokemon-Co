from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 1\n0 0\n"), edge("3 1\n0 3 0\n"), stress("5 3\n1 3 5 7 9\n")]
