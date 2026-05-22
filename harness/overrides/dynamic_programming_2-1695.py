from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n7\n"), edge("5\n1 2 3 2 1\n"), edge("4\n1 2 3 4\n"), stress("8\n1 3 2 4 2 3 1 5\n")]
