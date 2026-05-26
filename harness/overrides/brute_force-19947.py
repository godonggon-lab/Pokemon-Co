from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("10000 1\n"), edge("10000 3\n"), stress("12345 10\n")]
