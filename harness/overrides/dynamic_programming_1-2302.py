from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n0\n"), edge("5\n0\n"), edge("9\n2\n4\n7\n"), edge("10\n3\n1\n5\n10\n"), stress("40\n4\n5\n10\n20\n35\n")]
