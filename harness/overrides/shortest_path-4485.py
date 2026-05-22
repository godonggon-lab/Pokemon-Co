from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5\n0\n"), edge("3\n5 5 4\n3 9 1\n3 2 7\n0\n"), stress("5\n" + "\n".join(" ".join(str((r*c+c)%9+1) for c in range(5)) for r in range(5)) + "\n0\n")]
