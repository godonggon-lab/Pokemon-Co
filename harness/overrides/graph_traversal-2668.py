from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1\n"), edge("3\n2\n3\n1\n"), stress("6\n2\n1\n4\n5\n3\n6\n")]
