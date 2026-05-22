from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1\n"), edge("3\n1 1 2\n"), edge("5\n5 1 2 7 3\n"), stress("20\n" + " ".join(str(i % 10 + 1) for i in range(20)) + "\n")]
