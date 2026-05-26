from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n7\n"), edge("5\n5 4 3 2 1\n"), stress("7\n15 11 4 8 5 2 4\n")]
