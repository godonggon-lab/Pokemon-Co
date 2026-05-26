from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("10 3 2\n"), edge("8 2 1\n"), stress("20 5 3\n")]
