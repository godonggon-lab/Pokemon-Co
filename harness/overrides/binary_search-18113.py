from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1 1\n3\n"), edge("2 2 3\n10\n6\n"), stress("5 3 5\n20\n12\n8\n4\n30\n")]
