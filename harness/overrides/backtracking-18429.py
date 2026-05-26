from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 5\n5\n"), edge("3 4\n3 7 5\n"), stress("5 3\n1 2 3 4 5\n")]
