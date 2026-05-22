from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("0 1\n"), edge("1 1\n"), edge("2 2\n"), edge("20 2\n"), edge("20 20\n"), stress("200 200\n")]
