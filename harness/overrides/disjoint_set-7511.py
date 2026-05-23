from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n3\n1\n0 1\n2\n0 1\n1 2\n"), stress("2\n4\n2\n0 1\n2 3\n3\n0 1\n1 2\n2 3\n3\n0\n2\n0 1\n1 2\n")]
