from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 10 1\n10 5\n"), edge("2 10 3\n3 1\n7 2\n4 3\n"), stress("3 20 5\n5 3\n8 4\n10 5\n2 1\n9 6\n")]
