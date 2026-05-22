from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 0\n1\n"), edge("5 6\n1\n5 1 1\n1 2 2\n1 3 3\n2 3 4\n2 4 5\n3 4 6\n"), stress("4 5\n2\n2 1 1\n2 3 2\n3 4 3\n1 4 10\n4 1 1\n")]
