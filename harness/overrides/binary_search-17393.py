from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5\n5\n"), edge("5\n3 5 7 9 10\n1 4 6 8 10\n"), stress("6\n2 4 8 16 32 64\n1 2 4 8 16 32\n")]
