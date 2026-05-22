from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1 1\n0\n0 1\n"), edge("4 8 4\n6 1 4 9\n7 2\n3 3\n4 5\n5 1\n2 2\n1 4\n8 4\n9 4\n"), stress("20 20 30\n" + " ".join(str(i*10) for i in range(20)) + "\n" + "\n".join(f"{i*7} {i%10}" for i in range(20)) + "\n")]
