from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n2 1\n1 2\n"), edge("2\n3 3\n1 2\n2 3\n1 3\n5 4\n1 2\n2 3\n3 4\n4 5\n"), stress("1\n20 19\n" + "\n".join(f"{i} {i+1}" for i in range(1, 20)) + "\n")]
