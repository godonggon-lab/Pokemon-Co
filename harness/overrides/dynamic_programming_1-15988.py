from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n1\n2\n3\n"), edge("4\n4\n7\n10\n100\n"), stress("5\n1000\n10000\n100000\n500000\n1000000\n")]
