from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n3 3\n4 2\n5 5\n"), edge("3\n10 1\n10 5\n10 10\n"), stress("3\n100 50\n200 100\n1000 500\n")]
