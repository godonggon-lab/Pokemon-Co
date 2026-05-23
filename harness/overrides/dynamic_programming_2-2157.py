from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 2 1\n1 2 5\n"), edge("4 3 5\n1 2 5\n2 4 7\n1 3 10\n3 4 1\n4 1 100\n"), stress("5 4 7\n1 2 5\n2 3 6\n3 5 7\n1 4 20\n4 5 1\n2 5 8\n5 2 100\n")]
