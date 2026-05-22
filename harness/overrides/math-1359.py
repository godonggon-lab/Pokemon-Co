from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("5 2 1\n"), edge("10 3 2\n"), stress("20 10 5\n")]
