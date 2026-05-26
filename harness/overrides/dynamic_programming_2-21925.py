from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2\n1 1\n"), edge("4\n1 2 2 1\n"), stress("6\n1 2 1 1 2 1\n")]
