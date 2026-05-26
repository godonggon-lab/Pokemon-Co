from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 5\n5\n"), edge("3 10\n1 4 5\n"), stress("5 20\n2 7 9 11 14\n")]
