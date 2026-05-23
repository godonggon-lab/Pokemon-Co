from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("5\n1\n5 1\n"), edge("10\n2\n1 10\n5 2\n"), stress("20\n3\n1 5\n5 3\n10 2\n")]
