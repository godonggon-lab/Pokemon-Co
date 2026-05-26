from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 0\n5\n"), edge("3 2\n1 2 3\n1 2\n2 3\n"), stress("5 5\n5 1 4 2 3\n1 3\n2 3\n2 4\n4 5\n5 1\n")]
