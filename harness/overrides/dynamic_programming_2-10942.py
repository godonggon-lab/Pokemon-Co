from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n7\n1\n1 1\n"), edge("5\n1 2 3 2 1\n3\n1 5\n2 4\n1 3\n"), stress("8\n1 2 2 1 3 4 4 3\n5\n1 4\n5 8\n2 3\n3 6\n4 5\n")]
