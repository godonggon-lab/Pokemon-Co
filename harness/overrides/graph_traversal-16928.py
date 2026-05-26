from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("0 0\n"), edge("1 1\n2 100\n99 1\n"), stress("3 2\n3 22\n5 8\n11 26\n27 1\n21 9\n")]
