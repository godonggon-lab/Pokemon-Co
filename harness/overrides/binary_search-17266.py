from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("10\n1\n5\n"), edge("10\n2\n0 10\n"), stress("100\n5\n5 20 50 70 95\n")]
