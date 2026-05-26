from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 2\n0 5\n5 0\n1 2 4\n1 2 5\n"), stress("4 3\n0 2 9 9\n2 0 2 9\n9 2 0 2\n9 9 2 0\n1 4 6\n1 4 5\n4 1 6\n")]
