from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2\n-5 10\n"), edge("5\n-99 -2 -1 4 98\n"), edge("5\n1 2 3 4 5\n"), stress("100\n" + " ".join(str(i-50) for i in range(100)) + "\n")]
