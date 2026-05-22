from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n10\n20\n1000\n"), edge("5\n1\n2\n3\n4\n5\n"), stress("10\n" + "\n".join(str(i * 97 % 1000 + 1) for i in range(10)) + "\n")]
