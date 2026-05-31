from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("20 2\n"), edge("5 3\n"), stress("100 50\n")]
