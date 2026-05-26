from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 1\n5\n7\n"), edge("1\n3 3\n1 5 10\n2 6 11\n"), stress("2\n4 5\n1 4 8 20\n2 3 9 15 30\n2 2\n100 1\n50 150\n")]
