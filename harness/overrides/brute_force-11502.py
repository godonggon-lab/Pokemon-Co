from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n7\n"), edge("3\n11\n25\n999\n"), stress("5\n33\n99\n123\n777\n1000\n")]
