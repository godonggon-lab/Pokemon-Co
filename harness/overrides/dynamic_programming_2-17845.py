from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("5 1\n10 6\n"), edge("10 3\n10 5\n40 4\n30 6\n"), stress("15 5\n10 5\n12 6\n5 3\n30 8\n4 2\n")]
