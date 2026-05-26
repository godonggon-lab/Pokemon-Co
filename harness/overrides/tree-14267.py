from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n-1\n1 5\n"), edge("5 3\n-1 1 1 2 2\n2 10\n3 5\n5 7\n"), stress("6 4\n-1 1 2 2 3 3\n1 1\n2 2\n3 3\n6 4\n")]
