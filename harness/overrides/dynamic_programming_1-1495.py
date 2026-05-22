from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 5 10\n5\n"), edge("2 5 10\n6 6\n"), stress("5 10 20\n5 3 7 10 2\n")]
