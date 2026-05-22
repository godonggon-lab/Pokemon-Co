from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2\n1\n1 2 5\n1 2\n"), edge("4\n4\n1 2 2\n1 3 2\n2 4 3\n3 4 3\n1 4\n"), stress("5\n6\n1 2 1\n1 3 2\n2 4 4\n3 4 3\n4 5 5\n2 5 2\n1 5\n")]
