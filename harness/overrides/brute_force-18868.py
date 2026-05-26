from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 3\n1 2 3\n10 20 30\n"), edge("2 3\n1 1 2\n3 3 4\n"), stress("4 4\n1 2 3 4\n4 3 2 1\n10 20 30 40\n5 5 6 7\n")]
