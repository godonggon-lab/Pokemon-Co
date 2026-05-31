from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("20\n"), edge("1729\n"), stress("10000\n")]
