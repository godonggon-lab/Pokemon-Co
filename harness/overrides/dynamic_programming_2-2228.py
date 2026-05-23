from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n5\n"), edge("5 2\n1\n2\n-10\n3\n4\n"), stress("7 3\n5\n-1\n4\n-2\n3\n-10\n8\n")]
