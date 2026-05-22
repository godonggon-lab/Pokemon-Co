from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("4 6\n1 2 3\n2 3 3\n3 4 1\n1 3 5\n2 4 5\n1 4 4\n2 3\n"), edge("3 1\n1 2 1\n2 3\n"), stress("5 6\n1 2 1\n2 3 2\n3 5 3\n1 4 2\n4 5 2\n2 5 10\n2 4\n")]
