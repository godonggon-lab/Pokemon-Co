from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 4 1 3\n"), edge("4 6 1 2\n"), stress("7 11 5 9\n")]
