from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 10\n5\n"), edge("3 10\n5\n10\n3\n"), stress("6 100\n5\n7\n4\n10\n9\n12\n")]
