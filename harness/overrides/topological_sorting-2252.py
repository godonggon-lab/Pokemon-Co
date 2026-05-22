from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 0\n"), edge("3 2\n1 3\n2 3\n"), stress("5 4\n1 2\n1 3\n3 4\n2 5\n")]
