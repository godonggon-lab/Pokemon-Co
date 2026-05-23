from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n3 1 12 1\n"), edge("2\n3 1 6 1\n6 1 12 1\n"), stress("4\n1 1 3 1\n3 1 5 1\n5 1 9 1\n9 1 12 1\n")]
