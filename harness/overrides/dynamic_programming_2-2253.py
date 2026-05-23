from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 0\n"), edge("5 1\n3\n"), stress("10 2\n4\n7\n")]
