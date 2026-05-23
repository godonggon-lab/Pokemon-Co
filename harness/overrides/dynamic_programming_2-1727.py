from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n10\n20\n"), edge("2 3\n1 10\n2 9 20\n"), stress("4 6\n1 3 20 30\n2 4 5 25 28 40\n")]
