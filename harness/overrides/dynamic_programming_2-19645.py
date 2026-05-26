from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n1 2 3\n"), edge("4\n1 1 1 1\n"), stress("5\n2 3 5 7 11\n")]
