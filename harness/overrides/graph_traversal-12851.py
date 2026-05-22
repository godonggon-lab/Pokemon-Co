from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("5 17\n"), edge("0 0\n"), edge("10 1\n"), edge("1 100\n"), stress("0 100000\n")]
