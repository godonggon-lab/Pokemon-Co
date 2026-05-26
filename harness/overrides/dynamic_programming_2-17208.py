from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1 1\n1 1\n"), edge("3 5 5\n3 3\n2 2\n5 5\n"), stress("5 10 10\n3 4\n4 3\n2 5\n5 2\n6 6\n")]
