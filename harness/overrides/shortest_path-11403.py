from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n0\n"), edge("3\n0 1 0\n0 0 1\n1 0 0\n"), stress("6\n" + "\n".join(" ".join("1" if (i+1)%6==j else "0" for j in range(6)) for i in range(6)) + "\n")]
