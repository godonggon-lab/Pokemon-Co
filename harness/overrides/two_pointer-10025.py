from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 0\n5 10\n"), edge("4 1\n1 0\n2 1\n3 2\n4 10\n"), stress("30 10\n" + "\n".join(f"{i%9+1} {i*100}" for i in range(30)) + "\n")]
