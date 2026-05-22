from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2\n1 2\n1\n1 2\n"), edge("9\n7 3\n7\n1 2\n1 3\n2 7\n2 8\n2 9\n4 5\n4 6\n"), edge("4\n1 4\n1\n2 3\n"), stress("20\n1 20\n19\n" + "\n".join(f"{i} {i+1}" for i in range(1, 20)) + "\n")]
