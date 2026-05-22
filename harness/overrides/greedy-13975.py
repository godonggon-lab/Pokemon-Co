from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1\n10\n"), edge("2\n4\n40 30 30 50\n3\n1 1 1\n"), stress("1\n30\n" + " ".join(str((i*17)%100+1) for i in range(30)) + "\n")]
