from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5\n0\n"), edge("3\n-1\n-2\n-3\n0\n"), edge("5\n1\n2\n-5\n4\n5\n0\n"), stress("20\n" + "\n".join(str((i * 7) % 21 - 10) for i in range(20)) + "\n0\n")]
