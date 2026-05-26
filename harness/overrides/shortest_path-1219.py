from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 0 2 2\n0 1 10\n1 2 10\n10 10 100\n"), edge("3 0 2 1\n0 1 5\n10 10 10\n"), stress("4 0 3 4\n0 1 1\n1 2 1\n2 1 1\n2 3 1\n10 10 10 10\n")]
