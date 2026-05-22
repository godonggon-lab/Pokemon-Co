from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n1\n2\n3\n"), edge("3\n4\n7\n10\n"), stress("4\n100\n1000\n10000\n100000\n")]
