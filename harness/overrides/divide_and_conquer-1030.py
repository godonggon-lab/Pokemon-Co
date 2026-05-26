from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 3 1 0 2 0 2\n"), edge("2 3 1 0 8 0 8\n"), stress("3 3 1 5 15 4 14\n")]
