from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 10\n5\n"), edge("3 5\n1\n2\n3\n"), stress("5 20\n10\n1\n7\n4\n15\n")]
