from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n1\n3\n4\n"), edge("2\n100\n1000000000000000000\n"), stress("5\n10\n1000\n999999\n123456789\n9876543210\n")]
