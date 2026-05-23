from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("4\n1 1\n0 0\n1 0\n0 1\n1 1\n"), edge("3\n2 2\n0 0\n2 0\n0 2\n"), stress("7\n2 3\n0 0\n2 0\n0 3\n2 3\n4 3\n4 0\n9 9\n")]
