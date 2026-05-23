from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5 10\n"), edge("3\n1 1\n2 10\n3 1\n"), stress("5\n10 5\n1 3\n7 20\n20 1\n15 6\n")]
