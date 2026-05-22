from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n2\n1 2\n5\n"), edge("2\n3\n1 5 10\n100\n2\n2 3\n10\n"), stress("1\n5\n1 2 5 10 20\n200\n")]
