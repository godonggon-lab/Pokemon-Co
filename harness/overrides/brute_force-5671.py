from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 20\n"), edge("87 104\n"), edge("990 1020\n"), stress("1 5000\n5000 10000\n")]
