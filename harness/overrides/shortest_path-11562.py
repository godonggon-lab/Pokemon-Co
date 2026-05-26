from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 1\n1 2 0\n2\n1 2\n2 1\n"), stress("4 3\n1 2 0\n2 3 1\n4 3 0\n3\n1 3\n3 1\n4 1\n")]
