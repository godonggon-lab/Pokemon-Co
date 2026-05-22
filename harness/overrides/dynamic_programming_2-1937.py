from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n7\n"), edge("2\n1 2\n4 3\n"), stress("4\n14 9 12 10\n1 11 5 4\n7 15 2 13\n6 3 16 8\n")]
