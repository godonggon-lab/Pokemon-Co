from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1\n"), edge("2\n1 4\n"), stress("5\n1 3 9 27 81\n")]
