from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 1 2\n1 2\n2 3\n"), edge("4 3 4\n1 2\n2 3\n3 4\n1 4\n"), stress("5 4 6\n1 2\n2 3\n3 4\n4 5\n1 5\n2 5\n")]
