from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n5\n1\n1 1 1 1\n"), edge("3 3\n1 2 3\n4 5 6\n7 8 9\n3\n1 1 3 3\n2 2 3 3\n1 2 2 3\n"), stress("10 10\n" + "\n".join(" ".join(str((r+c)%10) for c in range(10)) for r in range(10)) + "\n1\n1 1 10 10\n")]
