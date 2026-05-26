from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1\n7\n"), edge("1\n4\n40 30 30 50\n"), stress("2\n5\n1 2 3 4 5\n6\n10 20 30 40 50 60\n")]
