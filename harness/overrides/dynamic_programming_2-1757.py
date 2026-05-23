from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n5\n"), edge("3 1\n5\n10\n20\n"), stress("6 2\n3\n8\n4\n7\n6\n5\n")]
