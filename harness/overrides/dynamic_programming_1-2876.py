from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 2\n"), edge("3\n1 1\n1 2\n1 3\n"), edge("4\n5 4\n4 5\n5 5\n1 5\n"), stress("20\n" + "\n".join(f"{i%5+1} {(i+2)%5+1}" for i in range(20)) + "\n")]
