from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1\n-5\n"), edge("2\n5\n1 2 3 4 5\n5\n-1 -2 -3 -4 -5\n"), stress("1\n50\n" + " ".join(str((i * 7) % 21 - 10) for i in range(50)) + "\n")]
