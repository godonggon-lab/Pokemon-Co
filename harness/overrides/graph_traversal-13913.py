from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("5 17\n"), edge("10 3\n"), stress("1 20\n")]
