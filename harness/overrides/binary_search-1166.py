from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 10 20 30\n"), edge("8 10 10 10\n"), stress("1000000 100 200 300\n")]
