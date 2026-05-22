from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("10 0\n"), edge("100 1\n"), edge("999 9\n"), stress("100000 7\n")]
