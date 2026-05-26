from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 5 10 3\n1 5 6\n"), edge("4 10 20 5\n3 7 12 18\n"), stress("6 15 40 10\n1 5 10 20 25 30\n")]
