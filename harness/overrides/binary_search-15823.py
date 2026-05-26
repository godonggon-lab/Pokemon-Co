from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 1\n1 2 3\n"), edge("5 2\n1 2 1 3 4\n"), stress("10 3\n1 2 3 1 2 4 5 6 4 7\n")]
