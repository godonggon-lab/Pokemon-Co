from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n3 10\n"), edge("2\n3 8\n5 8\n"), edge("4\n1 7\n2 6\n3 8\n4 9\n"), stress("10\n" + "\n".join(f"{i%7+1} {(i*5)%13+1}" for i in range(10)) + "\n")]
