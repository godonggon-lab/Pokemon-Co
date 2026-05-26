from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1 10\n5\n1\n"), edge("2 3 20\n4\n10\n15\n1\n2\n"), stress("3 5 100\n10\n25\n40\n70\n90\n1\n2\n4\n")]
