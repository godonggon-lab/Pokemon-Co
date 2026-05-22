from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n10\n"), edge("3 5\n10\n10\n10\n"), stress("20 100\n" + "\n".join(str((i * 31) % 1000 + 10) for i in range(20)) + "\n")]
