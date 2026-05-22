from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1\n2\n"), edge("9\n5 12 7 10 9 1 2 3 11\n13\n"), edge("5\n1 1 1 1 1\n2\n"), stress("100\n" + " ".join(str(i + 1) for i in range(100)) + "\n101\n")]
