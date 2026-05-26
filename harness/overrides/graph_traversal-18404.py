from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 1\n1 1\n3 2\n"), edge("5 2\n3 3\n1 2\n5 5\n"), stress("8 3\n1 1\n8 8\n4 5\n2 3\n")]
