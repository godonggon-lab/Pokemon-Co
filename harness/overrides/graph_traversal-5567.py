from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n0\n"), edge("6\n5\n1 2\n1 3\n3 4\n2 5\n5 6\n"), edge("5\n2\n2 3\n4 5\n"), stress("20\n19\n" + "\n".join(f"{i} {i+1}" for i in range(1, 20)) + "\n")]
