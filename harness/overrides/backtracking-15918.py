from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 1 3\n"), edge("4 2 5\n"), stress("5 1 6\n")]
