from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n7\n"), edge("3\n3 2 5\n"), stress("5\n4 6 8 3 7\n")]
