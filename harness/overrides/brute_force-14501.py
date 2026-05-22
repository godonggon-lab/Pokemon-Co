from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 10\n"), edge("7\n3 10\n5 20\n1 10\n1 20\n2 15\n4 40\n2 200\n"), stress("15\n" + "\n".join(f"{i%5+1} {(i*13)%100+1}" for i in range(15)) + "\n")]
