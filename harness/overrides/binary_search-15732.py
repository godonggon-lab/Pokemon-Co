from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("10 1 3\n1 10 2\n"), edge("10 2 5\n1 5 1\n6 10 1\n"), stress("100 3 20\n1 100 3\n2 80 5\n50 100 7\n")]
