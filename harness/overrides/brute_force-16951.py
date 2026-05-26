from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n7\n"), edge("3\n1 2 3\n"), stress("5\n1 3 5 7 8\n")]
