from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 2 1 3 10\n1 2 5\n2 3 5\n"), edge("3 1 1 3 10\n1 2 5\n"), stress("5 6 1 5 10\n1 2 4\n2 5 6\n1 3 7\n3 5 2\n2 3 1\n4 5 1\n")]
