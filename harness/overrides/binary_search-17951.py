from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n7\n"), edge("5 2\n1 2 3 4 5\n"), stress("8 3\n10 1 3 9 4 8 2 7\n")]
