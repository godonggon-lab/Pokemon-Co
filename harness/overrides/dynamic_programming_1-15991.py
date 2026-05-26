from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n1\n2\n3\n"), stress("5\n4\n5\n10\n20\n100\n")]
