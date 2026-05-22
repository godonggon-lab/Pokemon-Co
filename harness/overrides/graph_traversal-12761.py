from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 3 1 20\n"), edge("5 7 10 10\n"), edge("3 4 100 1\n"), stress("7 11 0 100000\n")]
