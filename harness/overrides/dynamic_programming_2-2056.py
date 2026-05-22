from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5 0\n"), edge("3\n5 0\n10 1 1\n3 1 1\n"), stress("5\n10 0\n5 1 1\n7 1 1\n4 2 2 3\n3 1 4\n")]
