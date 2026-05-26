from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 10\n1 1 10\n"), edge("2 3\n1 10 10\n2 10 10\n"), stress("4 5\n1 7 20\n2 3 10\n1 20 30\n1 1 100\n")]
