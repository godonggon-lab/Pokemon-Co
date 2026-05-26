from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2\n1 2\n"), edge("5\n1 2 3 4 5\n"), stress("6\n6 1 5 2 4 3\n")]
