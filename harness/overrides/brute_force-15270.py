from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 0\n"), edge("4 2\n1 2\n3 4\n"), edge("5 4\n1 2\n2 3\n3 4\n4 5\n"), stress("10 10\n" + "\n".join(f"{i} {i+1}" for i in range(1,10)) + "\n1 10\n")]
