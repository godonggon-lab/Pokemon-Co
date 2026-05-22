from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 3\n2 3 5\n"), edge("6 2\n2 3\n"), stress("100 5\n7 11 13 17 19\n")]
