from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 1\n"), edge("4\n1 8\n3 9\n2 2\n4 1\n"), stress("6\n1 3\n2 2\n3 6\n4 4\n5 5\n6 1\n")]
