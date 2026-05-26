from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n0 0 0 0\n"), edge("3\n0 0 1 1\n"), stress("7\n6 6 0 1\n")]
