from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 3\n1 2 1\n2 3 1\n3 1 1\n2\n1 2\n"), edge("4 5\n1 2 2\n2 1 2\n2 3 3\n3 4 1\n4 1 5\n2\n1 3\n"), stress("5 7\n1 2 2\n2 3 2\n3 4 2\n4 5 2\n5 1 2\n1 3 5\n2 5 4\n3\n1 3 5\n")]
