from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n-1 0 1\n"), edge("5\n0 0 0 0 0\n"), edge("6\n-2 -1 0 1 2 3\n"), stress("50\n" + " ".join(str(i%21-10) for i in range(50)) + "\n")]
