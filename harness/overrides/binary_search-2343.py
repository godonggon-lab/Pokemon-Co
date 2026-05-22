from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n5\n"), edge("9 3\n1 2 3 4 5 6 7 8 9\n"), edge("5 5\n10 20 30 40 50\n"), stress("100 10\n" + " ".join(str(i % 17 + 1) for i in range(100)) + "\n")]
