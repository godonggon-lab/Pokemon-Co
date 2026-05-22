from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 1\n1 2 5\n"), edge("5 6\n1 2 2\n1 3 5\n2 3 1\n2 4 2\n3 5 5\n4 5 1\n"), stress("20 19\n" + "\n".join(f"{i} {i+1} {i%7+1}" for i in range(1,20)) + "\n")]
