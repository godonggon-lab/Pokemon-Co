from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5 10\n"), edge("3\n1 2\n2 5\n3 2\n"), edge("4\n1 5\n2 3\n4 5\n5 1\n"), edge("7\n2 4\n11 4\n15 8\n4 6\n5 3\n8 10\n13 6\n"), stress("20\n" + "\n".join(f"{i*2+1} {(i*7)%13+1}" for i in range(20)) + "\n")]
