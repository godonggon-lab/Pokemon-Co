from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("5 1\n5 7\n"), edge("10 3\n5 5\n5 9\n10 3\n"), stress("15 5\n5 10\n4 8\n6 7\n10 6\n1 100\n")]
