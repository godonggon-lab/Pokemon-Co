from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 2\n0 1\n1 2\n"), edge("3 3\n0 1\n1 2\n2 0\n"), stress("5 5\n0 1\n1 2\n3 4\n2 3\n4 0\n")]
