from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 1\n1\n1\n"), edge("6 7\n1\n5\n3\n3\n5\n1\n"), stress("20 10\n" + "\n".join(str(i%10+1) for i in range(20)) + "\n")]
