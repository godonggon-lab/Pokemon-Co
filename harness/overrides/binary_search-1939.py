from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 1\n1 2 7\n1 2\n"), edge("3 3\n1 2 3\n2 3 4\n1 3 2\n1 3\n"), stress("5 6\n1 2 5\n2 5 4\n1 3 10\n3 4 3\n4 5 8\n2 4 6\n1 5\n")]
