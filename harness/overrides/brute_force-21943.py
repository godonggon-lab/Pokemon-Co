from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2\n1 2\n1 0\n"), edge("4\n1 2 3 4\n2 1\n"), stress("5\n5 4 3 2 1\n3 1\n")]
