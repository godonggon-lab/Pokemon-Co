from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n99\n100\n"), edge("3\n1 21 79\n20 30 25\n"), stress("5\n10 20 30 40 50\n5 20 30 40 100\n")]
