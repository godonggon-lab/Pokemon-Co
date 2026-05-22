from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("0\n"), edge("3\n10 1\n20 1\n30 2\n"), stress("6\n50 2\n10 1\n20 2\n30 1\n40 3\n60 3\n")]
