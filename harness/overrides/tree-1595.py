from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge(""), edge("1 2 3\n"), stress("1 2 5\n2 3 7\n2 4 2\n4 5 9\n")]
