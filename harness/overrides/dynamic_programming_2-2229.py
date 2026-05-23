from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n7\n"), edge("4\n1 5 2 4\n"), stress("6\n10 1 7 3 9 2\n")]
