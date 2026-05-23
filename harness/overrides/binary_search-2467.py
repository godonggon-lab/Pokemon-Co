from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2\n-1 2\n"), edge("5\n-99 -2 -1 4 98\n"), stress("6\n-100 -50 -3 2 49 90\n")]
