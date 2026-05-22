from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n3\n1 2 3\n"), edge("1\n7\n3 1 3 7 3 4 6\n"), stress("1\n20\n" + " ".join(str(i%20+1) for i in range(1,21)) + "\n")]
