from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5 7\n"), edge("3\n5 3\n3 2\n2 6\n"), stress("5\n10 20\n20 5\n5 30\n30 2\n2 8\n")]
