from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 0\n10.0\n0 0\n3 4\n"), edge("3 1\n5.0\n0 0\n3 4\n6 8\n1 2\n"), stress("4 1\n5.5\n0 0\n3 4\n6 8\n10 10\n2 3\n")]
