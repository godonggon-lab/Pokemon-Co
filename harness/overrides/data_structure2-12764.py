from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 2\n"), edge("3\n1 5\n2 3\n4 6\n"), stress("20\n" + "\n".join(f"{i} {i+10}" for i in range(20)) + "\n")]
