from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n1 2 3\n1\n"), edge("6\n1 2 3 4 5 6\n2\n"), stress("9\n5 1 3 8 2 7 4 6 9\n2\n")]
