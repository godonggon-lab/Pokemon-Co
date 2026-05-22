from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("30 40 10\n"), edge("10 10 5\n"), stress("100 120 30\n")]
