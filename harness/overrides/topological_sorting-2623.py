from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 1\n3 1 2 3\n"), edge("3 2\n2 1 2\n2 2 1\n"), stress("5 3\n3 1 3 5\n2 2 4\n3 1 2 4\n")]
