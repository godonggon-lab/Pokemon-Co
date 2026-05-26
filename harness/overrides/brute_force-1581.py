from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1 1 1\n"), edge("3 0 2 1\n"), stress("2 3 3 2\n")]
