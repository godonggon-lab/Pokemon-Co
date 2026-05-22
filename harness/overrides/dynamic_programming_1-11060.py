from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n0\n"), edge("5\n1 1 1 1 0\n"), edge("5\n0 1 1 1 1\n"), stress("100\n" + " ".join(str(i%5) for i in range(100)) + "\n")]
