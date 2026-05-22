from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 1\n1 2\n"), edge("6 7\n3 6\n4 3\n3 2\n1 3\n1 2\n2 4\n5 2\n"), stress("20 19\n" + "\n".join(f"{i} {i+1}" for i in range(1,20)) + "\n")]
