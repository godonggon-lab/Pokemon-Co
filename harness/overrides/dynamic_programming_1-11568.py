from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5\n"), edge("5\n1 2 3 4 5\n"), edge("5\n5 4 3 2 1\n"), stress("50\n" + " ".join(str((i * 19) % 30) for i in range(50)) + "\n")]
