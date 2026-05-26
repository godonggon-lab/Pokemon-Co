from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n7\n"), edge("2 3\n1 2 3\n4 5 6\n"), stress("4 4\n1 0 2 3\n4 1 0 5\n2 2 2 2\n9 0 1 1\n")]
