from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 2 2\n1 2 1\n2 3 1\n"), edge("3 3 2\n1 3 1\n1 2 10\n2 3 10\n"), stress("5 6 3\n1 2 2\n2 5 4\n1 3 1\n3 4 1\n4 5 1\n2 3 10\n")]
