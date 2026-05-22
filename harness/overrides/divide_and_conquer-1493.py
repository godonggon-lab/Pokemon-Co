from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1 1\n1\n0 1\n"), edge("4 4 4\n1\n1 8\n"), edge("4 4 4\n1\n2 1\n"), stress("10 12 8\n4\n0 100\n1 50\n2 10\n3 1\n")]
