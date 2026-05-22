from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("5 2\n"), edge("10 0\n"), edge("10 10\n"), edge("100 50\n"), stress("1000 500\n")]
