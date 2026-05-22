from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1 1\n"), edge("3 1 4\n"), edge("5 3 5\n"), stress("10 5 10\n")]
