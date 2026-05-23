from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 2\n0 2\n"), edge("2 5\n0 2\n0 5\n"), stress("6 6\n1 1\n2 2\n3 3\n3 5\n2 6\n10 6\n")]
