from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n1\n0 0\n"), edge("3 3\n1 1 1\n1 1 1\n1 1 1\n0 0\n"), stress("5 5\n" + "\n".join(" ".join(str((r+c)%2) for c in range(5)) for r in range(5)) + "\n0 0\n")]
