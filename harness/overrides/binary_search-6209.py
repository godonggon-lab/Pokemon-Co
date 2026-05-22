from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("10 0 0\n"), edge("25 5 2\n2\n11\n14\n17\n21\n"), stress("1000 20 5\n" + "\n".join(str((i+1)*40) for i in range(20)) + "\n")]
