from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 10\n"), edge("3\n2 10\n3 20\n4 100\n"), stress("3\n10 2000\n5 500\n8 1000\n")]
