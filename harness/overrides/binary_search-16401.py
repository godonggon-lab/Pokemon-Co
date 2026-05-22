from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n10\n"), edge("3 10\n1 2 3 4 5 6 7 8 9 10\n"), edge("100 2\n1 1\n"), stress("100 20\n" + " ".join(str((i*19)%1000+1) for i in range(20)) + "\n")]
