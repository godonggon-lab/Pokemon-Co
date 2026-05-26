from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 5\n6 10\n"), edge("4 7\n6 13\n4 8\n3 6\n5 12\n"), stress("6 15\n5 10\n4 7\n6 12\n3 5\n8 20\n2 3\n")]
