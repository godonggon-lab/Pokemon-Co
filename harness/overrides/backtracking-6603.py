from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("6 1 2 3 4 5 6\n0\n"), stress("7 1 2 3 4 5 6 7\n8 3 5 7 11 13 17 19 23\n0\n")]
