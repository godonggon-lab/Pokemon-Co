from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("5 5\n2\n2 3\n3 2\n"), edge("2 2\n2\n2 2\n2 2\n"), stress("10 8\n4\n3 4\n5 2\n8 1\n6 6\n")]
