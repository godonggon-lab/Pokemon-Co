from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n7\n"), edge("7 5\n7\n1\n7\n4\n4\n"), edge("10 3\n100\n1\n1\n"), stress("100 20\n" + "\n".join(str((i * 37) % 1000 + 1) for i in range(20)) + "\n")]
