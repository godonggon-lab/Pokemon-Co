from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n1\n"), edge("5 2\n1 2 1 2 1\n"), edge("5 3\n2 2 2 2 2\n"), stress("100 10\n" + " ".join("1" if i % 7 == 0 else "2" for i in range(100)) + "\n")]
