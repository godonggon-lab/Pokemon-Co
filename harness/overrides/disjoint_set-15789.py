from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 1\n1 2\n1 3 0\n"), stress("8 3\n1 2\n3 4\n5 6\n1 7 2\n")]
