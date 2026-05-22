from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("0 10\n"), edge("2 10\n0 5 3\n5 10 3\n"), stress("5 50\n0 10 5\n10 20 5\n0 30 20\n25 50 10\n40 45 1\n")]
