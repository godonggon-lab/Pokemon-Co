from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n"), edge("3 4\n"), edge("4 6\n"), edge("5 100\n"), stress("10 100\n")]
