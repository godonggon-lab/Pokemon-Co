from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5\n"), edge("3\n1 2 3\n"), edge("3\n2 3 4\n"), edge("5\n1 1 1 2 3\n"), stress("20\n" + " ".join(str(i % 9 + 1) for i in range(20)) + "\n")]
