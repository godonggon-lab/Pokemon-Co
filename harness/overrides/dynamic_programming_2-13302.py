from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 0\n"), edge("5 2\n2 4\n"), stress("10 3\n2 5 9\n")]
