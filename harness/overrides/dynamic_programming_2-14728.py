from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 5\n6 10\n"), edge("3 10\n5 10\n4 40\n6 30\n"), stress("5 15\n5 10\n6 12\n3 5\n8 30\n2 4\n")]
